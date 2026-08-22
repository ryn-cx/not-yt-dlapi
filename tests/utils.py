# TODO: Validate
"""Helpers shared by every endpoint's tests.

Nothing here knows about a particular endpoint. What an endpoint's own test file
brings is the ids it downloads, the class it parses into and what it expects to
find; recording a response and reading it back is the same either way.
"""

from __future__ import annotations

import json
import operator
from collections.abc import Sequence
from datetime import UTC, datetime, timedelta
from pathlib import Path
from typing import TYPE_CHECKING, Any, ClassVar

import pytest
from pydantic import BaseModel

if TYPE_CHECKING:
    from collections.abc import Callable

    from not_yt_dlapi.base_response_model import BaseResponseModel

type Dump = dict[str, Any]


# TODO: Validate
class RecordedEndpoint:
    ENDPOINT: ClassVar[type]
    SUFFIX: ClassVar[str] = ".json"
    MODEL: ClassVar[type[BaseResponseModel]]
    UPDATE_FREQUENCY: ClassVar[timedelta] = timedelta(days=7)

    IGNORED: ClassVar[tuple[str, ...]] = ()
    SAME_TYPE: ClassVar[tuple[str, ...]] = ()
    SORTED: ClassVar[tuple[str, ...]] = ()
    LESS_THAN: ClassVar[tuple[str, ...]] = ()
    LESS_THAN_OR_EQUAL: ClassVar[tuple[str, ...]] = ()
    GREATER_THAN: ClassVar[tuple[str, ...]] = ()
    GREATER_THAN_OR_EQUAL: ClassVar[tuple[str, ...]] = ()

    @classmethod
    def _build_file_path(cls, folder: str, name: str | int, suffix: str) -> Path:
        root = Path(__file__).parent / folder / cls.ENDPOINT.__name__
        return root.joinpath(*cls.__qualname__.split(".")) / f"{name}{suffix}"

    @classmethod
    def dumped_file_path(cls, name: str | int) -> Path:
        return cls._build_file_path("_files", name, cls.SUFFIX)

    @classmethod
    def dumped_file_content(cls, name: str | int) -> str:
        return cls.dumped_file_path(name).read_text(encoding="utf-8")

    @classmethod
    def write_file(cls, path: Path, content: str) -> None:
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content, encoding="utf-8")

    # TODO: Validate
    @classmethod
    def dumped_file_age(cls, name: str | int) -> timedelta:
        modified = cls.dumped_file_path(name).stat().st_mtime
        return datetime.now(UTC) - datetime.fromtimestamp(modified, UTC)

    # TODO: Validate
    @classmethod
    def dump_model(
        cls,
        model: BaseResponseModel | Sequence[BaseResponseModel],
    ) -> str:
        if isinstance(model, Sequence):
            return json.dumps([entry.raw for entry in model], indent=2)
        return model.raw

    # TODO: Validate
    @classmethod
    def download_test(
        cls,
        name: str | int,
        download: Callable[[], BaseResponseModel | Sequence[BaseResponseModel]],
    ) -> None:
        """Test that the response from the API's structure does not change."""
        dumped_file_path = cls.dumped_file_path(name)

        # If the file does not exist the file just needs to be downloaded with no
        # verification.
        if not dumped_file_path.exists():
            cls.write_file(dumped_file_path, cls.dump_model(download()))
            return

        if cls.dumped_file_age(name) < cls.UPDATE_FREQUENCY:
            pytest.skip("The dumped files are up to date.")

        existing_model = cls.load_models(cls.dumped_file_content(name))
        new_model = download()
        if differences := cls.differences(existing_model, new_model):
            new_file_path = dumped_file_path.with_name(f"{name}.new{cls.SUFFIX}")
            cls.write_file(new_file_path, cls.dump_model(new_model))
            reported = "\n".join(differences)
            pytest.fail(
                f"The downloaded file for {name} does not match the recorded one. "
                f"The old file was kept and the new one saved as "
                f"{new_file_path.name}.\n{reported}",
            )

        dumped_file_path.touch()

    # TODO: Validate
    @classmethod
    def recorded_model_path(cls, name: str | int) -> Path:
        return cls._build_file_path("_expected_model_dumps", name, ".json")

    # TODO: Validate
    @classmethod
    def recorded_model_dump(cls, name: str | int) -> Dump | list[Dump]:
        dump: Dump | list[Dump] = json.loads(
            cls.recorded_model_path(name).read_text(encoding="utf-8"),
        )
        return dump

    # TODO: Validate
    @classmethod
    def recorded_model_content(
        cls,
        name: str | int,
        current_dump: Dump | list[Dump],
    ) -> Dump | list[Dump]:
        model_path = cls.recorded_model_path(name)
        if not model_path.exists():
            # Nothing has been recorded to compare against, so what was just
            # parsed is written down and stands as the expected dump.
            cls.write_file(model_path, json.dumps(current_dump, indent=2))
            return current_dump
        return cls.recorded_model_dump(name)

    # TODO: Validate
    @classmethod
    def differences(
        cls,
        old_value: object,
        new_value: object,
        field_path: str = "",
        field_id: str = "",
    ) -> list[str]:
        """List every field of the model whose value moved in a way it may not."""
        if field_id in cls.IGNORED:
            return []

        if field_id in cls.SAME_TYPE:
            old_type = type(old_value).__name__
            new_type = type(new_value).__name__
            moved = f"{field_path}: was a {old_type}, now a {new_type}"
            return [] if old_type == new_type else [moved]

        if isinstance(old_value, BaseModel) and isinstance(new_value, BaseModel):
            model_name = type(old_value).__name__
            return [
                difference
                for name in type(old_value).model_fields
                # raw holds the whole document, so it is never compared.
                if name != "raw"
                for difference in cls.differences(
                    getattr(old_value, name),
                    getattr(new_value, name),
                    f"{field_path}.{name}" if field_path else name,
                    f"{model_name}.{name}",
                )
            ]

        if isinstance(old_value, list) and isinstance(new_value, list):
            if len(old_value) != len(new_value):
                held = f"held {len(old_value)} items, now holds {len(new_value)}"
                return [f"{field_path}: {held}"]
            # The API returns some lists in whatever order it likes, so they are
            # sorted before being held against each other.
            old_items = sorted(old_value) if field_id in cls.SORTED else old_value
            new_items = sorted(new_value) if field_id in cls.SORTED else new_value
            return [
                difference
                for index, (old_item, new_item) in enumerate(
                    zip(old_items, new_items, strict=True),
                )
                for difference in cls.differences(
                    old_item,
                    new_item,
                    f"{field_path}[{index}]",
                    field_id,
                )
            ]

        ordering = next(
            (
                comparison
                for names, comparison in (
                    (cls.LESS_THAN, operator.lt),
                    (cls.LESS_THAN_OR_EQUAL, operator.le),
                    (cls.GREATER_THAN, operator.gt),
                    (cls.GREATER_THAN_OR_EQUAL, operator.ge),
                )
                if field_id in names
            ),
            None,
        )
        # Only numbers are ordered. A field named under one of the comparisons
        # that holds anything else has to come back as it was.
        if (
            ordering is not None
            and isinstance(old_value, int | float)
            and isinstance(new_value, int | float)
        ):
            allowed = ordering(old_value, new_value)
            reason = f"which {ordering.__name__} does not allow"
        else:
            allowed = old_value == new_value
            reason = "and it may not change"

        moved = f"{field_path}: was {old_value!r}, now {new_value!r}, {reason}"
        return [] if allowed else [moved]

    # TODO: Validate
    @classmethod
    def load_models(cls, content: str) -> BaseResponseModel | list[BaseResponseModel]:
        """Parse the file into a model, or one model per response."""
        documents: Any = json.loads(content) if cls.SUFFIX == ".json" else content
        # A walk is recorded as the list of documents it was served, each of
        # them written out as it arrived, which is what tells it apart from a
        # response that is itself a list.
        if isinstance(documents, list) and all(
            isinstance(document, str) for document in documents
        ):
            return [cls.MODEL.from_response(document) for document in documents]
        return cls.MODEL.from_response(content)

    # TODO: Validate
    @classmethod
    def load_content(cls, content: str) -> Dump | list[Dump]:
        """Parse the file and dump the model, or one model per response."""
        models = cls.load_models(content)
        if isinstance(models, list):
            return [model.model_dump(mode="json") for model in models]
        return models.model_dump(mode="json")

    # TODO: Validate
    @classmethod
    def parse_test(cls, name: str | int) -> None:
        current_dump = cls.load_content(cls.dumped_file_content(name))
        expected_dump = cls.recorded_model_content(name, current_dump)

        assert current_dump == expected_dump
