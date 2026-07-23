from good_ass_pydantic_integrator import GAPIBaseModel
from pydantic import AwareDatetime, ConfigDict, Field
from datetime import timedelta

class Default(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    url: str
    width: int
    height: int

class Medium(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    url: str
    width: int
    height: int

class High(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    url: str
    width: int
    height: int

class Standard(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    url: str
    width: int
    height: int

class Maxres(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    url: str
    width: int
    height: int

class Thumbnails(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    default: Default
    medium: Medium
    high: High
    standard: Standard | None = None
    maxres: Maxres | None = None

class Localized(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    title: str
    description: str

class Snippet(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
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

class RegionRestriction(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    allowed: list[str] | None = None
    blocked: list[str] | None = None

class ContentRating(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    yt_rating: str | None = Field(None, alias='ytRating')

class ContentDetails(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    duration: timedelta | None = None
    dimension: timedelta
    definition: str
    caption: str
    licensed_content: bool = Field(..., alias='licensedContent')
    region_restriction: RegionRestriction | None = Field(None, alias='regionRestriction')
    content_rating: ContentRating = Field(..., alias='contentRating')
    projection: str

class Status(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    upload_status: str = Field(..., alias='uploadStatus')
    privacy_status: str = Field(..., alias='privacyStatus')
    license: str
    embeddable: bool
    public_stats_viewable: bool = Field(..., alias='publicStatsViewable')
    made_for_kids: bool = Field(..., alias='madeForKids')
    publish_at: AwareDatetime | None = Field(None, alias='publishAt')

class Statistics(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    view_count: str | None = Field(None, alias='viewCount')
    like_count: str | None = Field(None, alias='likeCount')
    favorite_count: str = Field(..., alias='favoriteCount')
    comment_count: str | None = Field(None, alias='commentCount')

class Player(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    embed_html: str = Field(..., alias='embedHtml')

class TopicDetails(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    topic_categories: list[str] = Field(..., alias='topicCategories')

class Location(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    latitude: float
    longitude: float
    altitude: int

class RecordingDetails(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    location_description: str | None = Field(None, alias='locationDescription')
    location: Location | None = None
    recording_date: AwareDatetime | None = Field(None, alias='recordingDate')

class En(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    title: str
    description: str

class EnUs(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    title: str
    description: str

class Pl(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    title: str | None = None
    description: str

class Id(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    title: str | None = None
    description: str

class Te(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    title: str | None = None
    description: str

class Ml(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    title: str | None = None
    description: str

class EsUs(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    title: str | None = None
    description: str

class Pa(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    title: str | None = None
    description: str

class NlNl(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    title: str | None = None
    description: str

class It(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    title: str | None = None
    description: str

class Iw(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    title: str | None = None
    description: str

class Uk(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    title: str | None = None
    description: str

class Hi(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    title: str | None = None
    description: str

class Ja(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    title: str | None = None
    description: str

class PtBr(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    title: str | None = None
    description: str

class DeDe(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    title: str | None = None
    description: str

class Ta(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    title: str | None = None
    description: str

class Ru(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    title: str | None = None
    description: str

class Ko(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    title: str | None = None
    description: str

class FrFr(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    title: str | None = None
    description: str

class Bn(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    title: str | None = None
    description: str

class Ar(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    title: str | None = None
    description: str

class Zh(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    title: str
    description: str

class De(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    title: str
    description: str

class Nl(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    title: str
    description: str

class Th(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    title: str
    description: str

class Es(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    title: str
    description: str

class Pt(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    title: str
    description: str

class Tr(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    title: str
    description: str

class Fr(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    title: str
    description: str

class ZhTw(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    title: str
    description: str

class El(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    title: str
    description: str

class EnGb(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    title: str
    description: str

class FrCa(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    title: str
    description: str

class EsMx(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    title: str
    description: str

class EnCa(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    title: str
    description: str

class Hu(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    title: str
    description: str

class Sv(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    title: str
    description: str

class Fil(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    title: str
    description: str

class Gu(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    title: str
    description: str

class EsEs(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    title: str
    description: str

class Vi(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    title: str
    description: str

class Ur(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    title: str
    description: str

class Ms(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    title: str
    description: str

class No(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    title: str
    description: str

class ZhCn(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    title: str
    description: str

class Es419(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    title: str
    description: str

class PtPt(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    title: str
    description: str

class HiLatn(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    title: str
    description: str

class Hr(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    title: str
    description: str

class EnIe(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    title: str
    description: str

class ZhHant(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    title: str
    description: str

class ZhHans(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    title: str
    description: str

class Ca(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    title: str
    description: str

class ZhHk(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    title: str
    description: str

class YueHk(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    title: str
    description: str

class Yue(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    title: str
    description: str

class Cs(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    title: str
    description: str

class Fi(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    title: str
    description: str

class Sk(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    title: str
    description: str

class Sr(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    title: str
    description: str

class Ro(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    title: str
    description: str

class Fa(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    title: str
    description: str

class EnAu(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    title: str
    description: str

class Bg(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    title: str
    description: str

class EnIn(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    title: str
    description: str

class Az(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    title: str
    description: str

class Sl(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    title: str
    description: str

class Lt(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    title: str
    description: str

class Km(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    title: str
    description: str

class Da(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    title: str
    description: str

class Lv(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    title: str
    description: str

class Mr(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    title: str
    description: str

class Gd(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    title: str
    description: str

class Sq(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    title: str
    description: str

class Su(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    title: str
    description: str

class Ga(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    title: str
    description: str

class Hy(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    title: str
    description: str

class Be(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    title: str
    description: str

class La(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    title: str
    description: str

class Is(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    title: str
    description: str

class Mk(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    title: str
    description: str

class Mn(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    title: str
    description: str

class Cy(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    title: str
    description: str

class My(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    title: str
    description: str

class Ps(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    title: str
    description: str

class Ka(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    title: str
    description: str

class Kn(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    title: str
    description: str

class Or(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    title: str
    description: str

class Jv(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    title: str
    description: str

class Ku(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    title: str
    description: str

class Lb(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    title: str
    description: str

class Eu(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    title: str
    description: str

class Sm(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    title: str
    description: str

class Tk(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    title: str
    description: str

class Ne(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    title: str
    description: str

class Haw(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    title: str
    description: str

class Ug(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    title: str
    description: str

class Uz(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    title: str
    description: str

class Tg(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    title: str
    description: str

class Tt(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    title: str
    description: str

class Mi(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    title: str
    description: str

class Ky(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    title: str
    description: str

class Ig(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    title: str
    description: str

class Mt(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    title: str
    description: str

class St(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    title: str
    description: str

class Eo(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    title: str
    description: str

class Mg(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    title: str
    description: str

class Bs(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    title: str
    description: str

class Et(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    title: str
    description: str

class Xh(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    title: str
    description: str

class So(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    title: str
    description: str

class Yi(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    title: str
    description: str

class Zu(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    title: str
    description: str

class Sn(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    title: str
    description: str

class Gl(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    title: str
    description: str

class Co(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    title: str
    description: str

class Kk(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    title: str
    description: str

class Sw(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    title: str
    description: str

class Af(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    title: str
    description: str

class Si(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    title: str
    description: str

class Am(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    title: str
    description: str

class Ha(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    title: str
    description: str

class Rw(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    title: str
    description: str

class Fy(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    title: str
    description: str

class Ht(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    title: str
    description: str

class Lo(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    title: str
    description: str

class Sd(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    title: str
    description: str

class Yo(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    title: str
    description: str

class Scn(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    title: str
    description: str

class FrBe(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    title: str
    description: str

class Tl(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    title: str
    description: str

class Qu(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    title: str
    description: str

class NlBe(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    title: str
    description: str

class DeAt(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    title: str
    description: str

class DeCh(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    title: str
    description: str

class FrCh(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    title: str
    description: str

class MsSg(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    title: str
    description: str

class Ay(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    title: str
    description: str

class Oc(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    title: str
    description: str

class ZhSg(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    title: str
    description: str

class Br(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    title: str
    description: str

class Ln(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    title: str
    description: str

class To(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    title: str
    description: str

class Aa(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    title: str
    description: str

class Ba(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    title: str
    description: str

class Fj(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    title: str
    description: str

class BnIn(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    title: str
    description: str

class Kok(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    title: str
    description: str

class Ab(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    title: str
    description: str

class Gn(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    title: str
    description: str

class Ee(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    title: str
    description: str

class Rn(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    title: str
    description: str

class Bh(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    title: str
    description: str

class Lus(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    title: str
    description: str

class Sa(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    title: str
    description: str

class Iu(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    title: str
    description: str

class Bo(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    title: str
    description: str

class Om(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    title: str
    description: str

class Bm(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    title: str
    description: str

class Wo(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    title: str
    description: str

class Mai(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    title: str
    description: str

class As(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    title: str
    description: str

class Akk(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    title: str
    description: str

class FaAf(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    title: str
    description: str

class FaIr(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    title: str
    description: str

class RuLatn(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    title: str
    description: str

class Mo(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    title: str
    description: str

class MnMong(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    title: str
    description: str

class Sg(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    title: str
    description: str

class Ts(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    title: str
    description: str

class Fo(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    title: str
    description: str

class Tw(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    title: str
    description: str

class Dz(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    title: str
    description: str

class Tpi(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    title: str
    description: str

class SrLatn(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    title: str
    description: str

class SrCyrl(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    title: str
    description: str

class Tn(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    title: str
    description: str

class Pap(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    title: str
    description: str

class Ss(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    title: str
    description: str

class Lu(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    title: str
    description: str

class Ve(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    title: str
    description: str

class Doi(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    title: str
    description: str

class Ti(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    title: str
    description: str

class Sat(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    title: str
    description: str

class Lad(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    title: str
    description: str

class Arc(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    title: str
    description: str

class HakTw(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    title: str
    description: str

class NanTw(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    title: str
    description: str

class Lg(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    title: str
    description: str

class Ase(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    title: str
    description: str

class Ia(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    title: str
    description: str

class Ks(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    title: str
    description: str

class Sc(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    title: str
    description: str

class Cr(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    title: str
    description: str

class Ik(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    title: str
    description: str

class Ie(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    title: str
    description: str

class Cho(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    title: str
    description: str

class Nan(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    title: str
    description: str

class Hak(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    title: str
    description: str

class Vro(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    title: str
    description: str

class Kl(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    title: str
    description: str

class Vo(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    title: str
    description: str

class Chr(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    title: str
    description: str

class Tlh(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    title: str
    description: str

class Sdp(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    title: str
    description: str

class Cop(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    title: str
    description: str

class Rm(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    title: str
    description: str

class Und(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    title: str
    description: str

class Mni(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    title: str
    description: str

class Brx(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    title: str
    description: str

class Localizations(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    en: En | None = None
    en_us: EnUs | None = Field(None, alias='en-US')
    pl: Pl | None = None
    id: Id | None = None
    te: Te | None = None
    ml: Ml | None = None
    es_us: EsUs | None = Field(None, alias='es-US')
    pa: Pa | None = None
    nl_nl: NlNl | None = Field(None, alias='nl-NL')
    it: It | None = None
    iw: Iw | None = None
    uk: Uk | None = None
    hi: Hi | None = None
    ja: Ja | None = None
    pt_br: PtBr | None = Field(None, alias='pt-BR')
    de_de: DeDe | None = Field(None, alias='de-DE')
    ta: Ta | None = None
    ru: Ru | None = None
    ko: Ko | None = None
    fr_fr: FrFr | None = Field(None, alias='fr-FR')
    bn: Bn | None = None
    ar: Ar | None = None
    zh: Zh | None = None
    de: De | None = None
    nl: Nl | None = None
    th: Th | None = None
    es: Es | None = None
    pt: Pt | None = None
    tr: Tr | None = None
    fr: Fr | None = None
    zh_tw: ZhTw | None = Field(None, alias='zh-TW')
    el: El | None = None
    en_gb: EnGb | None = Field(None, alias='en-GB')
    fr_ca: FrCa | None = Field(None, alias='fr-CA')
    es_mx: EsMx | None = Field(None, alias='es-MX')
    en_ca: EnCa | None = Field(None, alias='en-CA')
    hu: Hu | None = None
    sv: Sv | None = None
    fil: Fil | None = None
    gu: Gu | None = None
    es_es: EsEs | None = Field(None, alias='es-ES')
    vi: Vi | None = None
    ur: Ur | None = None
    ms: Ms | None = None
    no: No | None = None
    zh_cn: ZhCn | None = Field(None, alias='zh-CN')
    es_419: Es419 | None = Field(None, alias='es-419')
    pt_pt: PtPt | None = Field(None, alias='pt-PT')
    hi_latn: HiLatn | None = Field(None, alias='hi-Latn')
    hr: Hr | None = None
    en_ie: EnIe | None = Field(None, alias='en-IE')
    zh_hant: ZhHant | None = Field(None, alias='zh-Hant')
    zh_hans: ZhHans | None = Field(None, alias='zh-Hans')
    ca: Ca | None = None
    zh_hk: ZhHk | None = Field(None, alias='zh-HK')
    yue_hk: YueHk | None = Field(None, alias='yue-HK')
    yue: Yue | None = None
    cs: Cs | None = None
    fi: Fi | None = None
    sk: Sk | None = None
    sr: Sr | None = None
    ro: Ro | None = None
    fa: Fa | None = None
    en_au: EnAu | None = Field(None, alias='en-AU')
    bg: Bg | None = None
    en_in: EnIn | None = Field(None, alias='en-IN')
    az: Az | None = None
    sl: Sl | None = None
    lt: Lt | None = None
    km: Km | None = None
    da: Da | None = None
    lv: Lv | None = None
    mr: Mr | None = None
    gd: Gd | None = None
    sq: Sq | None = None
    su: Su | None = None
    ga: Ga | None = None
    hy: Hy | None = None
    be: Be | None = None
    la: La | None = None
    is_: Is | None = Field(None, alias='is')
    mk: Mk | None = None
    mn: Mn | None = None
    cy: Cy | None = None
    my: My | None = None
    ps: Ps | None = None
    ka: Ka | None = None
    kn: Kn | None = None
    or_: Or | None = Field(None, alias='or')
    jv: Jv | None = None
    ku: Ku | None = None
    lb: Lb | None = None
    eu: Eu | None = None
    sm: Sm | None = None
    tk: Tk | None = None
    ne: Ne | None = None
    haw: Haw | None = None
    ug: Ug | None = None
    uz: Uz | None = None
    tg: Tg | None = None
    tt: Tt | None = None
    mi: Mi | None = None
    ky: Ky | None = None
    ig: Ig | None = None
    mt: Mt | None = None
    st: St | None = None
    eo: Eo | None = None
    mg: Mg | None = None
    bs: Bs | None = None
    et: Et | None = None
    xh: Xh | None = None
    so: So | None = None
    yi: Yi | None = None
    zu: Zu | None = None
    sn: Sn | None = None
    gl: Gl | None = None
    co: Co | None = None
    kk: Kk | None = None
    sw: Sw | None = None
    af: Af | None = None
    si: Si | None = None
    am: Am | None = None
    ha: Ha | None = None
    rw: Rw | None = None
    fy: Fy | None = None
    ht: Ht | None = None
    lo: Lo | None = None
    sd: Sd | None = None
    yo: Yo | None = None
    scn: Scn | None = None
    fr_be: FrBe | None = Field(None, alias='fr-BE')
    tl: Tl | None = None
    qu: Qu | None = None
    nl_be: NlBe | None = Field(None, alias='nl-BE')
    de_at: DeAt | None = Field(None, alias='de-AT')
    de_ch: DeCh | None = Field(None, alias='de-CH')
    fr_ch: FrCh | None = Field(None, alias='fr-CH')
    ms_sg: MsSg | None = Field(None, alias='ms-SG')
    ay: Ay | None = None
    oc: Oc | None = None
    zh_sg: ZhSg | None = Field(None, alias='zh-SG')
    br: Br | None = None
    ln: Ln | None = None
    to: To | None = None
    aa: Aa | None = None
    ba: Ba | None = None
    fj: Fj | None = None
    bn_in: BnIn | None = Field(None, alias='bn-IN')
    kok: Kok | None = None
    ab: Ab | None = None
    gn: Gn | None = None
    ee: Ee | None = None
    rn: Rn | None = None
    bh: Bh | None = None
    lus: Lus | None = None
    sa: Sa | None = None
    iu: Iu | None = None
    bo: Bo | None = None
    om: Om | None = None
    bm: Bm | None = None
    wo: Wo | None = None
    mai: Mai | None = None
    as_: As | None = Field(None, alias='as')
    akk: Akk | None = None
    fa_af: FaAf | None = Field(None, alias='fa-AF')
    fa_ir: FaIr | None = Field(None, alias='fa-IR')
    ru_latn: RuLatn | None = Field(None, alias='ru-Latn')
    mo: Mo | None = None
    mn_mong: MnMong | None = Field(None, alias='mn-Mong')
    sg: Sg | None = None
    ts: Ts | None = None
    fo: Fo | None = None
    tw: Tw | None = None
    dz: Dz | None = None
    tpi: Tpi | None = None
    sr_latn: SrLatn | None = Field(None, alias='sr-Latn')
    sr_cyrl: SrCyrl | None = Field(None, alias='sr-Cyrl')
    tn: Tn | None = None
    pap: Pap | None = None
    ss: Ss | None = None
    lu: Lu | None = None
    ve: Ve | None = None
    doi: Doi | None = None
    ti: Ti | None = None
    sat: Sat | None = None
    lad: Lad | None = None
    arc: Arc | None = None
    hak_tw: HakTw | None = Field(None, alias='hak-TW')
    nan_tw: NanTw | None = Field(None, alias='nan-TW')
    lg: Lg | None = None
    ase: Ase | None = None
    ia: Ia | None = None
    ks: Ks | None = None
    sc: Sc | None = None
    cr: Cr | None = None
    ik: Ik | None = None
    ie: Ie | None = None
    cho: Cho | None = None
    nan: Nan | None = None
    hak: Hak | None = None
    vro: Vro | None = None
    kl: Kl | None = None
    vo: Vo | None = None
    chr: Chr | None = None
    tlh: Tlh | None = None
    sdp: Sdp | None = None
    cop: Cop | None = None
    rm: Rm | None = None
    und: Und | None = None
    mni: Mni | None = None
    brx: Brx | None = None

class PaidProductPlacementDetails(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    has_paid_product_placement: bool = Field(..., alias='hasPaidProductPlacement')

class LiveStreamingDetails(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    active_live_chat_id: str | None = Field(None, alias='activeLiveChatId')
    actual_start_time: AwareDatetime | None = Field(None, alias='actualStartTime')
    actual_end_time: AwareDatetime | None = Field(None, alias='actualEndTime')
    scheduled_start_time: AwareDatetime | None = Field(None, alias='scheduledStartTime')
    concurrent_viewers: str | None = Field(None, alias='concurrentViewers')
    scheduled_end_time: AwareDatetime | None = Field(None, alias='scheduledEndTime')

class Item(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
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

class PageInfo(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    total_results: int = Field(..., alias='totalResults')
    results_per_page: int = Field(..., alias='resultsPerPage')

class NotYtDlapi(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    video_id: str
    part: str
    timestamp: AwareDatetime

class VideosModel(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    kind: str
    etag: str
    items: list[Item]
    page_info: PageInfo = Field(..., alias='pageInfo')
    not_yt_dlapi: NotYtDlapi | None = None
