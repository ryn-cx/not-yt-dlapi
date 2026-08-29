from typing import Any, Self
from pydantic import ModelWrapValidatorHandler, PrivateAttr, model_validator
from pydantic import ConfigDict
from pydantic import BaseModel, Field
from uuid import UUID

class Param(BaseModel):
    model_config = ConfigDict(defer_build=True)
    key: str
    value: str

class ServiceTrackingParam(BaseModel):
    model_config = ConfigDict(defer_build=True)
    service: str
    params: list[Param]

class MainAppWebResponseContext(BaseModel):
    model_config = ConfigDict(defer_build=True)
    logged_out: bool = Field(..., alias='loggedOut')
    tracking_param: str = Field(..., alias='trackingParam')

class WebResponseContextPreloadData(BaseModel):
    model_config = ConfigDict(defer_build=True)
    preload_message_names: list[str] = Field(..., alias='preloadMessageNames')

class WebResponseContextExtensionData(BaseModel):
    model_config = ConfigDict(defer_build=True)
    web_response_context_preload_data: WebResponseContextPreloadData = Field(..., alias='webResponseContextPreloadData')
    has_decorated: bool = Field(..., alias='hasDecorated')

class ResponseContext(BaseModel):
    model_config = ConfigDict(defer_build=True)
    visitor_data: str = Field(..., alias='visitorData')
    service_tracking_params: list[ServiceTrackingParam] = Field(..., alias='serviceTrackingParams')
    max_age_seconds: int = Field(..., alias='maxAgeSeconds')
    main_app_web_response_context: MainAppWebResponseContext = Field(..., alias='mainAppWebResponseContext')
    response_id: str = Field(..., alias='responseId')
    web_response_context_extension_data: WebResponseContextExtensionData = Field(..., alias='webResponseContextExtensionData')

class Thumbnail1(BaseModel):
    model_config = ConfigDict(defer_build=True)
    url: str
    width: int
    height: int

class SampledThumbnailColor(BaseModel):
    model_config = ConfigDict(defer_build=True)
    red: int
    green: int
    blue: int

class DarkColorPalette(BaseModel):
    model_config = ConfigDict(defer_build=True)
    section2_color: int = Field(..., alias='section2Color')
    icon_inactive_color: int = Field(..., alias='iconInactiveColor')
    icon_disabled_color: int = Field(..., alias='iconDisabledColor')

class VibrantColorPalette(BaseModel):
    model_config = ConfigDict(defer_build=True)
    icon_inactive_color: int = Field(..., alias='iconInactiveColor')

class Thumbnail(BaseModel):
    model_config = ConfigDict(defer_build=True)
    thumbnails: list[Thumbnail1]
    sampled_thumbnail_color: SampledThumbnailColor = Field(..., alias='sampledThumbnailColor')
    dark_color_palette: DarkColorPalette = Field(..., alias='darkColorPalette')
    vibrant_color_palette: VibrantColorPalette = Field(..., alias='vibrantColorPalette')

class WebCommandMetadata(BaseModel):
    model_config = ConfigDict(defer_build=True)
    url: str
    web_page_type: str = Field(..., alias='webPageType')
    root_ve: int = Field(..., alias='rootVe')

class CommandMetadata(BaseModel):
    model_config = ConfigDict(defer_build=True)
    web_command_metadata: WebCommandMetadata = Field(..., alias='webCommandMetadata')

class VssLoggingContext(BaseModel):
    model_config = ConfigDict(defer_build=True)
    serialized_context_data: str = Field(..., alias='serializedContextData')

class LoggingContext(BaseModel):
    model_config = ConfigDict(defer_build=True)
    vss_logging_context: VssLoggingContext = Field(..., alias='vssLoggingContext')

class CommonConfig(BaseModel):
    model_config = ConfigDict(defer_build=True)
    url: str

class Html5PlaybackOnesieConfig(BaseModel):
    model_config = ConfigDict(defer_build=True)
    common_config: CommonConfig = Field(..., alias='commonConfig')

class WatchEndpointSupportedOnesieConfig(BaseModel):
    model_config = ConfigDict(defer_build=True)
    html5_playback_onesie_config: Html5PlaybackOnesieConfig = Field(..., alias='html5PlaybackOnesieConfig')

class WatchEndpoint(BaseModel):
    model_config = ConfigDict(defer_build=True)
    video_id: str = Field(..., alias='videoId')
    playlist_id: str = Field(..., alias='playlistId')
    params: str
    logging_context: LoggingContext = Field(..., alias='loggingContext')
    watch_endpoint_supported_onesie_config: WatchEndpointSupportedOnesieConfig = Field(..., alias='watchEndpointSupportedOnesieConfig')
    player_params: str | None = Field(None, alias='playerParams')

class NavigationEndpoint(BaseModel):
    model_config = ConfigDict(defer_build=True)
    click_tracking_params: str = Field(..., alias='clickTrackingParams')
    command_metadata: CommandMetadata = Field(..., alias='commandMetadata')
    watch_endpoint: WatchEndpoint = Field(..., alias='watchEndpoint')

class Run(BaseModel):
    model_config = ConfigDict(defer_build=True)
    text: str
    navigation_endpoint: NavigationEndpoint = Field(..., alias='navigationEndpoint')

class Title(BaseModel):
    model_config = ConfigDict(defer_build=True)
    runs: list[Run]

class WebCommandMetadata1(BaseModel):
    model_config = ConfigDict(defer_build=True)
    url: str
    web_page_type: str = Field(..., alias='webPageType')
    root_ve: int = Field(..., alias='rootVe')
    api_url: str = Field(..., alias='apiUrl')

class CommandMetadata1(BaseModel):
    model_config = ConfigDict(defer_build=True)
    web_command_metadata: WebCommandMetadata1 = Field(..., alias='webCommandMetadata')

class BrowseEndpoint(BaseModel):
    model_config = ConfigDict(defer_build=True)
    browse_id: str = Field(..., alias='browseId')
    canonical_base_url: str = Field(..., alias='canonicalBaseUrl')

class NavigationEndpoint1(BaseModel):
    model_config = ConfigDict(defer_build=True)
    click_tracking_params: str = Field(..., alias='clickTrackingParams')
    command_metadata: CommandMetadata1 = Field(..., alias='commandMetadata')
    browse_endpoint: BrowseEndpoint = Field(..., alias='browseEndpoint')

class Run1(BaseModel):
    model_config = ConfigDict(defer_build=True)
    text: str
    navigation_endpoint: NavigationEndpoint1 | None = Field(None, alias='navigationEndpoint')

class ShortBylineText(BaseModel):
    model_config = ConfigDict(defer_build=True)
    runs: list[Run1]

class Run2(BaseModel):
    model_config = ConfigDict(defer_build=True)
    text: str

class VideoCountText(BaseModel):
    model_config = ConfigDict(defer_build=True)
    runs: list[Run2]

class WebCommandMetadata2(BaseModel):
    model_config = ConfigDict(defer_build=True)
    url: str
    web_page_type: str = Field(..., alias='webPageType')
    root_ve: int = Field(..., alias='rootVe')

class CommandMetadata2(BaseModel):
    model_config = ConfigDict(defer_build=True)
    web_command_metadata: WebCommandMetadata2 = Field(..., alias='webCommandMetadata')

class LoggingContext1(BaseModel):
    model_config = ConfigDict(defer_build=True)
    vss_logging_context: VssLoggingContext = Field(..., alias='vssLoggingContext')

class Html5PlaybackOnesieConfig1(BaseModel):
    model_config = ConfigDict(defer_build=True)
    common_config: CommonConfig = Field(..., alias='commonConfig')

class WatchEndpointSupportedOnesieConfig1(BaseModel):
    model_config = ConfigDict(defer_build=True)
    html5_playback_onesie_config: Html5PlaybackOnesieConfig1 = Field(..., alias='html5PlaybackOnesieConfig')

class WatchEndpoint1(BaseModel):
    model_config = ConfigDict(defer_build=True)
    video_id: str = Field(..., alias='videoId')
    playlist_id: str = Field(..., alias='playlistId')
    params: str
    logging_context: LoggingContext1 = Field(..., alias='loggingContext')
    watch_endpoint_supported_onesie_config: WatchEndpointSupportedOnesieConfig1 = Field(..., alias='watchEndpointSupportedOnesieConfig')
    player_params: str | None = Field(None, alias='playerParams')

class NavigationEndpoint2(BaseModel):
    model_config = ConfigDict(defer_build=True)
    click_tracking_params: str = Field(..., alias='clickTrackingParams')
    command_metadata: CommandMetadata2 = Field(..., alias='commandMetadata')
    watch_endpoint: WatchEndpoint1 = Field(..., alias='watchEndpoint')

class VideoCountShortText(BaseModel):
    model_config = ConfigDict(defer_build=True)
    simple_text: str = Field(..., alias='simpleText')

class Thumbnail2(BaseModel):
    model_config = ConfigDict(defer_build=True)
    url: str
    width: int
    height: int

class SidebarThumbnail(BaseModel):
    model_config = ConfigDict(defer_build=True)
    thumbnails: list[Thumbnail2]

class Run3(BaseModel):
    model_config = ConfigDict(defer_build=True)
    text: str
    bold: bool | None = None

class ThumbnailText(BaseModel):
    model_config = ConfigDict(defer_build=True)
    runs: list[Run3]

class Thumbnail3(BaseModel):
    model_config = ConfigDict(defer_build=True)
    thumbnails: list[Thumbnail2]
    sampled_thumbnail_color: SampledThumbnailColor = Field(..., alias='sampledThumbnailColor')
    dark_color_palette: DarkColorPalette = Field(..., alias='darkColorPalette')
    vibrant_color_palette: VibrantColorPalette = Field(..., alias='vibrantColorPalette')

class PlaylistCustomThumbnailRenderer(BaseModel):
    model_config = ConfigDict(defer_build=True)
    thumbnail: Thumbnail3

class ThumbnailRenderer(BaseModel):
    model_config = ConfigDict(defer_build=True)
    playlist_custom_thumbnail_renderer: PlaylistCustomThumbnailRenderer = Field(..., alias='playlistCustomThumbnailRenderer')

class WebCommandMetadata3(BaseModel):
    model_config = ConfigDict(defer_build=True)
    url: str
    web_page_type: str = Field(..., alias='webPageType')
    root_ve: int = Field(..., alias='rootVe')
    api_url: str = Field(..., alias='apiUrl')

class CommandMetadata3(BaseModel):
    model_config = ConfigDict(defer_build=True)
    web_command_metadata: WebCommandMetadata3 = Field(..., alias='webCommandMetadata')

class NavigationEndpoint3(BaseModel):
    model_config = ConfigDict(defer_build=True)
    click_tracking_params: str = Field(..., alias='clickTrackingParams')
    command_metadata: CommandMetadata3 = Field(..., alias='commandMetadata')
    browse_endpoint: BrowseEndpoint = Field(..., alias='browseEndpoint')

class Run4(BaseModel):
    model_config = ConfigDict(defer_build=True)
    text: str
    navigation_endpoint: NavigationEndpoint3 | None = Field(None, alias='navigationEndpoint')

class LongBylineText(BaseModel):
    model_config = ConfigDict(defer_build=True)
    runs: list[Run4]

class Text(BaseModel):
    model_config = ConfigDict(defer_build=True)
    simple_text: str = Field(..., alias='simpleText')

class Icon(BaseModel):
    model_config = ConfigDict(defer_build=True)
    icon_type: str = Field(..., alias='iconType')

class ThumbnailOverlayBottomPanelRenderer(BaseModel):
    model_config = ConfigDict(defer_build=True)
    text: Text
    icon: Icon

class Run5(BaseModel):
    model_config = ConfigDict(defer_build=True)
    text: str

class Text1(BaseModel):
    model_config = ConfigDict(defer_build=True)
    runs: list[Run5]

class ThumbnailOverlayHoverTextRenderer(BaseModel):
    model_config = ConfigDict(defer_build=True)
    text: Text1
    icon: Icon

class Text2(BaseModel):
    model_config = ConfigDict(defer_build=True)
    runs: list[Run5]

class ThumbnailOverlayNowPlayingRenderer(BaseModel):
    model_config = ConfigDict(defer_build=True)
    text: Text2

class ThumbnailOverlay(BaseModel):
    model_config = ConfigDict(defer_build=True)
    thumbnail_overlay_bottom_panel_renderer: ThumbnailOverlayBottomPanelRenderer | None = Field(None, alias='thumbnailOverlayBottomPanelRenderer')
    thumbnail_overlay_hover_text_renderer: ThumbnailOverlayHoverTextRenderer | None = Field(None, alias='thumbnailOverlayHoverTextRenderer')
    thumbnail_overlay_now_playing_renderer: ThumbnailOverlayNowPlayingRenderer | None = Field(None, alias='thumbnailOverlayNowPlayingRenderer')

class CommandMetadata4(BaseModel):
    model_config = ConfigDict(defer_build=True)
    web_command_metadata: WebCommandMetadata3 = Field(..., alias='webCommandMetadata')

class BrowseEndpoint2(BaseModel):
    model_config = ConfigDict(defer_build=True)
    browse_id: str = Field(..., alias='browseId')

class NavigationEndpoint4(BaseModel):
    model_config = ConfigDict(defer_build=True)
    click_tracking_params: str = Field(..., alias='clickTrackingParams')
    command_metadata: CommandMetadata4 = Field(..., alias='commandMetadata')
    browse_endpoint: BrowseEndpoint2 = Field(..., alias='browseEndpoint')

class Run7(BaseModel):
    model_config = ConfigDict(defer_build=True)
    text: str
    navigation_endpoint: NavigationEndpoint4 = Field(..., alias='navigationEndpoint')

class ViewPlaylistText(BaseModel):
    model_config = ConfigDict(defer_build=True)
    runs: list[Run7]

class GridPlaylistRenderer(BaseModel):
    model_config = ConfigDict(defer_build=True)
    playlist_id: str = Field(..., alias='playlistId')
    thumbnail: Thumbnail
    title: Title
    short_byline_text: ShortBylineText = Field(..., alias='shortBylineText')
    video_count_text: VideoCountText = Field(..., alias='videoCountText')
    navigation_endpoint: NavigationEndpoint2 = Field(..., alias='navigationEndpoint')
    video_count_short_text: VideoCountShortText = Field(..., alias='videoCountShortText')
    tracking_params: str = Field(..., alias='trackingParams')
    sidebar_thumbnails: list[SidebarThumbnail] | None = Field(None, alias='sidebarThumbnails')
    thumbnail_text: ThumbnailText = Field(..., alias='thumbnailText')
    thumbnail_renderer: ThumbnailRenderer = Field(..., alias='thumbnailRenderer')
    long_byline_text: LongBylineText = Field(..., alias='longBylineText')
    thumbnail_overlays: list[ThumbnailOverlay] = Field(..., alias='thumbnailOverlays')
    view_playlist_text: ViewPlaylistText = Field(..., alias='viewPlaylistText')

class WebCommandMetadata5(BaseModel):
    model_config = ConfigDict(defer_build=True)
    send_post: bool = Field(..., alias='sendPost')
    api_url: str = Field(..., alias='apiUrl')

class CommandMetadata5(BaseModel):
    model_config = ConfigDict(defer_build=True)
    web_command_metadata: WebCommandMetadata5 = Field(..., alias='webCommandMetadata')

class ContinuationCommand(BaseModel):
    model_config = ConfigDict(defer_build=True)
    token: str
    request: str

class ContinuationEndpoint(BaseModel):
    model_config = ConfigDict(defer_build=True)
    click_tracking_params: str = Field(..., alias='clickTrackingParams')
    command_metadata: CommandMetadata5 = Field(..., alias='commandMetadata')
    continuation_command: ContinuationCommand = Field(..., alias='continuationCommand')

class ContinuationItemRenderer(BaseModel):
    model_config = ConfigDict(defer_build=True)
    trigger: str
    continuation_endpoint: ContinuationEndpoint = Field(..., alias='continuationEndpoint')

class Item(BaseModel):
    model_config = ConfigDict(defer_build=True)
    grid_playlist_renderer: GridPlaylistRenderer | None = Field(None, alias='gridPlaylistRenderer')
    continuation_item_renderer: ContinuationItemRenderer | None = Field(None, alias='continuationItemRenderer')

class GridRenderer(BaseModel):
    model_config = ConfigDict(defer_build=True)
    items: list[Item]
    is_collapsible: bool = Field(..., alias='isCollapsible')
    tracking_params: str = Field(..., alias='trackingParams')
    target_id: UUID = Field(..., alias='targetId')

class ContinuationItem(BaseModel):
    model_config = ConfigDict(defer_build=True)
    grid_renderer: GridRenderer = Field(..., alias='gridRenderer')

class AppendContinuationItemsAction(BaseModel):
    model_config = ConfigDict(defer_build=True)
    continuation_items: list[ContinuationItem] = Field(..., alias='continuationItems')
    target_id: UUID = Field(..., alias='targetId')

class OnResponseReceivedEndpoint(BaseModel):
    model_config = ConfigDict(defer_build=True)
    click_tracking_params: str = Field(..., alias='clickTrackingParams')
    append_continuation_items_action: AppendContinuationItemsAction = Field(..., alias='appendContinuationItemsAction')

class WebCommandMetadata6(BaseModel):
    model_config = ConfigDict(defer_build=True)
    url: str
    web_page_type: str = Field(..., alias='webPageType')
    root_ve: int = Field(..., alias='rootVe')
    api_url: str = Field(..., alias='apiUrl')

class CommandMetadata6(BaseModel):
    model_config = ConfigDict(defer_build=True)
    web_command_metadata: WebCommandMetadata6 = Field(..., alias='webCommandMetadata')

class BrowseEndpoint3(BaseModel):
    model_config = ConfigDict(defer_build=True)
    browse_id: str = Field(..., alias='browseId')
    params: str
    canonical_base_url: str = Field(..., alias='canonicalBaseUrl')

class Endpoint(BaseModel):
    model_config = ConfigDict(defer_build=True)
    click_tracking_params: str = Field(..., alias='clickTrackingParams')
    command_metadata: CommandMetadata6 = Field(..., alias='commandMetadata')
    browse_endpoint: BrowseEndpoint3 = Field(..., alias='browseEndpoint')

class Title2(BaseModel):
    model_config = ConfigDict(defer_build=True)
    simple_text: str = Field(..., alias='simpleText')

class Accessibility(BaseModel):
    model_config = ConfigDict(defer_build=True)
    label: str

class AccessibilityData1(BaseModel):
    model_config = ConfigDict(defer_build=True)
    label: str

class AccessibilityData(BaseModel):
    model_config = ConfigDict(defer_build=True)
    accessibility_data: AccessibilityData1 = Field(..., alias='accessibilityData')

class ChangeEngagementPanelVisibilityAction(BaseModel):
    model_config = ConfigDict(defer_build=True)
    target_id: UUID = Field(..., alias='targetId')
    visibility: str

class Command(BaseModel):
    model_config = ConfigDict(defer_build=True)
    click_tracking_params: str = Field(..., alias='clickTrackingParams')
    change_engagement_panel_visibility_action: ChangeEngagementPanelVisibilityAction = Field(..., alias='changeEngagementPanelVisibilityAction')

class ButtonRenderer(BaseModel):
    model_config = ConfigDict(defer_build=True)
    style: str
    size: str
    is_disabled: bool = Field(..., alias='isDisabled')
    icon: Icon
    accessibility: Accessibility
    tracking_params: str = Field(..., alias='trackingParams')
    accessibility_data: AccessibilityData = Field(..., alias='accessibilityData')
    command: Command

class VisibilityButton(BaseModel):
    model_config = ConfigDict(defer_build=True)
    button_renderer: ButtonRenderer = Field(..., alias='buttonRenderer')

class EngagementPanelTitleHeaderRenderer(BaseModel):
    model_config = ConfigDict(defer_build=True)
    title: Title2
    visibility_button: VisibilityButton = Field(..., alias='visibilityButton')
    tracking_params: str = Field(..., alias='trackingParams')

class Header(BaseModel):
    model_config = ConfigDict(defer_build=True)
    engagement_panel_title_header_renderer: EngagementPanelTitleHeaderRenderer = Field(..., alias='engagementPanelTitleHeaderRenderer')

class WebCommandMetadata7(BaseModel):
    model_config = ConfigDict(defer_build=True)
    send_post: bool = Field(..., alias='sendPost')
    api_url: str = Field(..., alias='apiUrl')

class CommandMetadata7(BaseModel):
    model_config = ConfigDict(defer_build=True)
    web_command_metadata: WebCommandMetadata7 = Field(..., alias='webCommandMetadata')

class ContinuationEndpoint1(BaseModel):
    model_config = ConfigDict(defer_build=True)
    click_tracking_params: str = Field(..., alias='clickTrackingParams')
    command_metadata: CommandMetadata7 = Field(..., alias='commandMetadata')
    continuation_command: ContinuationCommand = Field(..., alias='continuationCommand')

class ContinuationItemRenderer1(BaseModel):
    model_config = ConfigDict(defer_build=True)
    trigger: str
    continuation_endpoint: ContinuationEndpoint1 = Field(..., alias='continuationEndpoint')

class Content5(BaseModel):
    model_config = ConfigDict(defer_build=True)
    continuation_item_renderer: ContinuationItemRenderer1 = Field(..., alias='continuationItemRenderer')

class ItemSectionRenderer1(BaseModel):
    model_config = ConfigDict(defer_build=True)
    contents: list[Content5]
    tracking_params: str = Field(..., alias='trackingParams')
    section_identifier: UUID = Field(..., alias='sectionIdentifier')
    target_id: UUID = Field(..., alias='targetId')

class Content4(BaseModel):
    model_config = ConfigDict(defer_build=True)
    item_section_renderer: ItemSectionRenderer1 = Field(..., alias='itemSectionRenderer')

class ScrollPaneStyle(BaseModel):
    model_config = ConfigDict(defer_build=True)
    scrollable: bool

class SectionListRenderer1(BaseModel):
    model_config = ConfigDict(defer_build=True)
    contents: list[Content4]
    tracking_params: str = Field(..., alias='trackingParams')
    scroll_pane_style: ScrollPaneStyle = Field(..., alias='scrollPaneStyle')

class Content3(BaseModel):
    model_config = ConfigDict(defer_build=True)
    section_list_renderer: SectionListRenderer1 = Field(..., alias='sectionListRenderer')

class Identifier(BaseModel):
    model_config = ConfigDict(defer_build=True)
    surface: str
    tag: UUID

class EngagementPanelSectionListRenderer(BaseModel):
    model_config = ConfigDict(defer_build=True)
    header: Header
    content: Content3
    target_id: UUID = Field(..., alias='targetId')
    identifier: Identifier
    size: str

class EngagementPanel(BaseModel):
    model_config = ConfigDict(defer_build=True)
    engagement_panel_section_list_renderer: EngagementPanelSectionListRenderer = Field(..., alias='engagementPanelSectionListRenderer')

class EngagementPanelPopupPresentationConfig(BaseModel):
    model_config = ConfigDict(defer_build=True)
    popup_type: str = Field(..., alias='popupType')

class EngagementPanelPresentationConfigs(BaseModel):
    model_config = ConfigDict(defer_build=True)
    engagement_panel_popup_presentation_config: EngagementPanelPopupPresentationConfig = Field(..., alias='engagementPanelPopupPresentationConfig')

class ShowEngagementPanelEndpoint(BaseModel):
    model_config = ConfigDict(defer_build=True)
    engagement_panel: EngagementPanel = Field(..., alias='engagementPanel')
    identifier: Identifier
    engagement_panel_presentation_configs: EngagementPanelPresentationConfigs = Field(..., alias='engagementPanelPresentationConfigs')

class NavigationEndpoint5(BaseModel):
    model_config = ConfigDict(defer_build=True)
    click_tracking_params: str = Field(..., alias='clickTrackingParams')
    show_engagement_panel_endpoint: ShowEngagementPanelEndpoint = Field(..., alias='showEngagementPanelEndpoint')

class Run8(BaseModel):
    model_config = ConfigDict(defer_build=True)
    text: str
    navigation_endpoint: NavigationEndpoint5 = Field(..., alias='navigationEndpoint')

class Title1(BaseModel):
    model_config = ConfigDict(defer_build=True)
    runs: list[Run8]

class Title3(BaseModel):
    model_config = ConfigDict(defer_build=True)
    simple_text: str = Field(..., alias='simpleText')

class AccessibilityData3(BaseModel):
    model_config = ConfigDict(defer_build=True)
    label: str

class AccessibilityData2(BaseModel):
    model_config = ConfigDict(defer_build=True)
    accessibility_data: AccessibilityData3 = Field(..., alias='accessibilityData')

class Command1(BaseModel):
    model_config = ConfigDict(defer_build=True)
    click_tracking_params: str = Field(..., alias='clickTrackingParams')
    change_engagement_panel_visibility_action: ChangeEngagementPanelVisibilityAction = Field(..., alias='changeEngagementPanelVisibilityAction')

class ButtonRenderer1(BaseModel):
    model_config = ConfigDict(defer_build=True)
    style: str
    size: str
    is_disabled: bool = Field(..., alias='isDisabled')
    icon: Icon
    accessibility: Accessibility
    tracking_params: str = Field(..., alias='trackingParams')
    accessibility_data: AccessibilityData2 = Field(..., alias='accessibilityData')
    command: Command1

class VisibilityButton1(BaseModel):
    model_config = ConfigDict(defer_build=True)
    button_renderer: ButtonRenderer1 = Field(..., alias='buttonRenderer')

class EngagementPanelTitleHeaderRenderer1(BaseModel):
    model_config = ConfigDict(defer_build=True)
    title: Title3
    visibility_button: VisibilityButton1 = Field(..., alias='visibilityButton')
    tracking_params: str = Field(..., alias='trackingParams')

class Header1(BaseModel):
    model_config = ConfigDict(defer_build=True)
    engagement_panel_title_header_renderer: EngagementPanelTitleHeaderRenderer1 = Field(..., alias='engagementPanelTitleHeaderRenderer')

class CommandMetadata8(BaseModel):
    model_config = ConfigDict(defer_build=True)
    web_command_metadata: WebCommandMetadata7 = Field(..., alias='webCommandMetadata')

class ContinuationEndpoint2(BaseModel):
    model_config = ConfigDict(defer_build=True)
    click_tracking_params: str = Field(..., alias='clickTrackingParams')
    command_metadata: CommandMetadata8 = Field(..., alias='commandMetadata')
    continuation_command: ContinuationCommand = Field(..., alias='continuationCommand')

class ContinuationItemRenderer2(BaseModel):
    model_config = ConfigDict(defer_build=True)
    trigger: str
    continuation_endpoint: ContinuationEndpoint2 = Field(..., alias='continuationEndpoint')

class Content8(BaseModel):
    model_config = ConfigDict(defer_build=True)
    continuation_item_renderer: ContinuationItemRenderer2 = Field(..., alias='continuationItemRenderer')

class ItemSectionRenderer2(BaseModel):
    model_config = ConfigDict(defer_build=True)
    contents: list[Content8]
    tracking_params: str = Field(..., alias='trackingParams')
    section_identifier: UUID = Field(..., alias='sectionIdentifier')
    target_id: UUID = Field(..., alias='targetId')

class Content7(BaseModel):
    model_config = ConfigDict(defer_build=True)
    item_section_renderer: ItemSectionRenderer2 = Field(..., alias='itemSectionRenderer')

class SectionListRenderer2(BaseModel):
    model_config = ConfigDict(defer_build=True)
    contents: list[Content7]
    tracking_params: str = Field(..., alias='trackingParams')
    scroll_pane_style: ScrollPaneStyle = Field(..., alias='scrollPaneStyle')

class Content6(BaseModel):
    model_config = ConfigDict(defer_build=True)
    section_list_renderer: SectionListRenderer2 = Field(..., alias='sectionListRenderer')

class EngagementPanelSectionListRenderer1(BaseModel):
    model_config = ConfigDict(defer_build=True)
    header: Header1
    content: Content6
    target_id: UUID = Field(..., alias='targetId')
    identifier: Identifier
    size: str

class EngagementPanel1(BaseModel):
    model_config = ConfigDict(defer_build=True)
    engagement_panel_section_list_renderer: EngagementPanelSectionListRenderer1 = Field(..., alias='engagementPanelSectionListRenderer')

class EngagementPanelPresentationConfigs1(BaseModel):
    model_config = ConfigDict(defer_build=True)
    engagement_panel_popup_presentation_config: EngagementPanelPopupPresentationConfig = Field(..., alias='engagementPanelPopupPresentationConfig')

class ShowEngagementPanelEndpoint1(BaseModel):
    model_config = ConfigDict(defer_build=True)
    engagement_panel: EngagementPanel1 = Field(..., alias='engagementPanel')
    identifier: Identifier
    engagement_panel_presentation_configs: EngagementPanelPresentationConfigs1 = Field(..., alias='engagementPanelPresentationConfigs')

class Endpoint1(BaseModel):
    model_config = ConfigDict(defer_build=True)
    click_tracking_params: str = Field(..., alias='clickTrackingParams')
    show_engagement_panel_endpoint: ShowEngagementPanelEndpoint1 = Field(..., alias='showEngagementPanelEndpoint')

class Source(BaseModel):
    model_config = ConfigDict(defer_build=True)
    url: str
    width: int
    height: int

class Image(BaseModel):
    model_config = ConfigDict(defer_build=True)
    sources: list[Source]

class ClientResource(BaseModel):
    model_config = ConfigDict(defer_build=True)
    image_name: str = Field(..., alias='imageName')

class Source1(BaseModel):
    model_config = ConfigDict(defer_build=True)
    client_resource: ClientResource = Field(..., alias='clientResource')

class Icon4(BaseModel):
    model_config = ConfigDict(defer_build=True)
    sources: list[Source1]

class BackgroundColor(BaseModel):
    model_config = ConfigDict(defer_build=True)
    light_theme: int = Field(..., alias='lightTheme')
    dark_theme: int = Field(..., alias='darkTheme')

class ThumbnailBadgeViewModel(BaseModel):
    model_config = ConfigDict(defer_build=True)
    icon: Icon4
    text: str
    badge_style: str = Field(..., alias='badgeStyle')
    background_color: BackgroundColor = Field(..., alias='backgroundColor')

class ThumbnailBadge(BaseModel):
    model_config = ConfigDict(defer_build=True)
    thumbnail_badge_view_model: ThumbnailBadgeViewModel = Field(..., alias='thumbnailBadgeViewModel')

class ThumbnailOverlayBadgeViewModel(BaseModel):
    model_config = ConfigDict(defer_build=True)
    thumbnail_badges: list[ThumbnailBadge] = Field(..., alias='thumbnailBadges')
    position: str

class Source2(BaseModel):
    model_config = ConfigDict(defer_build=True)
    client_resource: ClientResource = Field(..., alias='clientResource')

class Icon5(BaseModel):
    model_config = ConfigDict(defer_build=True)
    sources: list[Source2]

class StyleRun(BaseModel):
    model_config = ConfigDict(defer_build=True)
    start_index: int = Field(..., alias='startIndex')
    length: int

class Text3(BaseModel):
    model_config = ConfigDict(defer_build=True)
    content: str
    style_runs: list[StyleRun] = Field(..., alias='styleRuns')

class ThumbnailHoverOverlayViewModel(BaseModel):
    model_config = ConfigDict(defer_build=True)
    icon: Icon5
    text: Text3
    style: str

class Overlay(BaseModel):
    model_config = ConfigDict(defer_build=True)
    thumbnail_overlay_badge_view_model: ThumbnailOverlayBadgeViewModel | None = Field(None, alias='thumbnailOverlayBadgeViewModel')
    thumbnail_hover_overlay_view_model: ThumbnailHoverOverlayViewModel | None = Field(None, alias='thumbnailHoverOverlayViewModel')

class ThumbnailViewModel(BaseModel):
    model_config = ConfigDict(defer_build=True)
    image: Image
    overlays: list[Overlay]
    background_color: BackgroundColor = Field(..., alias='backgroundColor')

class PrimaryThumbnail(BaseModel):
    model_config = ConfigDict(defer_build=True)
    thumbnail_view_model: ThumbnailViewModel = Field(..., alias='thumbnailViewModel')

class StackColor(BaseModel):
    model_config = ConfigDict(defer_build=True)
    light_theme: int = Field(..., alias='lightTheme')
    dark_theme: int = Field(..., alias='darkTheme')

class CollectionThumbnailViewModel(BaseModel):
    model_config = ConfigDict(defer_build=True)
    primary_thumbnail: PrimaryThumbnail = Field(..., alias='primaryThumbnail')
    stack_color: StackColor = Field(..., alias='stackColor')

class ContentImage(BaseModel):
    model_config = ConfigDict(defer_build=True)
    collection_thumbnail_view_model: CollectionThumbnailViewModel = Field(..., alias='collectionThumbnailViewModel')

class Title4(BaseModel):
    model_config = ConfigDict(defer_build=True)
    content: str

class WebCommandMetadata9(BaseModel):
    model_config = ConfigDict(defer_build=True)
    url: str
    web_page_type: str = Field(..., alias='webPageType')
    root_ve: int = Field(..., alias='rootVe')
    api_url: str = Field(..., alias='apiUrl')

class CommandMetadata9(BaseModel):
    model_config = ConfigDict(defer_build=True)
    web_command_metadata: WebCommandMetadata9 = Field(..., alias='webCommandMetadata')

class BrowseEndpoint4(BaseModel):
    model_config = ConfigDict(defer_build=True)
    browse_id: str = Field(..., alias='browseId')
    canonical_base_url: str | None = Field(None, alias='canonicalBaseUrl')

class InnertubeCommand(BaseModel):
    model_config = ConfigDict(defer_build=True)
    click_tracking_params: str = Field(..., alias='clickTrackingParams')
    command_metadata: CommandMetadata9 = Field(..., alias='commandMetadata')
    browse_endpoint: BrowseEndpoint4 = Field(..., alias='browseEndpoint')

class OnTap(BaseModel):
    model_config = ConfigDict(defer_build=True)
    innertube_command: InnertubeCommand = Field(..., alias='innertubeCommand')

class CommandRun(BaseModel):
    model_config = ConfigDict(defer_build=True)
    start_index: int = Field(..., alias='startIndex')
    length: int
    on_tap: OnTap = Field(..., alias='onTap')

class StyleRun1(BaseModel):
    model_config = ConfigDict(defer_build=True)
    start_index: int = Field(..., alias='startIndex')
    length: int
    weight_label: str = Field(..., alias='weightLabel')

class Text4(BaseModel):
    model_config = ConfigDict(defer_build=True)
    content: str
    command_runs: list[CommandRun] | None = Field(None, alias='commandRuns')
    style_runs: list[StyleRun1] | None = Field(None, alias='styleRuns')

class MetadataPart(BaseModel):
    model_config = ConfigDict(defer_build=True)
    text: Text4

class MetadataRow(BaseModel):
    model_config = ConfigDict(defer_build=True)
    metadata_parts: list[MetadataPart] = Field(..., alias='metadataParts')

class ContentMetadataViewModel(BaseModel):
    model_config = ConfigDict(defer_build=True)
    metadata_rows: list[MetadataRow] = Field(..., alias='metadataRows')
    delimiter: str

class Metadata1(BaseModel):
    model_config = ConfigDict(defer_build=True)
    content_metadata_view_model: ContentMetadataViewModel = Field(..., alias='contentMetadataViewModel')

class LockupMetadataViewModel(BaseModel):
    model_config = ConfigDict(defer_build=True)
    title: Title4
    metadata: Metadata1

class Metadata(BaseModel):
    model_config = ConfigDict(defer_build=True)
    lockup_metadata_view_model: LockupMetadataViewModel = Field(..., alias='lockupMetadataViewModel')

class WebCommandMetadata10(BaseModel):
    model_config = ConfigDict(defer_build=True)
    url: str
    web_page_type: str = Field(..., alias='webPageType')
    root_ve: int = Field(..., alias='rootVe')

class CommandMetadata10(BaseModel):
    model_config = ConfigDict(defer_build=True)
    web_command_metadata: WebCommandMetadata10 = Field(..., alias='webCommandMetadata')

class LoggingContext2(BaseModel):
    model_config = ConfigDict(defer_build=True)
    vss_logging_context: VssLoggingContext = Field(..., alias='vssLoggingContext')

class Html5PlaybackOnesieConfig2(BaseModel):
    model_config = ConfigDict(defer_build=True)
    common_config: CommonConfig = Field(..., alias='commonConfig')

class WatchEndpointSupportedOnesieConfig2(BaseModel):
    model_config = ConfigDict(defer_build=True)
    html5_playback_onesie_config: Html5PlaybackOnesieConfig2 = Field(..., alias='html5PlaybackOnesieConfig')

class WatchEndpoint2(BaseModel):
    model_config = ConfigDict(defer_build=True)
    video_id: str = Field(..., alias='videoId')
    playlist_id: str = Field(..., alias='playlistId')
    params: str
    logging_context: LoggingContext2 = Field(..., alias='loggingContext')
    watch_endpoint_supported_onesie_config: WatchEndpointSupportedOnesieConfig2 = Field(..., alias='watchEndpointSupportedOnesieConfig')
    player_params: str | None = Field(None, alias='playerParams')

class InnertubeCommand1(BaseModel):
    model_config = ConfigDict(defer_build=True)
    click_tracking_params: str = Field(..., alias='clickTrackingParams')
    command_metadata: CommandMetadata10 = Field(..., alias='commandMetadata')
    watch_endpoint: WatchEndpoint2 = Field(..., alias='watchEndpoint')

class OnSelect(BaseModel):
    model_config = ConfigDict(defer_build=True)
    innertube_command: InnertubeCommand1 = Field(..., alias='innertubeCommand')

class CommandMetadata11(BaseModel):
    model_config = ConfigDict(defer_build=True)
    web_command_metadata: WebCommandMetadata10 = Field(..., alias='webCommandMetadata')

class LoggingContext3(BaseModel):
    model_config = ConfigDict(defer_build=True)
    vss_logging_context: VssLoggingContext = Field(..., alias='vssLoggingContext')

class Html5PlaybackOnesieConfig3(BaseModel):
    model_config = ConfigDict(defer_build=True)
    common_config: CommonConfig = Field(..., alias='commonConfig')

class WatchEndpointSupportedOnesieConfig3(BaseModel):
    model_config = ConfigDict(defer_build=True)
    html5_playback_onesie_config: Html5PlaybackOnesieConfig3 = Field(..., alias='html5PlaybackOnesieConfig')

class WatchEndpoint3(BaseModel):
    model_config = ConfigDict(defer_build=True)
    video_id: str = Field(..., alias='videoId')
    playlist_id: str = Field(..., alias='playlistId')
    player_params: str = Field(..., alias='playerParams')
    logging_context: LoggingContext3 = Field(..., alias='loggingContext')
    watch_endpoint_supported_onesie_config: WatchEndpointSupportedOnesieConfig3 = Field(..., alias='watchEndpointSupportedOnesieConfig')

class InnertubeCommand2(BaseModel):
    model_config = ConfigDict(defer_build=True)
    click_tracking_params: str = Field(..., alias='clickTrackingParams')
    command_metadata: CommandMetadata11 = Field(..., alias='commandMetadata')
    watch_endpoint: WatchEndpoint3 = Field(..., alias='watchEndpoint')

class OnVisible(BaseModel):
    model_config = ConfigDict(defer_build=True)
    innertube_command: InnertubeCommand2 = Field(..., alias='innertubeCommand')

class InlinePlayerData(BaseModel):
    model_config = ConfigDict(defer_build=True)
    on_select: OnSelect = Field(..., alias='onSelect')
    on_visible: OnVisible = Field(..., alias='onVisible')

class ItemPlayback(BaseModel):
    model_config = ConfigDict(defer_build=True)
    inline_player_data: InlinePlayerData = Field(..., alias='inlinePlayerData')

class Visibility(BaseModel):
    model_config = ConfigDict(defer_build=True)
    types: str

class LoggingDirectives(BaseModel):
    model_config = ConfigDict(defer_build=True)
    tracking_params: str = Field(..., alias='trackingParams')
    visibility: Visibility

class LoggingContext4(BaseModel):
    model_config = ConfigDict(defer_build=True)
    logging_directives: LoggingDirectives = Field(..., alias='loggingDirectives')

class CommandMetadata12(BaseModel):
    model_config = ConfigDict(defer_build=True)
    web_command_metadata: WebCommandMetadata10 = Field(..., alias='webCommandMetadata')

class LoggingContext5(BaseModel):
    model_config = ConfigDict(defer_build=True)
    vss_logging_context: VssLoggingContext = Field(..., alias='vssLoggingContext')

class Html5PlaybackOnesieConfig4(BaseModel):
    model_config = ConfigDict(defer_build=True)
    common_config: CommonConfig = Field(..., alias='commonConfig')

class WatchEndpointSupportedOnesieConfig4(BaseModel):
    model_config = ConfigDict(defer_build=True)
    html5_playback_onesie_config: Html5PlaybackOnesieConfig4 = Field(..., alias='html5PlaybackOnesieConfig')

class WatchEndpoint4(BaseModel):
    model_config = ConfigDict(defer_build=True)
    video_id: str = Field(..., alias='videoId')
    playlist_id: str = Field(..., alias='playlistId')
    params: str
    logging_context: LoggingContext5 = Field(..., alias='loggingContext')
    watch_endpoint_supported_onesie_config: WatchEndpointSupportedOnesieConfig4 = Field(..., alias='watchEndpointSupportedOnesieConfig')
    player_params: str | None = Field(None, alias='playerParams')

class InnertubeCommand3(BaseModel):
    model_config = ConfigDict(defer_build=True)
    click_tracking_params: str = Field(..., alias='clickTrackingParams')
    command_metadata: CommandMetadata12 = Field(..., alias='commandMetadata')
    watch_endpoint: WatchEndpoint4 = Field(..., alias='watchEndpoint')

class OnTap1(BaseModel):
    model_config = ConfigDict(defer_build=True)
    innertube_command: InnertubeCommand3 = Field(..., alias='innertubeCommand')

class CommandContext(BaseModel):
    model_config = ConfigDict(defer_build=True)
    on_tap: OnTap1 = Field(..., alias='onTap')

class RendererContext(BaseModel):
    model_config = ConfigDict(defer_build=True)
    logging_context: LoggingContext4 = Field(..., alias='loggingContext')
    command_context: CommandContext = Field(..., alias='commandContext')

class LockupViewModel(BaseModel):
    model_config = ConfigDict(defer_build=True)
    content_image: ContentImage = Field(..., alias='contentImage')
    metadata: Metadata
    content_id: str = Field(..., alias='contentId')
    content_type: str = Field(..., alias='contentType')
    item_playback: ItemPlayback = Field(..., alias='itemPlayback')
    renderer_context: RendererContext = Field(..., alias='rendererContext')

class Item1(BaseModel):
    model_config = ConfigDict(defer_build=True)
    lockup_view_model: LockupViewModel = Field(..., alias='lockupViewModel')

class Icon6(BaseModel):
    model_config = ConfigDict(defer_build=True)
    icon_type: str = Field(..., alias='iconType')

class ButtonRenderer2(BaseModel):
    model_config = ConfigDict(defer_build=True)
    style: str
    size: str
    is_disabled: bool = Field(..., alias='isDisabled')
    icon: Icon6
    accessibility: Accessibility
    tracking_params: str = Field(..., alias='trackingParams')

class NextButton(BaseModel):
    model_config = ConfigDict(defer_build=True)
    button_renderer: ButtonRenderer2 = Field(..., alias='buttonRenderer')

class ButtonRenderer3(BaseModel):
    model_config = ConfigDict(defer_build=True)
    style: str
    size: str
    is_disabled: bool = Field(..., alias='isDisabled')
    icon: Icon6
    accessibility: Accessibility
    tracking_params: str = Field(..., alias='trackingParams')

class PreviousButton(BaseModel):
    model_config = ConfigDict(defer_build=True)
    button_renderer: ButtonRenderer3 = Field(..., alias='buttonRenderer')

class HorizontalListRenderer(BaseModel):
    model_config = ConfigDict(defer_build=True)
    items: list[Item1]
    tracking_params: str = Field(..., alias='trackingParams')
    visible_item_count: int = Field(..., alias='visibleItemCount')
    next_button: NextButton = Field(..., alias='nextButton')
    previous_button: PreviousButton = Field(..., alias='previousButton')
    force16_by9_thumbnail_aspect_ratio: bool = Field(..., alias='force16By9ThumbnailAspectRatio')

class Content9(BaseModel):
    model_config = ConfigDict(defer_build=True)
    horizontal_list_renderer: HorizontalListRenderer = Field(..., alias='horizontalListRenderer')

class Text5(BaseModel):
    model_config = ConfigDict(defer_build=True)
    simple_text: str = Field(..., alias='simpleText')

class Title5(BaseModel):
    model_config = ConfigDict(defer_build=True)
    simple_text: str = Field(..., alias='simpleText')

class AccessibilityData5(BaseModel):
    model_config = ConfigDict(defer_build=True)
    label: str

class AccessibilityData4(BaseModel):
    model_config = ConfigDict(defer_build=True)
    accessibility_data: AccessibilityData5 = Field(..., alias='accessibilityData')

class Command2(BaseModel):
    model_config = ConfigDict(defer_build=True)
    click_tracking_params: str = Field(..., alias='clickTrackingParams')
    change_engagement_panel_visibility_action: ChangeEngagementPanelVisibilityAction = Field(..., alias='changeEngagementPanelVisibilityAction')

class ButtonRenderer5(BaseModel):
    model_config = ConfigDict(defer_build=True)
    style: str
    size: str
    is_disabled: bool = Field(..., alias='isDisabled')
    icon: Icon6
    accessibility: Accessibility
    tracking_params: str = Field(..., alias='trackingParams')
    accessibility_data: AccessibilityData4 = Field(..., alias='accessibilityData')
    command: Command2

class VisibilityButton2(BaseModel):
    model_config = ConfigDict(defer_build=True)
    button_renderer: ButtonRenderer5 = Field(..., alias='buttonRenderer')

class EngagementPanelTitleHeaderRenderer2(BaseModel):
    model_config = ConfigDict(defer_build=True)
    title: Title5
    visibility_button: VisibilityButton2 = Field(..., alias='visibilityButton')
    tracking_params: str = Field(..., alias='trackingParams')

class Header2(BaseModel):
    model_config = ConfigDict(defer_build=True)
    engagement_panel_title_header_renderer: EngagementPanelTitleHeaderRenderer2 = Field(..., alias='engagementPanelTitleHeaderRenderer')

class WebCommandMetadata13(BaseModel):
    model_config = ConfigDict(defer_build=True)
    send_post: bool = Field(..., alias='sendPost')
    api_url: str = Field(..., alias='apiUrl')

class CommandMetadata13(BaseModel):
    model_config = ConfigDict(defer_build=True)
    web_command_metadata: WebCommandMetadata13 = Field(..., alias='webCommandMetadata')

class ContinuationEndpoint3(BaseModel):
    model_config = ConfigDict(defer_build=True)
    click_tracking_params: str = Field(..., alias='clickTrackingParams')
    command_metadata: CommandMetadata13 = Field(..., alias='commandMetadata')
    continuation_command: ContinuationCommand = Field(..., alias='continuationCommand')

class ContinuationItemRenderer3(BaseModel):
    model_config = ConfigDict(defer_build=True)
    trigger: str
    continuation_endpoint: ContinuationEndpoint3 = Field(..., alias='continuationEndpoint')

class Content12(BaseModel):
    model_config = ConfigDict(defer_build=True)
    continuation_item_renderer: ContinuationItemRenderer3 = Field(..., alias='continuationItemRenderer')

class ItemSectionRenderer3(BaseModel):
    model_config = ConfigDict(defer_build=True)
    contents: list[Content12]
    tracking_params: str = Field(..., alias='trackingParams')
    section_identifier: UUID = Field(..., alias='sectionIdentifier')
    target_id: UUID = Field(..., alias='targetId')

class Content11(BaseModel):
    model_config = ConfigDict(defer_build=True)
    item_section_renderer: ItemSectionRenderer3 = Field(..., alias='itemSectionRenderer')

class SectionListRenderer3(BaseModel):
    model_config = ConfigDict(defer_build=True)
    contents: list[Content11]
    tracking_params: str = Field(..., alias='trackingParams')
    scroll_pane_style: ScrollPaneStyle = Field(..., alias='scrollPaneStyle')

class Content10(BaseModel):
    model_config = ConfigDict(defer_build=True)
    section_list_renderer: SectionListRenderer3 = Field(..., alias='sectionListRenderer')

class EngagementPanelSectionListRenderer2(BaseModel):
    model_config = ConfigDict(defer_build=True)
    header: Header2
    content: Content10
    target_id: UUID = Field(..., alias='targetId')
    identifier: Identifier
    size: str

class EngagementPanel2(BaseModel):
    model_config = ConfigDict(defer_build=True)
    engagement_panel_section_list_renderer: EngagementPanelSectionListRenderer2 = Field(..., alias='engagementPanelSectionListRenderer')

class EngagementPanelPresentationConfigs2(BaseModel):
    model_config = ConfigDict(defer_build=True)
    engagement_panel_popup_presentation_config: EngagementPanelPopupPresentationConfig = Field(..., alias='engagementPanelPopupPresentationConfig')

class ShowEngagementPanelEndpoint2(BaseModel):
    model_config = ConfigDict(defer_build=True)
    engagement_panel: EngagementPanel2 = Field(..., alias='engagementPanel')
    identifier: Identifier
    engagement_panel_presentation_configs: EngagementPanelPresentationConfigs2 = Field(..., alias='engagementPanelPresentationConfigs')

class NavigationEndpoint6(BaseModel):
    model_config = ConfigDict(defer_build=True)
    click_tracking_params: str = Field(..., alias='clickTrackingParams')
    show_engagement_panel_endpoint: ShowEngagementPanelEndpoint2 = Field(..., alias='showEngagementPanelEndpoint')

class AccessibilityData7(BaseModel):
    model_config = ConfigDict(defer_build=True)
    label: str

class AccessibilityData6(BaseModel):
    model_config = ConfigDict(defer_build=True)
    accessibility_data: AccessibilityData7 = Field(..., alias='accessibilityData')

class ButtonRenderer4(BaseModel):
    model_config = ConfigDict(defer_build=True)
    style: str
    size: str
    is_disabled: bool = Field(..., alias='isDisabled')
    text: Text5
    navigation_endpoint: NavigationEndpoint6 = Field(..., alias='navigationEndpoint')
    tracking_params: str = Field(..., alias='trackingParams')
    accessibility_data: AccessibilityData6 = Field(..., alias='accessibilityData')

class TopLevelButton(BaseModel):
    model_config = ConfigDict(defer_build=True)
    button_renderer: ButtonRenderer4 = Field(..., alias='buttonRenderer')

class MenuRenderer(BaseModel):
    model_config = ConfigDict(defer_build=True)
    tracking_params: str = Field(..., alias='trackingParams')
    top_level_buttons: list[TopLevelButton] = Field(..., alias='topLevelButtons')

class Menu(BaseModel):
    model_config = ConfigDict(defer_build=True)
    menu_renderer: MenuRenderer = Field(..., alias='menuRenderer')

class ShelfRenderer(BaseModel):
    model_config = ConfigDict(defer_build=True)
    title: Title1
    endpoint: Endpoint1
    content: Content9
    tracking_params: str = Field(..., alias='trackingParams')
    menu: Menu

class Content2(BaseModel):
    model_config = ConfigDict(defer_build=True)
    shelf_renderer: ShelfRenderer = Field(..., alias='shelfRenderer')

class ItemSectionRenderer(BaseModel):
    model_config = ConfigDict(defer_build=True)
    contents: list[Content2]
    tracking_params: str = Field(..., alias='trackingParams')

class Content1(BaseModel):
    model_config = ConfigDict(defer_build=True)
    item_section_renderer: ItemSectionRenderer = Field(..., alias='itemSectionRenderer')

class SectionListRenderer(BaseModel):
    model_config = ConfigDict(defer_build=True)
    contents: list[Content1]
    tracking_params: str = Field(..., alias='trackingParams')
    target_id: str = Field(..., alias='targetId')
    disable_pull_to_refresh: bool = Field(..., alias='disablePullToRefresh')

class Content(BaseModel):
    model_config = ConfigDict(defer_build=True)
    section_list_renderer: SectionListRenderer = Field(..., alias='sectionListRenderer')

class TabRenderer(BaseModel):
    model_config = ConfigDict(defer_build=True)
    endpoint: Endpoint
    title: str
    selected: bool
    content: Content
    tracking_params: str = Field(..., alias='trackingParams')

class Tab(BaseModel):
    model_config = ConfigDict(defer_build=True)
    tab_renderer: TabRenderer = Field(..., alias='tabRenderer')

class TwoColumnBrowseResultsRenderer(BaseModel):
    model_config = ConfigDict(defer_build=True)
    tabs: list[Tab]

class Contents(BaseModel):
    model_config = ConfigDict(defer_build=True)
    two_column_browse_results_renderer: TwoColumnBrowseResultsRenderer = Field(..., alias='twoColumnBrowseResultsRenderer')

class Text6(BaseModel):
    model_config = ConfigDict(defer_build=True)
    content: str

class LoggingDirectives1(BaseModel):
    model_config = ConfigDict(defer_build=True)
    tracking_params: str = Field(..., alias='trackingParams')
    visibility: Visibility

class LoggingContext6(BaseModel):
    model_config = ConfigDict(defer_build=True)
    logging_directives: LoggingDirectives1 = Field(..., alias='loggingDirectives')

class RendererContext1(BaseModel):
    model_config = ConfigDict(defer_build=True)
    logging_context: LoggingContext6 = Field(..., alias='loggingContext')

class DynamicTextViewModel(BaseModel):
    model_config = ConfigDict(defer_build=True)
    text: Text6
    max_lines: int = Field(..., alias='maxLines')
    renderer_context: RendererContext1 = Field(..., alias='rendererContext')

class Title6(BaseModel):
    model_config = ConfigDict(defer_build=True)
    dynamic_text_view_model: DynamicTextViewModel = Field(..., alias='dynamicTextViewModel')

class Source3(BaseModel):
    model_config = ConfigDict(defer_build=True)
    url: str
    width: int
    height: int

class BorderImageProcessor(BaseModel):
    model_config = ConfigDict(defer_build=True)
    circular: bool

class Processor(BaseModel):
    model_config = ConfigDict(defer_build=True)
    border_image_processor: BorderImageProcessor = Field(..., alias='borderImageProcessor')

class Image2(BaseModel):
    model_config = ConfigDict(defer_build=True)
    sources: list[Source3]
    processor: Processor

class LoggingDirectives2(BaseModel):
    model_config = ConfigDict(defer_build=True)
    tracking_params: str = Field(..., alias='trackingParams')
    visibility: Visibility

class AvatarViewModel(BaseModel):
    model_config = ConfigDict(defer_build=True)
    image: Image2
    avatar_image_size: str = Field(..., alias='avatarImageSize')
    logging_directives: LoggingDirectives2 = Field(..., alias='loggingDirectives')

class Avatar(BaseModel):
    model_config = ConfigDict(defer_build=True)
    avatar_view_model: AvatarViewModel = Field(..., alias='avatarViewModel')

class DecoratedAvatarViewModel(BaseModel):
    model_config = ConfigDict(defer_build=True)
    avatar: Avatar

class Image1(BaseModel):
    model_config = ConfigDict(defer_build=True)
    decorated_avatar_view_model: DecoratedAvatarViewModel = Field(..., alias='decoratedAvatarViewModel')

class StyleRun2(BaseModel):
    model_config = ConfigDict(defer_build=True)
    start_index: int = Field(..., alias='startIndex')
    length: int

class Text7(BaseModel):
    model_config = ConfigDict(defer_build=True)
    content: str
    style_runs: list[StyleRun2] = Field(..., alias='styleRuns')

class MetadataPart1(BaseModel):
    model_config = ConfigDict(defer_build=True)
    text: Text7

class MetadataRow1(BaseModel):
    model_config = ConfigDict(defer_build=True)
    metadata_parts: list[MetadataPart1] = Field(..., alias='metadataParts')

class LoggingDirectives3(BaseModel):
    model_config = ConfigDict(defer_build=True)
    tracking_params: str = Field(..., alias='trackingParams')
    visibility: Visibility

class LoggingContext7(BaseModel):
    model_config = ConfigDict(defer_build=True)
    logging_directives: LoggingDirectives3 = Field(..., alias='loggingDirectives')

class RendererContext2(BaseModel):
    model_config = ConfigDict(defer_build=True)
    logging_context: LoggingContext7 = Field(..., alias='loggingContext')

class ContentMetadataViewModel1(BaseModel):
    model_config = ConfigDict(defer_build=True)
    metadata_rows: list[MetadataRow1] = Field(..., alias='metadataRows')
    delimiter: str
    renderer_context: RendererContext2 = Field(..., alias='rendererContext')

class Metadata2(BaseModel):
    model_config = ConfigDict(defer_build=True)
    content_metadata_view_model: ContentMetadataViewModel1 = Field(..., alias='contentMetadataViewModel')

class Description1(BaseModel):
    model_config = ConfigDict(defer_build=True)
    content: str

class StyleRun3(BaseModel):
    model_config = ConfigDict(defer_build=True)
    start_index: int = Field(..., alias='startIndex')
    length: int
    weight: int

class TruncationText(BaseModel):
    model_config = ConfigDict(defer_build=True)
    content: str
    style_runs: list[StyleRun3] = Field(..., alias='styleRuns')

class LoggingDirectives4(BaseModel):
    model_config = ConfigDict(defer_build=True)
    tracking_params: str = Field(..., alias='trackingParams')
    visibility: Visibility

class LoggingContext8(BaseModel):
    model_config = ConfigDict(defer_build=True)
    logging_directives: LoggingDirectives4 = Field(..., alias='loggingDirectives')

class AccessibilityContext(BaseModel):
    model_config = ConfigDict(defer_build=True)
    label: str

class Title7(BaseModel):
    model_config = ConfigDict(defer_build=True)
    simple_text: str = Field(..., alias='simpleText')

class AccessibilityData9(BaseModel):
    model_config = ConfigDict(defer_build=True)
    label: str

class AccessibilityData8(BaseModel):
    model_config = ConfigDict(defer_build=True)
    accessibility_data: AccessibilityData9 = Field(..., alias='accessibilityData')

class Command3(BaseModel):
    model_config = ConfigDict(defer_build=True)
    click_tracking_params: str = Field(..., alias='clickTrackingParams')
    change_engagement_panel_visibility_action: ChangeEngagementPanelVisibilityAction = Field(..., alias='changeEngagementPanelVisibilityAction')

class ButtonRenderer6(BaseModel):
    model_config = ConfigDict(defer_build=True)
    style: str
    size: str
    is_disabled: bool = Field(..., alias='isDisabled')
    icon: Icon6
    accessibility: Accessibility
    tracking_params: str = Field(..., alias='trackingParams')
    accessibility_data: AccessibilityData8 = Field(..., alias='accessibilityData')
    command: Command3

class VisibilityButton3(BaseModel):
    model_config = ConfigDict(defer_build=True)
    button_renderer: ButtonRenderer6 = Field(..., alias='buttonRenderer')

class EngagementPanelTitleHeaderRenderer3(BaseModel):
    model_config = ConfigDict(defer_build=True)
    title: Title7
    visibility_button: VisibilityButton3 = Field(..., alias='visibilityButton')
    tracking_params: str = Field(..., alias='trackingParams')

class Header4(BaseModel):
    model_config = ConfigDict(defer_build=True)
    engagement_panel_title_header_renderer: EngagementPanelTitleHeaderRenderer3 = Field(..., alias='engagementPanelTitleHeaderRenderer')

class CommandMetadata14(BaseModel):
    model_config = ConfigDict(defer_build=True)
    web_command_metadata: WebCommandMetadata13 = Field(..., alias='webCommandMetadata')

class ContinuationEndpoint4(BaseModel):
    model_config = ConfigDict(defer_build=True)
    click_tracking_params: str = Field(..., alias='clickTrackingParams')
    command_metadata: CommandMetadata14 = Field(..., alias='commandMetadata')
    continuation_command: ContinuationCommand = Field(..., alias='continuationCommand')

class ContinuationItemRenderer4(BaseModel):
    model_config = ConfigDict(defer_build=True)
    trigger: str
    continuation_endpoint: ContinuationEndpoint4 = Field(..., alias='continuationEndpoint')

class Content16(BaseModel):
    model_config = ConfigDict(defer_build=True)
    continuation_item_renderer: ContinuationItemRenderer4 = Field(..., alias='continuationItemRenderer')

class ItemSectionRenderer4(BaseModel):
    model_config = ConfigDict(defer_build=True)
    contents: list[Content16]
    tracking_params: str = Field(..., alias='trackingParams')
    section_identifier: UUID = Field(..., alias='sectionIdentifier')
    target_id: UUID = Field(..., alias='targetId')

class Content15(BaseModel):
    model_config = ConfigDict(defer_build=True)
    item_section_renderer: ItemSectionRenderer4 = Field(..., alias='itemSectionRenderer')

class SectionListRenderer4(BaseModel):
    model_config = ConfigDict(defer_build=True)
    contents: list[Content15]
    tracking_params: str = Field(..., alias='trackingParams')
    scroll_pane_style: ScrollPaneStyle = Field(..., alias='scrollPaneStyle')

class Content14(BaseModel):
    model_config = ConfigDict(defer_build=True)
    section_list_renderer: SectionListRenderer4 = Field(..., alias='sectionListRenderer')

class EngagementPanelSectionListRenderer3(BaseModel):
    model_config = ConfigDict(defer_build=True)
    header: Header4
    content: Content14
    target_id: UUID = Field(..., alias='targetId')
    identifier: Identifier

class EngagementPanel3(BaseModel):
    model_config = ConfigDict(defer_build=True)
    engagement_panel_section_list_renderer: EngagementPanelSectionListRenderer3 = Field(..., alias='engagementPanelSectionListRenderer')

class EngagementPanelPresentationConfigs3(BaseModel):
    model_config = ConfigDict(defer_build=True)
    engagement_panel_popup_presentation_config: EngagementPanelPopupPresentationConfig = Field(..., alias='engagementPanelPopupPresentationConfig')

class ShowEngagementPanelEndpoint3(BaseModel):
    model_config = ConfigDict(defer_build=True)
    engagement_panel: EngagementPanel3 = Field(..., alias='engagementPanel')
    identifier: Identifier
    engagement_panel_presentation_configs: EngagementPanelPresentationConfigs3 = Field(..., alias='engagementPanelPresentationConfigs')

class InnertubeCommand4(BaseModel):
    model_config = ConfigDict(defer_build=True)
    click_tracking_params: str = Field(..., alias='clickTrackingParams')
    show_engagement_panel_endpoint: ShowEngagementPanelEndpoint3 = Field(..., alias='showEngagementPanelEndpoint')

class OnTap2(BaseModel):
    model_config = ConfigDict(defer_build=True)
    innertube_command: InnertubeCommand4 = Field(..., alias='innertubeCommand')

class CommandContext1(BaseModel):
    model_config = ConfigDict(defer_build=True)
    on_tap: OnTap2 = Field(..., alias='onTap')

class RendererContext3(BaseModel):
    model_config = ConfigDict(defer_build=True)
    logging_context: LoggingContext8 = Field(..., alias='loggingContext')
    accessibility_context: AccessibilityContext = Field(..., alias='accessibilityContext')
    command_context: CommandContext1 = Field(..., alias='commandContext')

class DescriptionPreviewViewModel(BaseModel):
    model_config = ConfigDict(defer_build=True)
    description: Description1
    max_lines: int = Field(..., alias='maxLines')
    truncation_text: TruncationText = Field(..., alias='truncationText')
    always_show_truncation_text: bool = Field(..., alias='alwaysShowTruncationText')
    renderer_context: RendererContext3 = Field(..., alias='rendererContext')

class Description(BaseModel):
    model_config = ConfigDict(defer_build=True)
    description_preview_view_model: DescriptionPreviewViewModel = Field(..., alias='descriptionPreviewViewModel')

class WebCommandMetadata15(BaseModel):
    model_config = ConfigDict(defer_build=True)
    url: str
    web_page_type: str = Field(..., alias='webPageType')
    root_ve: int = Field(..., alias='rootVe')

class CommandMetadata15(BaseModel):
    model_config = ConfigDict(defer_build=True)
    web_command_metadata: WebCommandMetadata15 = Field(..., alias='webCommandMetadata')

class UrlEndpoint(BaseModel):
    model_config = ConfigDict(defer_build=True)
    url: str
    target: str

class InnertubeCommand5(BaseModel):
    model_config = ConfigDict(defer_build=True)
    click_tracking_params: str = Field(..., alias='clickTrackingParams')
    command_metadata: CommandMetadata15 = Field(..., alias='commandMetadata')
    url_endpoint: UrlEndpoint = Field(..., alias='urlEndpoint')

class OnTap3(BaseModel):
    model_config = ConfigDict(defer_build=True)
    innertube_command: InnertubeCommand5 = Field(..., alias='innertubeCommand')

class LoggingDirectives5(BaseModel):
    model_config = ConfigDict(defer_build=True)
    tracking_params: str = Field(..., alias='trackingParams')
    visibility: Visibility

class CommandRun1(BaseModel):
    model_config = ConfigDict(defer_build=True)
    start_index: int = Field(..., alias='startIndex')
    length: int
    on_tap: OnTap3 = Field(..., alias='onTap')
    logging_directives: LoggingDirectives5 = Field(..., alias='loggingDirectives')

class ColorMapItem(BaseModel):
    model_config = ConfigDict(defer_build=True)
    key: str
    value: int

class StyleRunColorMapExtension(BaseModel):
    model_config = ConfigDict(defer_build=True)
    color_map: list[ColorMapItem] = Field(..., alias='colorMap')

class StyleRunExtensions(BaseModel):
    model_config = ConfigDict(defer_build=True)
    style_run_color_map_extension: StyleRunColorMapExtension = Field(..., alias='styleRunColorMapExtension')

class StyleRun4(BaseModel):
    model_config = ConfigDict(defer_build=True)
    weight_label: str = Field(..., alias='weightLabel')
    style_run_extensions: StyleRunExtensions = Field(..., alias='styleRunExtensions')

class ClientResource2(BaseModel):
    model_config = ConfigDict(defer_build=True)
    icon: str

class YoutubeIconSource(BaseModel):
    model_config = ConfigDict(defer_build=True)
    client_resource: ClientResource2 = Field(..., alias='clientResource')

class CustomImageSource(BaseModel):
    model_config = ConfigDict(defer_build=True)
    youtube_icon_source: YoutubeIconSource = Field(..., alias='youtubeIconSource')

class Source4(BaseModel):
    model_config = ConfigDict(defer_build=True)
    custom_image_source: CustomImageSource = Field(..., alias='customImageSource')

class Image3(BaseModel):
    model_config = ConfigDict(defer_build=True)
    sources: list[Source4]

class ImageType(BaseModel):
    model_config = ConfigDict(defer_build=True)
    image: Image3

class Type(BaseModel):
    model_config = ConfigDict(defer_build=True)
    image_type: ImageType = Field(..., alias='imageType')

class Height(BaseModel):
    model_config = ConfigDict(defer_build=True)
    value: int
    unit: str

class Width(BaseModel):
    model_config = ConfigDict(defer_build=True)
    value: int
    unit: str

class LayoutProperties(BaseModel):
    model_config = ConfigDict(defer_build=True)
    height: Height
    width: Width

class Properties(BaseModel):
    model_config = ConfigDict(defer_build=True)
    layout_properties: LayoutProperties = Field(..., alias='layoutProperties')

class Element(BaseModel):
    model_config = ConfigDict(defer_build=True)
    type: Type
    properties: Properties

class AttachmentRun(BaseModel):
    model_config = ConfigDict(defer_build=True)
    start_index: int = Field(..., alias='startIndex')
    length: int
    element: Element
    alignment: str

class Text8(BaseModel):
    model_config = ConfigDict(defer_build=True)
    content: str
    command_runs: list[CommandRun1] = Field(..., alias='commandRuns')
    style_runs: list[StyleRun4] = Field(..., alias='styleRuns')
    attachment_runs: list[AttachmentRun] = Field(..., alias='attachmentRuns')

class LoggingDirectives6(BaseModel):
    model_config = ConfigDict(defer_build=True)
    tracking_params: str = Field(..., alias='trackingParams')
    visibility: Visibility

class LoggingContext9(BaseModel):
    model_config = ConfigDict(defer_build=True)
    logging_directives: LoggingDirectives6 = Field(..., alias='loggingDirectives')

class RendererContext4(BaseModel):
    model_config = ConfigDict(defer_build=True)
    logging_context: LoggingContext9 = Field(..., alias='loggingContext')

class AttributionViewModel(BaseModel):
    model_config = ConfigDict(defer_build=True)
    text: Text8
    renderer_context: RendererContext4 = Field(..., alias='rendererContext')

class Attribution(BaseModel):
    model_config = ConfigDict(defer_build=True)
    attribution_view_model: AttributionViewModel = Field(..., alias='attributionViewModel')

class Source5(BaseModel):
    model_config = ConfigDict(defer_build=True)
    url: str
    width: int
    height: int

class Image4(BaseModel):
    model_config = ConfigDict(defer_build=True)
    sources: list[Source5]

class LoggingDirectives7(BaseModel):
    model_config = ConfigDict(defer_build=True)
    tracking_params: str = Field(..., alias='trackingParams')
    visibility: Visibility

class LoggingContext10(BaseModel):
    model_config = ConfigDict(defer_build=True)
    logging_directives: LoggingDirectives7 = Field(..., alias='loggingDirectives')

class RendererContext5(BaseModel):
    model_config = ConfigDict(defer_build=True)
    logging_context: LoggingContext10 = Field(..., alias='loggingContext')

class ImageBannerViewModel(BaseModel):
    model_config = ConfigDict(defer_build=True)
    image: Image4
    style: str
    renderer_context: RendererContext5 = Field(..., alias='rendererContext')

class Banner(BaseModel):
    model_config = ConfigDict(defer_build=True)
    image_banner_view_model: ImageBannerViewModel = Field(..., alias='imageBannerViewModel')

class LoggingDirectives8(BaseModel):
    model_config = ConfigDict(defer_build=True)
    tracking_params: str = Field(..., alias='trackingParams')
    visibility: Visibility

class LoggingContext11(BaseModel):
    model_config = ConfigDict(defer_build=True)
    logging_directives: LoggingDirectives8 = Field(..., alias='loggingDirectives')

class RendererContext6(BaseModel):
    model_config = ConfigDict(defer_build=True)
    logging_context: LoggingContext11 = Field(..., alias='loggingContext')

class PageHeaderViewModel(BaseModel):
    model_config = ConfigDict(defer_build=True)
    title: Title6
    image: Image1
    metadata: Metadata2
    description: Description
    attribution: Attribution
    banner: Banner
    renderer_context: RendererContext6 = Field(..., alias='rendererContext')

class Content13(BaseModel):
    model_config = ConfigDict(defer_build=True)
    page_header_view_model: PageHeaderViewModel = Field(..., alias='pageHeaderViewModel')

class PageHeaderRenderer(BaseModel):
    model_config = ConfigDict(defer_build=True)
    page_title: str = Field(..., alias='pageTitle')
    content: Content13

class Header3(BaseModel):
    model_config = ConfigDict(defer_build=True)
    page_header_renderer: PageHeaderRenderer = Field(..., alias='pageHeaderRenderer')

class Thumbnail5(BaseModel):
    model_config = ConfigDict(defer_build=True)
    url: str
    width: int
    height: int

class Avatar1(BaseModel):
    model_config = ConfigDict(defer_build=True)
    thumbnails: list[Thumbnail5]

class ChannelMetadataRenderer(BaseModel):
    model_config = ConfigDict(defer_build=True)
    title: str
    description: str
    rss_url: str = Field(..., alias='rssUrl')
    external_id: str = Field(..., alias='externalId')
    keywords: str
    owner_urls: list[str] = Field(..., alias='ownerUrls')
    avatar: Avatar1
    channel_url: str = Field(..., alias='channelUrl')
    is_family_safe: bool = Field(..., alias='isFamilySafe')
    available_country_codes: list[str] = Field(..., alias='availableCountryCodes')
    music_artist_name: str = Field(..., alias='musicArtistName')
    android_deep_link: str = Field(..., alias='androidDeepLink')
    android_appindexing_link: str = Field(..., alias='androidAppindexingLink')
    ios_appindexing_link: str = Field(..., alias='iosAppindexingLink')
    vanity_channel_url: str = Field(..., alias='vanityChannelUrl')

class Metadata3(BaseModel):
    model_config = ConfigDict(defer_build=True)
    channel_metadata_renderer: ChannelMetadataRenderer = Field(..., alias='channelMetadataRenderer')

class IconImage(BaseModel):
    model_config = ConfigDict(defer_build=True)
    icon_type: str = Field(..., alias='iconType')

class Run9(BaseModel):
    model_config = ConfigDict(defer_build=True)
    text: str

class TooltipText(BaseModel):
    model_config = ConfigDict(defer_build=True)
    runs: list[Run9]

class WebCommandMetadata16(BaseModel):
    model_config = ConfigDict(defer_build=True)
    url: str
    web_page_type: str = Field(..., alias='webPageType')
    root_ve: int = Field(..., alias='rootVe')
    api_url: str = Field(..., alias='apiUrl')

class CommandMetadata16(BaseModel):
    model_config = ConfigDict(defer_build=True)
    web_command_metadata: WebCommandMetadata16 = Field(..., alias='webCommandMetadata')

class BrowseEndpoint5(BaseModel):
    model_config = ConfigDict(defer_build=True)
    browse_id: str = Field(..., alias='browseId')

class Endpoint2(BaseModel):
    model_config = ConfigDict(defer_build=True)
    click_tracking_params: str = Field(..., alias='clickTrackingParams')
    command_metadata: CommandMetadata16 = Field(..., alias='commandMetadata')
    browse_endpoint: BrowseEndpoint5 = Field(..., alias='browseEndpoint')

class TopbarLogoRenderer(BaseModel):
    model_config = ConfigDict(defer_build=True)
    icon_image: IconImage = Field(..., alias='iconImage')
    tooltip_text: TooltipText = Field(..., alias='tooltipText')
    endpoint: Endpoint2
    tracking_params: str = Field(..., alias='trackingParams')
    override_entity_key: str = Field(..., alias='overrideEntityKey')

class Logo(BaseModel):
    model_config = ConfigDict(defer_build=True)
    topbar_logo_renderer: TopbarLogoRenderer = Field(..., alias='topbarLogoRenderer')

class PlaceholderText(BaseModel):
    model_config = ConfigDict(defer_build=True)
    runs: list[Run9]

class WebSearchboxConfig(BaseModel):
    model_config = ConfigDict(defer_build=True)
    request_language: str = Field(..., alias='requestLanguage')
    request_domain: str = Field(..., alias='requestDomain')
    has_onscreen_keyboard: bool = Field(..., alias='hasOnscreenKeyboard')
    focus_searchbox: bool = Field(..., alias='focusSearchbox')

class Config(BaseModel):
    model_config = ConfigDict(defer_build=True)
    web_searchbox_config: WebSearchboxConfig = Field(..., alias='webSearchboxConfig')

class WebCommandMetadata17(BaseModel):
    model_config = ConfigDict(defer_build=True)
    url: str
    web_page_type: str = Field(..., alias='webPageType')
    root_ve: int = Field(..., alias='rootVe')

class CommandMetadata17(BaseModel):
    model_config = ConfigDict(defer_build=True)
    web_command_metadata: WebCommandMetadata17 = Field(..., alias='webCommandMetadata')

class SearchEndpoint1(BaseModel):
    model_config = ConfigDict(defer_build=True)
    query: str

class SearchEndpoint(BaseModel):
    model_config = ConfigDict(defer_build=True)
    click_tracking_params: str = Field(..., alias='clickTrackingParams')
    command_metadata: CommandMetadata17 = Field(..., alias='commandMetadata')
    search_endpoint: SearchEndpoint1 = Field(..., alias='searchEndpoint')

class AccessibilityData11(BaseModel):
    model_config = ConfigDict(defer_build=True)
    label: str

class AccessibilityData10(BaseModel):
    model_config = ConfigDict(defer_build=True)
    accessibility_data: AccessibilityData11 = Field(..., alias='accessibilityData')

class ButtonRenderer7(BaseModel):
    model_config = ConfigDict(defer_build=True)
    style: str
    size: str
    is_disabled: bool = Field(..., alias='isDisabled')
    icon: Icon6
    tracking_params: str = Field(..., alias='trackingParams')
    accessibility_data: AccessibilityData10 = Field(..., alias='accessibilityData')

class ClearButton(BaseModel):
    model_config = ConfigDict(defer_build=True)
    button_renderer: ButtonRenderer7 = Field(..., alias='buttonRenderer')

class Headline(BaseModel):
    model_config = ConfigDict(defer_build=True)
    content: str

class DialogHeaderViewModel(BaseModel):
    model_config = ConfigDict(defer_build=True)
    headline: Headline

class Header5(BaseModel):
    model_config = ConfigDict(defer_build=True)
    dialog_header_view_model: DialogHeaderViewModel = Field(..., alias='dialogHeaderViewModel')

class ButtonViewModel(BaseModel):
    model_config = ConfigDict(defer_build=True)
    title: str
    style: str
    tracking_params: str = Field(..., alias='trackingParams')
    is_full_width: bool = Field(..., alias='isFullWidth')
    type: str

class PrimaryButton(BaseModel):
    model_config = ConfigDict(defer_build=True)
    button_view_model: ButtonViewModel = Field(..., alias='buttonViewModel')

class SecondaryButton(BaseModel):
    model_config = ConfigDict(defer_build=True)
    button_view_model: ButtonViewModel = Field(..., alias='buttonViewModel')

class PanelFooterViewModel(BaseModel):
    model_config = ConfigDict(defer_build=True)
    primary_button: PrimaryButton = Field(..., alias='primaryButton')
    secondary_button: SecondaryButton = Field(..., alias='secondaryButton')
    should_hide_divider: bool = Field(..., alias='shouldHideDivider')

class Footer(BaseModel):
    model_config = ConfigDict(defer_build=True)
    panel_footer_view_model: PanelFooterViewModel = Field(..., alias='panelFooterViewModel')

class Text9(BaseModel):
    model_config = ConfigDict(defer_build=True)
    content: str

class Paragraph(BaseModel):
    model_config = ConfigDict(defer_build=True)
    text: Text9

class BasicContentViewModel(BaseModel):
    model_config = ConfigDict(defer_build=True)
    paragraphs: list[Paragraph]

class Content17(BaseModel):
    model_config = ConfigDict(defer_build=True)
    basic_content_view_model: BasicContentViewModel = Field(..., alias='basicContentViewModel')

class DialogViewModel(BaseModel):
    model_config = ConfigDict(defer_build=True)
    header: Header5
    footer: Footer
    content: Content17

class InlineContent(BaseModel):
    model_config = ConfigDict(defer_build=True)
    dialog_view_model: DialogViewModel = Field(..., alias='dialogViewModel')

class PanelLoadingStrategy(BaseModel):
    model_config = ConfigDict(defer_build=True)
    inline_content: InlineContent = Field(..., alias='inlineContent')

class ShowDialogCommand(BaseModel):
    model_config = ConfigDict(defer_build=True)
    panel_loading_strategy: PanelLoadingStrategy = Field(..., alias='panelLoadingStrategy')

class ShowImageSourceDialog(BaseModel):
    model_config = ConfigDict(defer_build=True)
    click_tracking_params: str = Field(..., alias='clickTrackingParams')
    show_dialog_command: ShowDialogCommand = Field(..., alias='showDialogCommand')

class FusionSearchboxRenderer(BaseModel):
    model_config = ConfigDict(defer_build=True)
    icon: Icon6
    placeholder_text: PlaceholderText = Field(..., alias='placeholderText')
    config: Config
    tracking_params: str = Field(..., alias='trackingParams')
    search_endpoint: SearchEndpoint = Field(..., alias='searchEndpoint')
    clear_button: ClearButton = Field(..., alias='clearButton')
    show_image_source_dialog: ShowImageSourceDialog = Field(..., alias='showImageSourceDialog')
    disable_ai_appearance: bool = Field(..., alias='disableAiAppearance')

class Searchbox(BaseModel):
    model_config = ConfigDict(defer_build=True)
    fusion_searchbox_renderer: FusionSearchboxRenderer = Field(..., alias='fusionSearchboxRenderer')

class WebCommandMetadata18(BaseModel):
    model_config = ConfigDict(defer_build=True)
    send_post: bool = Field(..., alias='sendPost')
    api_url: str = Field(..., alias='apiUrl')

class CommandMetadata18(BaseModel):
    model_config = ConfigDict(defer_build=True)
    web_command_metadata: WebCommandMetadata18 = Field(..., alias='webCommandMetadata')

class MultiPageMenuRenderer(BaseModel):
    model_config = ConfigDict(defer_build=True)
    tracking_params: str = Field(..., alias='trackingParams')
    style: str
    show_loading_spinner: bool = Field(..., alias='showLoadingSpinner')

class Popup(BaseModel):
    model_config = ConfigDict(defer_build=True)
    multi_page_menu_renderer: MultiPageMenuRenderer = Field(..., alias='multiPageMenuRenderer')

class OpenPopupAction(BaseModel):
    model_config = ConfigDict(defer_build=True)
    popup: Popup
    popup_type: str = Field(..., alias='popupType')
    be_reused: bool = Field(..., alias='beReused')

class Action(BaseModel):
    model_config = ConfigDict(defer_build=True)
    click_tracking_params: str = Field(..., alias='clickTrackingParams')
    open_popup_action: OpenPopupAction = Field(..., alias='openPopupAction')

class SignalServiceEndpoint(BaseModel):
    model_config = ConfigDict(defer_build=True)
    signal: str
    actions: list[Action]

class MenuRequest(BaseModel):
    model_config = ConfigDict(defer_build=True)
    click_tracking_params: str = Field(..., alias='clickTrackingParams')
    command_metadata: CommandMetadata18 = Field(..., alias='commandMetadata')
    signal_service_endpoint: SignalServiceEndpoint = Field(..., alias='signalServiceEndpoint')

class AccessibilityData12(BaseModel):
    model_config = ConfigDict(defer_build=True)
    label: str

class Accessibility6(BaseModel):
    model_config = ConfigDict(defer_build=True)
    accessibility_data: AccessibilityData12 = Field(..., alias='accessibilityData')

class TopbarMenuButtonRenderer(BaseModel):
    model_config = ConfigDict(defer_build=True)
    icon: Icon6
    menu_request: MenuRequest = Field(..., alias='menuRequest')
    tracking_params: str = Field(..., alias='trackingParams')
    accessibility: Accessibility6
    tooltip: str
    style: str

class Text10(BaseModel):
    model_config = ConfigDict(defer_build=True)
    runs: list[Run9]

class WebCommandMetadata19(BaseModel):
    model_config = ConfigDict(defer_build=True)
    url: str
    web_page_type: str = Field(..., alias='webPageType')
    root_ve: int = Field(..., alias='rootVe')

class CommandMetadata19(BaseModel):
    model_config = ConfigDict(defer_build=True)
    web_command_metadata: WebCommandMetadata19 = Field(..., alias='webCommandMetadata')

class SignInEndpoint(BaseModel):
    model_config = ConfigDict(defer_build=True)
    idam_tag: str = Field(..., alias='idamTag')

class NavigationEndpoint7(BaseModel):
    model_config = ConfigDict(defer_build=True)
    click_tracking_params: str = Field(..., alias='clickTrackingParams')
    command_metadata: CommandMetadata19 = Field(..., alias='commandMetadata')
    sign_in_endpoint: SignInEndpoint = Field(..., alias='signInEndpoint')

class ButtonRenderer8(BaseModel):
    model_config = ConfigDict(defer_build=True)
    style: str
    size: str
    text: Text10
    icon: Icon6
    navigation_endpoint: NavigationEndpoint7 = Field(..., alias='navigationEndpoint')
    tracking_params: str = Field(..., alias='trackingParams')
    target_id: str = Field(..., alias='targetId')

class TopbarButton(BaseModel):
    model_config = ConfigDict(defer_build=True)
    topbar_menu_button_renderer: TopbarMenuButtonRenderer | None = Field(None, alias='topbarMenuButtonRenderer')
    button_renderer: ButtonRenderer8 | None = Field(None, alias='buttonRenderer')

class Title8(BaseModel):
    model_config = ConfigDict(defer_build=True)
    runs: list[Run9]

class Title9(BaseModel):
    model_config = ConfigDict(defer_build=True)
    runs: list[Run9]

class Label(BaseModel):
    model_config = ConfigDict(defer_build=True)
    runs: list[Run9]

class HotkeyAccessibilityLabel(BaseModel):
    model_config = ConfigDict(defer_build=True)
    accessibility_data: AccessibilityData12 = Field(..., alias='accessibilityData')

class HotkeyDialogSectionOptionRenderer(BaseModel):
    model_config = ConfigDict(defer_build=True)
    label: Label
    hotkey: str
    hotkey_accessibility_label: HotkeyAccessibilityLabel | None = Field(None, alias='hotkeyAccessibilityLabel')

class Option(BaseModel):
    model_config = ConfigDict(defer_build=True)
    hotkey_dialog_section_option_renderer: HotkeyDialogSectionOptionRenderer = Field(..., alias='hotkeyDialogSectionOptionRenderer')

class HotkeyDialogSectionRenderer(BaseModel):
    model_config = ConfigDict(defer_build=True)
    title: Title9
    options: list[Option]

class Section(BaseModel):
    model_config = ConfigDict(defer_build=True)
    hotkey_dialog_section_renderer: HotkeyDialogSectionRenderer = Field(..., alias='hotkeyDialogSectionRenderer')

class Text11(BaseModel):
    model_config = ConfigDict(defer_build=True)
    runs: list[Run9]

class ButtonRenderer9(BaseModel):
    model_config = ConfigDict(defer_build=True)
    style: str
    size: str
    is_disabled: bool = Field(..., alias='isDisabled')
    text: Text11
    tracking_params: str = Field(..., alias='trackingParams')

class DismissButton(BaseModel):
    model_config = ConfigDict(defer_build=True)
    button_renderer: ButtonRenderer9 = Field(..., alias='buttonRenderer')

class HotkeyDialogRenderer(BaseModel):
    model_config = ConfigDict(defer_build=True)
    title: Title8
    sections: list[Section]
    dismiss_button: DismissButton = Field(..., alias='dismissButton')
    tracking_params: str = Field(..., alias='trackingParams')

class HotkeyDialog(BaseModel):
    model_config = ConfigDict(defer_build=True)
    hotkey_dialog_renderer: HotkeyDialogRenderer = Field(..., alias='hotkeyDialogRenderer')

class WebCommandMetadata20(BaseModel):
    model_config = ConfigDict(defer_build=True)
    send_post: bool = Field(..., alias='sendPost')

class CommandMetadata20(BaseModel):
    model_config = ConfigDict(defer_build=True)
    web_command_metadata: WebCommandMetadata20 = Field(..., alias='webCommandMetadata')

class SignalAction(BaseModel):
    model_config = ConfigDict(defer_build=True)
    signal: str

class Action1(BaseModel):
    model_config = ConfigDict(defer_build=True)
    click_tracking_params: str = Field(..., alias='clickTrackingParams')
    signal_action: SignalAction = Field(..., alias='signalAction')

class SignalServiceEndpoint1(BaseModel):
    model_config = ConfigDict(defer_build=True)
    signal: str
    actions: list[Action1]

class Command4(BaseModel):
    model_config = ConfigDict(defer_build=True)
    click_tracking_params: str = Field(..., alias='clickTrackingParams')
    command_metadata: CommandMetadata20 = Field(..., alias='commandMetadata')
    signal_service_endpoint: SignalServiceEndpoint1 = Field(..., alias='signalServiceEndpoint')

class ButtonRenderer10(BaseModel):
    model_config = ConfigDict(defer_build=True)
    tracking_params: str = Field(..., alias='trackingParams')
    command: Command4

class BackButton(BaseModel):
    model_config = ConfigDict(defer_build=True)
    button_renderer: ButtonRenderer10 = Field(..., alias='buttonRenderer')

class CommandMetadata21(BaseModel):
    model_config = ConfigDict(defer_build=True)
    web_command_metadata: WebCommandMetadata20 = Field(..., alias='webCommandMetadata')

class Action2(BaseModel):
    model_config = ConfigDict(defer_build=True)
    click_tracking_params: str = Field(..., alias='clickTrackingParams')
    signal_action: SignalAction = Field(..., alias='signalAction')

class SignalServiceEndpoint2(BaseModel):
    model_config = ConfigDict(defer_build=True)
    signal: str
    actions: list[Action2]

class Command5(BaseModel):
    model_config = ConfigDict(defer_build=True)
    click_tracking_params: str = Field(..., alias='clickTrackingParams')
    command_metadata: CommandMetadata21 = Field(..., alias='commandMetadata')
    signal_service_endpoint: SignalServiceEndpoint2 = Field(..., alias='signalServiceEndpoint')

class ButtonRenderer11(BaseModel):
    model_config = ConfigDict(defer_build=True)
    tracking_params: str = Field(..., alias='trackingParams')
    command: Command5

class ForwardButton(BaseModel):
    model_config = ConfigDict(defer_build=True)
    button_renderer: ButtonRenderer11 = Field(..., alias='buttonRenderer')

class Text12(BaseModel):
    model_config = ConfigDict(defer_build=True)
    runs: list[Run9]

class CommandMetadata22(BaseModel):
    model_config = ConfigDict(defer_build=True)
    web_command_metadata: WebCommandMetadata20 = Field(..., alias='webCommandMetadata')

class Action3(BaseModel):
    model_config = ConfigDict(defer_build=True)
    click_tracking_params: str = Field(..., alias='clickTrackingParams')
    signal_action: SignalAction = Field(..., alias='signalAction')

class SignalServiceEndpoint3(BaseModel):
    model_config = ConfigDict(defer_build=True)
    signal: str
    actions: list[Action3]

class Command6(BaseModel):
    model_config = ConfigDict(defer_build=True)
    click_tracking_params: str = Field(..., alias='clickTrackingParams')
    command_metadata: CommandMetadata22 = Field(..., alias='commandMetadata')
    signal_service_endpoint: SignalServiceEndpoint3 = Field(..., alias='signalServiceEndpoint')

class ButtonRenderer12(BaseModel):
    model_config = ConfigDict(defer_build=True)
    style: str
    size: str
    is_disabled: bool = Field(..., alias='isDisabled')
    text: Text12
    tracking_params: str = Field(..., alias='trackingParams')
    command: Command6

class A11ySkipNavigationButton(BaseModel):
    model_config = ConfigDict(defer_build=True)
    button_renderer: ButtonRenderer12 = Field(..., alias='buttonRenderer')

class CommandMetadata23(BaseModel):
    model_config = ConfigDict(defer_build=True)
    web_command_metadata: WebCommandMetadata20 = Field(..., alias='webCommandMetadata')

class PlaceholderHeader(BaseModel):
    model_config = ConfigDict(defer_build=True)
    runs: list[Run9]

class PromptHeader(BaseModel):
    model_config = ConfigDict(defer_build=True)
    runs: list[Run9]

class ExampleQuery1(BaseModel):
    model_config = ConfigDict(defer_build=True)
    runs: list[Run9]

class ExampleQuery2(BaseModel):
    model_config = ConfigDict(defer_build=True)
    runs: list[Run9]

class PromptMicrophoneLabel(BaseModel):
    model_config = ConfigDict(defer_build=True)
    runs: list[Run9]

class LoadingHeader(BaseModel):
    model_config = ConfigDict(defer_build=True)
    runs: list[Run9]

class ConnectionErrorHeader(BaseModel):
    model_config = ConfigDict(defer_build=True)
    runs: list[Run9]

class ConnectionErrorMicrophoneLabel(BaseModel):
    model_config = ConfigDict(defer_build=True)
    runs: list[Run9]

class PermissionsHeader(BaseModel):
    model_config = ConfigDict(defer_build=True)
    runs: list[Run9]

class PermissionsSubtext(BaseModel):
    model_config = ConfigDict(defer_build=True)
    runs: list[Run9]

class DisabledHeader(BaseModel):
    model_config = ConfigDict(defer_build=True)
    runs: list[Run9]

class DisabledSubtext(BaseModel):
    model_config = ConfigDict(defer_build=True)
    runs: list[Run9]

class MicrophoneButtonAriaLabel(BaseModel):
    model_config = ConfigDict(defer_build=True)
    runs: list[Run9]

class AccessibilityData14(BaseModel):
    model_config = ConfigDict(defer_build=True)
    accessibility_data: AccessibilityData12 = Field(..., alias='accessibilityData')

class ButtonRenderer14(BaseModel):
    model_config = ConfigDict(defer_build=True)
    style: str
    size: str
    is_disabled: bool = Field(..., alias='isDisabled')
    icon: Icon6
    tracking_params: str = Field(..., alias='trackingParams')
    accessibility_data: AccessibilityData14 = Field(..., alias='accessibilityData')

class ExitButton(BaseModel):
    model_config = ConfigDict(defer_build=True)
    button_renderer: ButtonRenderer14 = Field(..., alias='buttonRenderer')

class MicrophoneOffPromptHeader(BaseModel):
    model_config = ConfigDict(defer_build=True)
    runs: list[Run9]

class VoiceSearchDialogRenderer(BaseModel):
    model_config = ConfigDict(defer_build=True)
    placeholder_header: PlaceholderHeader = Field(..., alias='placeholderHeader')
    prompt_header: PromptHeader = Field(..., alias='promptHeader')
    example_query1: ExampleQuery1 = Field(..., alias='exampleQuery1')
    example_query2: ExampleQuery2 = Field(..., alias='exampleQuery2')
    prompt_microphone_label: PromptMicrophoneLabel = Field(..., alias='promptMicrophoneLabel')
    loading_header: LoadingHeader = Field(..., alias='loadingHeader')
    connection_error_header: ConnectionErrorHeader = Field(..., alias='connectionErrorHeader')
    connection_error_microphone_label: ConnectionErrorMicrophoneLabel = Field(..., alias='connectionErrorMicrophoneLabel')
    permissions_header: PermissionsHeader = Field(..., alias='permissionsHeader')
    permissions_subtext: PermissionsSubtext = Field(..., alias='permissionsSubtext')
    disabled_header: DisabledHeader = Field(..., alias='disabledHeader')
    disabled_subtext: DisabledSubtext = Field(..., alias='disabledSubtext')
    microphone_button_aria_label: MicrophoneButtonAriaLabel = Field(..., alias='microphoneButtonAriaLabel')
    exit_button: ExitButton = Field(..., alias='exitButton')
    tracking_params: str = Field(..., alias='trackingParams')
    microphone_off_prompt_header: MicrophoneOffPromptHeader = Field(..., alias='microphoneOffPromptHeader')

class Popup1(BaseModel):
    model_config = ConfigDict(defer_build=True)
    voice_search_dialog_renderer: VoiceSearchDialogRenderer = Field(..., alias='voiceSearchDialogRenderer')

class OpenPopupAction1(BaseModel):
    model_config = ConfigDict(defer_build=True)
    popup: Popup1
    popup_type: str = Field(..., alias='popupType')

class Action4(BaseModel):
    model_config = ConfigDict(defer_build=True)
    click_tracking_params: str = Field(..., alias='clickTrackingParams')
    open_popup_action: OpenPopupAction1 = Field(..., alias='openPopupAction')

class SignalServiceEndpoint4(BaseModel):
    model_config = ConfigDict(defer_build=True)
    signal: str
    actions: list[Action4]

class ServiceEndpoint(BaseModel):
    model_config = ConfigDict(defer_build=True)
    click_tracking_params: str = Field(..., alias='clickTrackingParams')
    command_metadata: CommandMetadata23 = Field(..., alias='commandMetadata')
    signal_service_endpoint: SignalServiceEndpoint4 = Field(..., alias='signalServiceEndpoint')

class AccessibilityData17(BaseModel):
    model_config = ConfigDict(defer_build=True)
    label: str

class AccessibilityData16(BaseModel):
    model_config = ConfigDict(defer_build=True)
    accessibility_data: AccessibilityData17 = Field(..., alias='accessibilityData')

class ButtonRenderer13(BaseModel):
    model_config = ConfigDict(defer_build=True)
    style: str
    size: str
    is_disabled: bool = Field(..., alias='isDisabled')
    service_endpoint: ServiceEndpoint = Field(..., alias='serviceEndpoint')
    icon: Icon6
    tooltip: str
    tracking_params: str = Field(..., alias='trackingParams')
    accessibility_data: AccessibilityData16 = Field(..., alias='accessibilityData')

class VoiceSearchButton(BaseModel):
    model_config = ConfigDict(defer_build=True)
    button_renderer: ButtonRenderer13 = Field(..., alias='buttonRenderer')

class DesktopTopbarRenderer(BaseModel):
    model_config = ConfigDict(defer_build=True)
    logo: Logo
    searchbox: Searchbox
    tracking_params: str = Field(..., alias='trackingParams')
    topbar_buttons: list[TopbarButton] = Field(..., alias='topbarButtons')
    hotkey_dialog: HotkeyDialog = Field(..., alias='hotkeyDialog')
    back_button: BackButton = Field(..., alias='backButton')
    forward_button: ForwardButton = Field(..., alias='forwardButton')
    a11y_skip_navigation_button: A11ySkipNavigationButton = Field(..., alias='a11ySkipNavigationButton')
    voice_search_button: VoiceSearchButton = Field(..., alias='voiceSearchButton')

class Topbar(BaseModel):
    model_config = ConfigDict(defer_build=True)
    desktop_topbar_renderer: DesktopTopbarRenderer = Field(..., alias='desktopTopbarRenderer')

class Thumbnail6(BaseModel):
    model_config = ConfigDict(defer_build=True)
    thumbnails: list[Thumbnail5]

class LinkAlternate(BaseModel):
    model_config = ConfigDict(defer_build=True)
    href_url: str = Field(..., alias='hrefUrl')

class MicroformatDataRenderer(BaseModel):
    model_config = ConfigDict(defer_build=True)
    url_canonical: str = Field(..., alias='urlCanonical')
    title: str
    description: str
    thumbnail: Thumbnail6
    site_name: str = Field(..., alias='siteName')
    app_name: str = Field(..., alias='appName')
    android_package: str = Field(..., alias='androidPackage')
    ios_app_store_id: str = Field(..., alias='iosAppStoreId')
    ios_app_arguments: str = Field(..., alias='iosAppArguments')
    og_type: str = Field(..., alias='ogType')
    url_applinks_web: str = Field(..., alias='urlApplinksWeb')
    url_applinks_ios: str = Field(..., alias='urlApplinksIos')
    url_applinks_android: str = Field(..., alias='urlApplinksAndroid')
    url_twitter_ios: str = Field(..., alias='urlTwitterIos')
    url_twitter_android: str = Field(..., alias='urlTwitterAndroid')
    twitter_card_type: str = Field(..., alias='twitterCardType')
    twitter_site_handle: str = Field(..., alias='twitterSiteHandle')
    schema_dot_org_type: str = Field(..., alias='schemaDotOrgType')
    noindex: bool
    unlisted: bool
    family_safe: bool = Field(..., alias='familySafe')
    available_countries: list[str] = Field(..., alias='availableCountries')
    link_alternates: list[LinkAlternate] = Field(..., alias='linkAlternates')

class Microformat(BaseModel):
    model_config = ConfigDict(defer_build=True)
    microformat_data_renderer: MicroformatDataRenderer = Field(..., alias='microformatDataRenderer')

class TopicModel(BaseModel):
    model_config = ConfigDict(defer_build=True)
    response_context: ResponseContext = Field(..., alias='responseContext')
    tracking_params: str = Field(..., alias='trackingParams')
    on_response_received_endpoints: list[OnResponseReceivedEndpoint] | None = Field(None, alias='onResponseReceivedEndpoints')
    contents: Contents | None = None
    header: Header3 | None = None
    metadata: Metadata3 | None = None
    topbar: Topbar | None = None
    microformat: Microformat | None = None
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
