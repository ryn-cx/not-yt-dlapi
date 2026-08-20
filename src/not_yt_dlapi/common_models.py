# TODO: Validate
"""The pieces of a response that more than one endpoint is answered with.

Every model here, and every model an endpoint keeps, is shaped the way the API
documents the resource: one class per documented object, one field per
documented property, named as the docs name it but written in snake_case and
read back through the camelCase the API sends. What a property is is the API's
own wording for it.

Every endpoint asks for every part the API will hand out, so nothing is missing
here because the request did not ask for it. A property is optional only where
the resource itself decides whether to carry it, which the docs say and the
recorded responses show.
"""

from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field
from pydantic.alias_generators import to_camel


# TODO: Validate
class APIModel(BaseModel):
    """A documented object, read from the camelCase the API writes it in.

    The alias generator is what lets a field be named the way Python names
    things while still being read out of the name the API sends, so nothing has
    to say the same word twice.
    """

    model_config = ConfigDict(
        frozen=True,
        populate_by_name=True,
        alias_generator=to_camel,
    )


# TODO: Validate
class Thumbnail(APIModel):
    """One of the images in a resource's map of thumbnails.

    Attributes:
        url: The image's URL.
        width: The image's width.
        height: The image's height.
    """

    url: str
    width: int
    height: int


# TODO: Validate
class Thumbnails(APIModel):
    """The images a resource has, one field per image the API names.

    The API writes this as a map, but the names it may put in it are the five
    the docs list and no others, so it is written here as the five it lists.

    Which of the five a resource carries is decided by the resource: the two
    largest are only made for a video uploaded big enough to need them, and a
    recorded response has been seen carrying neither `default` nor `high`, so
    every one of them is allowed to be missing.

    Attributes:
        default: The default thumbnail image, 120px wide and 90px tall.
        medium: A higher resolution version of the image, 320px wide and 180px
            tall.
        high: A high resolution version of the image, 480px wide and 360px tall.
        standard: An even higher resolution version of the image, 640px wide and
            480px tall.
        maxres: The highest resolution version of the image, 1280px wide and
            720px tall.
    """

    default: Thumbnail | None = None
    medium: Thumbnail | None = None
    high: Thumbnail | None = None
    standard: Thumbnail | None = None
    maxres: Thumbnail | None = None


# TODO: Validate
class Localization(APIModel):
    """A title and description in one language.

    A translation carries whichever of the two was written for it rather than
    both: a playlist translated in name only has a title and no description, and
    a video whose description alone was translated has the other way round.

    Attributes:
        title: The localized title.
        description: The localized description.
    """

    title: str | None = None
    description: str | None = None


# TODO: Validate
class Localizations(APIModel):
    """The translations a resource carries, one field per language.

    The API writes this as a map keyed by language code, and every code it will
    key it with is one of the languages `i18nLanguages` lists, so it is written
    here as one field per language rather than as a map. A field is named after
    its code with the punctuation the code carries turned into an underscore,
    and the three codes that spell a Python keyword take a trailing one, so the
    code itself is what each field is read out of and written back as.

    A resource is translated into whichever languages its owner translated it
    into and no others, so every field is allowed to be missing.
    """

    af: Localization | None = Field(default=None, alias="af")
    am: Localization | None = Field(default=None, alias="am")
    ar: Localization | None = Field(default=None, alias="ar")
    ar_xb: Localization | None = Field(default=None, alias="ar-XB")
    as_: Localization | None = Field(default=None, alias="as")
    az: Localization | None = Field(default=None, alias="az")
    be: Localization | None = Field(default=None, alias="be")
    bg: Localization | None = Field(default=None, alias="bg")
    bn: Localization | None = Field(default=None, alias="bn")
    bs: Localization | None = Field(default=None, alias="bs")
    ca: Localization | None = Field(default=None, alias="ca")
    cs: Localization | None = Field(default=None, alias="cs")
    da: Localization | None = Field(default=None, alias="da")
    de: Localization | None = Field(default=None, alias="de")
    de_at: Localization | None = Field(default=None, alias="de-AT")
    de_ch: Localization | None = Field(default=None, alias="de-CH")
    de_de: Localization | None = Field(default=None, alias="de-DE")
    el: Localization | None = Field(default=None, alias="el")
    en: Localization | None = Field(default=None, alias="en")
    en_au: Localization | None = Field(default=None, alias="en-AU")
    en_ca: Localization | None = Field(default=None, alias="en-CA")
    en_gb: Localization | None = Field(default=None, alias="en-GB")
    en_ie: Localization | None = Field(default=None, alias="en-IE")
    en_in: Localization | None = Field(default=None, alias="en-IN")
    en_sg: Localization | None = Field(default=None, alias="en-SG")
    en_us: Localization | None = Field(default=None, alias="en-US")
    en_xa: Localization | None = Field(default=None, alias="en-XA")
    en_za: Localization | None = Field(default=None, alias="en-ZA")
    es: Localization | None = Field(default=None, alias="es")
    es_419: Localization | None = Field(default=None, alias="es-419")
    es_es: Localization | None = Field(default=None, alias="es-ES")
    es_mx: Localization | None = Field(default=None, alias="es-MX")
    es_us: Localization | None = Field(default=None, alias="es-US")
    et: Localization | None = Field(default=None, alias="et")
    eu: Localization | None = Field(default=None, alias="eu")
    fa: Localization | None = Field(default=None, alias="fa")
    fi: Localization | None = Field(default=None, alias="fi")
    fil: Localization | None = Field(default=None, alias="fil")
    fr: Localization | None = Field(default=None, alias="fr")
    fr_be: Localization | None = Field(default=None, alias="fr-BE")
    fr_ca: Localization | None = Field(default=None, alias="fr-CA")
    fr_ch: Localization | None = Field(default=None, alias="fr-CH")
    fr_fr: Localization | None = Field(default=None, alias="fr-FR")
    gl: Localization | None = Field(default=None, alias="gl")
    gu: Localization | None = Field(default=None, alias="gu")
    hi: Localization | None = Field(default=None, alias="hi")
    hr: Localization | None = Field(default=None, alias="hr")
    hu: Localization | None = Field(default=None, alias="hu")
    hy: Localization | None = Field(default=None, alias="hy")
    id: Localization | None = Field(default=None, alias="id")
    is_: Localization | None = Field(default=None, alias="is")
    it: Localization | None = Field(default=None, alias="it")
    iw: Localization | None = Field(default=None, alias="iw")
    ja: Localization | None = Field(default=None, alias="ja")
    ka: Localization | None = Field(default=None, alias="ka")
    kk: Localization | None = Field(default=None, alias="kk")
    km: Localization | None = Field(default=None, alias="km")
    kn: Localization | None = Field(default=None, alias="kn")
    ko: Localization | None = Field(default=None, alias="ko")
    ky: Localization | None = Field(default=None, alias="ky")
    lo: Localization | None = Field(default=None, alias="lo")
    lt: Localization | None = Field(default=None, alias="lt")
    lv: Localization | None = Field(default=None, alias="lv")
    mk: Localization | None = Field(default=None, alias="mk")
    ml: Localization | None = Field(default=None, alias="ml")
    mn: Localization | None = Field(default=None, alias="mn")
    mr: Localization | None = Field(default=None, alias="mr")
    ms: Localization | None = Field(default=None, alias="ms")
    my: Localization | None = Field(default=None, alias="my")
    ne: Localization | None = Field(default=None, alias="ne")
    nl: Localization | None = Field(default=None, alias="nl")
    nl_be: Localization | None = Field(default=None, alias="nl-BE")
    nl_nl: Localization | None = Field(default=None, alias="nl-NL")
    no: Localization | None = Field(default=None, alias="no")
    or_: Localization | None = Field(default=None, alias="or")
    pa: Localization | None = Field(default=None, alias="pa")
    pl: Localization | None = Field(default=None, alias="pl")
    pt: Localization | None = Field(default=None, alias="pt")
    pt_br: Localization | None = Field(default=None, alias="pt-BR")
    pt_pt: Localization | None = Field(default=None, alias="pt-PT")
    ro: Localization | None = Field(default=None, alias="ro")
    ru: Localization | None = Field(default=None, alias="ru")
    si: Localization | None = Field(default=None, alias="si")
    sk: Localization | None = Field(default=None, alias="sk")
    sl: Localization | None = Field(default=None, alias="sl")
    sq: Localization | None = Field(default=None, alias="sq")
    sr: Localization | None = Field(default=None, alias="sr")
    sr_latn: Localization | None = Field(default=None, alias="sr-Latn")
    sv: Localization | None = Field(default=None, alias="sv")
    sw: Localization | None = Field(default=None, alias="sw")
    ta: Localization | None = Field(default=None, alias="ta")
    te: Localization | None = Field(default=None, alias="te")
    th: Localization | None = Field(default=None, alias="th")
    tr: Localization | None = Field(default=None, alias="tr")
    uk: Localization | None = Field(default=None, alias="uk")
    ur: Localization | None = Field(default=None, alias="ur")
    uz: Localization | None = Field(default=None, alias="uz")
    vi: Localization | None = Field(default=None, alias="vi")
    zh: Localization | None = Field(default=None, alias="zh")
    zh_cn: Localization | None = Field(default=None, alias="zh-CN")
    zh_hk: Localization | None = Field(default=None, alias="zh-HK")
    zh_tw: Localization | None = Field(default=None, alias="zh-TW")
    zu: Localization | None = Field(default=None, alias="zu")


# TODO: Validate
class PageInfo(APIModel):
    """The `pageInfo` object encapsulates paging information for the result set.

    Attributes:
        total_results: The total number of results in the result set.
        results_per_page: The number of results included in the API response.
    """

    total_results: int
    results_per_page: int
