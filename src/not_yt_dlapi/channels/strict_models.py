from typing import Self
from pydantic import ModelWrapValidatorHandler, PrivateAttr, model_validator
from pydantic import AwareDatetime, BaseModel, Field
from typing import Any

class PageInfo(BaseModel):
    total_results: int = Field(..., alias='totalResults')
    results_per_page: int = Field(..., alias='resultsPerPage')

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

class Thumbnails(BaseModel):
    default: Default
    medium: Medium
    high: High

class Localized(BaseModel):
    title: str
    description: str

class Snippet(BaseModel):
    title: str
    description: str
    custom_url: str | None = Field(None, alias='customUrl')
    published_at: AwareDatetime = Field(..., alias='publishedAt')
    thumbnails: Thumbnails
    localized: Localized
    country: str | None = None

class RelatedPlaylists(BaseModel):
    likes: str
    uploads: str

class ContentDetails(BaseModel):
    related_playlists: RelatedPlaylists = Field(..., alias='relatedPlaylists')

class Statistics(BaseModel):
    view_count: str = Field(..., alias='viewCount')
    subscriber_count: str = Field(..., alias='subscriberCount')
    hidden_subscriber_count: bool = Field(..., alias='hiddenSubscriberCount')
    video_count: str = Field(..., alias='videoCount')

class Status(BaseModel):
    privacy_status: str = Field(..., alias='privacyStatus')
    is_linked: bool = Field(..., alias='isLinked')
    long_uploads_status: str = Field(..., alias='longUploadsStatus')
    made_for_kids: bool | None = Field(None, alias='madeForKids')

class Channel(BaseModel):
    title: str
    keywords: str | None = None
    unsubscribed_trailer: str | None = Field(None, alias='unsubscribedTrailer')
    country: str | None = None
    description: str | None = None

class Image(BaseModel):
    banner_external_url: str = Field(..., alias='bannerExternalUrl')

class BrandingSettings(BaseModel):
    channel: Channel
    image: Image

class TopicDetails(BaseModel):
    topic_ids: list[str] = Field(..., alias='topicIds')
    topic_categories: list[str] = Field(..., alias='topicCategories')

class Ne(BaseModel):
    title: str
    description: str | None = None

class Bn(BaseModel):
    title: str
    description: str | None = None

class Hy(BaseModel):
    title: str
    description: str

class Ru(BaseModel):
    title: str
    description: str

class EsUs(BaseModel):
    title: str
    description: str | None = None

class Hr(BaseModel):
    title: str
    description: str

class Hi(BaseModel):
    title: str
    description: str | None = None

class Pa(BaseModel):
    title: str
    description: str | None = None

class EnIn(BaseModel):
    title: str
    description: str | None = None

class Eu(BaseModel):
    title: str
    description: str

class PtPt(BaseModel):
    title: str
    description: str | None = None

class Hu(BaseModel):
    title: str
    description: str

class Sk(BaseModel):
    title: str
    description: str | None = None

class Ta(BaseModel):
    title: str
    description: str | None = None

class Lo(BaseModel):
    title: str
    description: str | None = None

class Sq(BaseModel):
    title: str
    description: str | None = None

class Ja(BaseModel):
    title: str
    description: str | None = None

class Km(BaseModel):
    title: str
    description: str | None = None

class Af(BaseModel):
    title: str
    description: str | None = None

class Es(BaseModel):
    title: str
    description: str

class Ur(BaseModel):
    title: str
    description: str | None = None

class Et(BaseModel):
    title: str
    description: str | None = None

class Iw(BaseModel):
    title: str
    description: str

class Sr(BaseModel):
    title: str
    description: str

class Fi(BaseModel):
    title: str
    description: str

class Da(BaseModel):
    title: str
    description: str

class ZhTw(BaseModel):
    title: str
    description: str

class De(BaseModel):
    title: str
    description: str

class Cs(BaseModel):
    title: str
    description: str

class Bs(BaseModel):
    title: str
    description: str | None = None

class As(BaseModel):
    title: str
    description: str | None = None

class My(BaseModel):
    title: str
    description: str | None = None

class Sl(BaseModel):
    title: str
    description: str | None = None

class It(BaseModel):
    title: str
    description: str

class Id(BaseModel):
    title: str
    description: str

class Be(BaseModel):
    title: str
    description: str | None = None

class Pl(BaseModel):
    title: str
    description: str

class EnGb(BaseModel):
    title: str
    description: str | None = None

class ZhHk(BaseModel):
    title: str
    description: str | None = None

class Th(BaseModel):
    title: str
    description: str | None = None

class Is(BaseModel):
    title: str
    description: str

class Fr(BaseModel):
    title: str
    description: str

class Ro(BaseModel):
    title: str
    description: str | None = None

class Am(BaseModel):
    title: str
    description: str | None = None

class No(BaseModel):
    title: str
    description: str

class En(BaseModel):
    title: str
    description: str

class Fil(BaseModel):
    title: str
    description: str | None = None

class Nl(BaseModel):
    title: str
    description: str

class Fa(BaseModel):
    title: str
    description: str

class Bg(BaseModel):
    title: str
    description: str

class SrLatn(BaseModel):
    title: str
    description: str | None = None

class Mn(BaseModel):
    title: str
    description: str

class Az(BaseModel):
    title: str
    description: str | None = None

class Kn(BaseModel):
    title: str
    description: str | None = None

class Pt(BaseModel):
    title: str
    description: str

class Sw(BaseModel):
    title: str
    description: str | None = None

class Tr(BaseModel):
    title: str
    description: str

class Sv(BaseModel):
    title: str
    description: str

class Ca(BaseModel):
    title: str
    description: str

class Ko(BaseModel):
    title: str
    description: str

class Or(BaseModel):
    title: str
    description: str | None = None

class Ml(BaseModel):
    title: str
    description: str | None = None

class ZhCn(BaseModel):
    title: str
    description: str | None = None

class Mr(BaseModel):
    title: str
    description: str | None = None

class Ky(BaseModel):
    title: str
    description: str | None = None

class Zu(BaseModel):
    title: str
    description: str | None = None

class FrCa(BaseModel):
    title: str
    description: str | None = None

class Es419(BaseModel):
    title: str
    description: str | None = None

class Si(BaseModel):
    title: str
    description: str | None = None

class Ka(BaseModel):
    title: str
    description: str | None = None

class Gu(BaseModel):
    title: str
    description: str | None = None

class Ar(BaseModel):
    title: str
    description: str

class Gl(BaseModel):
    title: str
    description: str | None = None

class Vi(BaseModel):
    title: str
    description: str | None = None

class Uk(BaseModel):
    title: str
    description: str

class Lv(BaseModel):
    title: str
    description: str | None = None

class Mk(BaseModel):
    title: str
    description: str | None = None

class Kk(BaseModel):
    title: str
    description: str | None = None

class Ms(BaseModel):
    title: str
    description: str

class Lt(BaseModel):
    title: str
    description: str | None = None

class Te(BaseModel):
    title: str
    description: str | None = None

class El(BaseModel):
    title: str
    description: str | None = None

class Uz(BaseModel):
    title: str
    description: str | None = None

class Zh(BaseModel):
    description: str

class PtBr(BaseModel):
    title: str
    description: str | None = None

class Localizations(BaseModel):
    ne: Ne
    bn: Bn
    hy: Hy
    ru: Ru
    es_us: EsUs = Field(..., alias='es-US')
    hr: Hr
    hi: Hi
    pa: Pa
    en_in: EnIn = Field(..., alias='en-IN')
    eu: Eu
    pt_pt: PtPt = Field(..., alias='pt-PT')
    hu: Hu
    sk: Sk
    ta: Ta
    lo: Lo
    sq: Sq
    ja: Ja
    km: Km
    af: Af
    es: Es
    ur: Ur
    et: Et
    iw: Iw
    sr: Sr
    fi: Fi
    da: Da
    zh_tw: ZhTw = Field(..., alias='zh-TW')
    de: De
    cs: Cs
    bs: Bs
    as_: As = Field(..., alias='as')
    my: My
    sl: Sl
    it: It
    id: Id
    be: Be
    pl: Pl
    en_gb: EnGb = Field(..., alias='en-GB')
    zh_hk: ZhHk = Field(..., alias='zh-HK')
    th: Th
    is_: Is = Field(..., alias='is')
    fr: Fr
    ro: Ro
    am: Am
    no: No
    en: En
    fil: Fil
    nl: Nl
    fa: Fa
    bg: Bg
    sr_latn: SrLatn = Field(..., alias='sr-Latn')
    mn: Mn
    az: Az
    kn: Kn
    pt: Pt
    sw: Sw
    tr: Tr
    sv: Sv
    ca: Ca
    ko: Ko
    or_: Or = Field(..., alias='or')
    ml: Ml
    zh_cn: ZhCn = Field(..., alias='zh-CN')
    mr: Mr
    ky: Ky
    zu: Zu
    fr_ca: FrCa = Field(..., alias='fr-CA')
    es_419: Es419 = Field(..., alias='es-419')
    si: Si
    ka: Ka
    gu: Gu
    ar: Ar
    gl: Gl
    vi: Vi
    uk: Uk
    lv: Lv
    mk: Mk
    kk: Kk
    ms: Ms
    lt: Lt
    te: Te
    el: El
    uz: Uz
    zh: Zh | None = None
    pt_br: PtBr = Field(..., alias='pt-BR')

class Item(BaseModel):
    kind: str
    etag: str
    id: str
    snippet: Snippet
    content_details: ContentDetails = Field(..., alias='contentDetails')
    statistics: Statistics
    status: Status
    branding_settings: BrandingSettings = Field(..., alias='brandingSettings')
    content_owner_details: dict[str, Any] = Field(..., alias='contentOwnerDetails')
    topic_details: TopicDetails | None = Field(None, alias='topicDetails')
    localizations: Localizations | None = None

class ChannelsModel(BaseModel):
    kind: str
    etag: str
    page_info: PageInfo = Field(..., alias='pageInfo')
    items: list[Item] | None = None
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
