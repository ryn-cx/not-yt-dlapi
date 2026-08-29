from typing import Self
from pydantic import ModelWrapValidatorHandler, PrivateAttr, model_validator
from pydantic import AwareDatetime, BaseModel, ConfigDict, Field
from typing import Any

class PageInfo(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    total_results: int | None = Field(None, alias='totalResults')
    results_per_page: int | None = Field(None, alias='resultsPerPage')

class Default(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    url: str | None = None
    width: int | None = None
    height: int | None = None

class Medium(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    url: str | None = None
    width: int | None = None
    height: int | None = None

class High(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    url: str | None = None
    width: int | None = None
    height: int | None = None

class Thumbnails(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    default: Default | None = None
    medium: Medium | None = None
    high: High | None = None

class Localized(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    title: str | None = None
    description: str | None = None

class Snippet(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    title: str | None = None
    description: str | None = None
    custom_url: str | None = Field(None, alias='customUrl')
    published_at: AwareDatetime | None = Field(None, alias='publishedAt')
    thumbnails: Thumbnails | None = None
    localized: Localized | None = None
    country: str | None = None

class RelatedPlaylists(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    likes: str | None = None
    uploads: str | None = None

class ContentDetails(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    related_playlists: RelatedPlaylists | None = Field(None, alias='relatedPlaylists')

class Statistics(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    view_count: str | None = Field(None, alias='viewCount')
    subscriber_count: str | None = Field(None, alias='subscriberCount')
    hidden_subscriber_count: bool | None = Field(None, alias='hiddenSubscriberCount')
    video_count: str | None = Field(None, alias='videoCount')

class Status(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    privacy_status: str | None = Field(None, alias='privacyStatus')
    is_linked: bool | None = Field(None, alias='isLinked')
    long_uploads_status: str | None = Field(None, alias='longUploadsStatus')
    made_for_kids: bool | None = Field(None, alias='madeForKids')

class Channel(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    title: str | None = None
    keywords: str | None = None
    unsubscribed_trailer: str | None = Field(None, alias='unsubscribedTrailer')
    country: str | None = None
    description: str | None = None

class Image(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    banner_external_url: str | None = Field(None, alias='bannerExternalUrl')

class BrandingSettings(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    channel: Channel | None = None
    image: Image | None = None

class TopicDetails(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    topic_ids: list[str] | None = Field(None, alias='topicIds')
    topic_categories: list[str] | None = Field(None, alias='topicCategories')

class Ne(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    title: str | None = None
    description: str | None = None

class Bn(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    title: str | None = None
    description: str | None = None

class Hy(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    title: str | None = None
    description: str | None = None

class Ru(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    title: str | None = None
    description: str | None = None

class EsUs(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    title: str | None = None
    description: str | None = None

class Hr(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    title: str | None = None
    description: str | None = None

class Hi(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    title: str | None = None
    description: str | None = None

class Pa(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    title: str | None = None
    description: str | None = None

class EnIn(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    title: str | None = None
    description: str | None = None

class Eu(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    title: str | None = None
    description: str | None = None

class PtPt(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    title: str | None = None
    description: str | None = None

class Hu(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    title: str | None = None
    description: str | None = None

class Sk(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    title: str | None = None
    description: str | None = None

class Ta(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    title: str | None = None
    description: str | None = None

class Lo(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    title: str | None = None
    description: str | None = None

class Sq(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    title: str | None = None
    description: str | None = None

class Ja(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    title: str | None = None
    description: str | None = None

class Km(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    title: str | None = None
    description: str | None = None

class Af(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    title: str | None = None
    description: str | None = None

class Es(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    title: str | None = None
    description: str | None = None

class Ur(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    title: str | None = None
    description: str | None = None

class Et(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    title: str | None = None
    description: str | None = None

class Iw(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    title: str | None = None
    description: str | None = None

class Sr(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    title: str | None = None
    description: str | None = None

class Fi(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    title: str | None = None
    description: str | None = None

class Da(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    title: str | None = None
    description: str | None = None

class ZhTw(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    title: str | None = None
    description: str | None = None

class De(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    title: str | None = None
    description: str | None = None

class Cs(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    title: str | None = None
    description: str | None = None

class Bs(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    title: str | None = None
    description: str | None = None

class As(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    title: str | None = None
    description: str | None = None

class My(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    title: str | None = None
    description: str | None = None

class Sl(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    title: str | None = None
    description: str | None = None

class It(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    title: str | None = None
    description: str | None = None

class Id(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    title: str | None = None
    description: str | None = None

class Be(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    title: str | None = None
    description: str | None = None

class Pl(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    title: str | None = None
    description: str | None = None

class EnGb(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    title: str | None = None
    description: str | None = None

class ZhHk(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    title: str | None = None
    description: str | None = None

class Th(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    title: str | None = None
    description: str | None = None

class Is(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    title: str | None = None
    description: str | None = None

class Fr(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    title: str | None = None
    description: str | None = None

class Ro(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    title: str | None = None
    description: str | None = None

class Am(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    title: str | None = None
    description: str | None = None

class No(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    title: str | None = None
    description: str | None = None

class En(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    title: str | None = None
    description: str | None = None

class Fil(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    title: str | None = None
    description: str | None = None

class Nl(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    title: str | None = None
    description: str | None = None

class Fa(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    title: str | None = None
    description: str | None = None

class Bg(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    title: str | None = None
    description: str | None = None

class SrLatn(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    title: str | None = None
    description: str | None = None

class Mn(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    title: str | None = None
    description: str | None = None

class Az(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    title: str | None = None
    description: str | None = None

class Kn(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    title: str | None = None
    description: str | None = None

class Pt(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    title: str | None = None
    description: str | None = None

class Sw(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    title: str | None = None
    description: str | None = None

class Tr(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    title: str | None = None
    description: str | None = None

class Sv(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    title: str | None = None
    description: str | None = None

class Ca(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    title: str | None = None
    description: str | None = None

class Ko(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    title: str | None = None
    description: str | None = None

class Or(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    title: str | None = None
    description: str | None = None

class Ml(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    title: str | None = None
    description: str | None = None

class ZhCn(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    title: str | None = None
    description: str | None = None

class Mr(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    title: str | None = None
    description: str | None = None

class Ky(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    title: str | None = None
    description: str | None = None

class Zu(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    title: str | None = None
    description: str | None = None

class FrCa(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    title: str | None = None
    description: str | None = None

class Es419(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    title: str | None = None
    description: str | None = None

class Si(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    title: str | None = None
    description: str | None = None

class Ka(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    title: str | None = None
    description: str | None = None

class Gu(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    title: str | None = None
    description: str | None = None

class Ar(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    title: str | None = None
    description: str | None = None

class Gl(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    title: str | None = None
    description: str | None = None

class Vi(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    title: str | None = None
    description: str | None = None

class Uk(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    title: str | None = None
    description: str | None = None

class Lv(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    title: str | None = None
    description: str | None = None

class Mk(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    title: str | None = None
    description: str | None = None

class Kk(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    title: str | None = None
    description: str | None = None

class Ms(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    title: str | None = None
    description: str | None = None

class Lt(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    title: str | None = None
    description: str | None = None

class Te(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    title: str | None = None
    description: str | None = None

class El(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    title: str | None = None
    description: str | None = None

class Uz(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    title: str | None = None
    description: str | None = None

class Zh(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    description: str | None = None

class PtBr(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    title: str | None = None
    description: str | None = None

class Localizations(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    ne: Ne | None = None
    bn: Bn | None = None
    hy: Hy | None = None
    ru: Ru | None = None
    es_us: EsUs | None = Field(None, alias='es-US')
    hr: Hr | None = None
    hi: Hi | None = None
    pa: Pa | None = None
    en_in: EnIn | None = Field(None, alias='en-IN')
    eu: Eu | None = None
    pt_pt: PtPt | None = Field(None, alias='pt-PT')
    hu: Hu | None = None
    sk: Sk | None = None
    ta: Ta | None = None
    lo: Lo | None = None
    sq: Sq | None = None
    ja: Ja | None = None
    km: Km | None = None
    af: Af | None = None
    es: Es | None = None
    ur: Ur | None = None
    et: Et | None = None
    iw: Iw | None = None
    sr: Sr | None = None
    fi: Fi | None = None
    da: Da | None = None
    zh_tw: ZhTw | None = Field(None, alias='zh-TW')
    de: De | None = None
    cs: Cs | None = None
    bs: Bs | None = None
    as_: As | None = Field(None, alias='as')
    my: My | None = None
    sl: Sl | None = None
    it: It | None = None
    id: Id | None = None
    be: Be | None = None
    pl: Pl | None = None
    en_gb: EnGb | None = Field(None, alias='en-GB')
    zh_hk: ZhHk | None = Field(None, alias='zh-HK')
    th: Th | None = None
    is_: Is | None = Field(None, alias='is')
    fr: Fr | None = None
    ro: Ro | None = None
    am: Am | None = None
    no: No | None = None
    en: En | None = None
    fil: Fil | None = None
    nl: Nl | None = None
    fa: Fa | None = None
    bg: Bg | None = None
    sr_latn: SrLatn | None = Field(None, alias='sr-Latn')
    mn: Mn | None = None
    az: Az | None = None
    kn: Kn | None = None
    pt: Pt | None = None
    sw: Sw | None = None
    tr: Tr | None = None
    sv: Sv | None = None
    ca: Ca | None = None
    ko: Ko | None = None
    or_: Or | None = Field(None, alias='or')
    ml: Ml | None = None
    zh_cn: ZhCn | None = Field(None, alias='zh-CN')
    mr: Mr | None = None
    ky: Ky | None = None
    zu: Zu | None = None
    fr_ca: FrCa | None = Field(None, alias='fr-CA')
    es_419: Es419 | None = Field(None, alias='es-419')
    si: Si | None = None
    ka: Ka | None = None
    gu: Gu | None = None
    ar: Ar | None = None
    gl: Gl | None = None
    vi: Vi | None = None
    uk: Uk | None = None
    lv: Lv | None = None
    mk: Mk | None = None
    kk: Kk | None = None
    ms: Ms | None = None
    lt: Lt | None = None
    te: Te | None = None
    el: El | None = None
    uz: Uz | None = None
    zh: Zh | None = None
    pt_br: PtBr | None = Field(None, alias='pt-BR')

class Item(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    kind: str | None = None
    etag: str | None = None
    id: str | None = None
    snippet: Snippet | None = None
    content_details: ContentDetails | None = Field(None, alias='contentDetails')
    statistics: Statistics | None = None
    status: Status | None = None
    branding_settings: BrandingSettings | None = Field(None, alias='brandingSettings')
    content_owner_details: dict[str, Any] | None = Field(None, alias='contentOwnerDetails')
    topic_details: TopicDetails | None = Field(None, alias='topicDetails')
    localizations: Localizations | None = None

class ChannelsModel(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    kind: str | None = None
    etag: str | None = None
    page_info: PageInfo | None = Field(None, alias='pageInfo')
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
