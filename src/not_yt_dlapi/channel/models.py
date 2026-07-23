from pydantic import AwareDatetime, ConfigDict, Field
from good_ass_pydantic_integrator import GAPIBaseModel
from typing import Any

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

class Thumbnails(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    default: Default
    medium: Medium
    high: High

class Localized(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    title: str
    description: str

class Snippet(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    title: str
    description: str
    custom_url: str | None = Field(None, alias='customUrl')
    published_at: AwareDatetime = Field(..., alias='publishedAt')
    thumbnails: Thumbnails
    localized: Localized
    country: str | None = None
    default_language: str | None = Field(None, alias='defaultLanguage')

class RelatedPlaylists(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    likes: str
    uploads: str

class ContentDetails(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    related_playlists: RelatedPlaylists = Field(..., alias='relatedPlaylists')

class Statistics(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    view_count: str = Field(..., alias='viewCount')
    subscriber_count: str = Field(..., alias='subscriberCount')
    hidden_subscriber_count: bool = Field(..., alias='hiddenSubscriberCount')
    video_count: str = Field(..., alias='videoCount')

class TopicDetails(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    topic_ids: list[str] | None = Field(None, alias='topicIds')
    topic_categories: list[str] | None = Field(None, alias='topicCategories')

class Status(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    privacy_status: str = Field(..., alias='privacyStatus')
    is_linked: bool = Field(..., alias='isLinked')
    long_uploads_status: str = Field(..., alias='longUploadsStatus')
    made_for_kids: bool | None = Field(None, alias='madeForKids')

class Channel(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    title: str
    description: str | None = None
    keywords: str | None = None
    unsubscribed_trailer: str | None = Field(None, alias='unsubscribedTrailer')
    country: str | None = None
    default_language: str | None = Field(None, alias='defaultLanguage')
    tracking_analytics_account_id: str | None = Field(None, alias='trackingAnalyticsAccountId')

class Image(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    banner_external_url: str = Field(..., alias='bannerExternalUrl')

class BrandingSettings(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    channel: Channel
    image: Image

class EnGb(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    title: str
    description: str

class KoKr(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    title: str
    description: str

class ZhTw(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    title: str
    description: str

class EnUs(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    title: str
    description: str

class JaJp(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    title: str
    description: str

class ZhHk(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    title: str
    description: str

class EsEs(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    title: str
    description: str

class ItIt(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    title: str
    description: str

class HuHu(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    title: str
    description: str

class IdId(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    title: str
    description: str

class ZhCn(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    title: str
    description: str

class FrFr(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    title: str
    description: str

class DeDe(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    title: str
    description: str

class PtBr(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    title: str
    description: str

class ThTh(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    title: str
    description: str

class PlPl(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    title: str
    description: str

class EnIn(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    title: str
    description: str

class UrPk(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    title: str
    description: str

class ZuZa(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    title: str
    description: str

class SwTz(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    title: str
    description: str

class KnIn(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    title: str
    description: str

class HyAm(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    title: str
    description: str

class MnMn(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    title: str
    description: str

class FrCa(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    title: str
    description: str

class KaGe(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    title: str
    description: str

class ElGr(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    title: str
    description: str

class LvLv(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    title: str
    description: str

class FiFi(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    title: str
    description: str

class NbNo(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    title: str
    description: str

class LoLa(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    title: str
    description: str

class DaDk(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    title: str
    description: str

class KyKg(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    title: str
    description: str

class ViVn(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    title: str
    description: str

class UzUz(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    title: str
    description: str

class OrIn(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    title: str
    description: str

class AsIn(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    title: str
    description: str

class MlIn(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    title: str
    description: str

class PtPt(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    title: str
    description: str

class EuEs(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    title: str
    description: str

class PaIn(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    title: str
    description: str

class SiLk(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    title: str
    description: str

class RoRo(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    title: str
    description: str

class TrTr(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    title: str
    description: str

class EsUs(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    title: str
    description: str

class FilPh(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    title: str
    description: str

class TaIn(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    title: str
    description: str

class SrRs(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    title: str
    description: str

class IsIs(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    title: str
    description: str

class SkSk(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    title: str
    description: str

class BnBd(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    title: str
    description: str

class MyMm(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    title: str
    description: str

class CaEs(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    title: str
    description: str

class BgBg(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    title: str
    description: str

class SlSi(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    title: str
    description: str

class BeBy(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    title: str
    description: str

class MrIn(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    title: str
    description: str

class KmKh(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    title: str
    description: str

class IwIl(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    title: str
    description: str

class EsMx(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    title: str
    description: str

class HrHr(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    title: str
    description: str

class LtLt(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    title: str
    description: str

class AfZa(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    title: str
    description: str

class EtEe(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    title: str
    description: str

class NeNp(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    title: str
    description: str

class NlNl(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    title: str
    description: str

class CsCz(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    title: str
    description: str

class KkKz(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    title: str
    description: str

class SqAl(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    title: str
    description: str

class AmEt(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    title: str
    description: str

class RuRu(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    title: str
    description: str

class MsMy(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    title: str
    description: str

class GuIn(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    title: str
    description: str

class HiIn(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    title: str
    description: str

class MkMk(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    title: str
    description: str

class FaIr(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    title: str
    description: str

class BsBa(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    title: str
    description: str

class ArEg(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    title: str
    description: str

class AzAz(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    title: str
    description: str

class GlEs(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    title: str
    description: str

class UkUa(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    title: str
    description: str

class TeIn(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    title: str
    description: str

class SvSe(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    title: str
    description: str

class Ks(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    description: str

class Af(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    title: str
    description: str

class Th(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    title: str
    description: str

class Mk(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    title: str
    description: str | None = None

class Ms(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    title: str
    description: str | None = None

class Ka(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    title: str
    description: str

class As(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    title: str
    description: str | None = None

class My(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    title: str
    description: str | None = None

class EsUs1(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    title: str
    description: str | None = None

class Kn(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    title: str
    description: str | None = None

class Hi(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    title: str
    description: str | None = None

class Fil(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    title: str
    description: str | None = None

class Pa(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    title: str
    description: str | None = None

class Hu(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    title: str
    description: str

class Nl(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    title: str
    description: str

class Ne(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    title: str
    description: str | None = None

class Sr(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    title: str
    description: str

class Uz(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    title: str
    description: str | None = None

class Bn(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    title: str
    description: str | None = None

class Sq(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    title: str
    description: str | None = None

class Ky(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    title: str
    description: str | None = None

class Sl(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    title: str
    description: str | None = None

class Uk(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    title: str
    description: str

class Ko(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    title: str
    description: str

class Is(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    title: str
    description: str

class Es(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    title: str
    description: str

class Kk(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    title: str
    description: str

class Et(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    title: str
    description: str

class Si(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    title: str
    description: str | None = None

class ZhTw1(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    title: str
    description: str

class Am(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    title: str
    description: str | None = None

class Tr(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    title: str
    description: str

class Bs(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    title: str
    description: str | None = None

class Az(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    title: str
    description: str | None = None

class Da(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    title: str
    description: str

class Ur(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    title: str
    description: str

class De(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    title: str
    description: str

class Ml(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    title: str
    description: str | None = None

class Ja(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    title: str
    description: str

class Gl(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    title: str
    description: str | None = None

class Id(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    title: str
    description: str

class Fa(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    title: str
    description: str

class FrCa1(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    title: str
    description: str | None = None

class EnGb1(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    title: str
    description: str | None = None

class EnIn1(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    title: str
    description: str | None = None

class Cy(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    description: str

class Bg(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    title: str
    description: str

class ZhCn1(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    title: str
    description: str | None = None

class Lt(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    title: str
    description: str

class Pt(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    title: str
    description: str

class Ca(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    title: str
    description: str | None = None

class El(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    title: str
    description: str

class Mr(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    title: str
    description: str | None = None

class PtBr1(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    title: str
    description: str | None = None

class Es419(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    title: str
    description: str | None = None

class Ro(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    title: str
    description: str

class Hr(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    title: str
    description: str | None = None

class Zu(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    title: str
    description: str | None = None

class ZhHk1(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    title: str
    description: str | None = None

class Sw(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    title: str
    description: str | None = None

class Sv(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    title: str
    description: str

class Hy(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    title: str
    description: str

class Iw(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    title: str
    description: str

class Ru(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    title: str
    description: str

class Sk(GAPIBaseModel):
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

class Pl(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    title: str
    description: str

class Lv(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    title: str
    description: str

class Eu(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    title: str
    description: str | None = None

class Gu(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    title: str
    description: str | None = None

class Vi(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    title: str
    description: str

class SrLatn(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    title: str
    description: str | None = None

class Be(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    title: str
    description: str | None = None

class Ta(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    title: str
    description: str | None = None

class PtPt1(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    title: str
    description: str | None = None

class Mn(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    title: str
    description: str | None = None

class Ar(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    title: str
    description: str

class Km(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    title: str
    description: str | None = None

class En(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    title: str
    description: str

class Zh(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    description: str

class Te(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    title: str
    description: str | None = None

class Fr(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    title: str
    description: str

class No(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    title: str
    description: str

class It(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    title: str
    description: str

class Lo(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    title: str
    description: str | None = None

class Or(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    title: str
    description: str | None = None

class Localizations(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    en_gb: EnGb | None = Field(None, alias='en_GB')
    ko_kr: KoKr | None = Field(None, alias='ko_KR')
    zh_tw: ZhTw | None = Field(None, alias='zh_TW')
    en_us: EnUs | None = Field(None, alias='en_US')
    ja_jp: JaJp | None = Field(None, alias='ja_JP')
    zh_hk: ZhHk | None = Field(None, alias='zh_HK')
    es_es: EsEs | None = Field(None, alias='es_ES')
    it_it: ItIt | None = Field(None, alias='it_IT')
    hu_hu: HuHu | None = Field(None, alias='hu_HU')
    id_id: IdId | None = Field(None, alias='id_ID')
    zh_cn: ZhCn | None = Field(None, alias='zh_CN')
    fr_fr: FrFr | None = Field(None, alias='fr_FR')
    de_de: DeDe | None = Field(None, alias='de_DE')
    pt_br: PtBr | None = Field(None, alias='pt_BR')
    th_th: ThTh | None = Field(None, alias='th_TH')
    pl_pl: PlPl | None = Field(None, alias='pl_PL')
    en_in: EnIn | None = Field(None, alias='en_IN')
    ur_pk: UrPk | None = Field(None, alias='ur_PK')
    zu_za: ZuZa | None = Field(None, alias='zu_ZA')
    sw_tz: SwTz | None = Field(None, alias='sw_TZ')
    kn_in: KnIn | None = Field(None, alias='kn_IN')
    hy_am: HyAm | None = Field(None, alias='hy_AM')
    mn_mn: MnMn | None = Field(None, alias='mn_MN')
    fr_ca: FrCa | None = Field(None, alias='fr_CA')
    ka_ge: KaGe | None = Field(None, alias='ka_GE')
    el_gr: ElGr | None = Field(None, alias='el_GR')
    lv_lv: LvLv | None = Field(None, alias='lv_LV')
    fi_fi: FiFi | None = Field(None, alias='fi_FI')
    nb_no: NbNo | None = Field(None, alias='nb_NO')
    lo_la: LoLa | None = Field(None, alias='lo_LA')
    da_dk: DaDk | None = Field(None, alias='da_DK')
    ky_kg: KyKg | None = Field(None, alias='ky_KG')
    vi_vn: ViVn | None = Field(None, alias='vi_VN')
    uz_uz: UzUz | None = Field(None, alias='uz_UZ')
    or_in: OrIn | None = Field(None, alias='or_IN')
    as_in: AsIn | None = Field(None, alias='as_IN')
    ml_in: MlIn | None = Field(None, alias='ml_IN')
    pt_pt: PtPt | None = Field(None, alias='pt_PT')
    eu_es: EuEs | None = Field(None, alias='eu_ES')
    pa_in: PaIn | None = Field(None, alias='pa_IN')
    si_lk: SiLk | None = Field(None, alias='si_LK')
    ro_ro: RoRo | None = Field(None, alias='ro_RO')
    tr_tr: TrTr | None = Field(None, alias='tr_TR')
    es_us: EsUs | None = Field(None, alias='es_US')
    fil_ph: FilPh | None = Field(None, alias='fil_PH')
    ta_in: TaIn | None = Field(None, alias='ta_IN')
    sr_rs: SrRs | None = Field(None, alias='sr_RS')
    is_is: IsIs | None = Field(None, alias='is_IS')
    sk_sk: SkSk | None = Field(None, alias='sk_SK')
    bn_bd: BnBd | None = Field(None, alias='bn_BD')
    my_mm: MyMm | None = Field(None, alias='my_MM')
    ca_es: CaEs | None = Field(None, alias='ca_ES')
    bg_bg: BgBg | None = Field(None, alias='bg_BG')
    sl_si: SlSi | None = Field(None, alias='sl_SI')
    be_by: BeBy | None = Field(None, alias='be_BY')
    mr_in: MrIn | None = Field(None, alias='mr_IN')
    km_kh: KmKh | None = Field(None, alias='km_KH')
    iw_il: IwIl | None = Field(None, alias='iw_IL')
    es_mx: EsMx | None = Field(None, alias='es_MX')
    hr_hr: HrHr | None = Field(None, alias='hr_HR')
    lt_lt: LtLt | None = Field(None, alias='lt_LT')
    af_za: AfZa | None = Field(None, alias='af_ZA')
    et_ee: EtEe | None = Field(None, alias='et_EE')
    ne_np: NeNp | None = Field(None, alias='ne_NP')
    nl_nl: NlNl | None = Field(None, alias='nl_NL')
    cs_cz: CsCz | None = Field(None, alias='cs_CZ')
    kk_kz: KkKz | None = Field(None, alias='kk_KZ')
    sq_al: SqAl | None = Field(None, alias='sq_AL')
    am_et: AmEt | None = Field(None, alias='am_ET')
    ru_ru: RuRu | None = Field(None, alias='ru_RU')
    ms_my: MsMy | None = Field(None, alias='ms_MY')
    gu_in: GuIn | None = Field(None, alias='gu_IN')
    hi_in: HiIn | None = Field(None, alias='hi_IN')
    mk_mk: MkMk | None = Field(None, alias='mk_MK')
    fa_ir: FaIr | None = Field(None, alias='fa_IR')
    bs_ba: BsBa | None = Field(None, alias='bs_BA')
    ar_eg: ArEg | None = Field(None, alias='ar_EG')
    az_az: AzAz | None = Field(None, alias='az_AZ')
    gl_es: GlEs | None = Field(None, alias='gl_ES')
    uk_ua: UkUa | None = Field(None, alias='uk_UA')
    te_in: TeIn | None = Field(None, alias='te_IN')
    sv_se: SvSe | None = Field(None, alias='sv_SE')
    ks: Ks | None = None
    af: Af | None = None
    th: Th | None = None
    mk: Mk | None = None
    ms: Ms | None = None
    ka: Ka | None = None
    as_: As | None = Field(None, alias='as')
    my: My | None = None
    es_us_1: EsUs1 | None = Field(None, alias='es-US')
    kn: Kn | None = None
    hi: Hi | None = None
    fil: Fil | None = None
    pa: Pa | None = None
    hu: Hu | None = None
    nl: Nl | None = None
    ne: Ne | None = None
    sr: Sr | None = None
    uz: Uz | None = None
    bn: Bn | None = None
    sq: Sq | None = None
    ky: Ky | None = None
    sl: Sl | None = None
    uk: Uk | None = None
    ko: Ko | None = None
    is_: Is | None = Field(None, alias='is')
    es: Es | None = None
    kk: Kk | None = None
    et: Et | None = None
    si: Si | None = None
    zh_tw_1: ZhTw1 | None = Field(None, alias='zh-TW')
    am: Am | None = None
    tr: Tr | None = None
    bs: Bs | None = None
    az: Az | None = None
    da: Da | None = None
    ur: Ur | None = None
    de: De | None = None
    ml: Ml | None = None
    ja: Ja | None = None
    gl: Gl | None = None
    id: Id | None = None
    fa: Fa | None = None
    fr_ca_1: FrCa1 | None = Field(None, alias='fr-CA')
    en_gb_1: EnGb1 | None = Field(None, alias='en-GB')
    en_in_1: EnIn1 | None = Field(None, alias='en-IN')
    cy: Cy | None = None
    bg: Bg | None = None
    zh_cn_1: ZhCn1 | None = Field(None, alias='zh-CN')
    lt: Lt | None = None
    pt: Pt | None = None
    ca: Ca | None = None
    el: El | None = None
    mr: Mr | None = None
    pt_br_1: PtBr1 | None = Field(None, alias='pt-BR')
    es_419: Es419 | None = Field(None, alias='es-419')
    ro: Ro | None = None
    hr: Hr | None = None
    zu: Zu | None = None
    zh_hk_1: ZhHk1 | None = Field(None, alias='zh-HK')
    sw: Sw | None = None
    sv: Sv | None = None
    hy: Hy | None = None
    iw: Iw | None = None
    ru: Ru | None = None
    sk: Sk | None = None
    cs: Cs | None = None
    fi: Fi | None = None
    pl: Pl | None = None
    lv: Lv | None = None
    eu: Eu | None = None
    gu: Gu | None = None
    vi: Vi | None = None
    sr_latn: SrLatn | None = Field(None, alias='sr-Latn')
    be: Be | None = None
    ta: Ta | None = None
    pt_pt_1: PtPt1 | None = Field(None, alias='pt-PT')
    mn: Mn | None = None
    ar: Ar | None = None
    km: Km | None = None
    en: En | None = None
    zh: Zh | None = None
    te: Te | None = None
    fr: Fr | None = None
    no: No | None = None
    it: It | None = None
    lo: Lo | None = None
    or_: Or | None = Field(None, alias='or')

class Item(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    kind: str
    etag: str
    id: str
    snippet: Snippet
    content_details: ContentDetails = Field(..., alias='contentDetails')
    statistics: Statistics
    topic_details: TopicDetails | None = Field(None, alias='topicDetails')
    status: Status
    branding_settings: BrandingSettings = Field(..., alias='brandingSettings')
    content_owner_details: dict[str, Any] = Field(..., alias='contentOwnerDetails')
    localizations: Localizations | None = None

class NotYtDlapi(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    channel_id: str | None = None
    part: str
    timestamp: AwareDatetime
    handle: str | None = None
    username: str | None = None

class ChannelsModel(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    kind: str
    etag: str
    page_info: PageInfo = Field(..., alias='pageInfo')
    items: list[Item]
    not_yt_dlapi: NotYtDlapi | None = None
