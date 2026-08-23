from typing import Any, Self
from pydantic import ModelWrapValidatorHandler, PrivateAttr, model_validator
from pydantic import AwareDatetime, BaseModel, Field

class PageInfo(BaseModel):
    total_results: int = Field(..., alias='totalResults')
    results_per_page: int = Field(..., alias='resultsPerPage')

class Medium(BaseModel):
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

class Default(BaseModel):
    url: str
    width: int
    height: int

class High(BaseModel):
    url: str
    width: int
    height: int

class Thumbnails(BaseModel):
    medium: Medium
    standard: Standard | None = None
    maxres: Maxres | None = None
    default: Default | None = None
    high: High | None = None

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
    localized: Localized
    default_language: str | None = Field(None, alias='defaultLanguage')

class Status(BaseModel):
    privacy_status: str = Field(..., alias='privacyStatus')

class ContentDetails(BaseModel):
    item_count: int = Field(..., alias='itemCount')

class Player(BaseModel):
    embed_html: str = Field(..., alias='embedHtml')

class Ja(BaseModel):
    title: str

class ZhTw(BaseModel):
    title: str

class Sw(BaseModel):
    title: str

class Am(BaseModel):
    title: str

class ZhCn(BaseModel):
    title: str

class Fr(BaseModel):
    title: str

class Pl(BaseModel):
    title: str

class Kn(BaseModel):
    title: str

class Ko(BaseModel):
    title: str

class Gu(BaseModel):
    title: str

class Ru(BaseModel):
    title: str

class Ca(BaseModel):
    title: str

class Km(BaseModel):
    title: str

class Fa(BaseModel):
    title: str

class Az(BaseModel):
    title: str

class De(BaseModel):
    title: str

class Hu(BaseModel):
    title: str

class En(BaseModel):
    title: str
    description: str | None = None

class Mr(BaseModel):
    title: str

class Uk(BaseModel):
    title: str

class Cs(BaseModel):
    title: str

class Si(BaseModel):
    title: str

class It(BaseModel):
    title: str

class Ka(BaseModel):
    title: str

class Sl(BaseModel):
    title: str

class Fil(BaseModel):
    title: str

class Ar(BaseModel):
    title: str

class Es419(BaseModel):
    title: str

class My(BaseModel):
    title: str

class Sv(BaseModel):
    title: str

class No(BaseModel):
    title: str

class EsUs(BaseModel):
    title: str

class Kk(BaseModel):
    title: str

class Hi(BaseModel):
    title: str

class Mk(BaseModel):
    title: str

class Ne(BaseModel):
    title: str

class Sq(BaseModel):
    title: str

class Bs(BaseModel):
    title: str

class PtPt(BaseModel):
    title: str

class Sk(BaseModel):
    title: str

class Lt(BaseModel):
    title: str

class As(BaseModel):
    title: str

class Te(BaseModel):
    title: str

class FrCa(BaseModel):
    title: str

class Nl(BaseModel):
    title: str

class Or(BaseModel):
    title: str

class Mn(BaseModel):
    title: str

class ZhHk(BaseModel):
    title: str

class Id(BaseModel):
    title: str

class EnGb(BaseModel):
    title: str

class Sr(BaseModel):
    title: str

class El(BaseModel):
    title: str

class EnIn(BaseModel):
    title: str

class Es(BaseModel):
    title: str

class Ur(BaseModel):
    title: str

class Th(BaseModel):
    title: str

class Vi(BaseModel):
    title: str

class Bg(BaseModel):
    title: str

class Tr(BaseModel):
    title: str

class Lv(BaseModel):
    title: str

class Is(BaseModel):
    title: str

class Et(BaseModel):
    title: str

class Ta(BaseModel):
    title: str

class Ms(BaseModel):
    title: str

class Da(BaseModel):
    title: str

class Hr(BaseModel):
    title: str

class Pa(BaseModel):
    title: str

class Af(BaseModel):
    title: str

class SrLatn(BaseModel):
    title: str

class Zu(BaseModel):
    title: str

class Ky(BaseModel):
    title: str

class Hy(BaseModel):
    title: str

class Iw(BaseModel):
    title: str

class Pt(BaseModel):
    title: str

class Eu(BaseModel):
    title: str

class Bn(BaseModel):
    title: str

class Fi(BaseModel):
    title: str

class Ml(BaseModel):
    title: str

class Ro(BaseModel):
    title: str

class Gl(BaseModel):
    title: str

class Be(BaseModel):
    title: str

class Lo(BaseModel):
    title: str

class Uz(BaseModel):
    title: str

class ArXb(BaseModel):
    title: str

class EnXa(BaseModel):
    title: str

class Localizations(BaseModel):
    ja: Ja
    zh_tw: ZhTw = Field(..., alias='zh-TW')
    sw: Sw
    am: Am
    zh_cn: ZhCn = Field(..., alias='zh-CN')
    fr: Fr
    pl: Pl
    kn: Kn
    ko: Ko
    gu: Gu
    ru: Ru
    ca: Ca
    km: Km
    fa: Fa
    az: Az
    de: De
    hu: Hu
    en: En
    mr: Mr
    uk: Uk
    cs: Cs
    si: Si
    it: It
    ka: Ka
    sl: Sl
    fil: Fil
    ar: Ar
    es_419: Es419 = Field(..., alias='es-419')
    my: My
    sv: Sv
    no: No
    es_us: EsUs = Field(..., alias='es-US')
    kk: Kk
    hi: Hi
    mk: Mk
    ne: Ne
    sq: Sq
    bs: Bs
    pt_pt: PtPt = Field(..., alias='pt-PT')
    sk: Sk
    lt: Lt
    as_: As = Field(..., alias='as')
    te: Te
    fr_ca: FrCa = Field(..., alias='fr-CA')
    nl: Nl
    or_: Or = Field(..., alias='or')
    mn: Mn
    zh_hk: ZhHk = Field(..., alias='zh-HK')
    id: Id
    en_gb: EnGb = Field(..., alias='en-GB')
    sr: Sr
    el: El
    en_in: EnIn = Field(..., alias='en-IN')
    es: Es
    ur: Ur
    th: Th
    vi: Vi
    bg: Bg
    tr: Tr
    lv: Lv
    is_: Is = Field(..., alias='is')
    et: Et
    ta: Ta
    ms: Ms
    da: Da
    hr: Hr
    pa: Pa
    af: Af
    sr_latn: SrLatn = Field(..., alias='sr-Latn')
    zu: Zu
    ky: Ky
    hy: Hy
    iw: Iw
    pt: Pt
    eu: Eu
    bn: Bn
    fi: Fi
    ml: Ml
    ro: Ro
    gl: Gl
    be: Be
    lo: Lo
    uz: Uz
    ar_xb: ArXb | None = Field(None, alias='ar-XB')
    en_xa: EnXa | None = Field(None, alias='en-XA')

class Item(BaseModel):
    kind: str
    etag: str
    id: str
    snippet: Snippet
    status: Status
    content_details: ContentDetails = Field(..., alias='contentDetails')
    player: Player
    localizations: Localizations | None = None

class PlaylistsModel(BaseModel):
    kind: str
    etag: str
    page_info: PageInfo = Field(..., alias='pageInfo')
    items: list[Item]
    next_page_token: str | None = Field(None, alias='nextPageToken')
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
