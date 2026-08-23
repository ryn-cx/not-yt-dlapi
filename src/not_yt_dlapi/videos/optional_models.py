from typing import Self
from pydantic import ModelWrapValidatorHandler, PrivateAttr, model_validator
from pydantic import AwareDatetime, BaseModel, ConfigDict, Field
from datetime import timedelta
from typing import Any

class Default(BaseModel):
    model_config = ConfigDict(extra='ignore')
    url: str | None = None
    width: int | None = None
    height: int | None = None

class Medium(BaseModel):
    model_config = ConfigDict(extra='ignore')
    url: str | None = None
    width: int | None = None
    height: int | None = None

class High(BaseModel):
    model_config = ConfigDict(extra='ignore')
    url: str | None = None
    width: int | None = None
    height: int | None = None

class Standard(BaseModel):
    model_config = ConfigDict(extra='ignore')
    url: str | None = None
    width: int | None = None
    height: int | None = None

class Maxres(BaseModel):
    model_config = ConfigDict(extra='ignore')
    url: str | None = None
    width: int | None = None
    height: int | None = None

class Thumbnails(BaseModel):
    model_config = ConfigDict(extra='ignore')
    default: Default | None = None
    medium: Medium | None = None
    high: High | None = None
    standard: Standard | None = None
    maxres: Maxres | None = None

class Localized(BaseModel):
    model_config = ConfigDict(extra='ignore')
    title: str | None = None
    description: str | None = None

class Snippet(BaseModel):
    model_config = ConfigDict(extra='ignore')
    published_at: AwareDatetime | None = Field(None, alias='publishedAt')
    channel_id: str | None = Field(None, alias='channelId')
    title: str | None = None
    description: str | None = None
    thumbnails: Thumbnails | None = None
    channel_title: str | None = Field(None, alias='channelTitle')
    category_id: str | None = Field(None, alias='categoryId')
    live_broadcast_content: str | None = Field(None, alias='liveBroadcastContent')
    default_language: str | None = Field(None, alias='defaultLanguage')
    localized: Localized | None = None
    default_audio_language: str | None = Field(None, alias='defaultAudioLanguage')
    tags: list[str] | None = None

class RegionRestriction(BaseModel):
    model_config = ConfigDict(extra='ignore')
    allowed: list[str] | None = None
    blocked: list[str] | None = None

class ContentDetails(BaseModel):
    model_config = ConfigDict(extra='ignore')
    duration: timedelta | None = None
    dimension: timedelta | None = None
    definition: str | None = None
    caption: str | None = None
    licensed_content: bool | None = Field(None, alias='licensedContent')
    region_restriction: RegionRestriction | None = Field(None, alias='regionRestriction')
    content_rating: dict[str, Any] | None = Field(None, alias='contentRating')
    projection: str | None = None

class Status(BaseModel):
    model_config = ConfigDict(extra='ignore')
    upload_status: str | None = Field(None, alias='uploadStatus')
    privacy_status: str | None = Field(None, alias='privacyStatus')
    license: str | None = None
    embeddable: bool | None = None
    public_stats_viewable: bool | None = Field(None, alias='publicStatsViewable')
    made_for_kids: bool | None = Field(None, alias='madeForKids')

class Statistics(BaseModel):
    model_config = ConfigDict(extra='ignore')
    like_count: str | None = Field(None, alias='likeCount')
    favorite_count: str | None = Field(None, alias='favoriteCount')
    comment_count: str | None = Field(None, alias='commentCount')
    view_count: str | None = Field(None, alias='viewCount')

class Player(BaseModel):
    model_config = ConfigDict(extra='ignore')
    embed_html: str | None = Field(None, alias='embedHtml')

class TopicDetails(BaseModel):
    model_config = ConfigDict(extra='ignore')
    topic_categories: list[str] | None = Field(None, alias='topicCategories')

class Location(BaseModel):
    model_config = ConfigDict(extra='ignore')
    latitude: float | None = None
    longitude: float | None = None
    altitude: int | None = None

class RecordingDetails(BaseModel):
    model_config = ConfigDict(extra='ignore')
    location_description: str | None = Field(None, alias='locationDescription')
    location: Location | None = None
    recording_date: AwareDatetime | None = Field(None, alias='recordingDate')

class Und(BaseModel):
    model_config = ConfigDict(extra='ignore')
    title: str | None = None
    description: str | None = None

class En(BaseModel):
    model_config = ConfigDict(extra='ignore')
    title: str | None = None
    description: str | None = None

class De(BaseModel):
    model_config = ConfigDict(extra='ignore')
    title: str | None = None
    description: str | None = None

class Id(BaseModel):
    model_config = ConfigDict(extra='ignore')
    title: str | None = None
    description: str | None = None

class NlNl(BaseModel):
    model_config = ConfigDict(extra='ignore')
    title: str | None = None
    description: str | None = None

class Ar(BaseModel):
    model_config = ConfigDict(extra='ignore')
    title: str | None = None
    description: str | None = None

class Uk(BaseModel):
    model_config = ConfigDict(extra='ignore')
    title: str | None = None
    description: str | None = None

class Bn(BaseModel):
    model_config = ConfigDict(extra='ignore')
    title: str | None = None
    description: str | None = None

class Ml(BaseModel):
    model_config = ConfigDict(extra='ignore')
    title: str | None = None
    description: str | None = None

class Ta(BaseModel):
    model_config = ConfigDict(extra='ignore')
    title: str | None = None
    description: str | None = None

class DeDe(BaseModel):
    model_config = ConfigDict(extra='ignore')
    title: str | None = None
    description: str | None = None

class Ru(BaseModel):
    model_config = ConfigDict(extra='ignore')
    title: str | None = None
    description: str | None = None

class Hi(BaseModel):
    model_config = ConfigDict(extra='ignore')
    title: str | None = None
    description: str | None = None

class It(BaseModel):
    model_config = ConfigDict(extra='ignore')
    title: str | None = None
    description: str | None = None

class Pa(BaseModel):
    model_config = ConfigDict(extra='ignore')
    title: str | None = None
    description: str | None = None

class Ko(BaseModel):
    model_config = ConfigDict(extra='ignore')
    title: str | None = None
    description: str | None = None

class Te(BaseModel):
    model_config = ConfigDict(extra='ignore')
    title: str | None = None
    description: str | None = None

class FrFr(BaseModel):
    model_config = ConfigDict(extra='ignore')
    title: str | None = None
    description: str | None = None

class Pl(BaseModel):
    model_config = ConfigDict(extra='ignore')
    title: str | None = None
    description: str | None = None

class Iw(BaseModel):
    model_config = ConfigDict(extra='ignore')
    title: str | None = None
    description: str | None = None

class PtBr(BaseModel):
    model_config = ConfigDict(extra='ignore')
    title: str | None = None
    description: str | None = None

class Ja(BaseModel):
    model_config = ConfigDict(extra='ignore')
    title: str | None = None
    description: str | None = None

class EsUs(BaseModel):
    model_config = ConfigDict(extra='ignore')
    title: str | None = None
    description: str | None = None

class EnGb(BaseModel):
    model_config = ConfigDict(extra='ignore')
    title: str | None = None
    description: str | None = None

class Localizations(BaseModel):
    model_config = ConfigDict(extra='ignore')
    und: Und | None = None
    en: En | None = None
    de: De | None = None
    id: Id | None = None
    nl_nl: NlNl | None = Field(None, alias='nl-NL')
    ar: Ar | None = None
    uk: Uk | None = None
    bn: Bn | None = None
    ml: Ml | None = None
    ta: Ta | None = None
    de_de: DeDe | None = Field(None, alias='de-DE')
    ru: Ru | None = None
    hi: Hi | None = None
    it: It | None = None
    pa: Pa | None = None
    ko: Ko | None = None
    te: Te | None = None
    fr_fr: FrFr | None = Field(None, alias='fr-FR')
    pl: Pl | None = None
    iw: Iw | None = None
    pt_br: PtBr | None = Field(None, alias='pt-BR')
    ja: Ja | None = None
    es_us: EsUs | None = Field(None, alias='es-US')
    en_gb: EnGb | None = Field(None, alias='en-GB')

class PaidProductPlacementDetails(BaseModel):
    model_config = ConfigDict(extra='ignore')
    has_paid_product_placement: bool | None = Field(None, alias='hasPaidProductPlacement')

class LiveStreamingDetails(BaseModel):
    model_config = ConfigDict(extra='ignore')
    actual_start_time: AwareDatetime | None = Field(None, alias='actualStartTime')
    actual_end_time: AwareDatetime | None = Field(None, alias='actualEndTime')
    scheduled_start_time: AwareDatetime | None = Field(None, alias='scheduledStartTime')

class Item(BaseModel):
    model_config = ConfigDict(extra='ignore')
    kind: str | None = None
    etag: str | None = None
    id: str | None = None
    snippet: Snippet | None = None
    content_details: ContentDetails | None = Field(None, alias='contentDetails')
    status: Status | None = None
    statistics: Statistics | None = None
    player: Player | None = None
    topic_details: TopicDetails | None = Field(None, alias='topicDetails')
    recording_details: RecordingDetails | None = Field(None, alias='recordingDetails')
    localizations: Localizations | None = None
    paid_product_placement_details: PaidProductPlacementDetails | None = Field(None, alias='paidProductPlacementDetails')
    live_streaming_details: LiveStreamingDetails | None = Field(None, alias='liveStreamingDetails')

class PageInfo(BaseModel):
    model_config = ConfigDict(extra='ignore')
    total_results: int | None = Field(None, alias='totalResults')
    results_per_page: int | None = Field(None, alias='resultsPerPage')

class VideosModel(BaseModel):
    model_config = ConfigDict(extra='ignore')
    kind: str | None = None
    etag: str | None = None
    items: list[Item] | None = None
    page_info: PageInfo | None = Field(None, alias='pageInfo')
    _raw_input: Any = PrivateAttr(default=None)

    @model_validator(mode='wrap')
    @classmethod
    def _capture_raw_input(cls, data: Any, handler: ModelWrapValidatorHandler[Self]) -> Self:
        """Validate the model and keep the input it was built from."""
        model = handler(data)
        model._raw_input = data
        return model

    @property
    def raw_input(self) -> Any:
        """The input this model was validated from, as it was handed over."""
        return self._raw_input
