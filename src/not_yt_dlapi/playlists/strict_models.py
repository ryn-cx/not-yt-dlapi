from typing import Any, Self
from pydantic import ModelWrapValidatorHandler, PrivateAttr, model_validator
from pydantic import ConfigDict
from pydantic import AwareDatetime, BaseModel, Field

class PageInfo(BaseModel):
    model_config = ConfigDict(defer_build=True)
    total_results: int = Field(..., alias='totalResults')
    results_per_page: int = Field(..., alias='resultsPerPage')

class Medium(BaseModel):
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

class Default(BaseModel):
    model_config = ConfigDict(defer_build=True)
    url: str
    width: int
    height: int

class High(BaseModel):
    model_config = ConfigDict(defer_build=True)
    url: str
    width: int
    height: int

class Thumbnails(BaseModel):
    model_config = ConfigDict(defer_build=True)
    medium: Medium
    standard: Standard | None = None
    maxres: Maxres | None = None
    default: Default | None = None
    high: High | None = None

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
    localized: Localized
    default_language: str | None = Field(None, alias='defaultLanguage')

class Status(BaseModel):
    model_config = ConfigDict(defer_build=True)
    privacy_status: str = Field(..., alias='privacyStatus')

class ContentDetails(BaseModel):
    model_config = ConfigDict(defer_build=True)
    item_count: int = Field(..., alias='itemCount')

class Player(BaseModel):
    model_config = ConfigDict(defer_build=True)
    embed_html: str = Field(..., alias='embedHtml')

class Ja(BaseModel):
    model_config = ConfigDict(defer_build=True)
    title: str

class ZhTw(BaseModel):
    model_config = ConfigDict(defer_build=True)
    title: str

class Sw(BaseModel):
    model_config = ConfigDict(defer_build=True)
    title: str

class Am(BaseModel):
    model_config = ConfigDict(defer_build=True)
    title: str

class ZhCn(BaseModel):
    model_config = ConfigDict(defer_build=True)
    title: str

class Fr(BaseModel):
    model_config = ConfigDict(defer_build=True)
    title: str

class Pl(BaseModel):
    model_config = ConfigDict(defer_build=True)
    title: str

class Kn(BaseModel):
    model_config = ConfigDict(defer_build=True)
    title: str

class Ko(BaseModel):
    model_config = ConfigDict(defer_build=True)
    title: str

class Gu(BaseModel):
    model_config = ConfigDict(defer_build=True)
    title: str

class Ru(BaseModel):
    model_config = ConfigDict(defer_build=True)
    title: str

class Ca(BaseModel):
    model_config = ConfigDict(defer_build=True)
    title: str

class Km(BaseModel):
    model_config = ConfigDict(defer_build=True)
    title: str

class Fa(BaseModel):
    model_config = ConfigDict(defer_build=True)
    title: str

class Az(BaseModel):
    model_config = ConfigDict(defer_build=True)
    title: str

class De(BaseModel):
    model_config = ConfigDict(defer_build=True)
    title: str

class Hu(BaseModel):
    model_config = ConfigDict(defer_build=True)
    title: str

class En(BaseModel):
    model_config = ConfigDict(defer_build=True)
    title: str
    description: str | None = None

class Mr(BaseModel):
    model_config = ConfigDict(defer_build=True)
    title: str

class Uk(BaseModel):
    model_config = ConfigDict(defer_build=True)
    title: str

class Cs(BaseModel):
    model_config = ConfigDict(defer_build=True)
    title: str

class Si(BaseModel):
    model_config = ConfigDict(defer_build=True)
    title: str

class It(BaseModel):
    model_config = ConfigDict(defer_build=True)
    title: str

class Ka(BaseModel):
    model_config = ConfigDict(defer_build=True)
    title: str

class Sl(BaseModel):
    model_config = ConfigDict(defer_build=True)
    title: str

class Fil(BaseModel):
    model_config = ConfigDict(defer_build=True)
    title: str

class Ar(BaseModel):
    model_config = ConfigDict(defer_build=True)
    title: str

class Es419(BaseModel):
    model_config = ConfigDict(defer_build=True)
    title: str

class My(BaseModel):
    model_config = ConfigDict(defer_build=True)
    title: str

class Sv(BaseModel):
    model_config = ConfigDict(defer_build=True)
    title: str

class No(BaseModel):
    model_config = ConfigDict(defer_build=True)
    title: str

class EsUs(BaseModel):
    model_config = ConfigDict(defer_build=True)
    title: str

class Kk(BaseModel):
    model_config = ConfigDict(defer_build=True)
    title: str

class Hi(BaseModel):
    model_config = ConfigDict(defer_build=True)
    title: str

class Mk(BaseModel):
    model_config = ConfigDict(defer_build=True)
    title: str

class Ne(BaseModel):
    model_config = ConfigDict(defer_build=True)
    title: str

class Sq(BaseModel):
    model_config = ConfigDict(defer_build=True)
    title: str

class Bs(BaseModel):
    model_config = ConfigDict(defer_build=True)
    title: str

class PtPt(BaseModel):
    model_config = ConfigDict(defer_build=True)
    title: str

class Sk(BaseModel):
    model_config = ConfigDict(defer_build=True)
    title: str

class Lt(BaseModel):
    model_config = ConfigDict(defer_build=True)
    title: str

class As(BaseModel):
    model_config = ConfigDict(defer_build=True)
    title: str

class Te(BaseModel):
    model_config = ConfigDict(defer_build=True)
    title: str

class FrCa(BaseModel):
    model_config = ConfigDict(defer_build=True)
    title: str

class Nl(BaseModel):
    model_config = ConfigDict(defer_build=True)
    title: str

class Or(BaseModel):
    model_config = ConfigDict(defer_build=True)
    title: str

class Mn(BaseModel):
    model_config = ConfigDict(defer_build=True)
    title: str

class ZhHk(BaseModel):
    model_config = ConfigDict(defer_build=True)
    title: str

class Id(BaseModel):
    model_config = ConfigDict(defer_build=True)
    title: str

class EnGb(BaseModel):
    model_config = ConfigDict(defer_build=True)
    title: str

class Sr(BaseModel):
    model_config = ConfigDict(defer_build=True)
    title: str

class El(BaseModel):
    model_config = ConfigDict(defer_build=True)
    title: str

class EnIn(BaseModel):
    model_config = ConfigDict(defer_build=True)
    title: str

class Es(BaseModel):
    model_config = ConfigDict(defer_build=True)
    title: str

class Ur(BaseModel):
    model_config = ConfigDict(defer_build=True)
    title: str

class Th(BaseModel):
    model_config = ConfigDict(defer_build=True)
    title: str

class Vi(BaseModel):
    model_config = ConfigDict(defer_build=True)
    title: str

class Bg(BaseModel):
    model_config = ConfigDict(defer_build=True)
    title: str

class Tr(BaseModel):
    model_config = ConfigDict(defer_build=True)
    title: str

class Lv(BaseModel):
    model_config = ConfigDict(defer_build=True)
    title: str

class Is(BaseModel):
    model_config = ConfigDict(defer_build=True)
    title: str

class Et(BaseModel):
    model_config = ConfigDict(defer_build=True)
    title: str

class Ta(BaseModel):
    model_config = ConfigDict(defer_build=True)
    title: str

class Ms(BaseModel):
    model_config = ConfigDict(defer_build=True)
    title: str

class Da(BaseModel):
    model_config = ConfigDict(defer_build=True)
    title: str

class Hr(BaseModel):
    model_config = ConfigDict(defer_build=True)
    title: str

class Pa(BaseModel):
    model_config = ConfigDict(defer_build=True)
    title: str

class Af(BaseModel):
    model_config = ConfigDict(defer_build=True)
    title: str

class SrLatn(BaseModel):
    model_config = ConfigDict(defer_build=True)
    title: str

class Zu(BaseModel):
    model_config = ConfigDict(defer_build=True)
    title: str

class Ky(BaseModel):
    model_config = ConfigDict(defer_build=True)
    title: str

class Hy(BaseModel):
    model_config = ConfigDict(defer_build=True)
    title: str

class Iw(BaseModel):
    model_config = ConfigDict(defer_build=True)
    title: str

class Pt(BaseModel):
    model_config = ConfigDict(defer_build=True)
    title: str

class Eu(BaseModel):
    model_config = ConfigDict(defer_build=True)
    title: str

class Bn(BaseModel):
    model_config = ConfigDict(defer_build=True)
    title: str

class Fi(BaseModel):
    model_config = ConfigDict(defer_build=True)
    title: str

class Ml(BaseModel):
    model_config = ConfigDict(defer_build=True)
    title: str

class Ro(BaseModel):
    model_config = ConfigDict(defer_build=True)
    title: str

class Gl(BaseModel):
    model_config = ConfigDict(defer_build=True)
    title: str

class Be(BaseModel):
    model_config = ConfigDict(defer_build=True)
    title: str

class Lo(BaseModel):
    model_config = ConfigDict(defer_build=True)
    title: str

class Uz(BaseModel):
    model_config = ConfigDict(defer_build=True)
    title: str

class ArXb(BaseModel):
    model_config = ConfigDict(defer_build=True)
    title: str

class EnXa(BaseModel):
    model_config = ConfigDict(defer_build=True)
    title: str

class Localizations(BaseModel):
    model_config = ConfigDict(defer_build=True)
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
    model_config = ConfigDict(defer_build=True)
    kind: str
    etag: str
    id: str
    snippet: Snippet
    status: Status
    content_details: ContentDetails = Field(..., alias='contentDetails')
    player: Player
    localizations: Localizations | None = None

class PlaylistsModel(BaseModel):
    model_config = ConfigDict(defer_build=True)
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
