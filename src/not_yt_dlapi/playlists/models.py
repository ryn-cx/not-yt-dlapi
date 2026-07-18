# ruff: noqa: D100, D101, D102, TC001, TC002, TC003
from good_ass_pydantic_integrator import GAPIBaseModel
from pydantic import AwareDatetime, ConfigDict, Field


class PageInfo(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    total_results: int = Field(..., alias="totalResults")
    results_per_page: int = Field(..., alias="resultsPerPage")


class Medium(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    url: str
    width: int
    height: int


class Standard(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    url: str
    width: int
    height: int


class Maxres(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    url: str
    width: int
    height: int


class Default(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    url: str
    width: int
    height: int


class High(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    url: str
    width: int
    height: int


class Thumbnails(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    medium: Medium
    standard: Standard | None = None
    maxres: Maxres | None = None
    default: Default | None = None
    high: High | None = None


class Localized(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    title: str
    description: str


class Snippet(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    published_at: AwareDatetime = Field(..., alias="publishedAt")
    channel_id: str = Field(..., alias="channelId")
    title: str
    description: str
    thumbnails: Thumbnails
    channel_title: str = Field(..., alias="channelTitle")
    localized: Localized
    default_language: str | None = Field(None, alias="defaultLanguage")


class Status(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    privacy_status: str = Field(..., alias="privacyStatus")


class ContentDetails(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    item_count: int = Field(..., alias="itemCount")


class Player(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    embed_html: str = Field(..., alias="embedHtml")


class Ru(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    title: str


class Fa(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    title: str


class Eu(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    title: str


class Da(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    title: str


class Id(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    title: str


class No(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    title: str


class Tr(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    title: str


class Hi(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    title: str


class PtPt(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    title: str


class ZhTw(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    title: str


class Si(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    title: str


class Az(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    title: str


class EnGb(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    title: str


class Or(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    title: str


class EsUs(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    title: str


class Iw(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    title: str


class Ur(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    title: str


class Sr(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    title: str


class Ja(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    title: str


class Mk(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    title: str


class Pt(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    title: str


class EnIn(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    title: str


class ZhHk(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    title: str


class Sw(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    title: str


class En(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    title: str
    description: str


class Uz(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    title: str


class Es419(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    title: str


class As(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    title: str


class My(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    title: str


class Lo(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    title: str


class Km(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    title: str


class Fi(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    title: str


class Lt(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    title: str


class Vi(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    title: str


class Th(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    title: str


class Am(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    title: str


class Be(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    title: str


class Ca(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    title: str


class Ky(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    title: str


class Ar(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    title: str


class Et(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    title: str


class Hy(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    title: str


class Ms(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    title: str


class Cs(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    title: str


class Te(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    title: str


class Mn(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    title: str


class Es(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    title: str


class Af(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    title: str


class ZhCn(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    title: str


class Gu(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    title: str


class Sv(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    title: str


class Ro(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    title: str


class It(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    title: str


class Hu(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    title: str


class Ko(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    title: str


class Ml(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    title: str


class Is(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    title: str


class Uk(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    title: str


class FrCa(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    title: str


class Fr(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    title: str


class Kk(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    title: str


class Mr(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    title: str


class De(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    title: str


class Bg(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    title: str


class Fil(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    title: str


class ArXb(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    title: str


class Nl(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    title: str


class Gl(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    title: str


class Bs(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    title: str


class Ka(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    title: str


class SrLatn(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    title: str


class Ne(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    title: str


class Pa(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    title: str


class Sk(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    title: str


class Pl(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    title: str


class Ta(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    title: str


class Sq(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    title: str


class Sl(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    title: str


class El(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    title: str


class Hr(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    title: str


class Zu(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    title: str


class Kn(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    title: str


class Lv(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    title: str


class Bn(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    title: str


class EnXa(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    title: str


class Localizations(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    ru: Ru
    fa: Fa
    eu: Eu
    da: Da
    id: Id
    no: No
    tr: Tr
    hi: Hi
    pt_pt: PtPt = Field(..., alias="pt-PT")
    zh_tw: ZhTw = Field(..., alias="zh-TW")
    si: Si
    az: Az
    en_gb: EnGb = Field(..., alias="en-GB")
    or_: Or = Field(..., alias="or")
    es_us: EsUs = Field(..., alias="es-US")
    iw: Iw
    ur: Ur
    sr: Sr
    ja: Ja
    mk: Mk
    pt: Pt
    en_in: EnIn = Field(..., alias="en-IN")
    zh_hk: ZhHk = Field(..., alias="zh-HK")
    sw: Sw
    en: En
    uz: Uz
    es_419: Es419 = Field(..., alias="es-419")
    as_: As = Field(..., alias="as")
    my: My
    lo: Lo
    km: Km
    fi: Fi
    lt: Lt
    vi: Vi
    th: Th
    am: Am
    be: Be
    ca: Ca
    ky: Ky
    ar: Ar
    et: Et
    hy: Hy
    ms: Ms
    cs: Cs
    te: Te
    mn: Mn
    es: Es
    af: Af
    zh_cn: ZhCn = Field(..., alias="zh-CN")
    gu: Gu
    sv: Sv
    ro: Ro
    it: It
    hu: Hu
    ko: Ko
    ml: Ml
    is_: Is = Field(..., alias="is")
    uk: Uk
    fr_ca: FrCa = Field(..., alias="fr-CA")
    fr: Fr
    kk: Kk
    mr: Mr
    de: De
    bg: Bg
    fil: Fil
    ar_xb: ArXb = Field(..., alias="ar-XB")
    nl: Nl
    gl: Gl
    bs: Bs
    ka: Ka
    sr_latn: SrLatn = Field(..., alias="sr-Latn")
    ne: Ne
    pa: Pa
    sk: Sk
    pl: Pl
    ta: Ta
    sq: Sq
    sl: Sl
    el: El
    hr: Hr
    zu: Zu
    kn: Kn
    lv: Lv
    bn: Bn
    en_xa: EnXa = Field(..., alias="en-XA")


class Item(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    kind: str
    etag: str
    id: str
    snippet: Snippet
    status: Status
    content_details: ContentDetails = Field(..., alias="contentDetails")
    player: Player
    localizations: Localizations | None = None


class PlaylistsModel(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    kind: str
    etag: str
    page_info: PageInfo = Field(..., alias="pageInfo")
    items: list[Item]
