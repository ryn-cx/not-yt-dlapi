from pydantic import AwareDatetime, ConfigDict, Field
from good_ass_pydantic_integrator import GAPIBaseModel

class PageInfo(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    total_results: int = Field(..., alias='totalResults')
    results_per_page: int = Field(..., alias='resultsPerPage')

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
    default: Default | None = None
    medium: Medium
    high: High | None = None
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
    default_language: str | None = Field(None, alias='defaultLanguage')
    localized: Localized

class Status(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    privacy_status: str = Field(..., alias='privacyStatus')
    podcast_status: str | None = Field(None, alias='podcastStatus')

class ContentDetails(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    item_count: int = Field(..., alias='itemCount')

class Player(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    embed_html: str = Field(..., alias='embedHtml')

class En(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    title: str
    description: str | None = None

class Ru(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    title: str
    description: str | None = None

class Ja(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    title: str
    description: str | None = None

class EnXa(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    title: str

class Mr(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    title: str

class Sw(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    title: str

class Th(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    title: str

class Ro(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    title: str

class Vi(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    title: str

class Ta(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    title: str

class Te(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    title: str

class Da(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    title: str

class Pt(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    title: str

class Et(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    title: str

class PtPt(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    title: str

class Bg(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    title: str

class Sv(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    title: str

class ZhTw(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    title: str

class EnGb(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    title: str
    description: str | None = None

class Ar(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    title: str

class No(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    title: str

class Ml(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    title: str

class Fr(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    title: str

class Ms(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    title: str

class It(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    title: str

class ZhHk(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    title: str

class Sr(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    title: str

class Id(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    title: str

class Kn(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    title: str

class Ko(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    title: str

class ZhCn(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    title: str

class Lt(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    title: str

class Lv(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    title: str

class Zu(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    title: str

class Es419(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    title: str

class Tr(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    title: str

class Cs(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    title: str

class FrCa(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    title: str

class Sl(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    title: str

class Hi(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    title: str

class Pl(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    title: str

class Nl(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    title: str

class Uk(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    title: str

class Eu(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    title: str

class El(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    title: str

class Gu(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    title: str

class Es(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    title: str

class Fi(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    title: str

class Ca(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    title: str

class Fa(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    title: str

class De(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    title: str

class Ur(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    title: str

class Hu(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    title: str

class Am(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    title: str

class Bn(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    title: str

class Iw(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    title: str

class Gl(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    title: str

class Is(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    title: str

class Sk(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    title: str

class Fil(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    title: str

class Af(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    title: str

class Hr(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    title: str

class Kk(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    title: str

class Mk(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    title: str

class Or(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    title: str

class SrLatn(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    title: str

class My(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    title: str

class Ne(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    title: str

class Uz(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    title: str

class Mn(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    title: str

class EnIn(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    title: str

class Km(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    title: str

class Be(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    title: str

class ArXb(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    title: str

class Ka(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    title: str

class Hy(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    title: str

class Bs(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    title: str

class Si(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    title: str

class Az(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    title: str

class EsUs(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    title: str

class Pa(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    title: str

class As(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    title: str

class Sq(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    title: str

class Lo(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    title: str

class Ky(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    title: str

class Localizations(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    en: En | None = None
    ru: Ru | None = None
    ja: Ja | None = None
    en_xa: EnXa | None = Field(None, alias='en-XA')
    mr: Mr | None = None
    sw: Sw | None = None
    th: Th | None = None
    ro: Ro | None = None
    vi: Vi | None = None
    ta: Ta | None = None
    te: Te | None = None
    da: Da | None = None
    pt: Pt | None = None
    et: Et | None = None
    pt_pt: PtPt | None = Field(None, alias='pt-PT')
    bg: Bg | None = None
    sv: Sv | None = None
    zh_tw: ZhTw | None = Field(None, alias='zh-TW')
    en_gb: EnGb | None = Field(None, alias='en-GB')
    ar: Ar | None = None
    no: No | None = None
    ml: Ml | None = None
    fr: Fr | None = None
    ms: Ms | None = None
    it: It | None = None
    zh_hk: ZhHk | None = Field(None, alias='zh-HK')
    sr: Sr | None = None
    id: Id | None = None
    kn: Kn | None = None
    ko: Ko | None = None
    zh_cn: ZhCn | None = Field(None, alias='zh-CN')
    lt: Lt | None = None
    lv: Lv | None = None
    zu: Zu | None = None
    es_419: Es419 | None = Field(None, alias='es-419')
    tr: Tr | None = None
    cs: Cs | None = None
    fr_ca: FrCa | None = Field(None, alias='fr-CA')
    sl: Sl | None = None
    hi: Hi | None = None
    pl: Pl | None = None
    nl: Nl | None = None
    uk: Uk | None = None
    eu: Eu | None = None
    el: El | None = None
    gu: Gu | None = None
    es: Es | None = None
    fi: Fi | None = None
    ca: Ca | None = None
    fa: Fa | None = None
    de: De | None = None
    ur: Ur | None = None
    hu: Hu | None = None
    am: Am | None = None
    bn: Bn | None = None
    iw: Iw | None = None
    gl: Gl | None = None
    is_: Is | None = Field(None, alias='is')
    sk: Sk | None = None
    fil: Fil | None = None
    af: Af | None = None
    hr: Hr | None = None
    kk: Kk | None = None
    mk: Mk | None = None
    or_: Or | None = Field(None, alias='or')
    sr_latn: SrLatn | None = Field(None, alias='sr-Latn')
    my: My | None = None
    ne: Ne | None = None
    uz: Uz | None = None
    mn: Mn | None = None
    en_in: EnIn | None = Field(None, alias='en-IN')
    km: Km | None = None
    be: Be | None = None
    ar_xb: ArXb | None = Field(None, alias='ar-XB')
    ka: Ka | None = None
    hy: Hy | None = None
    bs: Bs | None = None
    si: Si | None = None
    az: Az | None = None
    es_us: EsUs | None = Field(None, alias='es-US')
    pa: Pa | None = None
    as_: As | None = Field(None, alias='as')
    sq: Sq | None = None
    lo: Lo | None = None
    ky: Ky | None = None

class Item(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    kind: str
    etag: str
    id: str
    snippet: Snippet
    status: Status
    content_details: ContentDetails = Field(..., alias='contentDetails')
    player: Player
    localizations: Localizations | None = None

class NotYtDlapi(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    channel_id: str | None = None
    part: str
    timestamp: AwareDatetime
    playlist_id: str | None = None

class PlaylistsModel(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    kind: str
    etag: str
    page_info: PageInfo = Field(..., alias='pageInfo')
    items: list[Item]
    next_page_token: str | None = Field(None, alias='nextPageToken')
    not_yt_dlapi: NotYtDlapi | None = None
