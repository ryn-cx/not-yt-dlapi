from typing import Self
from pydantic import ModelWrapValidatorHandler, PrivateAttr, model_validator
from pydantic import AwareDatetime, BaseModel, ConfigDict, Field
from datetime import timedelta
from typing import Any

class Default(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    url: str | Any = Field(default=None, union_mode='left_to_right')
    width: int | Any = Field(default=None, union_mode='left_to_right')
    height: int | Any = Field(default=None, union_mode='left_to_right')

class Medium(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    url: str | Any = Field(default=None, union_mode='left_to_right')
    width: int | Any = Field(default=None, union_mode='left_to_right')
    height: int | Any = Field(default=None, union_mode='left_to_right')

class High(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    url: str | Any = Field(default=None, union_mode='left_to_right')
    width: int | Any = Field(default=None, union_mode='left_to_right')
    height: int | Any = Field(default=None, union_mode='left_to_right')

class Standard(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    url: str | Any = Field(default=None, union_mode='left_to_right')
    width: int | Any = Field(default=None, union_mode='left_to_right')
    height: int | Any = Field(default=None, union_mode='left_to_right')

class Maxres(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    url: str | Any = Field(default=None, union_mode='left_to_right')
    width: int | Any = Field(default=None, union_mode='left_to_right')
    height: int | Any = Field(default=None, union_mode='left_to_right')

class Thumbnails(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    default: Default | Any = Field(default=None, union_mode='left_to_right')
    medium: Medium | Any = Field(default=None, union_mode='left_to_right')
    high: High | Any = Field(default=None, union_mode='left_to_right')
    standard: Standard | Any = Field(default=None, union_mode='left_to_right')
    maxres: Maxres | Any = Field(default=None, union_mode='left_to_right')

class Localized(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    title: str | Any = Field(default=None, union_mode='left_to_right')
    description: str | Any = Field(default=None, union_mode='left_to_right')

class Snippet(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    published_at: AwareDatetime | Any = Field(None, alias='publishedAt', union_mode='left_to_right')
    channel_id: str | Any = Field(None, alias='channelId', union_mode='left_to_right')
    title: str | Any = Field(default=None, union_mode='left_to_right')
    description: str | Any = Field(default=None, union_mode='left_to_right')
    thumbnails: Thumbnails | Any = Field(default=None, union_mode='left_to_right')
    channel_title: str | Any = Field(None, alias='channelTitle', union_mode='left_to_right')
    tags: list[str] | Any = Field(default=None, union_mode='left_to_right')
    category_id: str | Any = Field(None, alias='categoryId', union_mode='left_to_right')
    live_broadcast_content: str | Any = Field(None, alias='liveBroadcastContent', union_mode='left_to_right')
    default_language: str | Any = Field(None, alias='defaultLanguage', union_mode='left_to_right')
    localized: Localized | Any = Field(default=None, union_mode='left_to_right')
    default_audio_language: str | Any = Field(None, alias='defaultAudioLanguage', union_mode='left_to_right')

class RegionRestriction(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    blocked: list[str] | Any = Field(default=None, union_mode='left_to_right')
    allowed: list[str] | Any = Field(default=None, union_mode='left_to_right')

class ContentDetails(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    duration: timedelta | Any = Field(default=None, union_mode='left_to_right')
    dimension: timedelta | Any = Field(default=None, union_mode='left_to_right')
    definition: str | Any = Field(default=None, union_mode='left_to_right')
    caption: str | Any = Field(default=None, union_mode='left_to_right')
    licensed_content: bool | Any = Field(None, alias='licensedContent', union_mode='left_to_right')
    content_rating: dict[str, Any] | Any = Field(None, alias='contentRating', union_mode='left_to_right')
    projection: str | Any = Field(default=None, union_mode='left_to_right')
    region_restriction: RegionRestriction | Any = Field(None, alias='regionRestriction', union_mode='left_to_right')

class Status(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    upload_status: str | Any = Field(None, alias='uploadStatus', union_mode='left_to_right')
    privacy_status: str | Any = Field(None, alias='privacyStatus', union_mode='left_to_right')
    license: str | Any = Field(default=None, union_mode='left_to_right')
    embeddable: bool | Any = Field(default=None, union_mode='left_to_right')
    public_stats_viewable: bool | Any = Field(None, alias='publicStatsViewable', union_mode='left_to_right')
    made_for_kids: bool | Any = Field(None, alias='madeForKids', union_mode='left_to_right')

class Statistics(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    view_count: str | Any = Field(None, alias='viewCount', union_mode='left_to_right')
    like_count: str | Any = Field(None, alias='likeCount', union_mode='left_to_right')
    favorite_count: str | Any = Field(None, alias='favoriteCount', union_mode='left_to_right')
    comment_count: str | Any = Field(None, alias='commentCount', union_mode='left_to_right')

class Player(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    embed_html: str | Any = Field(None, alias='embedHtml', union_mode='left_to_right')

class TopicDetails(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    topic_categories: list[str] | Any = Field(None, alias='topicCategories', union_mode='left_to_right')

class Location(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    latitude: float | Any = Field(default=None, union_mode='left_to_right')
    longitude: float | Any = Field(default=None, union_mode='left_to_right')
    altitude: int | Any = Field(default=None, union_mode='left_to_right')

class RecordingDetails(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    location_description: str | Any = Field(None, alias='locationDescription', union_mode='left_to_right')
    location: Location | Any = Field(default=None, union_mode='left_to_right')
    recording_date: AwareDatetime | Any = Field(None, alias='recordingDate', union_mode='left_to_right')

class Id(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    title: str | Any = Field(default=None, union_mode='left_to_right')
    description: str | Any = Field(default=None, union_mode='left_to_right')

class Ml(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    title: str | Any = Field(default=None, union_mode='left_to_right')
    description: str | Any = Field(default=None, union_mode='left_to_right')

class Ru(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    title: str | Any = Field(default=None, union_mode='left_to_right')
    description: str | Any = Field(default=None, union_mode='left_to_right')

class Ja(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    title: str | Any = Field(default=None, union_mode='left_to_right')
    description: str | Any = Field(default=None, union_mode='left_to_right')

class Bn(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    title: str | Any = Field(default=None, union_mode='left_to_right')
    description: str | Any = Field(default=None, union_mode='left_to_right')

class Hi(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    title: str | Any = Field(default=None, union_mode='left_to_right')
    description: str | Any = Field(default=None, union_mode='left_to_right')

class Te(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    title: str | Any = Field(default=None, union_mode='left_to_right')
    description: str | Any = Field(default=None, union_mode='left_to_right')

class En(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    title: str | Any = Field(default=None, union_mode='left_to_right')
    description: str | Any = Field(default=None, union_mode='left_to_right')

class NlNl(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    title: str | Any = Field(default=None, union_mode='left_to_right')
    description: str | Any = Field(default=None, union_mode='left_to_right')

class Iw(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    title: str | Any = Field(default=None, union_mode='left_to_right')
    description: str | Any = Field(default=None, union_mode='left_to_right')

class It(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    title: str | Any = Field(default=None, union_mode='left_to_right')
    description: str | Any = Field(default=None, union_mode='left_to_right')

class Ko(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    title: str | Any = Field(default=None, union_mode='left_to_right')
    description: str | Any = Field(default=None, union_mode='left_to_right')

class EsUs(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    title: str | Any = Field(default=None, union_mode='left_to_right')
    description: str | Any = Field(default=None, union_mode='left_to_right')

class Ta(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    title: str | Any = Field(default=None, union_mode='left_to_right')
    description: str | Any = Field(default=None, union_mode='left_to_right')

class DeDe(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    title: str | Any = Field(default=None, union_mode='left_to_right')
    description: str | Any = Field(default=None, union_mode='left_to_right')

class FrFr(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    title: str | Any = Field(default=None, union_mode='left_to_right')
    description: str | Any = Field(default=None, union_mode='left_to_right')

class PtBr(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    title: str | Any = Field(default=None, union_mode='left_to_right')
    description: str | Any = Field(default=None, union_mode='left_to_right')

class Pl(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    title: str | Any = Field(default=None, union_mode='left_to_right')
    description: str | Any = Field(default=None, union_mode='left_to_right')

class Uk(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    title: str | Any = Field(default=None, union_mode='left_to_right')
    description: str | Any = Field(default=None, union_mode='left_to_right')

class Pa(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    title: str | Any = Field(default=None, union_mode='left_to_right')
    description: str | Any = Field(default=None, union_mode='left_to_right')

class Ar(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    title: str | Any = Field(default=None, union_mode='left_to_right')
    description: str | Any = Field(default=None, union_mode='left_to_right')

class EnGb(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    title: str | Any = Field(default=None, union_mode='left_to_right')
    description: str | Any = Field(default=None, union_mode='left_to_right')

class Und(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    title: str | Any = Field(default=None, union_mode='left_to_right')
    description: str | Any = Field(default=None, union_mode='left_to_right')

class De(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    title: str | Any = Field(default=None, union_mode='left_to_right')
    description: str | Any = Field(default=None, union_mode='left_to_right')

class Localizations(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    id: Id | Any = Field(default=None, union_mode='left_to_right')
    ml: Ml | Any = Field(default=None, union_mode='left_to_right')
    ru: Ru | Any = Field(default=None, union_mode='left_to_right')
    ja: Ja | Any = Field(default=None, union_mode='left_to_right')
    bn: Bn | Any = Field(default=None, union_mode='left_to_right')
    hi: Hi | Any = Field(default=None, union_mode='left_to_right')
    te: Te | Any = Field(default=None, union_mode='left_to_right')
    en: En | Any = Field(default=None, union_mode='left_to_right')
    nl_nl: NlNl | Any = Field(None, alias='nl-NL', union_mode='left_to_right')
    iw: Iw | Any = Field(default=None, union_mode='left_to_right')
    it: It | Any = Field(default=None, union_mode='left_to_right')
    ko: Ko | Any = Field(default=None, union_mode='left_to_right')
    es_us: EsUs | Any = Field(None, alias='es-US', union_mode='left_to_right')
    ta: Ta | Any = Field(default=None, union_mode='left_to_right')
    de_de: DeDe | Any = Field(None, alias='de-DE', union_mode='left_to_right')
    fr_fr: FrFr | Any = Field(None, alias='fr-FR', union_mode='left_to_right')
    pt_br: PtBr | Any = Field(None, alias='pt-BR', union_mode='left_to_right')
    pl: Pl | Any = Field(default=None, union_mode='left_to_right')
    uk: Uk | Any = Field(default=None, union_mode='left_to_right')
    pa: Pa | Any = Field(default=None, union_mode='left_to_right')
    ar: Ar | Any = Field(default=None, union_mode='left_to_right')
    en_gb: EnGb | Any = Field(None, alias='en-GB', union_mode='left_to_right')
    und: Und | Any = Field(default=None, union_mode='left_to_right')
    de: De | Any = Field(default=None, union_mode='left_to_right')

class PaidProductPlacementDetails(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    has_paid_product_placement: bool | Any = Field(None, alias='hasPaidProductPlacement', union_mode='left_to_right')

class LiveStreamingDetails(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    actual_start_time: AwareDatetime | Any = Field(None, alias='actualStartTime', union_mode='left_to_right')
    actual_end_time: AwareDatetime | Any = Field(None, alias='actualEndTime', union_mode='left_to_right')
    scheduled_start_time: AwareDatetime | Any = Field(None, alias='scheduledStartTime', union_mode='left_to_right')
    active_live_chat_id: str | Any = Field(None, alias='activeLiveChatId', union_mode='left_to_right')

class Item(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    kind: str | Any = Field(default=None, union_mode='left_to_right')
    etag: str | Any = Field(default=None, union_mode='left_to_right')
    id: str | Any = Field(default=None, union_mode='left_to_right')
    snippet: Snippet | Any = Field(default=None, union_mode='left_to_right')
    content_details: ContentDetails | Any = Field(None, alias='contentDetails', union_mode='left_to_right')
    status: Status | Any = Field(default=None, union_mode='left_to_right')
    statistics: Statistics | Any = Field(default=None, union_mode='left_to_right')
    player: Player | Any = Field(default=None, union_mode='left_to_right')
    topic_details: TopicDetails | Any = Field(None, alias='topicDetails', union_mode='left_to_right')
    recording_details: RecordingDetails | Any = Field(None, alias='recordingDetails', union_mode='left_to_right')
    localizations: Localizations | Any = Field(default=None, union_mode='left_to_right')
    paid_product_placement_details: PaidProductPlacementDetails | Any = Field(None, alias='paidProductPlacementDetails', union_mode='left_to_right')
    live_streaming_details: LiveStreamingDetails | Any = Field(None, alias='liveStreamingDetails', union_mode='left_to_right')

class PageInfo(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    total_results: int | Any = Field(None, alias='totalResults', union_mode='left_to_right')
    results_per_page: int | Any = Field(None, alias='resultsPerPage', union_mode='left_to_right')

class VideosModel(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    kind: str | Any = Field(default=None, union_mode='left_to_right')
    etag: str | Any = Field(default=None, union_mode='left_to_right')
    items: list[Item] | Any = Field(default=None, union_mode='left_to_right')
    page_info: PageInfo | Any = Field(None, alias='pageInfo', union_mode='left_to_right')
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
