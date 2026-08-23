from typing import Self
from pydantic import ModelWrapValidatorHandler, PrivateAttr, model_validator
from pydantic import AwareDatetime, BaseModel, Field
from datetime import timedelta
from typing import Any

class Default(BaseModel):
    url: str
    width: int
    height: int

class Medium(BaseModel):
    url: str
    width: int
    height: int

class High(BaseModel):
    url: str
    width: int
    height: int

class Standard(BaseModel):
    url: str
    width: int
    height: int

class Maxres(BaseModel):
    url: str
    width: int
    height: int

class Thumbnails(BaseModel):
    default: Default
    medium: Medium
    high: High
    standard: Standard | None = None
    maxres: Maxres | None = None

class Localized(BaseModel):
    title: str
    description: str

class Snippet(BaseModel):
    published_at: AwareDatetime = Field(..., alias='publishedAt')
    channel_id: str = Field(..., alias='channelId')
    title: str
    description: str
    thumbnails: Thumbnails
    channel_title: str = Field(..., alias='channelTitle')
    category_id: str = Field(..., alias='categoryId')
    live_broadcast_content: str = Field(..., alias='liveBroadcastContent')
    default_language: str = Field(..., alias='defaultLanguage')
    localized: Localized
    default_audio_language: str | None = Field(None, alias='defaultAudioLanguage')
    tags: list[str] | None = None

class RegionRestriction(BaseModel):
    allowed: list[str] | None = None
    blocked: list[str] | None = None

class ContentDetails(BaseModel):
    duration: timedelta
    dimension: timedelta
    definition: str
    caption: str
    licensed_content: bool = Field(..., alias='licensedContent')
    region_restriction: RegionRestriction | None = Field(None, alias='regionRestriction')
    content_rating: dict[str, Any] = Field(..., alias='contentRating')
    projection: str

class Status(BaseModel):
    upload_status: str = Field(..., alias='uploadStatus')
    privacy_status: str = Field(..., alias='privacyStatus')
    license: str
    embeddable: bool
    public_stats_viewable: bool = Field(..., alias='publicStatsViewable')
    made_for_kids: bool = Field(..., alias='madeForKids')

class Statistics(BaseModel):
    like_count: str = Field(..., alias='likeCount')
    favorite_count: str = Field(..., alias='favoriteCount')
    comment_count: str | None = Field(None, alias='commentCount')
    view_count: str | None = Field(None, alias='viewCount')

class Player(BaseModel):
    embed_html: str = Field(..., alias='embedHtml')

class TopicDetails(BaseModel):
    topic_categories: list[str] = Field(..., alias='topicCategories')

class Location(BaseModel):
    latitude: float
    longitude: float
    altitude: int

class RecordingDetails(BaseModel):
    location_description: str | None = Field(None, alias='locationDescription')
    location: Location | None = None
    recording_date: AwareDatetime | None = Field(None, alias='recordingDate')

class Und(BaseModel):
    title: str
    description: str

class En(BaseModel):
    title: str
    description: str

class De(BaseModel):
    title: str
    description: str

class Id(BaseModel):
    title: str
    description: str

class NlNl(BaseModel):
    title: str
    description: str

class Ar(BaseModel):
    title: str
    description: str

class Uk(BaseModel):
    title: str
    description: str

class Bn(BaseModel):
    title: str
    description: str

class Ml(BaseModel):
    title: str
    description: str

class Ta(BaseModel):
    title: str
    description: str

class DeDe(BaseModel):
    title: str
    description: str

class Ru(BaseModel):
    title: str | None = None
    description: str

class Hi(BaseModel):
    title: str
    description: str

class It(BaseModel):
    title: str
    description: str

class Pa(BaseModel):
    title: str
    description: str

class Ko(BaseModel):
    title: str
    description: str

class Te(BaseModel):
    title: str
    description: str

class FrFr(BaseModel):
    title: str
    description: str

class Pl(BaseModel):
    title: str
    description: str

class Iw(BaseModel):
    title: str
    description: str

class PtBr(BaseModel):
    title: str
    description: str

class Ja(BaseModel):
    title: str
    description: str

class EsUs(BaseModel):
    title: str
    description: str

class EnGb(BaseModel):
    title: str
    description: str

class Localizations(BaseModel):
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
    has_paid_product_placement: bool = Field(..., alias='hasPaidProductPlacement')

class LiveStreamingDetails(BaseModel):
    actual_start_time: AwareDatetime = Field(..., alias='actualStartTime')
    actual_end_time: AwareDatetime = Field(..., alias='actualEndTime')
    scheduled_start_time: AwareDatetime = Field(..., alias='scheduledStartTime')

class Item(BaseModel):
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
    total_results: int = Field(..., alias='totalResults')
    results_per_page: int = Field(..., alias='resultsPerPage')

class VideosModel(BaseModel):
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
