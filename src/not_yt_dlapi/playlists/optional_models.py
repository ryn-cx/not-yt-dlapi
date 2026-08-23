from typing import Any, Self
from pydantic import ModelWrapValidatorHandler, PrivateAttr, model_validator
from pydantic import AwareDatetime, BaseModel, ConfigDict, Field

class PageInfo(BaseModel):
    model_config = ConfigDict(extra='ignore')
    total_results: int | None = Field(None, alias='totalResults')
    results_per_page: int | None = Field(None, alias='resultsPerPage')

class Medium(BaseModel):
    model_config = ConfigDict(extra='ignore')
    url: str | None = None
    width: int | None = None
    height: int | None = None

class Standard(BaseModel):
    model_config = ConfigDict(extra='ignore')
    url: str | None = None
    width: int | None = None
    height: int | None = None

class Maxres(BaseModel):
    model_config = ConfigDict(extra='ignore')
    url: str | None = None
    width: int | None = None
    height: int | None = None

class Default(BaseModel):
    model_config = ConfigDict(extra='ignore')
    url: str | None = None
    width: int | None = None
    height: int | None = None

class High(BaseModel):
    model_config = ConfigDict(extra='ignore')
    url: str | None = None
    width: int | None = None
    height: int | None = None

class Thumbnails(BaseModel):
    model_config = ConfigDict(extra='ignore')
    medium: Medium | None = None
    standard: Standard | None = None
    maxres: Maxres | None = None
    default: Default | None = None
    high: High | None = None

class Localized(BaseModel):
    model_config = ConfigDict(extra='ignore')
    title: str | None = None
    description: str | None = None

class Snippet(BaseModel):
    model_config = ConfigDict(extra='ignore')
    published_at: AwareDatetime | None = Field(None, alias='publishedAt')
    channel_id: str | None = Field(None, alias='channelId')
    title: str | None = None
    description: str | None = None
    thumbnails: Thumbnails | None = None
    channel_title: str | None = Field(None, alias='channelTitle')
    localized: Localized | None = None
    default_language: str | None = Field(None, alias='defaultLanguage')

class Status(BaseModel):
    model_config = ConfigDict(extra='ignore')
    privacy_status: str | None = Field(None, alias='privacyStatus')

class ContentDetails(BaseModel):
    model_config = ConfigDict(extra='ignore')
    item_count: int | None = Field(None, alias='itemCount')

class Player(BaseModel):
    model_config = ConfigDict(extra='ignore')
    embed_html: str | None = Field(None, alias='embedHtml')

class Ja(BaseModel):
    model_config = ConfigDict(extra='ignore')
    title: str | None = None

class ZhTw(BaseModel):
    model_config = ConfigDict(extra='ignore')
    title: str | None = None

class Sw(BaseModel):
    model_config = ConfigDict(extra='ignore')
    title: str | None = None

class Am(BaseModel):
    model_config = ConfigDict(extra='ignore')
    title: str | None = None

class ZhCn(BaseModel):
    model_config = ConfigDict(extra='ignore')
    title: str | None = None

class Fr(BaseModel):
    model_config = ConfigDict(extra='ignore')
    title: str | None = None

class Pl(BaseModel):
    model_config = ConfigDict(extra='ignore')
    title: str | None = None

class Kn(BaseModel):
    model_config = ConfigDict(extra='ignore')
    title: str | None = None

class Ko(BaseModel):
    model_config = ConfigDict(extra='ignore')
    title: str | None = None

class Gu(BaseModel):
    model_config = ConfigDict(extra='ignore')
    title: str | None = None

class Ru(BaseModel):
    model_config = ConfigDict(extra='ignore')
    title: str | None = None

class Ca(BaseModel):
    model_config = ConfigDict(extra='ignore')
    title: str | None = None

class Km(BaseModel):
    model_config = ConfigDict(extra='ignore')
    title: str | None = None

class Fa(BaseModel):
    model_config = ConfigDict(extra='ignore')
    title: str | None = None

class Az(BaseModel):
    model_config = ConfigDict(extra='ignore')
    title: str | None = None

class De(BaseModel):
    model_config = ConfigDict(extra='ignore')
    title: str | None = None

class Hu(BaseModel):
    model_config = ConfigDict(extra='ignore')
    title: str | None = None

class En(BaseModel):
    model_config = ConfigDict(extra='ignore')
    title: str | None = None
    description: str | None = None

class Mr(BaseModel):
    model_config = ConfigDict(extra='ignore')
    title: str | None = None

class Uk(BaseModel):
    model_config = ConfigDict(extra='ignore')
    title: str | None = None

class Cs(BaseModel):
    model_config = ConfigDict(extra='ignore')
    title: str | None = None

class Si(BaseModel):
    model_config = ConfigDict(extra='ignore')
    title: str | None = None

class It(BaseModel):
    model_config = ConfigDict(extra='ignore')
    title: str | None = None

class Ka(BaseModel):
    model_config = ConfigDict(extra='ignore')
    title: str | None = None

class Sl(BaseModel):
    model_config = ConfigDict(extra='ignore')
    title: str | None = None

class Fil(BaseModel):
    model_config = ConfigDict(extra='ignore')
    title: str | None = None

class Ar(BaseModel):
    model_config = ConfigDict(extra='ignore')
    title: str | None = None

class Es419(BaseModel):
    model_config = ConfigDict(extra='ignore')
    title: str | None = None

class My(BaseModel):
    model_config = ConfigDict(extra='ignore')
    title: str | None = None

class Sv(BaseModel):
    model_config = ConfigDict(extra='ignore')
    title: str | None = None

class No(BaseModel):
    model_config = ConfigDict(extra='ignore')
    title: str | None = None

class EsUs(BaseModel):
    model_config = ConfigDict(extra='ignore')
    title: str | None = None

class Kk(BaseModel):
    model_config = ConfigDict(extra='ignore')
    title: str | None = None

class Hi(BaseModel):
    model_config = ConfigDict(extra='ignore')
    title: str | None = None

class Mk(BaseModel):
    model_config = ConfigDict(extra='ignore')
    title: str | None = None

class Ne(BaseModel):
    model_config = ConfigDict(extra='ignore')
    title: str | None = None

class Sq(BaseModel):
    model_config = ConfigDict(extra='ignore')
    title: str | None = None

class Bs(BaseModel):
    model_config = ConfigDict(extra='ignore')
    title: str | None = None

class PtPt(BaseModel):
    model_config = ConfigDict(extra='ignore')
    title: str | None = None

class Sk(BaseModel):
    model_config = ConfigDict(extra='ignore')
    title: str | None = None

class Lt(BaseModel):
    model_config = ConfigDict(extra='ignore')
    title: str | None = None

class As(BaseModel):
    model_config = ConfigDict(extra='ignore')
    title: str | None = None

class Te(BaseModel):
    model_config = ConfigDict(extra='ignore')
    title: str | None = None

class FrCa(BaseModel):
    model_config = ConfigDict(extra='ignore')
    title: str | None = None

class Nl(BaseModel):
    model_config = ConfigDict(extra='ignore')
    title: str | None = None

class Or(BaseModel):
    model_config = ConfigDict(extra='ignore')
    title: str | None = None

class Mn(BaseModel):
    model_config = ConfigDict(extra='ignore')
    title: str | None = None

class ZhHk(BaseModel):
    model_config = ConfigDict(extra='ignore')
    title: str | None = None

class Id(BaseModel):
    model_config = ConfigDict(extra='ignore')
    title: str | None = None

class EnGb(BaseModel):
    model_config = ConfigDict(extra='ignore')
    title: str | None = None

class Sr(BaseModel):
    model_config = ConfigDict(extra='ignore')
    title: str | None = None

class El(BaseModel):
    model_config = ConfigDict(extra='ignore')
    title: str | None = None

class EnIn(BaseModel):
    model_config = ConfigDict(extra='ignore')
    title: str | None = None

class Es(BaseModel):
    model_config = ConfigDict(extra='ignore')
    title: str | None = None

class Ur(BaseModel):
    model_config = ConfigDict(extra='ignore')
    title: str | None = None

class Th(BaseModel):
    model_config = ConfigDict(extra='ignore')
    title: str | None = None

class Vi(BaseModel):
    model_config = ConfigDict(extra='ignore')
    title: str | None = None

class Bg(BaseModel):
    model_config = ConfigDict(extra='ignore')
    title: str | None = None

class Tr(BaseModel):
    model_config = ConfigDict(extra='ignore')
    title: str | None = None

class Lv(BaseModel):
    model_config = ConfigDict(extra='ignore')
    title: str | None = None

class Is(BaseModel):
    model_config = ConfigDict(extra='ignore')
    title: str | None = None

class Et(BaseModel):
    model_config = ConfigDict(extra='ignore')
    title: str | None = None

class Ta(BaseModel):
    model_config = ConfigDict(extra='ignore')
    title: str | None = None

class Ms(BaseModel):
    model_config = ConfigDict(extra='ignore')
    title: str | None = None

class Da(BaseModel):
    model_config = ConfigDict(extra='ignore')
    title: str | None = None

class Hr(BaseModel):
    model_config = ConfigDict(extra='ignore')
    title: str | None = None

class Pa(BaseModel):
    model_config = ConfigDict(extra='ignore')
    title: str | None = None

class Af(BaseModel):
    model_config = ConfigDict(extra='ignore')
    title: str | None = None

class SrLatn(BaseModel):
    model_config = ConfigDict(extra='ignore')
    title: str | None = None

class Zu(BaseModel):
    model_config = ConfigDict(extra='ignore')
    title: str | None = None

class Ky(BaseModel):
    model_config = ConfigDict(extra='ignore')
    title: str | None = None

class Hy(BaseModel):
    model_config = ConfigDict(extra='ignore')
    title: str | None = None

class Iw(BaseModel):
    model_config = ConfigDict(extra='ignore')
    title: str | None = None

class Pt(BaseModel):
    model_config = ConfigDict(extra='ignore')
    title: str | None = None

class Eu(BaseModel):
    model_config = ConfigDict(extra='ignore')
    title: str | None = None

class Bn(BaseModel):
    model_config = ConfigDict(extra='ignore')
    title: str | None = None

class Fi(BaseModel):
    model_config = ConfigDict(extra='ignore')
    title: str | None = None

class Ml(BaseModel):
    model_config = ConfigDict(extra='ignore')
    title: str | None = None

class Ro(BaseModel):
    model_config = ConfigDict(extra='ignore')
    title: str | None = None

class Gl(BaseModel):
    model_config = ConfigDict(extra='ignore')
    title: str | None = None

class Be(BaseModel):
    model_config = ConfigDict(extra='ignore')
    title: str | None = None

class Lo(BaseModel):
    model_config = ConfigDict(extra='ignore')
    title: str | None = None

class Uz(BaseModel):
    model_config = ConfigDict(extra='ignore')
    title: str | None = None

class ArXb(BaseModel):
    model_config = ConfigDict(extra='ignore')
    title: str | None = None

class EnXa(BaseModel):
    model_config = ConfigDict(extra='ignore')
    title: str | None = None

class Localizations(BaseModel):
    model_config = ConfigDict(extra='ignore')
    ja: Ja | None = None
    zh_tw: ZhTw | None = Field(None, alias='zh-TW')
    sw: Sw | None = None
    am: Am | None = None
    zh_cn: ZhCn | None = Field(None, alias='zh-CN')
    fr: Fr | None = None
    pl: Pl | None = None
    kn: Kn | None = None
    ko: Ko | None = None
    gu: Gu | None = None
    ru: Ru | None = None
    ca: Ca | None = None
    km: Km | None = None
    fa: Fa | None = None
    az: Az | None = None
    de: De | None = None
    hu: Hu | None = None
    en: En | None = None
    mr: Mr | None = None
    uk: Uk | None = None
    cs: Cs | None = None
    si: Si | None = None
    it: It | None = None
    ka: Ka | None = None
    sl: Sl | None = None
    fil: Fil | None = None
    ar: Ar | None = None
    es_419: Es419 | None = Field(None, alias='es-419')
    my: My | None = None
    sv: Sv | None = None
    no: No | None = None
    es_us: EsUs | None = Field(None, alias='es-US')
    kk: Kk | None = None
    hi: Hi | None = None
    mk: Mk | None = None
    ne: Ne | None = None
    sq: Sq | None = None
    bs: Bs | None = None
    pt_pt: PtPt | None = Field(None, alias='pt-PT')
    sk: Sk | None = None
    lt: Lt | None = None
    as_: As | None = Field(None, alias='as')
    te: Te | None = None
    fr_ca: FrCa | None = Field(None, alias='fr-CA')
    nl: Nl | None = None
    or_: Or | None = Field(None, alias='or')
    mn: Mn | None = None
    zh_hk: ZhHk | None = Field(None, alias='zh-HK')
    id: Id | None = None
    en_gb: EnGb | None = Field(None, alias='en-GB')
    sr: Sr | None = None
    el: El | None = None
    en_in: EnIn | None = Field(None, alias='en-IN')
    es: Es | None = None
    ur: Ur | None = None
    th: Th | None = None
    vi: Vi | None = None
    bg: Bg | None = None
    tr: Tr | None = None
    lv: Lv | None = None
    is_: Is | None = Field(None, alias='is')
    et: Et | None = None
    ta: Ta | None = None
    ms: Ms | None = None
    da: Da | None = None
    hr: Hr | None = None
    pa: Pa | None = None
    af: Af | None = None
    sr_latn: SrLatn | None = Field(None, alias='sr-Latn')
    zu: Zu | None = None
    ky: Ky | None = None
    hy: Hy | None = None
    iw: Iw | None = None
    pt: Pt | None = None
    eu: Eu | None = None
    bn: Bn | None = None
    fi: Fi | None = None
    ml: Ml | None = None
    ro: Ro | None = None
    gl: Gl | None = None
    be: Be | None = None
    lo: Lo | None = None
    uz: Uz | None = None
    ar_xb: ArXb | None = Field(None, alias='ar-XB')
    en_xa: EnXa | None = Field(None, alias='en-XA')

class Item(BaseModel):
    model_config = ConfigDict(extra='ignore')
    kind: str | None = None
    etag: str | None = None
    id: str | None = None
    snippet: Snippet | None = None
    status: Status | None = None
    content_details: ContentDetails | None = Field(None, alias='contentDetails')
    player: Player | None = None
    localizations: Localizations | None = None

class PlaylistsModel(BaseModel):
    model_config = ConfigDict(extra='ignore')
    kind: str | None = None
    etag: str | None = None
    page_info: PageInfo | None = Field(None, alias='pageInfo')
    items: list[Item] | None = None
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
