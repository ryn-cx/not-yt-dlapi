from typing import Self
from pydantic import ModelWrapValidatorHandler, PrivateAttr, model_validator
from pydantic import ConfigDict
from pydantic import AwareDatetime, BaseModel, Field
from datetime import timedelta
from typing import Any

class Default(BaseModel):
    model_config = ConfigDict(defer_build=True)
    url: str
    width: int
    height: int

class Medium(BaseModel):
    model_config = ConfigDict(defer_build=True)
    url: str
    width: int
    height: int

class High(BaseModel):
    model_config = ConfigDict(defer_build=True)
    url: str
    width: int
    height: int

class Standard(BaseModel):
    model_config = ConfigDict(defer_build=True)
    url: str
    width: int
    height: int

class Maxres(BaseModel):
    model_config = ConfigDict(defer_build=True)
    url: str
    width: int
    height: int

class Thumbnails(BaseModel):
    model_config = ConfigDict(defer_build=True)
    default: Default
    medium: Medium
    high: High
    standard: Standard | None = None
    maxres: Maxres | None = None

class Localized(BaseModel):
    model_config = ConfigDict(defer_build=True)
    title: str
    description: str

class Snippet(BaseModel):
    model_config = ConfigDict(defer_build=True)
    published_at: AwareDatetime = Field(..., alias='publishedAt')
    channel_id: str = Field(..., alias='channelId')
    title: str
    description: str
    thumbnails: Thumbnails
    channel_title: str = Field(..., alias='channelTitle')
    tags: list[str] | None = None
    category_id: str = Field(..., alias='categoryId')
    live_broadcast_content: str = Field(..., alias='liveBroadcastContent')
    default_language: str = Field(..., alias='defaultLanguage')
    localized: Localized
    default_audio_language: str | None = Field(None, alias='defaultAudioLanguage')

class RegionRestriction(BaseModel):
    model_config = ConfigDict(defer_build=True)
    blocked: list[str] | None = None
    allowed: list[str] | None = None

class ContentDetails(BaseModel):
    model_config = ConfigDict(defer_build=True)
    duration: timedelta
    dimension: timedelta
    definition: str
    caption: str
    licensed_content: bool = Field(..., alias='licensedContent')
    content_rating: dict[str, Any] = Field(..., alias='contentRating')
    projection: str
    region_restriction: RegionRestriction | None = Field(None, alias='regionRestriction')

class Status(BaseModel):
    model_config = ConfigDict(defer_build=True)
    upload_status: str = Field(..., alias='uploadStatus')
    privacy_status: str = Field(..., alias='privacyStatus')
    license: str
    embeddable: bool
    public_stats_viewable: bool = Field(..., alias='publicStatsViewable')
    made_for_kids: bool = Field(..., alias='madeForKids')

class Statistics(BaseModel):
    model_config = ConfigDict(defer_build=True)
    view_count: str | None = Field(None, alias='viewCount')
    like_count: str = Field(..., alias='likeCount')
    favorite_count: str = Field(..., alias='favoriteCount')
    comment_count: str = Field(..., alias='commentCount')

class Player(BaseModel):
    model_config = ConfigDict(defer_build=True)
    embed_html: str = Field(..., alias='embedHtml')

class TopicDetails(BaseModel):
    model_config = ConfigDict(defer_build=True)
    topic_categories: list[str] = Field(..., alias='topicCategories')

class Location(BaseModel):
    model_config = ConfigDict(defer_build=True)
    latitude: float
    longitude: float
    altitude: int

class RecordingDetails(BaseModel):
    model_config = ConfigDict(defer_build=True)
    location_description: str | None = Field(None, alias='locationDescription')
    location: Location | None = None
    recording_date: AwareDatetime | None = Field(None, alias='recordingDate')

class Id(BaseModel):
    model_config = ConfigDict(defer_build=True)
    title: str
    description: str

class Ml(BaseModel):
    model_config = ConfigDict(defer_build=True)
    title: str
    description: str

class Ru(BaseModel):
    model_config = ConfigDict(defer_build=True)
    title: str | None = None
    description: str

class Ja(BaseModel):
    model_config = ConfigDict(defer_build=True)
    title: str
    description: str

class Bn(BaseModel):
    model_config = ConfigDict(defer_build=True)
    title: str
    description: str

class Hi(BaseModel):
    model_config = ConfigDict(defer_build=True)
    title: str
    description: str

class Te(BaseModel):
    model_config = ConfigDict(defer_build=True)
    title: str
    description: str

class En(BaseModel):
    model_config = ConfigDict(defer_build=True)
    title: str
    description: str

class NlNl(BaseModel):
    model_config = ConfigDict(defer_build=True)
    title: str
    description: str

class Iw(BaseModel):
    model_config = ConfigDict(defer_build=True)
    title: str
    description: str

class It(BaseModel):
    model_config = ConfigDict(defer_build=True)
    title: str
    description: str

class Ko(BaseModel):
    model_config = ConfigDict(defer_build=True)
    title: str
    description: str

class EsUs(BaseModel):
    model_config = ConfigDict(defer_build=True)
    title: str
    description: str

class Ta(BaseModel):
    model_config = ConfigDict(defer_build=True)
    title: str
    description: str

class DeDe(BaseModel):
    model_config = ConfigDict(defer_build=True)
    title: str
    description: str

class FrFr(BaseModel):
    model_config = ConfigDict(defer_build=True)
    title: str
    description: str

class PtBr(BaseModel):
    model_config = ConfigDict(defer_build=True)
    title: str
    description: str

class Pl(BaseModel):
    model_config = ConfigDict(defer_build=True)
    title: str
    description: str

class Uk(BaseModel):
    model_config = ConfigDict(defer_build=True)
    title: str
    description: str

class Pa(BaseModel):
    model_config = ConfigDict(defer_build=True)
    title: str
    description: str

class Ar(BaseModel):
    model_config = ConfigDict(defer_build=True)
    title: str
    description: str

class EnGb(BaseModel):
    model_config = ConfigDict(defer_build=True)
    title: str
    description: str

class Und(BaseModel):
    model_config = ConfigDict(defer_build=True)
    title: str
    description: str

class De(BaseModel):
    model_config = ConfigDict(defer_build=True)
    title: str
    description: str

class Localizations(BaseModel):
    model_config = ConfigDict(defer_build=True)
    id: Id | None = None
    ml: Ml | None = None
    ru: Ru | None = None
    ja: Ja | None = None
    bn: Bn | None = None
    hi: Hi | None = None
    te: Te | None = None
    en: En | None = None
    nl_nl: NlNl | None = Field(None, alias='nl-NL')
    iw: Iw | None = None
    it: It | None = None
    ko: Ko | None = None
    es_us: EsUs | None = Field(None, alias='es-US')
    ta: Ta | None = None
    de_de: DeDe | None = Field(None, alias='de-DE')
    fr_fr: FrFr | None = Field(None, alias='fr-FR')
    pt_br: PtBr | None = Field(None, alias='pt-BR')
    pl: Pl | None = None
    uk: Uk | None = None
    pa: Pa | None = None
    ar: Ar | None = None
    en_gb: EnGb | None = Field(None, alias='en-GB')
    und: Und | None = None
    de: De | None = None

class PaidProductPlacementDetails(BaseModel):
    model_config = ConfigDict(defer_build=True)
    has_paid_product_placement: bool = Field(..., alias='hasPaidProductPlacement')

class LiveStreamingDetails(BaseModel):
    model_config = ConfigDict(defer_build=True)
    actual_start_time: AwareDatetime | None = Field(None, alias='actualStartTime')
    actual_end_time: AwareDatetime | None = Field(None, alias='actualEndTime')
    scheduled_start_time: AwareDatetime | None = Field(None, alias='scheduledStartTime')
    active_live_chat_id: str | None = Field(None, alias='activeLiveChatId')

class Item(BaseModel):
    model_config = ConfigDict(defer_build=True)
    kind: str
    etag: str
    id: str
    snippet: Snippet
    content_details: ContentDetails = Field(..., alias='contentDetails')
    status: Status
    statistics: Statistics
    player: Player
    topic_details: TopicDetails | None = Field(None, alias='topicDetails')
    recording_details: RecordingDetails = Field(..., alias='recordingDetails')
    localizations: Localizations
    paid_product_placement_details: PaidProductPlacementDetails = Field(..., alias='paidProductPlacementDetails')
    live_streaming_details: LiveStreamingDetails | None = Field(None, alias='liveStreamingDetails')

class PageInfo(BaseModel):
    model_config = ConfigDict(defer_build=True)
    total_results: int = Field(..., alias='totalResults')
    results_per_page: int = Field(..., alias='resultsPerPage')

class VideosModel(BaseModel):
    model_config = ConfigDict(defer_build=True)
    kind: str
    etag: str
    items: list[Item]
    page_info: PageInfo = Field(..., alias='pageInfo')
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
