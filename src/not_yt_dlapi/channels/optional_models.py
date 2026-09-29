from typing import Self
from pydantic import ModelWrapValidatorHandler, PrivateAttr, model_validator
from pydantic import AwareDatetime, BaseModel, ConfigDict, Field
from typing import Any

class PageInfo(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    total_results: int | Any = Field(None, alias='totalResults', union_mode='left_to_right')
    results_per_page: int | Any = Field(None, alias='resultsPerPage', union_mode='left_to_right')

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

class Thumbnails(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    default: Default | Any = Field(default=None, union_mode='left_to_right')
    medium: Medium | Any = Field(default=None, union_mode='left_to_right')
    high: High | Any = Field(default=None, union_mode='left_to_right')

class Localized(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    title: str | Any = Field(default=None, union_mode='left_to_right')
    description: str | Any = Field(default=None, union_mode='left_to_right')

class Snippet(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    title: str | Any = Field(default=None, union_mode='left_to_right')
    description: str | Any = Field(default=None, union_mode='left_to_right')
    custom_url: str | Any = Field(None, alias='customUrl', union_mode='left_to_right')
    published_at: AwareDatetime | Any = Field(None, alias='publishedAt', union_mode='left_to_right')
    thumbnails: Thumbnails | Any = Field(default=None, union_mode='left_to_right')
    localized: Localized | Any = Field(default=None, union_mode='left_to_right')
    country: str | Any = Field(default=None, union_mode='left_to_right')

class RelatedPlaylists(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    likes: str | Any = Field(default=None, union_mode='left_to_right')
    uploads: str | Any = Field(default=None, union_mode='left_to_right')

class ContentDetails(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    related_playlists: RelatedPlaylists | Any = Field(None, alias='relatedPlaylists', union_mode='left_to_right')

class Statistics(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    view_count: str | Any = Field(None, alias='viewCount', union_mode='left_to_right')
    subscriber_count: str | Any = Field(None, alias='subscriberCount', union_mode='left_to_right')
    hidden_subscriber_count: bool | Any = Field(None, alias='hiddenSubscriberCount', union_mode='left_to_right')
    video_count: str | Any = Field(None, alias='videoCount', union_mode='left_to_right')

class Status(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    privacy_status: str | Any = Field(None, alias='privacyStatus', union_mode='left_to_right')
    is_linked: bool | Any = Field(None, alias='isLinked', union_mode='left_to_right')
    long_uploads_status: str | Any = Field(None, alias='longUploadsStatus', union_mode='left_to_right')
    made_for_kids: bool | Any = Field(None, alias='madeForKids', union_mode='left_to_right')

class Channel(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    title: str | Any = Field(default=None, union_mode='left_to_right')
    keywords: str | Any = Field(default=None, union_mode='left_to_right')
    unsubscribed_trailer: str | Any = Field(None, alias='unsubscribedTrailer', union_mode='left_to_right')
    country: str | Any = Field(default=None, union_mode='left_to_right')
    description: str | Any = Field(default=None, union_mode='left_to_right')

class Image(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    banner_external_url: str | Any = Field(None, alias='bannerExternalUrl', union_mode='left_to_right')

class BrandingSettings(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    channel: Channel | Any = Field(default=None, union_mode='left_to_right')
    image: Image | Any = Field(default=None, union_mode='left_to_right')

class TopicDetails(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    topic_ids: list[str] | Any = Field(None, alias='topicIds', union_mode='left_to_right')
    topic_categories: list[str] | Any = Field(None, alias='topicCategories', union_mode='left_to_right')

class Ne(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    title: str | Any = Field(default=None, union_mode='left_to_right')
    description: str | Any = Field(default=None, union_mode='left_to_right')

class Bn(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    title: str | Any = Field(default=None, union_mode='left_to_right')
    description: str | Any = Field(default=None, union_mode='left_to_right')

class Hy(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    title: str | Any = Field(default=None, union_mode='left_to_right')
    description: str | Any = Field(default=None, union_mode='left_to_right')

class Ru(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    title: str | Any = Field(default=None, union_mode='left_to_right')
    description: str | Any = Field(default=None, union_mode='left_to_right')

class EsUs(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    title: str | Any = Field(default=None, union_mode='left_to_right')
    description: str | Any = Field(default=None, union_mode='left_to_right')

class Hr(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    title: str | Any = Field(default=None, union_mode='left_to_right')
    description: str | Any = Field(default=None, union_mode='left_to_right')

class Hi(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    title: str | Any = Field(default=None, union_mode='left_to_right')
    description: str | Any = Field(default=None, union_mode='left_to_right')

class Pa(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    title: str | Any = Field(default=None, union_mode='left_to_right')
    description: str | Any = Field(default=None, union_mode='left_to_right')

class EnIn(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    title: str | Any = Field(default=None, union_mode='left_to_right')
    description: str | Any = Field(default=None, union_mode='left_to_right')

class Eu(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    title: str | Any = Field(default=None, union_mode='left_to_right')
    description: str | Any = Field(default=None, union_mode='left_to_right')

class PtPt(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    title: str | Any = Field(default=None, union_mode='left_to_right')
    description: str | Any = Field(default=None, union_mode='left_to_right')

class Hu(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    title: str | Any = Field(default=None, union_mode='left_to_right')
    description: str | Any = Field(default=None, union_mode='left_to_right')

class Sk(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    title: str | Any = Field(default=None, union_mode='left_to_right')
    description: str | Any = Field(default=None, union_mode='left_to_right')

class Ta(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    title: str | Any = Field(default=None, union_mode='left_to_right')
    description: str | Any = Field(default=None, union_mode='left_to_right')

class Lo(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    title: str | Any = Field(default=None, union_mode='left_to_right')
    description: str | Any = Field(default=None, union_mode='left_to_right')

class Sq(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    title: str | Any = Field(default=None, union_mode='left_to_right')
    description: str | Any = Field(default=None, union_mode='left_to_right')

class Ja(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    title: str | Any = Field(default=None, union_mode='left_to_right')
    description: str | Any = Field(default=None, union_mode='left_to_right')

class Km(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    title: str | Any = Field(default=None, union_mode='left_to_right')
    description: str | Any = Field(default=None, union_mode='left_to_right')

class Af(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    title: str | Any = Field(default=None, union_mode='left_to_right')
    description: str | Any = Field(default=None, union_mode='left_to_right')

class Es(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    title: str | Any = Field(default=None, union_mode='left_to_right')
    description: str | Any = Field(default=None, union_mode='left_to_right')

class Ur(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    title: str | Any = Field(default=None, union_mode='left_to_right')
    description: str | Any = Field(default=None, union_mode='left_to_right')

class Et(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    title: str | Any = Field(default=None, union_mode='left_to_right')
    description: str | Any = Field(default=None, union_mode='left_to_right')

class Iw(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    title: str | Any = Field(default=None, union_mode='left_to_right')
    description: str | Any = Field(default=None, union_mode='left_to_right')

class Sr(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    title: str | Any = Field(default=None, union_mode='left_to_right')
    description: str | Any = Field(default=None, union_mode='left_to_right')

class Fi(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    title: str | Any = Field(default=None, union_mode='left_to_right')
    description: str | Any = Field(default=None, union_mode='left_to_right')

class Da(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    title: str | Any = Field(default=None, union_mode='left_to_right')
    description: str | Any = Field(default=None, union_mode='left_to_right')

class ZhTw(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    title: str | Any = Field(default=None, union_mode='left_to_right')
    description: str | Any = Field(default=None, union_mode='left_to_right')

class De(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    title: str | Any = Field(default=None, union_mode='left_to_right')
    description: str | Any = Field(default=None, union_mode='left_to_right')

class Cs(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    title: str | Any = Field(default=None, union_mode='left_to_right')
    description: str | Any = Field(default=None, union_mode='left_to_right')

class Bs(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    title: str | Any = Field(default=None, union_mode='left_to_right')
    description: str | Any = Field(default=None, union_mode='left_to_right')

class As(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    title: str | Any = Field(default=None, union_mode='left_to_right')
    description: str | Any = Field(default=None, union_mode='left_to_right')

class My(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    title: str | Any = Field(default=None, union_mode='left_to_right')
    description: str | Any = Field(default=None, union_mode='left_to_right')

class Sl(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    title: str | Any = Field(default=None, union_mode='left_to_right')
    description: str | Any = Field(default=None, union_mode='left_to_right')

class It(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    title: str | Any = Field(default=None, union_mode='left_to_right')
    description: str | Any = Field(default=None, union_mode='left_to_right')

class Id(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    title: str | Any = Field(default=None, union_mode='left_to_right')
    description: str | Any = Field(default=None, union_mode='left_to_right')

class Be(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    title: str | Any = Field(default=None, union_mode='left_to_right')
    description: str | Any = Field(default=None, union_mode='left_to_right')

class Pl(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    title: str | Any = Field(default=None, union_mode='left_to_right')
    description: str | Any = Field(default=None, union_mode='left_to_right')

class EnGb(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    title: str | Any = Field(default=None, union_mode='left_to_right')
    description: str | Any = Field(default=None, union_mode='left_to_right')

class ZhHk(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    title: str | Any = Field(default=None, union_mode='left_to_right')
    description: str | Any = Field(default=None, union_mode='left_to_right')

class Th(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    title: str | Any = Field(default=None, union_mode='left_to_right')
    description: str | Any = Field(default=None, union_mode='left_to_right')

class Is(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    title: str | Any = Field(default=None, union_mode='left_to_right')
    description: str | Any = Field(default=None, union_mode='left_to_right')

class Fr(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    title: str | Any = Field(default=None, union_mode='left_to_right')
    description: str | Any = Field(default=None, union_mode='left_to_right')

class Ro(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    title: str | Any = Field(default=None, union_mode='left_to_right')
    description: str | Any = Field(default=None, union_mode='left_to_right')

class Am(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    title: str | Any = Field(default=None, union_mode='left_to_right')
    description: str | Any = Field(default=None, union_mode='left_to_right')

class No(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    title: str | Any = Field(default=None, union_mode='left_to_right')
    description: str | Any = Field(default=None, union_mode='left_to_right')

class En(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    title: str | Any = Field(default=None, union_mode='left_to_right')
    description: str | Any = Field(default=None, union_mode='left_to_right')

class Fil(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    title: str | Any = Field(default=None, union_mode='left_to_right')
    description: str | Any = Field(default=None, union_mode='left_to_right')

class Nl(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    title: str | Any = Field(default=None, union_mode='left_to_right')
    description: str | Any = Field(default=None, union_mode='left_to_right')

class Fa(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    title: str | Any = Field(default=None, union_mode='left_to_right')
    description: str | Any = Field(default=None, union_mode='left_to_right')

class Bg(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    title: str | Any = Field(default=None, union_mode='left_to_right')
    description: str | Any = Field(default=None, union_mode='left_to_right')

class SrLatn(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    title: str | Any = Field(default=None, union_mode='left_to_right')
    description: str | Any = Field(default=None, union_mode='left_to_right')

class Mn(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    title: str | Any = Field(default=None, union_mode='left_to_right')
    description: str | Any = Field(default=None, union_mode='left_to_right')

class Az(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    title: str | Any = Field(default=None, union_mode='left_to_right')
    description: str | Any = Field(default=None, union_mode='left_to_right')

class Kn(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    title: str | Any = Field(default=None, union_mode='left_to_right')
    description: str | Any = Field(default=None, union_mode='left_to_right')

class Pt(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    title: str | Any = Field(default=None, union_mode='left_to_right')
    description: str | Any = Field(default=None, union_mode='left_to_right')

class Sw(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    title: str | Any = Field(default=None, union_mode='left_to_right')
    description: str | Any = Field(default=None, union_mode='left_to_right')

class Tr(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    title: str | Any = Field(default=None, union_mode='left_to_right')
    description: str | Any = Field(default=None, union_mode='left_to_right')

class Sv(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    title: str | Any = Field(default=None, union_mode='left_to_right')
    description: str | Any = Field(default=None, union_mode='left_to_right')

class Ca(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    title: str | Any = Field(default=None, union_mode='left_to_right')
    description: str | Any = Field(default=None, union_mode='left_to_right')

class Ko(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    title: str | Any = Field(default=None, union_mode='left_to_right')
    description: str | Any = Field(default=None, union_mode='left_to_right')

class Or(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    title: str | Any = Field(default=None, union_mode='left_to_right')
    description: str | Any = Field(default=None, union_mode='left_to_right')

class Ml(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    title: str | Any = Field(default=None, union_mode='left_to_right')
    description: str | Any = Field(default=None, union_mode='left_to_right')

class ZhCn(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    title: str | Any = Field(default=None, union_mode='left_to_right')
    description: str | Any = Field(default=None, union_mode='left_to_right')

class Mr(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    title: str | Any = Field(default=None, union_mode='left_to_right')
    description: str | Any = Field(default=None, union_mode='left_to_right')

class Ky(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    title: str | Any = Field(default=None, union_mode='left_to_right')
    description: str | Any = Field(default=None, union_mode='left_to_right')

class Zu(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    title: str | Any = Field(default=None, union_mode='left_to_right')
    description: str | Any = Field(default=None, union_mode='left_to_right')

class FrCa(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    title: str | Any = Field(default=None, union_mode='left_to_right')
    description: str | Any = Field(default=None, union_mode='left_to_right')

class Es419(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    title: str | Any = Field(default=None, union_mode='left_to_right')
    description: str | Any = Field(default=None, union_mode='left_to_right')

class Si(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    title: str | Any = Field(default=None, union_mode='left_to_right')
    description: str | Any = Field(default=None, union_mode='left_to_right')

class Ka(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    title: str | Any = Field(default=None, union_mode='left_to_right')
    description: str | Any = Field(default=None, union_mode='left_to_right')

class Gu(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    title: str | Any = Field(default=None, union_mode='left_to_right')
    description: str | Any = Field(default=None, union_mode='left_to_right')

class Ar(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    title: str | Any = Field(default=None, union_mode='left_to_right')
    description: str | Any = Field(default=None, union_mode='left_to_right')

class Gl(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    title: str | Any = Field(default=None, union_mode='left_to_right')
    description: str | Any = Field(default=None, union_mode='left_to_right')

class Vi(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    title: str | Any = Field(default=None, union_mode='left_to_right')
    description: str | Any = Field(default=None, union_mode='left_to_right')

class Uk(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    title: str | Any = Field(default=None, union_mode='left_to_right')
    description: str | Any = Field(default=None, union_mode='left_to_right')

class Lv(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    title: str | Any = Field(default=None, union_mode='left_to_right')
    description: str | Any = Field(default=None, union_mode='left_to_right')

class Mk(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    title: str | Any = Field(default=None, union_mode='left_to_right')
    description: str | Any = Field(default=None, union_mode='left_to_right')

class Kk(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    title: str | Any = Field(default=None, union_mode='left_to_right')
    description: str | Any = Field(default=None, union_mode='left_to_right')

class Ms(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    title: str | Any = Field(default=None, union_mode='left_to_right')
    description: str | Any = Field(default=None, union_mode='left_to_right')

class Lt(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    title: str | Any = Field(default=None, union_mode='left_to_right')
    description: str | Any = Field(default=None, union_mode='left_to_right')

class Te(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    title: str | Any = Field(default=None, union_mode='left_to_right')
    description: str | Any = Field(default=None, union_mode='left_to_right')

class El(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    title: str | Any = Field(default=None, union_mode='left_to_right')
    description: str | Any = Field(default=None, union_mode='left_to_right')

class Uz(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    title: str | Any = Field(default=None, union_mode='left_to_right')
    description: str | Any = Field(default=None, union_mode='left_to_right')

class Zh(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    description: str | Any = Field(default=None, union_mode='left_to_right')

class PtBr(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    title: str | Any = Field(default=None, union_mode='left_to_right')
    description: str | Any = Field(default=None, union_mode='left_to_right')

class Localizations(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    ne: Ne | Any = Field(default=None, union_mode='left_to_right')
    bn: Bn | Any = Field(default=None, union_mode='left_to_right')
    hy: Hy | Any = Field(default=None, union_mode='left_to_right')
    ru: Ru | Any = Field(default=None, union_mode='left_to_right')
    es_us: EsUs | Any = Field(None, alias='es-US', union_mode='left_to_right')
    hr: Hr | Any = Field(default=None, union_mode='left_to_right')
    hi: Hi | Any = Field(default=None, union_mode='left_to_right')
    pa: Pa | Any = Field(default=None, union_mode='left_to_right')
    en_in: EnIn | Any = Field(None, alias='en-IN', union_mode='left_to_right')
    eu: Eu | Any = Field(default=None, union_mode='left_to_right')
    pt_pt: PtPt | Any = Field(None, alias='pt-PT', union_mode='left_to_right')
    hu: Hu | Any = Field(default=None, union_mode='left_to_right')
    sk: Sk | Any = Field(default=None, union_mode='left_to_right')
    ta: Ta | Any = Field(default=None, union_mode='left_to_right')
    lo: Lo | Any = Field(default=None, union_mode='left_to_right')
    sq: Sq | Any = Field(default=None, union_mode='left_to_right')
    ja: Ja | Any = Field(default=None, union_mode='left_to_right')
    km: Km | Any = Field(default=None, union_mode='left_to_right')
    af: Af | Any = Field(default=None, union_mode='left_to_right')
    es: Es | Any = Field(default=None, union_mode='left_to_right')
    ur: Ur | Any = Field(default=None, union_mode='left_to_right')
    et: Et | Any = Field(default=None, union_mode='left_to_right')
    iw: Iw | Any = Field(default=None, union_mode='left_to_right')
    sr: Sr | Any = Field(default=None, union_mode='left_to_right')
    fi: Fi | Any = Field(default=None, union_mode='left_to_right')
    da: Da | Any = Field(default=None, union_mode='left_to_right')
    zh_tw: ZhTw | Any = Field(None, alias='zh-TW', union_mode='left_to_right')
    de: De | Any = Field(default=None, union_mode='left_to_right')
    cs: Cs | Any = Field(default=None, union_mode='left_to_right')
    bs: Bs | Any = Field(default=None, union_mode='left_to_right')
    as_: As | Any = Field(None, alias='as', union_mode='left_to_right')
    my: My | Any = Field(default=None, union_mode='left_to_right')
    sl: Sl | Any = Field(default=None, union_mode='left_to_right')
    it: It | Any = Field(default=None, union_mode='left_to_right')
    id: Id | Any = Field(default=None, union_mode='left_to_right')
    be: Be | Any = Field(default=None, union_mode='left_to_right')
    pl: Pl | Any = Field(default=None, union_mode='left_to_right')
    en_gb: EnGb | Any = Field(None, alias='en-GB', union_mode='left_to_right')
    zh_hk: ZhHk | Any = Field(None, alias='zh-HK', union_mode='left_to_right')
    th: Th | Any = Field(default=None, union_mode='left_to_right')
    is_: Is | Any = Field(None, alias='is', union_mode='left_to_right')
    fr: Fr | Any = Field(default=None, union_mode='left_to_right')
    ro: Ro | Any = Field(default=None, union_mode='left_to_right')
    am: Am | Any = Field(default=None, union_mode='left_to_right')
    no: No | Any = Field(default=None, union_mode='left_to_right')
    en: En | Any = Field(default=None, union_mode='left_to_right')
    fil: Fil | Any = Field(default=None, union_mode='left_to_right')
    nl: Nl | Any = Field(default=None, union_mode='left_to_right')
    fa: Fa | Any = Field(default=None, union_mode='left_to_right')
    bg: Bg | Any = Field(default=None, union_mode='left_to_right')
    sr_latn: SrLatn | Any = Field(None, alias='sr-Latn', union_mode='left_to_right')
    mn: Mn | Any = Field(default=None, union_mode='left_to_right')
    az: Az | Any = Field(default=None, union_mode='left_to_right')
    kn: Kn | Any = Field(default=None, union_mode='left_to_right')
    pt: Pt | Any = Field(default=None, union_mode='left_to_right')
    sw: Sw | Any = Field(default=None, union_mode='left_to_right')
    tr: Tr | Any = Field(default=None, union_mode='left_to_right')
    sv: Sv | Any = Field(default=None, union_mode='left_to_right')
    ca: Ca | Any = Field(default=None, union_mode='left_to_right')
    ko: Ko | Any = Field(default=None, union_mode='left_to_right')
    or_: Or | Any = Field(None, alias='or', union_mode='left_to_right')
    ml: Ml | Any = Field(default=None, union_mode='left_to_right')
    zh_cn: ZhCn | Any = Field(None, alias='zh-CN', union_mode='left_to_right')
    mr: Mr | Any = Field(default=None, union_mode='left_to_right')
    ky: Ky | Any = Field(default=None, union_mode='left_to_right')
    zu: Zu | Any = Field(default=None, union_mode='left_to_right')
    fr_ca: FrCa | Any = Field(None, alias='fr-CA', union_mode='left_to_right')
    es_419: Es419 | Any = Field(None, alias='es-419', union_mode='left_to_right')
    si: Si | Any = Field(default=None, union_mode='left_to_right')
    ka: Ka | Any = Field(default=None, union_mode='left_to_right')
    gu: Gu | Any = Field(default=None, union_mode='left_to_right')
    ar: Ar | Any = Field(default=None, union_mode='left_to_right')
    gl: Gl | Any = Field(default=None, union_mode='left_to_right')
    vi: Vi | Any = Field(default=None, union_mode='left_to_right')
    uk: Uk | Any = Field(default=None, union_mode='left_to_right')
    lv: Lv | Any = Field(default=None, union_mode='left_to_right')
    mk: Mk | Any = Field(default=None, union_mode='left_to_right')
    kk: Kk | Any = Field(default=None, union_mode='left_to_right')
    ms: Ms | Any = Field(default=None, union_mode='left_to_right')
    lt: Lt | Any = Field(default=None, union_mode='left_to_right')
    te: Te | Any = Field(default=None, union_mode='left_to_right')
    el: El | Any = Field(default=None, union_mode='left_to_right')
    uz: Uz | Any = Field(default=None, union_mode='left_to_right')
    zh: Zh | Any = Field(default=None, union_mode='left_to_right')
    pt_br: PtBr | Any = Field(None, alias='pt-BR', union_mode='left_to_right')

class Item(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    kind: str | Any = Field(default=None, union_mode='left_to_right')
    etag: str | Any = Field(default=None, union_mode='left_to_right')
    id: str | Any = Field(default=None, union_mode='left_to_right')
    snippet: Snippet | Any = Field(default=None, union_mode='left_to_right')
    content_details: ContentDetails | Any = Field(None, alias='contentDetails', union_mode='left_to_right')
    statistics: Statistics | Any = Field(default=None, union_mode='left_to_right')
    status: Status | Any = Field(default=None, union_mode='left_to_right')
    branding_settings: BrandingSettings | Any = Field(None, alias='brandingSettings', union_mode='left_to_right')
    content_owner_details: dict[str, Any] | Any = Field(None, alias='contentOwnerDetails', union_mode='left_to_right')
    topic_details: TopicDetails | Any = Field(None, alias='topicDetails', union_mode='left_to_right')
    localizations: Localizations | Any = Field(default=None, union_mode='left_to_right')

class ChannelsModel(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    kind: str | Any = Field(default=None, union_mode='left_to_right')
    etag: str | Any = Field(default=None, union_mode='left_to_right')
    page_info: PageInfo | Any = Field(None, alias='pageInfo', union_mode='left_to_right')
    items: list[Item] | Any = Field(default=None, union_mode='left_to_right')
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
