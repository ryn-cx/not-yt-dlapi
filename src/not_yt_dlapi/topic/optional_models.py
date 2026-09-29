from typing import Any, Self
from pydantic import ModelWrapValidatorHandler, PrivateAttr, model_validator
from pydantic import BaseModel, ConfigDict, Field
from uuid import UUID

class Param(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    key: str | Any = Field(default=None, union_mode='left_to_right')
    value: str | Any = Field(default=None, union_mode='left_to_right')

class ServiceTrackingParam(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    service: str | Any = Field(default=None, union_mode='left_to_right')
    params: list[Param] | Any = Field(default=None, union_mode='left_to_right')

class MainAppWebResponseContext(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    logged_out: bool | Any = Field(None, alias='loggedOut', union_mode='left_to_right')
    tracking_param: str | Any = Field(None, alias='trackingParam', union_mode='left_to_right')

class WebResponseContextPreloadData(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    preload_message_names: list[str] | Any = Field(None, alias='preloadMessageNames', union_mode='left_to_right')

class WebResponseContextExtensionData(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    web_response_context_preload_data: WebResponseContextPreloadData | Any = Field(None, alias='webResponseContextPreloadData', union_mode='left_to_right')
    has_decorated: bool | Any = Field(None, alias='hasDecorated', union_mode='left_to_right')

class ResponseContext(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    visitor_data: str | Any = Field(None, alias='visitorData', union_mode='left_to_right')
    service_tracking_params: list[ServiceTrackingParam] | Any = Field(None, alias='serviceTrackingParams', union_mode='left_to_right')
    max_age_seconds: int | Any = Field(None, alias='maxAgeSeconds', union_mode='left_to_right')
    main_app_web_response_context: MainAppWebResponseContext | Any = Field(None, alias='mainAppWebResponseContext', union_mode='left_to_right')
    response_id: str | Any = Field(None, alias='responseId', union_mode='left_to_right')
    web_response_context_extension_data: WebResponseContextExtensionData | Any = Field(None, alias='webResponseContextExtensionData', union_mode='left_to_right')

class Thumbnail1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    url: str | Any = Field(default=None, union_mode='left_to_right')
    width: int | Any = Field(default=None, union_mode='left_to_right')
    height: int | Any = Field(default=None, union_mode='left_to_right')

class SampledThumbnailColor(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    red: int | Any = Field(default=None, union_mode='left_to_right')
    green: int | Any = Field(default=None, union_mode='left_to_right')
    blue: int | Any = Field(default=None, union_mode='left_to_right')

class DarkColorPalette(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    section2_color: int | Any = Field(None, alias='section2Color', union_mode='left_to_right')
    icon_inactive_color: int | Any = Field(None, alias='iconInactiveColor', union_mode='left_to_right')
    icon_disabled_color: int | Any = Field(None, alias='iconDisabledColor', union_mode='left_to_right')

class VibrantColorPalette(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    icon_inactive_color: int | Any = Field(None, alias='iconInactiveColor', union_mode='left_to_right')

class Thumbnail(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    thumbnails: list[Thumbnail1] | Any = Field(default=None, union_mode='left_to_right')
    sampled_thumbnail_color: SampledThumbnailColor | Any = Field(None, alias='sampledThumbnailColor', union_mode='left_to_right')
    dark_color_palette: DarkColorPalette | Any = Field(None, alias='darkColorPalette', union_mode='left_to_right')
    vibrant_color_palette: VibrantColorPalette | Any = Field(None, alias='vibrantColorPalette', union_mode='left_to_right')

class WebCommandMetadata(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    url: str | Any = Field(default=None, union_mode='left_to_right')
    web_page_type: str | Any = Field(None, alias='webPageType', union_mode='left_to_right')
    root_ve: int | Any = Field(None, alias='rootVe', union_mode='left_to_right')

class CommandMetadata(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    web_command_metadata: WebCommandMetadata | Any = Field(None, alias='webCommandMetadata', union_mode='left_to_right')

class VssLoggingContext(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    serialized_context_data: str | Any = Field(None, alias='serializedContextData', union_mode='left_to_right')

class LoggingContext(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    vss_logging_context: VssLoggingContext | Any = Field(None, alias='vssLoggingContext', union_mode='left_to_right')

class CommonConfig(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    url: str | Any = Field(default=None, union_mode='left_to_right')

class Html5PlaybackOnesieConfig(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    common_config: CommonConfig | Any = Field(None, alias='commonConfig', union_mode='left_to_right')

class WatchEndpointSupportedOnesieConfig(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    html5_playback_onesie_config: Html5PlaybackOnesieConfig | Any = Field(None, alias='html5PlaybackOnesieConfig', union_mode='left_to_right')

class WatchEndpoint(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    video_id: str | Any = Field(None, alias='videoId', union_mode='left_to_right')
    playlist_id: str | Any = Field(None, alias='playlistId', union_mode='left_to_right')
    params: str | Any = Field(default=None, union_mode='left_to_right')
    logging_context: LoggingContext | Any = Field(None, alias='loggingContext', union_mode='left_to_right')
    watch_endpoint_supported_onesie_config: WatchEndpointSupportedOnesieConfig | Any = Field(None, alias='watchEndpointSupportedOnesieConfig', union_mode='left_to_right')
    player_params: str | Any = Field(None, alias='playerParams', union_mode='left_to_right')

class NavigationEndpoint(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    click_tracking_params: str | Any = Field(None, alias='clickTrackingParams', union_mode='left_to_right')
    command_metadata: CommandMetadata | Any = Field(None, alias='commandMetadata', union_mode='left_to_right')
    watch_endpoint: WatchEndpoint | Any = Field(None, alias='watchEndpoint', union_mode='left_to_right')

class Run(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    text: str | Any = Field(default=None, union_mode='left_to_right')
    navigation_endpoint: NavigationEndpoint | Any = Field(None, alias='navigationEndpoint', union_mode='left_to_right')

class Title(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    runs: list[Run] | Any = Field(default=None, union_mode='left_to_right')

class WebCommandMetadata1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    url: str | Any = Field(default=None, union_mode='left_to_right')
    web_page_type: str | Any = Field(None, alias='webPageType', union_mode='left_to_right')
    root_ve: int | Any = Field(None, alias='rootVe', union_mode='left_to_right')
    api_url: str | Any = Field(None, alias='apiUrl', union_mode='left_to_right')

class CommandMetadata1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    web_command_metadata: WebCommandMetadata1 | Any = Field(None, alias='webCommandMetadata', union_mode='left_to_right')

class BrowseEndpoint(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    browse_id: str | Any = Field(None, alias='browseId', union_mode='left_to_right')
    canonical_base_url: str | Any = Field(None, alias='canonicalBaseUrl', union_mode='left_to_right')

class NavigationEndpoint1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    click_tracking_params: str | Any = Field(None, alias='clickTrackingParams', union_mode='left_to_right')
    command_metadata: CommandMetadata1 | Any = Field(None, alias='commandMetadata', union_mode='left_to_right')
    browse_endpoint: BrowseEndpoint | Any = Field(None, alias='browseEndpoint', union_mode='left_to_right')

class Run1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    text: str | Any = Field(default=None, union_mode='left_to_right')
    navigation_endpoint: NavigationEndpoint1 | Any = Field(None, alias='navigationEndpoint', union_mode='left_to_right')

class ShortBylineText(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    runs: list[Run1] | Any = Field(default=None, union_mode='left_to_right')

class Run2(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    text: str | Any = Field(default=None, union_mode='left_to_right')

class VideoCountText(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    runs: list[Run2] | Any = Field(default=None, union_mode='left_to_right')

class WebCommandMetadata2(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    url: str | Any = Field(default=None, union_mode='left_to_right')
    web_page_type: str | Any = Field(None, alias='webPageType', union_mode='left_to_right')
    root_ve: int | Any = Field(None, alias='rootVe', union_mode='left_to_right')

class CommandMetadata2(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    web_command_metadata: WebCommandMetadata2 | Any = Field(None, alias='webCommandMetadata', union_mode='left_to_right')

class LoggingContext1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    vss_logging_context: VssLoggingContext | Any = Field(None, alias='vssLoggingContext', union_mode='left_to_right')

class Html5PlaybackOnesieConfig1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    common_config: CommonConfig | Any = Field(None, alias='commonConfig', union_mode='left_to_right')

class WatchEndpointSupportedOnesieConfig1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    html5_playback_onesie_config: Html5PlaybackOnesieConfig1 | Any = Field(None, alias='html5PlaybackOnesieConfig', union_mode='left_to_right')

class WatchEndpoint1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    video_id: str | Any = Field(None, alias='videoId', union_mode='left_to_right')
    playlist_id: str | Any = Field(None, alias='playlistId', union_mode='left_to_right')
    params: str | Any = Field(default=None, union_mode='left_to_right')
    logging_context: LoggingContext1 | Any = Field(None, alias='loggingContext', union_mode='left_to_right')
    watch_endpoint_supported_onesie_config: WatchEndpointSupportedOnesieConfig1 | Any = Field(None, alias='watchEndpointSupportedOnesieConfig', union_mode='left_to_right')
    player_params: str | Any = Field(None, alias='playerParams', union_mode='left_to_right')

class NavigationEndpoint2(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    click_tracking_params: str | Any = Field(None, alias='clickTrackingParams', union_mode='left_to_right')
    command_metadata: CommandMetadata2 | Any = Field(None, alias='commandMetadata', union_mode='left_to_right')
    watch_endpoint: WatchEndpoint1 | Any = Field(None, alias='watchEndpoint', union_mode='left_to_right')

class VideoCountShortText(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    simple_text: str | Any = Field(None, alias='simpleText', union_mode='left_to_right')

class Thumbnail2(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    url: str | Any = Field(default=None, union_mode='left_to_right')
    width: int | Any = Field(default=None, union_mode='left_to_right')
    height: int | Any = Field(default=None, union_mode='left_to_right')

class SidebarThumbnail(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    thumbnails: list[Thumbnail2] | Any = Field(default=None, union_mode='left_to_right')

class Run3(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    text: str | Any = Field(default=None, union_mode='left_to_right')
    bold: bool | Any = Field(default=None, union_mode='left_to_right')

class ThumbnailText(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    runs: list[Run3] | Any = Field(default=None, union_mode='left_to_right')

class Thumbnail3(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    thumbnails: list[Thumbnail2] | Any = Field(default=None, union_mode='left_to_right')
    sampled_thumbnail_color: SampledThumbnailColor | Any = Field(None, alias='sampledThumbnailColor', union_mode='left_to_right')
    dark_color_palette: DarkColorPalette | Any = Field(None, alias='darkColorPalette', union_mode='left_to_right')
    vibrant_color_palette: VibrantColorPalette | Any = Field(None, alias='vibrantColorPalette', union_mode='left_to_right')

class PlaylistCustomThumbnailRenderer(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    thumbnail: Thumbnail3 | Any = Field(default=None, union_mode='left_to_right')

class ThumbnailRenderer(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    playlist_custom_thumbnail_renderer: PlaylistCustomThumbnailRenderer | Any = Field(None, alias='playlistCustomThumbnailRenderer', union_mode='left_to_right')

class WebCommandMetadata3(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    url: str | Any = Field(default=None, union_mode='left_to_right')
    web_page_type: str | Any = Field(None, alias='webPageType', union_mode='left_to_right')
    root_ve: int | Any = Field(None, alias='rootVe', union_mode='left_to_right')
    api_url: str | Any = Field(None, alias='apiUrl', union_mode='left_to_right')

class CommandMetadata3(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    web_command_metadata: WebCommandMetadata3 | Any = Field(None, alias='webCommandMetadata', union_mode='left_to_right')

class NavigationEndpoint3(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    click_tracking_params: str | Any = Field(None, alias='clickTrackingParams', union_mode='left_to_right')
    command_metadata: CommandMetadata3 | Any = Field(None, alias='commandMetadata', union_mode='left_to_right')
    browse_endpoint: BrowseEndpoint | Any = Field(None, alias='browseEndpoint', union_mode='left_to_right')

class Run4(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    text: str | Any = Field(default=None, union_mode='left_to_right')
    navigation_endpoint: NavigationEndpoint3 | Any = Field(None, alias='navigationEndpoint', union_mode='left_to_right')

class LongBylineText(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    runs: list[Run4] | Any = Field(default=None, union_mode='left_to_right')

class Text(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    simple_text: str | Any = Field(None, alias='simpleText', union_mode='left_to_right')

class Icon(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    icon_type: str | Any = Field(None, alias='iconType', union_mode='left_to_right')

class ThumbnailOverlayBottomPanelRenderer(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    text: Text | Any = Field(default=None, union_mode='left_to_right')
    icon: Icon | Any = Field(default=None, union_mode='left_to_right')

class Run5(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    text: str | Any = Field(default=None, union_mode='left_to_right')

class Text1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    runs: list[Run5] | Any = Field(default=None, union_mode='left_to_right')

class ThumbnailOverlayHoverTextRenderer(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    text: Text1 | Any = Field(default=None, union_mode='left_to_right')
    icon: Icon | Any = Field(default=None, union_mode='left_to_right')

class Text2(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    runs: list[Run5] | Any = Field(default=None, union_mode='left_to_right')

class ThumbnailOverlayNowPlayingRenderer(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    text: Text2 | Any = Field(default=None, union_mode='left_to_right')

class ThumbnailOverlay(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    thumbnail_overlay_bottom_panel_renderer: ThumbnailOverlayBottomPanelRenderer | Any = Field(None, alias='thumbnailOverlayBottomPanelRenderer', union_mode='left_to_right')
    thumbnail_overlay_hover_text_renderer: ThumbnailOverlayHoverTextRenderer | Any = Field(None, alias='thumbnailOverlayHoverTextRenderer', union_mode='left_to_right')
    thumbnail_overlay_now_playing_renderer: ThumbnailOverlayNowPlayingRenderer | Any = Field(None, alias='thumbnailOverlayNowPlayingRenderer', union_mode='left_to_right')

class CommandMetadata4(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    web_command_metadata: WebCommandMetadata3 | Any = Field(None, alias='webCommandMetadata', union_mode='left_to_right')

class BrowseEndpoint2(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    browse_id: str | Any = Field(None, alias='browseId', union_mode='left_to_right')

class NavigationEndpoint4(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    click_tracking_params: str | Any = Field(None, alias='clickTrackingParams', union_mode='left_to_right')
    command_metadata: CommandMetadata4 | Any = Field(None, alias='commandMetadata', union_mode='left_to_right')
    browse_endpoint: BrowseEndpoint2 | Any = Field(None, alias='browseEndpoint', union_mode='left_to_right')

class Run7(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    text: str | Any = Field(default=None, union_mode='left_to_right')
    navigation_endpoint: NavigationEndpoint4 | Any = Field(None, alias='navigationEndpoint', union_mode='left_to_right')

class ViewPlaylistText(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    runs: list[Run7] | Any = Field(default=None, union_mode='left_to_right')

class GridPlaylistRenderer(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    playlist_id: str | Any = Field(None, alias='playlistId', union_mode='left_to_right')
    thumbnail: Thumbnail | Any = Field(default=None, union_mode='left_to_right')
    title: Title | Any = Field(default=None, union_mode='left_to_right')
    short_byline_text: ShortBylineText | Any = Field(None, alias='shortBylineText', union_mode='left_to_right')
    video_count_text: VideoCountText | Any = Field(None, alias='videoCountText', union_mode='left_to_right')
    navigation_endpoint: NavigationEndpoint2 | Any = Field(None, alias='navigationEndpoint', union_mode='left_to_right')
    video_count_short_text: VideoCountShortText | Any = Field(None, alias='videoCountShortText', union_mode='left_to_right')
    tracking_params: str | Any = Field(None, alias='trackingParams', union_mode='left_to_right')
    sidebar_thumbnails: list[SidebarThumbnail] | Any = Field(None, alias='sidebarThumbnails', union_mode='left_to_right')
    thumbnail_text: ThumbnailText | Any = Field(None, alias='thumbnailText', union_mode='left_to_right')
    thumbnail_renderer: ThumbnailRenderer | Any = Field(None, alias='thumbnailRenderer', union_mode='left_to_right')
    long_byline_text: LongBylineText | Any = Field(None, alias='longBylineText', union_mode='left_to_right')
    thumbnail_overlays: list[ThumbnailOverlay] | Any = Field(None, alias='thumbnailOverlays', union_mode='left_to_right')
    view_playlist_text: ViewPlaylistText | Any = Field(None, alias='viewPlaylistText', union_mode='left_to_right')

class WebCommandMetadata5(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    send_post: bool | Any = Field(None, alias='sendPost', union_mode='left_to_right')
    api_url: str | Any = Field(None, alias='apiUrl', union_mode='left_to_right')

class CommandMetadata5(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    web_command_metadata: WebCommandMetadata5 | Any = Field(None, alias='webCommandMetadata', union_mode='left_to_right')

class ContinuationCommand(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    token: str | Any = Field(default=None, union_mode='left_to_right')
    request: str | Any = Field(default=None, union_mode='left_to_right')

class ContinuationEndpoint(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    click_tracking_params: str | Any = Field(None, alias='clickTrackingParams', union_mode='left_to_right')
    command_metadata: CommandMetadata5 | Any = Field(None, alias='commandMetadata', union_mode='left_to_right')
    continuation_command: ContinuationCommand | Any = Field(None, alias='continuationCommand', union_mode='left_to_right')

class ContinuationItemRenderer(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    trigger: str | Any = Field(default=None, union_mode='left_to_right')
    continuation_endpoint: ContinuationEndpoint | Any = Field(None, alias='continuationEndpoint', union_mode='left_to_right')

class Item(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    grid_playlist_renderer: GridPlaylistRenderer | Any = Field(None, alias='gridPlaylistRenderer', union_mode='left_to_right')
    continuation_item_renderer: ContinuationItemRenderer | Any = Field(None, alias='continuationItemRenderer', union_mode='left_to_right')

class GridRenderer(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    items: list[Item] | Any = Field(default=None, union_mode='left_to_right')
    is_collapsible: bool | Any = Field(None, alias='isCollapsible', union_mode='left_to_right')
    tracking_params: str | Any = Field(None, alias='trackingParams', union_mode='left_to_right')
    target_id: UUID | Any = Field(None, alias='targetId', union_mode='left_to_right')

class ContinuationItem(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    grid_renderer: GridRenderer | Any = Field(None, alias='gridRenderer', union_mode='left_to_right')

class AppendContinuationItemsAction(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    continuation_items: list[ContinuationItem] | Any = Field(None, alias='continuationItems', union_mode='left_to_right')
    target_id: UUID | Any = Field(None, alias='targetId', union_mode='left_to_right')

class OnResponseReceivedEndpoint(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    click_tracking_params: str | Any = Field(None, alias='clickTrackingParams', union_mode='left_to_right')
    append_continuation_items_action: AppendContinuationItemsAction | Any = Field(None, alias='appendContinuationItemsAction', union_mode='left_to_right')

class WebCommandMetadata6(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    url: str | Any = Field(default=None, union_mode='left_to_right')
    web_page_type: str | Any = Field(None, alias='webPageType', union_mode='left_to_right')
    root_ve: int | Any = Field(None, alias='rootVe', union_mode='left_to_right')
    api_url: str | Any = Field(None, alias='apiUrl', union_mode='left_to_right')

class CommandMetadata6(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    web_command_metadata: WebCommandMetadata6 | Any = Field(None, alias='webCommandMetadata', union_mode='left_to_right')

class BrowseEndpoint3(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    browse_id: str | Any = Field(None, alias='browseId', union_mode='left_to_right')
    params: str | Any = Field(default=None, union_mode='left_to_right')
    canonical_base_url: str | Any = Field(None, alias='canonicalBaseUrl', union_mode='left_to_right')

class Endpoint(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    click_tracking_params: str | Any = Field(None, alias='clickTrackingParams', union_mode='left_to_right')
    command_metadata: CommandMetadata6 | Any = Field(None, alias='commandMetadata', union_mode='left_to_right')
    browse_endpoint: BrowseEndpoint3 | Any = Field(None, alias='browseEndpoint', union_mode='left_to_right')

class Title2(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    simple_text: str | Any = Field(None, alias='simpleText', union_mode='left_to_right')

class Accessibility(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    label: str | Any = Field(default=None, union_mode='left_to_right')

class AccessibilityData1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    label: str | Any = Field(default=None, union_mode='left_to_right')

class AccessibilityData(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    accessibility_data: AccessibilityData1 | Any = Field(None, alias='accessibilityData', union_mode='left_to_right')

class ChangeEngagementPanelVisibilityAction(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    target_id: UUID | Any = Field(None, alias='targetId', union_mode='left_to_right')
    visibility: str | Any = Field(default=None, union_mode='left_to_right')

class Command(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    click_tracking_params: str | Any = Field(None, alias='clickTrackingParams', union_mode='left_to_right')
    change_engagement_panel_visibility_action: ChangeEngagementPanelVisibilityAction | Any = Field(None, alias='changeEngagementPanelVisibilityAction', union_mode='left_to_right')

class ButtonRenderer(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    style: str | Any = Field(default=None, union_mode='left_to_right')
    size: str | Any = Field(default=None, union_mode='left_to_right')
    is_disabled: bool | Any = Field(None, alias='isDisabled', union_mode='left_to_right')
    icon: Icon | Any = Field(default=None, union_mode='left_to_right')
    accessibility: Accessibility | Any = Field(default=None, union_mode='left_to_right')
    tracking_params: str | Any = Field(None, alias='trackingParams', union_mode='left_to_right')
    accessibility_data: AccessibilityData | Any = Field(None, alias='accessibilityData', union_mode='left_to_right')
    command: Command | Any = Field(default=None, union_mode='left_to_right')

class VisibilityButton(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    button_renderer: ButtonRenderer | Any = Field(None, alias='buttonRenderer', union_mode='left_to_right')

class EngagementPanelTitleHeaderRenderer(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    title: Title2 | Any = Field(default=None, union_mode='left_to_right')
    visibility_button: VisibilityButton | Any = Field(None, alias='visibilityButton', union_mode='left_to_right')
    tracking_params: str | Any = Field(None, alias='trackingParams', union_mode='left_to_right')

class Header(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    engagement_panel_title_header_renderer: EngagementPanelTitleHeaderRenderer | Any = Field(None, alias='engagementPanelTitleHeaderRenderer', union_mode='left_to_right')

class WebCommandMetadata7(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    send_post: bool | Any = Field(None, alias='sendPost', union_mode='left_to_right')
    api_url: str | Any = Field(None, alias='apiUrl', union_mode='left_to_right')

class CommandMetadata7(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    web_command_metadata: WebCommandMetadata7 | Any = Field(None, alias='webCommandMetadata', union_mode='left_to_right')

class ContinuationEndpoint1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    click_tracking_params: str | Any = Field(None, alias='clickTrackingParams', union_mode='left_to_right')
    command_metadata: CommandMetadata7 | Any = Field(None, alias='commandMetadata', union_mode='left_to_right')
    continuation_command: ContinuationCommand | Any = Field(None, alias='continuationCommand', union_mode='left_to_right')

class ContinuationItemRenderer1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    trigger: str | Any = Field(default=None, union_mode='left_to_right')
    continuation_endpoint: ContinuationEndpoint1 | Any = Field(None, alias='continuationEndpoint', union_mode='left_to_right')

class Content5(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    continuation_item_renderer: ContinuationItemRenderer1 | Any = Field(None, alias='continuationItemRenderer', union_mode='left_to_right')

class ItemSectionRenderer1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    contents: list[Content5] | Any = Field(default=None, union_mode='left_to_right')
    tracking_params: str | Any = Field(None, alias='trackingParams', union_mode='left_to_right')
    section_identifier: UUID | Any = Field(None, alias='sectionIdentifier', union_mode='left_to_right')
    target_id: UUID | Any = Field(None, alias='targetId', union_mode='left_to_right')

class Content4(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    item_section_renderer: ItemSectionRenderer1 | Any = Field(None, alias='itemSectionRenderer', union_mode='left_to_right')

class ScrollPaneStyle(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    scrollable: bool | Any = Field(default=None, union_mode='left_to_right')

class SectionListRenderer1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    contents: list[Content4] | Any = Field(default=None, union_mode='left_to_right')
    tracking_params: str | Any = Field(None, alias='trackingParams', union_mode='left_to_right')
    scroll_pane_style: ScrollPaneStyle | Any = Field(None, alias='scrollPaneStyle', union_mode='left_to_right')

class Content3(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    section_list_renderer: SectionListRenderer1 | Any = Field(None, alias='sectionListRenderer', union_mode='left_to_right')

class Identifier(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    surface: str | Any = Field(default=None, union_mode='left_to_right')
    tag: UUID | Any = Field(default=None, union_mode='left_to_right')

class EngagementPanelSectionListRenderer(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    header: Header | Any = Field(default=None, union_mode='left_to_right')
    content: Content3 | Any = Field(default=None, union_mode='left_to_right')
    target_id: UUID | Any = Field(None, alias='targetId', union_mode='left_to_right')
    identifier: Identifier | Any = Field(default=None, union_mode='left_to_right')
    size: str | Any = Field(default=None, union_mode='left_to_right')

class EngagementPanel(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    engagement_panel_section_list_renderer: EngagementPanelSectionListRenderer | Any = Field(None, alias='engagementPanelSectionListRenderer', union_mode='left_to_right')

class EngagementPanelPopupPresentationConfig(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    popup_type: str | Any = Field(None, alias='popupType', union_mode='left_to_right')

class EngagementPanelPresentationConfigs(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    engagement_panel_popup_presentation_config: EngagementPanelPopupPresentationConfig | Any = Field(None, alias='engagementPanelPopupPresentationConfig', union_mode='left_to_right')

class ShowEngagementPanelEndpoint(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    engagement_panel: EngagementPanel | Any = Field(None, alias='engagementPanel', union_mode='left_to_right')
    identifier: Identifier | Any = Field(default=None, union_mode='left_to_right')
    engagement_panel_presentation_configs: EngagementPanelPresentationConfigs | Any = Field(None, alias='engagementPanelPresentationConfigs', union_mode='left_to_right')

class NavigationEndpoint5(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    click_tracking_params: str | Any = Field(None, alias='clickTrackingParams', union_mode='left_to_right')
    show_engagement_panel_endpoint: ShowEngagementPanelEndpoint | Any = Field(None, alias='showEngagementPanelEndpoint', union_mode='left_to_right')

class Run8(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    text: str | Any = Field(default=None, union_mode='left_to_right')
    navigation_endpoint: NavigationEndpoint5 | Any = Field(None, alias='navigationEndpoint', union_mode='left_to_right')

class Title1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    runs: list[Run8] | Any = Field(default=None, union_mode='left_to_right')

class Title3(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    simple_text: str | Any = Field(None, alias='simpleText', union_mode='left_to_right')

class AccessibilityData3(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    label: str | Any = Field(default=None, union_mode='left_to_right')

class AccessibilityData2(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    accessibility_data: AccessibilityData3 | Any = Field(None, alias='accessibilityData', union_mode='left_to_right')

class Command1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    click_tracking_params: str | Any = Field(None, alias='clickTrackingParams', union_mode='left_to_right')
    change_engagement_panel_visibility_action: ChangeEngagementPanelVisibilityAction | Any = Field(None, alias='changeEngagementPanelVisibilityAction', union_mode='left_to_right')

class ButtonRenderer1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    style: str | Any = Field(default=None, union_mode='left_to_right')
    size: str | Any = Field(default=None, union_mode='left_to_right')
    is_disabled: bool | Any = Field(None, alias='isDisabled', union_mode='left_to_right')
    icon: Icon | Any = Field(default=None, union_mode='left_to_right')
    accessibility: Accessibility | Any = Field(default=None, union_mode='left_to_right')
    tracking_params: str | Any = Field(None, alias='trackingParams', union_mode='left_to_right')
    accessibility_data: AccessibilityData2 | Any = Field(None, alias='accessibilityData', union_mode='left_to_right')
    command: Command1 | Any = Field(default=None, union_mode='left_to_right')

class VisibilityButton1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    button_renderer: ButtonRenderer1 | Any = Field(None, alias='buttonRenderer', union_mode='left_to_right')

class EngagementPanelTitleHeaderRenderer1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    title: Title3 | Any = Field(default=None, union_mode='left_to_right')
    visibility_button: VisibilityButton1 | Any = Field(None, alias='visibilityButton', union_mode='left_to_right')
    tracking_params: str | Any = Field(None, alias='trackingParams', union_mode='left_to_right')

class Header1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    engagement_panel_title_header_renderer: EngagementPanelTitleHeaderRenderer1 | Any = Field(None, alias='engagementPanelTitleHeaderRenderer', union_mode='left_to_right')

class CommandMetadata8(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    web_command_metadata: WebCommandMetadata7 | Any = Field(None, alias='webCommandMetadata', union_mode='left_to_right')

class ContinuationEndpoint2(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    click_tracking_params: str | Any = Field(None, alias='clickTrackingParams', union_mode='left_to_right')
    command_metadata: CommandMetadata8 | Any = Field(None, alias='commandMetadata', union_mode='left_to_right')
    continuation_command: ContinuationCommand | Any = Field(None, alias='continuationCommand', union_mode='left_to_right')

class ContinuationItemRenderer2(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    trigger: str | Any = Field(default=None, union_mode='left_to_right')
    continuation_endpoint: ContinuationEndpoint2 | Any = Field(None, alias='continuationEndpoint', union_mode='left_to_right')

class Content8(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    continuation_item_renderer: ContinuationItemRenderer2 | Any = Field(None, alias='continuationItemRenderer', union_mode='left_to_right')

class ItemSectionRenderer2(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    contents: list[Content8] | Any = Field(default=None, union_mode='left_to_right')
    tracking_params: str | Any = Field(None, alias='trackingParams', union_mode='left_to_right')
    section_identifier: UUID | Any = Field(None, alias='sectionIdentifier', union_mode='left_to_right')
    target_id: UUID | Any = Field(None, alias='targetId', union_mode='left_to_right')

class Content7(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    item_section_renderer: ItemSectionRenderer2 | Any = Field(None, alias='itemSectionRenderer', union_mode='left_to_right')

class SectionListRenderer2(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    contents: list[Content7] | Any = Field(default=None, union_mode='left_to_right')
    tracking_params: str | Any = Field(None, alias='trackingParams', union_mode='left_to_right')
    scroll_pane_style: ScrollPaneStyle | Any = Field(None, alias='scrollPaneStyle', union_mode='left_to_right')

class Content6(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    section_list_renderer: SectionListRenderer2 | Any = Field(None, alias='sectionListRenderer', union_mode='left_to_right')

class EngagementPanelSectionListRenderer1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    header: Header1 | Any = Field(default=None, union_mode='left_to_right')
    content: Content6 | Any = Field(default=None, union_mode='left_to_right')
    target_id: UUID | Any = Field(None, alias='targetId', union_mode='left_to_right')
    identifier: Identifier | Any = Field(default=None, union_mode='left_to_right')
    size: str | Any = Field(default=None, union_mode='left_to_right')

class EngagementPanel1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    engagement_panel_section_list_renderer: EngagementPanelSectionListRenderer1 | Any = Field(None, alias='engagementPanelSectionListRenderer', union_mode='left_to_right')

class EngagementPanelPresentationConfigs1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    engagement_panel_popup_presentation_config: EngagementPanelPopupPresentationConfig | Any = Field(None, alias='engagementPanelPopupPresentationConfig', union_mode='left_to_right')

class ShowEngagementPanelEndpoint1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    engagement_panel: EngagementPanel1 | Any = Field(None, alias='engagementPanel', union_mode='left_to_right')
    identifier: Identifier | Any = Field(default=None, union_mode='left_to_right')
    engagement_panel_presentation_configs: EngagementPanelPresentationConfigs1 | Any = Field(None, alias='engagementPanelPresentationConfigs', union_mode='left_to_right')

class Endpoint1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    click_tracking_params: str | Any = Field(None, alias='clickTrackingParams', union_mode='left_to_right')
    show_engagement_panel_endpoint: ShowEngagementPanelEndpoint1 | Any = Field(None, alias='showEngagementPanelEndpoint', union_mode='left_to_right')

class Source(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    url: str | Any = Field(default=None, union_mode='left_to_right')
    width: int | Any = Field(default=None, union_mode='left_to_right')
    height: int | Any = Field(default=None, union_mode='left_to_right')

class Image(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    sources: list[Source] | Any = Field(default=None, union_mode='left_to_right')

class ClientResource(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    image_name: str | Any = Field(None, alias='imageName', union_mode='left_to_right')

class Source1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    client_resource: ClientResource | Any = Field(None, alias='clientResource', union_mode='left_to_right')

class Icon4(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    sources: list[Source1] | Any = Field(default=None, union_mode='left_to_right')

class BackgroundColor(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    light_theme: int | Any = Field(None, alias='lightTheme', union_mode='left_to_right')
    dark_theme: int | Any = Field(None, alias='darkTheme', union_mode='left_to_right')

class ThumbnailBadgeViewModel(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    icon: Icon4 | Any = Field(default=None, union_mode='left_to_right')
    text: str | Any = Field(default=None, union_mode='left_to_right')
    badge_style: str | Any = Field(None, alias='badgeStyle', union_mode='left_to_right')
    background_color: BackgroundColor | Any = Field(None, alias='backgroundColor', union_mode='left_to_right')

class ThumbnailBadge(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    thumbnail_badge_view_model: ThumbnailBadgeViewModel | Any = Field(None, alias='thumbnailBadgeViewModel', union_mode='left_to_right')

class ThumbnailOverlayBadgeViewModel(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    thumbnail_badges: list[ThumbnailBadge] | Any = Field(None, alias='thumbnailBadges', union_mode='left_to_right')
    position: str | Any = Field(default=None, union_mode='left_to_right')

class Source2(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    client_resource: ClientResource | Any = Field(None, alias='clientResource', union_mode='left_to_right')

class Icon5(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    sources: list[Source2] | Any = Field(default=None, union_mode='left_to_right')

class StyleRun(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    start_index: int | Any = Field(None, alias='startIndex', union_mode='left_to_right')
    length: int | Any = Field(default=None, union_mode='left_to_right')

class Text3(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    content: str | Any = Field(default=None, union_mode='left_to_right')
    style_runs: list[StyleRun] | Any = Field(None, alias='styleRuns', union_mode='left_to_right')

class ThumbnailHoverOverlayViewModel(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    icon: Icon5 | Any = Field(default=None, union_mode='left_to_right')
    text: Text3 | Any = Field(default=None, union_mode='left_to_right')
    style: str | Any = Field(default=None, union_mode='left_to_right')

class Overlay(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    thumbnail_overlay_badge_view_model: ThumbnailOverlayBadgeViewModel | Any = Field(None, alias='thumbnailOverlayBadgeViewModel', union_mode='left_to_right')
    thumbnail_hover_overlay_view_model: ThumbnailHoverOverlayViewModel | Any = Field(None, alias='thumbnailHoverOverlayViewModel', union_mode='left_to_right')

class ThumbnailViewModel(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    image: Image | Any = Field(default=None, union_mode='left_to_right')
    overlays: list[Overlay] | Any = Field(default=None, union_mode='left_to_right')
    background_color: BackgroundColor | Any = Field(None, alias='backgroundColor', union_mode='left_to_right')

class PrimaryThumbnail(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    thumbnail_view_model: ThumbnailViewModel | Any = Field(None, alias='thumbnailViewModel', union_mode='left_to_right')

class StackColor(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    light_theme: int | Any = Field(None, alias='lightTheme', union_mode='left_to_right')
    dark_theme: int | Any = Field(None, alias='darkTheme', union_mode='left_to_right')

class CollectionThumbnailViewModel(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    primary_thumbnail: PrimaryThumbnail | Any = Field(None, alias='primaryThumbnail', union_mode='left_to_right')
    stack_color: StackColor | Any = Field(None, alias='stackColor', union_mode='left_to_right')

class ContentImage(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    collection_thumbnail_view_model: CollectionThumbnailViewModel | Any = Field(None, alias='collectionThumbnailViewModel', union_mode='left_to_right')

class Title4(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    content: str | Any = Field(default=None, union_mode='left_to_right')

class WebCommandMetadata9(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    url: str | Any = Field(default=None, union_mode='left_to_right')
    web_page_type: str | Any = Field(None, alias='webPageType', union_mode='left_to_right')
    root_ve: int | Any = Field(None, alias='rootVe', union_mode='left_to_right')
    api_url: str | Any = Field(None, alias='apiUrl', union_mode='left_to_right')

class CommandMetadata9(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    web_command_metadata: WebCommandMetadata9 | Any = Field(None, alias='webCommandMetadata', union_mode='left_to_right')

class BrowseEndpoint4(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    browse_id: str | Any = Field(None, alias='browseId', union_mode='left_to_right')
    canonical_base_url: str | Any = Field(None, alias='canonicalBaseUrl', union_mode='left_to_right')

class InnertubeCommand(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    click_tracking_params: str | Any = Field(None, alias='clickTrackingParams', union_mode='left_to_right')
    command_metadata: CommandMetadata9 | Any = Field(None, alias='commandMetadata', union_mode='left_to_right')
    browse_endpoint: BrowseEndpoint4 | Any = Field(None, alias='browseEndpoint', union_mode='left_to_right')

class OnTap(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    innertube_command: InnertubeCommand | Any = Field(None, alias='innertubeCommand', union_mode='left_to_right')

class CommandRun(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    start_index: int | Any = Field(None, alias='startIndex', union_mode='left_to_right')
    length: int | Any = Field(default=None, union_mode='left_to_right')
    on_tap: OnTap | Any = Field(None, alias='onTap', union_mode='left_to_right')

class StyleRun1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    start_index: int | Any = Field(None, alias='startIndex', union_mode='left_to_right')
    length: int | Any = Field(default=None, union_mode='left_to_right')
    weight_label: str | Any = Field(None, alias='weightLabel', union_mode='left_to_right')

class Text4(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    content: str | Any = Field(default=None, union_mode='left_to_right')
    command_runs: list[CommandRun] | Any = Field(None, alias='commandRuns', union_mode='left_to_right')
    style_runs: list[StyleRun1] | Any = Field(None, alias='styleRuns', union_mode='left_to_right')

class MetadataPart(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    text: Text4 | Any = Field(default=None, union_mode='left_to_right')

class MetadataRow(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    metadata_parts: list[MetadataPart] | Any = Field(None, alias='metadataParts', union_mode='left_to_right')

class ContentMetadataViewModel(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    metadata_rows: list[MetadataRow] | Any = Field(None, alias='metadataRows', union_mode='left_to_right')
    delimiter: str | Any = Field(default=None, union_mode='left_to_right')

class Metadata1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    content_metadata_view_model: ContentMetadataViewModel | Any = Field(None, alias='contentMetadataViewModel', union_mode='left_to_right')

class LockupMetadataViewModel(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    title: Title4 | Any = Field(default=None, union_mode='left_to_right')
    metadata: Metadata1 | Any = Field(default=None, union_mode='left_to_right')

class Metadata(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    lockup_metadata_view_model: LockupMetadataViewModel | Any = Field(None, alias='lockupMetadataViewModel', union_mode='left_to_right')

class WebCommandMetadata10(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    url: str | Any = Field(default=None, union_mode='left_to_right')
    web_page_type: str | Any = Field(None, alias='webPageType', union_mode='left_to_right')
    root_ve: int | Any = Field(None, alias='rootVe', union_mode='left_to_right')

class CommandMetadata10(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    web_command_metadata: WebCommandMetadata10 | Any = Field(None, alias='webCommandMetadata', union_mode='left_to_right')

class LoggingContext2(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    vss_logging_context: VssLoggingContext | Any = Field(None, alias='vssLoggingContext', union_mode='left_to_right')

class Html5PlaybackOnesieConfig2(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    common_config: CommonConfig | Any = Field(None, alias='commonConfig', union_mode='left_to_right')

class WatchEndpointSupportedOnesieConfig2(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    html5_playback_onesie_config: Html5PlaybackOnesieConfig2 | Any = Field(None, alias='html5PlaybackOnesieConfig', union_mode='left_to_right')

class WatchEndpoint2(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    video_id: str | Any = Field(None, alias='videoId', union_mode='left_to_right')
    playlist_id: str | Any = Field(None, alias='playlistId', union_mode='left_to_right')
    params: str | Any = Field(default=None, union_mode='left_to_right')
    logging_context: LoggingContext2 | Any = Field(None, alias='loggingContext', union_mode='left_to_right')
    watch_endpoint_supported_onesie_config: WatchEndpointSupportedOnesieConfig2 | Any = Field(None, alias='watchEndpointSupportedOnesieConfig', union_mode='left_to_right')
    player_params: str | Any = Field(None, alias='playerParams', union_mode='left_to_right')

class InnertubeCommand1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    click_tracking_params: str | Any = Field(None, alias='clickTrackingParams', union_mode='left_to_right')
    command_metadata: CommandMetadata10 | Any = Field(None, alias='commandMetadata', union_mode='left_to_right')
    watch_endpoint: WatchEndpoint2 | Any = Field(None, alias='watchEndpoint', union_mode='left_to_right')

class OnSelect(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    innertube_command: InnertubeCommand1 | Any = Field(None, alias='innertubeCommand', union_mode='left_to_right')

class CommandMetadata11(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    web_command_metadata: WebCommandMetadata10 | Any = Field(None, alias='webCommandMetadata', union_mode='left_to_right')

class LoggingContext3(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    vss_logging_context: VssLoggingContext | Any = Field(None, alias='vssLoggingContext', union_mode='left_to_right')

class Html5PlaybackOnesieConfig3(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    common_config: CommonConfig | Any = Field(None, alias='commonConfig', union_mode='left_to_right')

class WatchEndpointSupportedOnesieConfig3(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    html5_playback_onesie_config: Html5PlaybackOnesieConfig3 | Any = Field(None, alias='html5PlaybackOnesieConfig', union_mode='left_to_right')

class WatchEndpoint3(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    video_id: str | Any = Field(None, alias='videoId', union_mode='left_to_right')
    playlist_id: str | Any = Field(None, alias='playlistId', union_mode='left_to_right')
    player_params: str | Any = Field(None, alias='playerParams', union_mode='left_to_right')
    logging_context: LoggingContext3 | Any = Field(None, alias='loggingContext', union_mode='left_to_right')
    watch_endpoint_supported_onesie_config: WatchEndpointSupportedOnesieConfig3 | Any = Field(None, alias='watchEndpointSupportedOnesieConfig', union_mode='left_to_right')

class InnertubeCommand2(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    click_tracking_params: str | Any = Field(None, alias='clickTrackingParams', union_mode='left_to_right')
    command_metadata: CommandMetadata11 | Any = Field(None, alias='commandMetadata', union_mode='left_to_right')
    watch_endpoint: WatchEndpoint3 | Any = Field(None, alias='watchEndpoint', union_mode='left_to_right')

class OnVisible(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    innertube_command: InnertubeCommand2 | Any = Field(None, alias='innertubeCommand', union_mode='left_to_right')

class InlinePlayerData(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    on_select: OnSelect | Any = Field(None, alias='onSelect', union_mode='left_to_right')
    on_visible: OnVisible | Any = Field(None, alias='onVisible', union_mode='left_to_right')

class ItemPlayback(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    inline_player_data: InlinePlayerData | Any = Field(None, alias='inlinePlayerData', union_mode='left_to_right')

class Visibility(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    types: str | Any = Field(default=None, union_mode='left_to_right')

class LoggingDirectives(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    tracking_params: str | Any = Field(None, alias='trackingParams', union_mode='left_to_right')
    visibility: Visibility | Any = Field(default=None, union_mode='left_to_right')

class LoggingContext4(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    logging_directives: LoggingDirectives | Any = Field(None, alias='loggingDirectives', union_mode='left_to_right')

class CommandMetadata12(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    web_command_metadata: WebCommandMetadata10 | Any = Field(None, alias='webCommandMetadata', union_mode='left_to_right')

class LoggingContext5(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    vss_logging_context: VssLoggingContext | Any = Field(None, alias='vssLoggingContext', union_mode='left_to_right')

class Html5PlaybackOnesieConfig4(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    common_config: CommonConfig | Any = Field(None, alias='commonConfig', union_mode='left_to_right')

class WatchEndpointSupportedOnesieConfig4(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    html5_playback_onesie_config: Html5PlaybackOnesieConfig4 | Any = Field(None, alias='html5PlaybackOnesieConfig', union_mode='left_to_right')

class WatchEndpoint4(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    video_id: str | Any = Field(None, alias='videoId', union_mode='left_to_right')
    playlist_id: str | Any = Field(None, alias='playlistId', union_mode='left_to_right')
    params: str | Any = Field(default=None, union_mode='left_to_right')
    logging_context: LoggingContext5 | Any = Field(None, alias='loggingContext', union_mode='left_to_right')
    watch_endpoint_supported_onesie_config: WatchEndpointSupportedOnesieConfig4 | Any = Field(None, alias='watchEndpointSupportedOnesieConfig', union_mode='left_to_right')
    player_params: str | Any = Field(None, alias='playerParams', union_mode='left_to_right')

class InnertubeCommand3(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    click_tracking_params: str | Any = Field(None, alias='clickTrackingParams', union_mode='left_to_right')
    command_metadata: CommandMetadata12 | Any = Field(None, alias='commandMetadata', union_mode='left_to_right')
    watch_endpoint: WatchEndpoint4 | Any = Field(None, alias='watchEndpoint', union_mode='left_to_right')

class OnTap1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    innertube_command: InnertubeCommand3 | Any = Field(None, alias='innertubeCommand', union_mode='left_to_right')

class CommandContext(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    on_tap: OnTap1 | Any = Field(None, alias='onTap', union_mode='left_to_right')

class RendererContext(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    logging_context: LoggingContext4 | Any = Field(None, alias='loggingContext', union_mode='left_to_right')
    command_context: CommandContext | Any = Field(None, alias='commandContext', union_mode='left_to_right')

class LockupViewModel(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    content_image: ContentImage | Any = Field(None, alias='contentImage', union_mode='left_to_right')
    metadata: Metadata | Any = Field(default=None, union_mode='left_to_right')
    content_id: str | Any = Field(None, alias='contentId', union_mode='left_to_right')
    content_type: str | Any = Field(None, alias='contentType', union_mode='left_to_right')
    item_playback: ItemPlayback | Any = Field(None, alias='itemPlayback', union_mode='left_to_right')
    renderer_context: RendererContext | Any = Field(None, alias='rendererContext', union_mode='left_to_right')

class Item1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    lockup_view_model: LockupViewModel | Any = Field(None, alias='lockupViewModel', union_mode='left_to_right')

class Icon6(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    icon_type: str | Any = Field(None, alias='iconType', union_mode='left_to_right')

class ButtonRenderer2(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    style: str | Any = Field(default=None, union_mode='left_to_right')
    size: str | Any = Field(default=None, union_mode='left_to_right')
    is_disabled: bool | Any = Field(None, alias='isDisabled', union_mode='left_to_right')
    icon: Icon6 | Any = Field(default=None, union_mode='left_to_right')
    accessibility: Accessibility | Any = Field(default=None, union_mode='left_to_right')
    tracking_params: str | Any = Field(None, alias='trackingParams', union_mode='left_to_right')

class NextButton(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    button_renderer: ButtonRenderer2 | Any = Field(None, alias='buttonRenderer', union_mode='left_to_right')

class ButtonRenderer3(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    style: str | Any = Field(default=None, union_mode='left_to_right')
    size: str | Any = Field(default=None, union_mode='left_to_right')
    is_disabled: bool | Any = Field(None, alias='isDisabled', union_mode='left_to_right')
    icon: Icon6 | Any = Field(default=None, union_mode='left_to_right')
    accessibility: Accessibility | Any = Field(default=None, union_mode='left_to_right')
    tracking_params: str | Any = Field(None, alias='trackingParams', union_mode='left_to_right')

class PreviousButton(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    button_renderer: ButtonRenderer3 | Any = Field(None, alias='buttonRenderer', union_mode='left_to_right')

class HorizontalListRenderer(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    items: list[Item1] | Any = Field(default=None, union_mode='left_to_right')
    tracking_params: str | Any = Field(None, alias='trackingParams', union_mode='left_to_right')
    visible_item_count: int | Any = Field(None, alias='visibleItemCount', union_mode='left_to_right')
    next_button: NextButton | Any = Field(None, alias='nextButton', union_mode='left_to_right')
    previous_button: PreviousButton | Any = Field(None, alias='previousButton', union_mode='left_to_right')
    force16_by9_thumbnail_aspect_ratio: bool | Any = Field(None, alias='force16By9ThumbnailAspectRatio', union_mode='left_to_right')

class Content9(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    horizontal_list_renderer: HorizontalListRenderer | Any = Field(None, alias='horizontalListRenderer', union_mode='left_to_right')

class Text5(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    simple_text: str | Any = Field(None, alias='simpleText', union_mode='left_to_right')

class Title5(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    simple_text: str | Any = Field(None, alias='simpleText', union_mode='left_to_right')

class AccessibilityData5(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    label: str | Any = Field(default=None, union_mode='left_to_right')

class AccessibilityData4(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    accessibility_data: AccessibilityData5 | Any = Field(None, alias='accessibilityData', union_mode='left_to_right')

class Command2(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    click_tracking_params: str | Any = Field(None, alias='clickTrackingParams', union_mode='left_to_right')
    change_engagement_panel_visibility_action: ChangeEngagementPanelVisibilityAction | Any = Field(None, alias='changeEngagementPanelVisibilityAction', union_mode='left_to_right')

class ButtonRenderer5(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    style: str | Any = Field(default=None, union_mode='left_to_right')
    size: str | Any = Field(default=None, union_mode='left_to_right')
    is_disabled: bool | Any = Field(None, alias='isDisabled', union_mode='left_to_right')
    icon: Icon6 | Any = Field(default=None, union_mode='left_to_right')
    accessibility: Accessibility | Any = Field(default=None, union_mode='left_to_right')
    tracking_params: str | Any = Field(None, alias='trackingParams', union_mode='left_to_right')
    accessibility_data: AccessibilityData4 | Any = Field(None, alias='accessibilityData', union_mode='left_to_right')
    command: Command2 | Any = Field(default=None, union_mode='left_to_right')

class VisibilityButton2(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    button_renderer: ButtonRenderer5 | Any = Field(None, alias='buttonRenderer', union_mode='left_to_right')

class EngagementPanelTitleHeaderRenderer2(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    title: Title5 | Any = Field(default=None, union_mode='left_to_right')
    visibility_button: VisibilityButton2 | Any = Field(None, alias='visibilityButton', union_mode='left_to_right')
    tracking_params: str | Any = Field(None, alias='trackingParams', union_mode='left_to_right')

class Header2(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    engagement_panel_title_header_renderer: EngagementPanelTitleHeaderRenderer2 | Any = Field(None, alias='engagementPanelTitleHeaderRenderer', union_mode='left_to_right')

class WebCommandMetadata13(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    send_post: bool | Any = Field(None, alias='sendPost', union_mode='left_to_right')
    api_url: str | Any = Field(None, alias='apiUrl', union_mode='left_to_right')

class CommandMetadata13(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    web_command_metadata: WebCommandMetadata13 | Any = Field(None, alias='webCommandMetadata', union_mode='left_to_right')

class ContinuationEndpoint3(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    click_tracking_params: str | Any = Field(None, alias='clickTrackingParams', union_mode='left_to_right')
    command_metadata: CommandMetadata13 | Any = Field(None, alias='commandMetadata', union_mode='left_to_right')
    continuation_command: ContinuationCommand | Any = Field(None, alias='continuationCommand', union_mode='left_to_right')

class ContinuationItemRenderer3(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    trigger: str | Any = Field(default=None, union_mode='left_to_right')
    continuation_endpoint: ContinuationEndpoint3 | Any = Field(None, alias='continuationEndpoint', union_mode='left_to_right')

class Content12(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    continuation_item_renderer: ContinuationItemRenderer3 | Any = Field(None, alias='continuationItemRenderer', union_mode='left_to_right')

class ItemSectionRenderer3(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    contents: list[Content12] | Any = Field(default=None, union_mode='left_to_right')
    tracking_params: str | Any = Field(None, alias='trackingParams', union_mode='left_to_right')
    section_identifier: UUID | Any = Field(None, alias='sectionIdentifier', union_mode='left_to_right')
    target_id: UUID | Any = Field(None, alias='targetId', union_mode='left_to_right')

class Content11(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    item_section_renderer: ItemSectionRenderer3 | Any = Field(None, alias='itemSectionRenderer', union_mode='left_to_right')

class SectionListRenderer3(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    contents: list[Content11] | Any = Field(default=None, union_mode='left_to_right')
    tracking_params: str | Any = Field(None, alias='trackingParams', union_mode='left_to_right')
    scroll_pane_style: ScrollPaneStyle | Any = Field(None, alias='scrollPaneStyle', union_mode='left_to_right')

class Content10(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    section_list_renderer: SectionListRenderer3 | Any = Field(None, alias='sectionListRenderer', union_mode='left_to_right')

class EngagementPanelSectionListRenderer2(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    header: Header2 | Any = Field(default=None, union_mode='left_to_right')
    content: Content10 | Any = Field(default=None, union_mode='left_to_right')
    target_id: UUID | Any = Field(None, alias='targetId', union_mode='left_to_right')
    identifier: Identifier | Any = Field(default=None, union_mode='left_to_right')
    size: str | Any = Field(default=None, union_mode='left_to_right')

class EngagementPanel2(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    engagement_panel_section_list_renderer: EngagementPanelSectionListRenderer2 | Any = Field(None, alias='engagementPanelSectionListRenderer', union_mode='left_to_right')

class EngagementPanelPresentationConfigs2(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    engagement_panel_popup_presentation_config: EngagementPanelPopupPresentationConfig | Any = Field(None, alias='engagementPanelPopupPresentationConfig', union_mode='left_to_right')

class ShowEngagementPanelEndpoint2(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    engagement_panel: EngagementPanel2 | Any = Field(None, alias='engagementPanel', union_mode='left_to_right')
    identifier: Identifier | Any = Field(default=None, union_mode='left_to_right')
    engagement_panel_presentation_configs: EngagementPanelPresentationConfigs2 | Any = Field(None, alias='engagementPanelPresentationConfigs', union_mode='left_to_right')

class NavigationEndpoint6(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    click_tracking_params: str | Any = Field(None, alias='clickTrackingParams', union_mode='left_to_right')
    show_engagement_panel_endpoint: ShowEngagementPanelEndpoint2 | Any = Field(None, alias='showEngagementPanelEndpoint', union_mode='left_to_right')

class AccessibilityData7(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    label: str | Any = Field(default=None, union_mode='left_to_right')

class AccessibilityData6(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    accessibility_data: AccessibilityData7 | Any = Field(None, alias='accessibilityData', union_mode='left_to_right')

class ButtonRenderer4(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    style: str | Any = Field(default=None, union_mode='left_to_right')
    size: str | Any = Field(default=None, union_mode='left_to_right')
    is_disabled: bool | Any = Field(None, alias='isDisabled', union_mode='left_to_right')
    text: Text5 | Any = Field(default=None, union_mode='left_to_right')
    navigation_endpoint: NavigationEndpoint6 | Any = Field(None, alias='navigationEndpoint', union_mode='left_to_right')
    tracking_params: str | Any = Field(None, alias='trackingParams', union_mode='left_to_right')
    accessibility_data: AccessibilityData6 | Any = Field(None, alias='accessibilityData', union_mode='left_to_right')

class TopLevelButton(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    button_renderer: ButtonRenderer4 | Any = Field(None, alias='buttonRenderer', union_mode='left_to_right')

class MenuRenderer(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    tracking_params: str | Any = Field(None, alias='trackingParams', union_mode='left_to_right')
    top_level_buttons: list[TopLevelButton] | Any = Field(None, alias='topLevelButtons', union_mode='left_to_right')

class Menu(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    menu_renderer: MenuRenderer | Any = Field(None, alias='menuRenderer', union_mode='left_to_right')

class ShelfRenderer(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    title: Title1 | Any = Field(default=None, union_mode='left_to_right')
    endpoint: Endpoint1 | Any = Field(default=None, union_mode='left_to_right')
    content: Content9 | Any = Field(default=None, union_mode='left_to_right')
    tracking_params: str | Any = Field(None, alias='trackingParams', union_mode='left_to_right')
    menu: Menu | Any = Field(default=None, union_mode='left_to_right')

class Content2(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    shelf_renderer: ShelfRenderer | Any = Field(None, alias='shelfRenderer', union_mode='left_to_right')

class ItemSectionRenderer(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    contents: list[Content2] | Any = Field(default=None, union_mode='left_to_right')
    tracking_params: str | Any = Field(None, alias='trackingParams', union_mode='left_to_right')

class Content1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    item_section_renderer: ItemSectionRenderer | Any = Field(None, alias='itemSectionRenderer', union_mode='left_to_right')

class SectionListRenderer(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    contents: list[Content1] | Any = Field(default=None, union_mode='left_to_right')
    tracking_params: str | Any = Field(None, alias='trackingParams', union_mode='left_to_right')
    target_id: str | Any = Field(None, alias='targetId', union_mode='left_to_right')
    disable_pull_to_refresh: bool | Any = Field(None, alias='disablePullToRefresh', union_mode='left_to_right')

class Content(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    section_list_renderer: SectionListRenderer | Any = Field(None, alias='sectionListRenderer', union_mode='left_to_right')

class TabRenderer(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    endpoint: Endpoint | Any = Field(default=None, union_mode='left_to_right')
    title: str | Any = Field(default=None, union_mode='left_to_right')
    selected: bool | Any = Field(default=None, union_mode='left_to_right')
    content: Content | Any = Field(default=None, union_mode='left_to_right')
    tracking_params: str | Any = Field(None, alias='trackingParams', union_mode='left_to_right')

class Tab(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    tab_renderer: TabRenderer | Any = Field(None, alias='tabRenderer', union_mode='left_to_right')

class TwoColumnBrowseResultsRenderer(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    tabs: list[Tab] | Any = Field(default=None, union_mode='left_to_right')

class Contents(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    two_column_browse_results_renderer: TwoColumnBrowseResultsRenderer | Any = Field(None, alias='twoColumnBrowseResultsRenderer', union_mode='left_to_right')

class Text6(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    content: str | Any = Field(default=None, union_mode='left_to_right')

class LoggingDirectives1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    tracking_params: str | Any = Field(None, alias='trackingParams', union_mode='left_to_right')
    visibility: Visibility | Any = Field(default=None, union_mode='left_to_right')

class LoggingContext6(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    logging_directives: LoggingDirectives1 | Any = Field(None, alias='loggingDirectives', union_mode='left_to_right')

class RendererContext1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    logging_context: LoggingContext6 | Any = Field(None, alias='loggingContext', union_mode='left_to_right')

class DynamicTextViewModel(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    text: Text6 | Any = Field(default=None, union_mode='left_to_right')
    max_lines: int | Any = Field(None, alias='maxLines', union_mode='left_to_right')
    renderer_context: RendererContext1 | Any = Field(None, alias='rendererContext', union_mode='left_to_right')

class Title6(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    dynamic_text_view_model: DynamicTextViewModel | Any = Field(None, alias='dynamicTextViewModel', union_mode='left_to_right')

class Source3(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    url: str | Any = Field(default=None, union_mode='left_to_right')
    width: int | Any = Field(default=None, union_mode='left_to_right')
    height: int | Any = Field(default=None, union_mode='left_to_right')

class BorderImageProcessor(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    circular: bool | Any = Field(default=None, union_mode='left_to_right')

class Processor(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    border_image_processor: BorderImageProcessor | Any = Field(None, alias='borderImageProcessor', union_mode='left_to_right')

class Image2(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    sources: list[Source3] | Any = Field(default=None, union_mode='left_to_right')
    processor: Processor | Any = Field(default=None, union_mode='left_to_right')

class LoggingDirectives2(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    tracking_params: str | Any = Field(None, alias='trackingParams', union_mode='left_to_right')
    visibility: Visibility | Any = Field(default=None, union_mode='left_to_right')

class AvatarViewModel(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    image: Image2 | Any = Field(default=None, union_mode='left_to_right')
    avatar_image_size: str | Any = Field(None, alias='avatarImageSize', union_mode='left_to_right')
    logging_directives: LoggingDirectives2 | Any = Field(None, alias='loggingDirectives', union_mode='left_to_right')

class Avatar(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    avatar_view_model: AvatarViewModel | Any = Field(None, alias='avatarViewModel', union_mode='left_to_right')

class DecoratedAvatarViewModel(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    avatar: Avatar | Any = Field(default=None, union_mode='left_to_right')

class Image1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    decorated_avatar_view_model: DecoratedAvatarViewModel | Any = Field(None, alias='decoratedAvatarViewModel', union_mode='left_to_right')

class StyleRun2(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    start_index: int | Any = Field(None, alias='startIndex', union_mode='left_to_right')
    length: int | Any = Field(default=None, union_mode='left_to_right')

class Text7(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    content: str | Any = Field(default=None, union_mode='left_to_right')
    style_runs: list[StyleRun2] | Any = Field(None, alias='styleRuns', union_mode='left_to_right')

class MetadataPart1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    text: Text7 | Any = Field(default=None, union_mode='left_to_right')

class MetadataRow1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    metadata_parts: list[MetadataPart1] | Any = Field(None, alias='metadataParts', union_mode='left_to_right')

class LoggingDirectives3(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    tracking_params: str | Any = Field(None, alias='trackingParams', union_mode='left_to_right')
    visibility: Visibility | Any = Field(default=None, union_mode='left_to_right')

class LoggingContext7(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    logging_directives: LoggingDirectives3 | Any = Field(None, alias='loggingDirectives', union_mode='left_to_right')

class RendererContext2(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    logging_context: LoggingContext7 | Any = Field(None, alias='loggingContext', union_mode='left_to_right')

class ContentMetadataViewModel1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    metadata_rows: list[MetadataRow1] | Any = Field(None, alias='metadataRows', union_mode='left_to_right')
    delimiter: str | Any = Field(default=None, union_mode='left_to_right')
    renderer_context: RendererContext2 | Any = Field(None, alias='rendererContext', union_mode='left_to_right')

class Metadata2(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    content_metadata_view_model: ContentMetadataViewModel1 | Any = Field(None, alias='contentMetadataViewModel', union_mode='left_to_right')

class Description1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    content: str | Any = Field(default=None, union_mode='left_to_right')

class StyleRun3(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    start_index: int | Any = Field(None, alias='startIndex', union_mode='left_to_right')
    length: int | Any = Field(default=None, union_mode='left_to_right')
    weight: int | Any = Field(default=None, union_mode='left_to_right')

class TruncationText(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    content: str | Any = Field(default=None, union_mode='left_to_right')
    style_runs: list[StyleRun3] | Any = Field(None, alias='styleRuns', union_mode='left_to_right')

class LoggingDirectives4(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    tracking_params: str | Any = Field(None, alias='trackingParams', union_mode='left_to_right')
    visibility: Visibility | Any = Field(default=None, union_mode='left_to_right')

class LoggingContext8(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    logging_directives: LoggingDirectives4 | Any = Field(None, alias='loggingDirectives', union_mode='left_to_right')

class AccessibilityContext(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    label: str | Any = Field(default=None, union_mode='left_to_right')

class Title7(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    simple_text: str | Any = Field(None, alias='simpleText', union_mode='left_to_right')

class AccessibilityData9(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    label: str | Any = Field(default=None, union_mode='left_to_right')

class AccessibilityData8(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    accessibility_data: AccessibilityData9 | Any = Field(None, alias='accessibilityData', union_mode='left_to_right')

class Command3(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    click_tracking_params: str | Any = Field(None, alias='clickTrackingParams', union_mode='left_to_right')
    change_engagement_panel_visibility_action: ChangeEngagementPanelVisibilityAction | Any = Field(None, alias='changeEngagementPanelVisibilityAction', union_mode='left_to_right')

class ButtonRenderer6(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    style: str | Any = Field(default=None, union_mode='left_to_right')
    size: str | Any = Field(default=None, union_mode='left_to_right')
    is_disabled: bool | Any = Field(None, alias='isDisabled', union_mode='left_to_right')
    icon: Icon6 | Any = Field(default=None, union_mode='left_to_right')
    accessibility: Accessibility | Any = Field(default=None, union_mode='left_to_right')
    tracking_params: str | Any = Field(None, alias='trackingParams', union_mode='left_to_right')
    accessibility_data: AccessibilityData8 | Any = Field(None, alias='accessibilityData', union_mode='left_to_right')
    command: Command3 | Any = Field(default=None, union_mode='left_to_right')

class VisibilityButton3(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    button_renderer: ButtonRenderer6 | Any = Field(None, alias='buttonRenderer', union_mode='left_to_right')

class EngagementPanelTitleHeaderRenderer3(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    title: Title7 | Any = Field(default=None, union_mode='left_to_right')
    visibility_button: VisibilityButton3 | Any = Field(None, alias='visibilityButton', union_mode='left_to_right')
    tracking_params: str | Any = Field(None, alias='trackingParams', union_mode='left_to_right')

class Header4(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    engagement_panel_title_header_renderer: EngagementPanelTitleHeaderRenderer3 | Any = Field(None, alias='engagementPanelTitleHeaderRenderer', union_mode='left_to_right')

class CommandMetadata14(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    web_command_metadata: WebCommandMetadata13 | Any = Field(None, alias='webCommandMetadata', union_mode='left_to_right')

class ContinuationEndpoint4(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    click_tracking_params: str | Any = Field(None, alias='clickTrackingParams', union_mode='left_to_right')
    command_metadata: CommandMetadata14 | Any = Field(None, alias='commandMetadata', union_mode='left_to_right')
    continuation_command: ContinuationCommand | Any = Field(None, alias='continuationCommand', union_mode='left_to_right')

class ContinuationItemRenderer4(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    trigger: str | Any = Field(default=None, union_mode='left_to_right')
    continuation_endpoint: ContinuationEndpoint4 | Any = Field(None, alias='continuationEndpoint', union_mode='left_to_right')

class Content16(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    continuation_item_renderer: ContinuationItemRenderer4 | Any = Field(None, alias='continuationItemRenderer', union_mode='left_to_right')

class ItemSectionRenderer4(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    contents: list[Content16] | Any = Field(default=None, union_mode='left_to_right')
    tracking_params: str | Any = Field(None, alias='trackingParams', union_mode='left_to_right')
    section_identifier: UUID | Any = Field(None, alias='sectionIdentifier', union_mode='left_to_right')
    target_id: UUID | Any = Field(None, alias='targetId', union_mode='left_to_right')

class Content15(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    item_section_renderer: ItemSectionRenderer4 | Any = Field(None, alias='itemSectionRenderer', union_mode='left_to_right')

class SectionListRenderer4(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    contents: list[Content15] | Any = Field(default=None, union_mode='left_to_right')
    tracking_params: str | Any = Field(None, alias='trackingParams', union_mode='left_to_right')
    scroll_pane_style: ScrollPaneStyle | Any = Field(None, alias='scrollPaneStyle', union_mode='left_to_right')

class Content14(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    section_list_renderer: SectionListRenderer4 | Any = Field(None, alias='sectionListRenderer', union_mode='left_to_right')

class EngagementPanelSectionListRenderer3(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    header: Header4 | Any = Field(default=None, union_mode='left_to_right')
    content: Content14 | Any = Field(default=None, union_mode='left_to_right')
    target_id: UUID | Any = Field(None, alias='targetId', union_mode='left_to_right')
    identifier: Identifier | Any = Field(default=None, union_mode='left_to_right')

class EngagementPanel3(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    engagement_panel_section_list_renderer: EngagementPanelSectionListRenderer3 | Any = Field(None, alias='engagementPanelSectionListRenderer', union_mode='left_to_right')

class EngagementPanelPresentationConfigs3(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    engagement_panel_popup_presentation_config: EngagementPanelPopupPresentationConfig | Any = Field(None, alias='engagementPanelPopupPresentationConfig', union_mode='left_to_right')

class ShowEngagementPanelEndpoint3(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    engagement_panel: EngagementPanel3 | Any = Field(None, alias='engagementPanel', union_mode='left_to_right')
    identifier: Identifier | Any = Field(default=None, union_mode='left_to_right')
    engagement_panel_presentation_configs: EngagementPanelPresentationConfigs3 | Any = Field(None, alias='engagementPanelPresentationConfigs', union_mode='left_to_right')

class InnertubeCommand4(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    click_tracking_params: str | Any = Field(None, alias='clickTrackingParams', union_mode='left_to_right')
    show_engagement_panel_endpoint: ShowEngagementPanelEndpoint3 | Any = Field(None, alias='showEngagementPanelEndpoint', union_mode='left_to_right')

class OnTap2(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    innertube_command: InnertubeCommand4 | Any = Field(None, alias='innertubeCommand', union_mode='left_to_right')

class CommandContext1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    on_tap: OnTap2 | Any = Field(None, alias='onTap', union_mode='left_to_right')

class RendererContext3(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    logging_context: LoggingContext8 | Any = Field(None, alias='loggingContext', union_mode='left_to_right')
    accessibility_context: AccessibilityContext | Any = Field(None, alias='accessibilityContext', union_mode='left_to_right')
    command_context: CommandContext1 | Any = Field(None, alias='commandContext', union_mode='left_to_right')

class DescriptionPreviewViewModel(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    description: Description1 | Any = Field(default=None, union_mode='left_to_right')
    max_lines: int | Any = Field(None, alias='maxLines', union_mode='left_to_right')
    truncation_text: TruncationText | Any = Field(None, alias='truncationText', union_mode='left_to_right')
    always_show_truncation_text: bool | Any = Field(None, alias='alwaysShowTruncationText', union_mode='left_to_right')
    renderer_context: RendererContext3 | Any = Field(None, alias='rendererContext', union_mode='left_to_right')

class Description(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    description_preview_view_model: DescriptionPreviewViewModel | Any = Field(None, alias='descriptionPreviewViewModel', union_mode='left_to_right')

class WebCommandMetadata15(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    url: str | Any = Field(default=None, union_mode='left_to_right')
    web_page_type: str | Any = Field(None, alias='webPageType', union_mode='left_to_right')
    root_ve: int | Any = Field(None, alias='rootVe', union_mode='left_to_right')

class CommandMetadata15(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    web_command_metadata: WebCommandMetadata15 | Any = Field(None, alias='webCommandMetadata', union_mode='left_to_right')

class UrlEndpoint(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    url: str | Any = Field(default=None, union_mode='left_to_right')
    target: str | Any = Field(default=None, union_mode='left_to_right')

class InnertubeCommand5(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    click_tracking_params: str | Any = Field(None, alias='clickTrackingParams', union_mode='left_to_right')
    command_metadata: CommandMetadata15 | Any = Field(None, alias='commandMetadata', union_mode='left_to_right')
    url_endpoint: UrlEndpoint | Any = Field(None, alias='urlEndpoint', union_mode='left_to_right')

class OnTap3(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    innertube_command: InnertubeCommand5 | Any = Field(None, alias='innertubeCommand', union_mode='left_to_right')

class LoggingDirectives5(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    tracking_params: str | Any = Field(None, alias='trackingParams', union_mode='left_to_right')
    visibility: Visibility | Any = Field(default=None, union_mode='left_to_right')

class CommandRun1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    start_index: int | Any = Field(None, alias='startIndex', union_mode='left_to_right')
    length: int | Any = Field(default=None, union_mode='left_to_right')
    on_tap: OnTap3 | Any = Field(None, alias='onTap', union_mode='left_to_right')
    logging_directives: LoggingDirectives5 | Any = Field(None, alias='loggingDirectives', union_mode='left_to_right')

class ColorMapItem(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    key: str | Any = Field(default=None, union_mode='left_to_right')
    value: int | Any = Field(default=None, union_mode='left_to_right')

class StyleRunColorMapExtension(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    color_map: list[ColorMapItem] | Any = Field(None, alias='colorMap', union_mode='left_to_right')

class StyleRunExtensions(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    style_run_color_map_extension: StyleRunColorMapExtension | Any = Field(None, alias='styleRunColorMapExtension', union_mode='left_to_right')

class StyleRun4(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    weight_label: str | Any = Field(None, alias='weightLabel', union_mode='left_to_right')
    style_run_extensions: StyleRunExtensions | Any = Field(None, alias='styleRunExtensions', union_mode='left_to_right')

class ClientResource2(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    icon: str | Any = Field(default=None, union_mode='left_to_right')

class YoutubeIconSource(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    client_resource: ClientResource2 | Any = Field(None, alias='clientResource', union_mode='left_to_right')

class CustomImageSource(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    youtube_icon_source: YoutubeIconSource | Any = Field(None, alias='youtubeIconSource', union_mode='left_to_right')

class Source4(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    custom_image_source: CustomImageSource | Any = Field(None, alias='customImageSource', union_mode='left_to_right')

class Image3(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    sources: list[Source4] | Any = Field(default=None, union_mode='left_to_right')

class ImageType(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    image: Image3 | Any = Field(default=None, union_mode='left_to_right')

class Type(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    image_type: ImageType | Any = Field(None, alias='imageType', union_mode='left_to_right')

class Height(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    value: int | Any = Field(default=None, union_mode='left_to_right')
    unit: str | Any = Field(default=None, union_mode='left_to_right')

class Width(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    value: int | Any = Field(default=None, union_mode='left_to_right')
    unit: str | Any = Field(default=None, union_mode='left_to_right')

class LayoutProperties(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    height: Height | Any = Field(default=None, union_mode='left_to_right')
    width: Width | Any = Field(default=None, union_mode='left_to_right')

class Properties(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    layout_properties: LayoutProperties | Any = Field(None, alias='layoutProperties', union_mode='left_to_right')

class Element(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    type: Type | Any = Field(default=None, union_mode='left_to_right')
    properties: Properties | Any = Field(default=None, union_mode='left_to_right')

class AttachmentRun(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    start_index: int | Any = Field(None, alias='startIndex', union_mode='left_to_right')
    length: int | Any = Field(default=None, union_mode='left_to_right')
    element: Element | Any = Field(default=None, union_mode='left_to_right')
    alignment: str | Any = Field(default=None, union_mode='left_to_right')

class Text8(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    content: str | Any = Field(default=None, union_mode='left_to_right')
    command_runs: list[CommandRun1] | Any = Field(None, alias='commandRuns', union_mode='left_to_right')
    style_runs: list[StyleRun4] | Any = Field(None, alias='styleRuns', union_mode='left_to_right')
    attachment_runs: list[AttachmentRun] | Any = Field(None, alias='attachmentRuns', union_mode='left_to_right')

class LoggingDirectives6(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    tracking_params: str | Any = Field(None, alias='trackingParams', union_mode='left_to_right')
    visibility: Visibility | Any = Field(default=None, union_mode='left_to_right')

class LoggingContext9(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    logging_directives: LoggingDirectives6 | Any = Field(None, alias='loggingDirectives', union_mode='left_to_right')

class RendererContext4(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    logging_context: LoggingContext9 | Any = Field(None, alias='loggingContext', union_mode='left_to_right')

class AttributionViewModel(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    text: Text8 | Any = Field(default=None, union_mode='left_to_right')
    renderer_context: RendererContext4 | Any = Field(None, alias='rendererContext', union_mode='left_to_right')

class Attribution(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    attribution_view_model: AttributionViewModel | Any = Field(None, alias='attributionViewModel', union_mode='left_to_right')

class Source5(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    url: str | Any = Field(default=None, union_mode='left_to_right')
    width: int | Any = Field(default=None, union_mode='left_to_right')
    height: int | Any = Field(default=None, union_mode='left_to_right')

class Image4(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    sources: list[Source5] | Any = Field(default=None, union_mode='left_to_right')

class LoggingDirectives7(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    tracking_params: str | Any = Field(None, alias='trackingParams', union_mode='left_to_right')
    visibility: Visibility | Any = Field(default=None, union_mode='left_to_right')

class LoggingContext10(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    logging_directives: LoggingDirectives7 | Any = Field(None, alias='loggingDirectives', union_mode='left_to_right')

class RendererContext5(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    logging_context: LoggingContext10 | Any = Field(None, alias='loggingContext', union_mode='left_to_right')

class ImageBannerViewModel(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    image: Image4 | Any = Field(default=None, union_mode='left_to_right')
    style: str | Any = Field(default=None, union_mode='left_to_right')
    renderer_context: RendererContext5 | Any = Field(None, alias='rendererContext', union_mode='left_to_right')

class Banner(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    image_banner_view_model: ImageBannerViewModel | Any = Field(None, alias='imageBannerViewModel', union_mode='left_to_right')

class LoggingDirectives8(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    tracking_params: str | Any = Field(None, alias='trackingParams', union_mode='left_to_right')
    visibility: Visibility | Any = Field(default=None, union_mode='left_to_right')

class LoggingContext11(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    logging_directives: LoggingDirectives8 | Any = Field(None, alias='loggingDirectives', union_mode='left_to_right')

class RendererContext6(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    logging_context: LoggingContext11 | Any = Field(None, alias='loggingContext', union_mode='left_to_right')

class PageHeaderViewModel(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    title: Title6 | Any = Field(default=None, union_mode='left_to_right')
    image: Image1 | Any = Field(default=None, union_mode='left_to_right')
    metadata: Metadata2 | Any = Field(default=None, union_mode='left_to_right')
    description: Description | Any = Field(default=None, union_mode='left_to_right')
    attribution: Attribution | Any = Field(default=None, union_mode='left_to_right')
    banner: Banner | Any = Field(default=None, union_mode='left_to_right')
    renderer_context: RendererContext6 | Any = Field(None, alias='rendererContext', union_mode='left_to_right')

class Content13(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    page_header_view_model: PageHeaderViewModel | Any = Field(None, alias='pageHeaderViewModel', union_mode='left_to_right')

class PageHeaderRenderer(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    page_title: str | Any = Field(None, alias='pageTitle', union_mode='left_to_right')
    content: Content13 | Any = Field(default=None, union_mode='left_to_right')

class Header3(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    page_header_renderer: PageHeaderRenderer | Any = Field(None, alias='pageHeaderRenderer', union_mode='left_to_right')

class Thumbnail5(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    url: str | Any = Field(default=None, union_mode='left_to_right')
    width: int | Any = Field(default=None, union_mode='left_to_right')
    height: int | Any = Field(default=None, union_mode='left_to_right')

class Avatar1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    thumbnails: list[Thumbnail5] | Any = Field(default=None, union_mode='left_to_right')

class ChannelMetadataRenderer(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    title: str | Any = Field(default=None, union_mode='left_to_right')
    description: str | Any = Field(default=None, union_mode='left_to_right')
    rss_url: str | Any = Field(None, alias='rssUrl', union_mode='left_to_right')
    external_id: str | Any = Field(None, alias='externalId', union_mode='left_to_right')
    keywords: str | Any = Field(default=None, union_mode='left_to_right')
    owner_urls: list[str] | Any = Field(None, alias='ownerUrls', union_mode='left_to_right')
    avatar: Avatar1 | Any = Field(default=None, union_mode='left_to_right')
    channel_url: str | Any = Field(None, alias='channelUrl', union_mode='left_to_right')
    is_family_safe: bool | Any = Field(None, alias='isFamilySafe', union_mode='left_to_right')
    available_country_codes: list[str] | Any = Field(None, alias='availableCountryCodes', union_mode='left_to_right')
    music_artist_name: str | Any = Field(None, alias='musicArtistName', union_mode='left_to_right')
    android_deep_link: str | Any = Field(None, alias='androidDeepLink', union_mode='left_to_right')
    android_appindexing_link: str | Any = Field(None, alias='androidAppindexingLink', union_mode='left_to_right')
    ios_appindexing_link: str | Any = Field(None, alias='iosAppindexingLink', union_mode='left_to_right')
    vanity_channel_url: str | Any = Field(None, alias='vanityChannelUrl', union_mode='left_to_right')

class Metadata3(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    channel_metadata_renderer: ChannelMetadataRenderer | Any = Field(None, alias='channelMetadataRenderer', union_mode='left_to_right')

class IconImage(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    icon_type: str | Any = Field(None, alias='iconType', union_mode='left_to_right')

class Run9(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    text: str | Any = Field(default=None, union_mode='left_to_right')

class TooltipText(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    runs: list[Run9] | Any = Field(default=None, union_mode='left_to_right')

class WebCommandMetadata16(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    url: str | Any = Field(default=None, union_mode='left_to_right')
    web_page_type: str | Any = Field(None, alias='webPageType', union_mode='left_to_right')
    root_ve: int | Any = Field(None, alias='rootVe', union_mode='left_to_right')
    api_url: str | Any = Field(None, alias='apiUrl', union_mode='left_to_right')

class CommandMetadata16(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    web_command_metadata: WebCommandMetadata16 | Any = Field(None, alias='webCommandMetadata', union_mode='left_to_right')

class BrowseEndpoint5(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    browse_id: str | Any = Field(None, alias='browseId', union_mode='left_to_right')

class Endpoint2(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    click_tracking_params: str | Any = Field(None, alias='clickTrackingParams', union_mode='left_to_right')
    command_metadata: CommandMetadata16 | Any = Field(None, alias='commandMetadata', union_mode='left_to_right')
    browse_endpoint: BrowseEndpoint5 | Any = Field(None, alias='browseEndpoint', union_mode='left_to_right')

class TopbarLogoRenderer(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    icon_image: IconImage | Any = Field(None, alias='iconImage', union_mode='left_to_right')
    tooltip_text: TooltipText | Any = Field(None, alias='tooltipText', union_mode='left_to_right')
    endpoint: Endpoint2 | Any = Field(default=None, union_mode='left_to_right')
    tracking_params: str | Any = Field(None, alias='trackingParams', union_mode='left_to_right')
    override_entity_key: str | Any = Field(None, alias='overrideEntityKey', union_mode='left_to_right')

class Logo(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    topbar_logo_renderer: TopbarLogoRenderer | Any = Field(None, alias='topbarLogoRenderer', union_mode='left_to_right')

class PlaceholderText(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    runs: list[Run9] | Any = Field(default=None, union_mode='left_to_right')

class WebSearchboxConfig(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    request_language: str | Any = Field(None, alias='requestLanguage', union_mode='left_to_right')
    request_domain: str | Any = Field(None, alias='requestDomain', union_mode='left_to_right')
    has_onscreen_keyboard: bool | Any = Field(None, alias='hasOnscreenKeyboard', union_mode='left_to_right')
    focus_searchbox: bool | Any = Field(None, alias='focusSearchbox', union_mode='left_to_right')

class Config(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    web_searchbox_config: WebSearchboxConfig | Any = Field(None, alias='webSearchboxConfig', union_mode='left_to_right')

class WebCommandMetadata17(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    url: str | Any = Field(default=None, union_mode='left_to_right')
    web_page_type: str | Any = Field(None, alias='webPageType', union_mode='left_to_right')
    root_ve: int | Any = Field(None, alias='rootVe', union_mode='left_to_right')

class CommandMetadata17(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    web_command_metadata: WebCommandMetadata17 | Any = Field(None, alias='webCommandMetadata', union_mode='left_to_right')

class SearchEndpoint1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    query: str | Any = Field(default=None, union_mode='left_to_right')

class SearchEndpoint(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    click_tracking_params: str | Any = Field(None, alias='clickTrackingParams', union_mode='left_to_right')
    command_metadata: CommandMetadata17 | Any = Field(None, alias='commandMetadata', union_mode='left_to_right')
    search_endpoint: SearchEndpoint1 | Any = Field(None, alias='searchEndpoint', union_mode='left_to_right')

class AccessibilityData11(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    label: str | Any = Field(default=None, union_mode='left_to_right')

class AccessibilityData10(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    accessibility_data: AccessibilityData11 | Any = Field(None, alias='accessibilityData', union_mode='left_to_right')

class ButtonRenderer7(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    style: str | Any = Field(default=None, union_mode='left_to_right')
    size: str | Any = Field(default=None, union_mode='left_to_right')
    is_disabled: bool | Any = Field(None, alias='isDisabled', union_mode='left_to_right')
    icon: Icon6 | Any = Field(default=None, union_mode='left_to_right')
    tracking_params: str | Any = Field(None, alias='trackingParams', union_mode='left_to_right')
    accessibility_data: AccessibilityData10 | Any = Field(None, alias='accessibilityData', union_mode='left_to_right')

class ClearButton(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    button_renderer: ButtonRenderer7 | Any = Field(None, alias='buttonRenderer', union_mode='left_to_right')

class Headline(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    content: str | Any = Field(default=None, union_mode='left_to_right')

class DialogHeaderViewModel(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    headline: Headline | Any = Field(default=None, union_mode='left_to_right')

class Header5(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    dialog_header_view_model: DialogHeaderViewModel | Any = Field(None, alias='dialogHeaderViewModel', union_mode='left_to_right')

class ButtonViewModel(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    title: str | Any = Field(default=None, union_mode='left_to_right')
    style: str | Any = Field(default=None, union_mode='left_to_right')
    tracking_params: str | Any = Field(None, alias='trackingParams', union_mode='left_to_right')
    is_full_width: bool | Any = Field(None, alias='isFullWidth', union_mode='left_to_right')
    type: str | Any = Field(default=None, union_mode='left_to_right')

class PrimaryButton(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    button_view_model: ButtonViewModel | Any = Field(None, alias='buttonViewModel', union_mode='left_to_right')

class SecondaryButton(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    button_view_model: ButtonViewModel | Any = Field(None, alias='buttonViewModel', union_mode='left_to_right')

class PanelFooterViewModel(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    primary_button: PrimaryButton | Any = Field(None, alias='primaryButton', union_mode='left_to_right')
    secondary_button: SecondaryButton | Any = Field(None, alias='secondaryButton', union_mode='left_to_right')
    should_hide_divider: bool | Any = Field(None, alias='shouldHideDivider', union_mode='left_to_right')

class Footer(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    panel_footer_view_model: PanelFooterViewModel | Any = Field(None, alias='panelFooterViewModel', union_mode='left_to_right')

class Text9(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    content: str | Any = Field(default=None, union_mode='left_to_right')

class Paragraph(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    text: Text9 | Any = Field(default=None, union_mode='left_to_right')

class BasicContentViewModel(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    paragraphs: list[Paragraph] | Any = Field(default=None, union_mode='left_to_right')

class Content17(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    basic_content_view_model: BasicContentViewModel | Any = Field(None, alias='basicContentViewModel', union_mode='left_to_right')

class DialogViewModel(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    header: Header5 | Any = Field(default=None, union_mode='left_to_right')
    footer: Footer | Any = Field(default=None, union_mode='left_to_right')
    content: Content17 | Any = Field(default=None, union_mode='left_to_right')

class InlineContent(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    dialog_view_model: DialogViewModel | Any = Field(None, alias='dialogViewModel', union_mode='left_to_right')

class PanelLoadingStrategy(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    inline_content: InlineContent | Any = Field(None, alias='inlineContent', union_mode='left_to_right')

class ShowDialogCommand(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    panel_loading_strategy: PanelLoadingStrategy | Any = Field(None, alias='panelLoadingStrategy', union_mode='left_to_right')

class ShowImageSourceDialog(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    click_tracking_params: str | Any = Field(None, alias='clickTrackingParams', union_mode='left_to_right')
    show_dialog_command: ShowDialogCommand | Any = Field(None, alias='showDialogCommand', union_mode='left_to_right')

class FusionSearchboxRenderer(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    icon: Icon6 | Any = Field(default=None, union_mode='left_to_right')
    placeholder_text: PlaceholderText | Any = Field(None, alias='placeholderText', union_mode='left_to_right')
    config: Config | Any = Field(default=None, union_mode='left_to_right')
    tracking_params: str | Any = Field(None, alias='trackingParams', union_mode='left_to_right')
    search_endpoint: SearchEndpoint | Any = Field(None, alias='searchEndpoint', union_mode='left_to_right')
    clear_button: ClearButton | Any = Field(None, alias='clearButton', union_mode='left_to_right')
    show_image_source_dialog: ShowImageSourceDialog | Any = Field(None, alias='showImageSourceDialog', union_mode='left_to_right')
    disable_ai_appearance: bool | Any = Field(None, alias='disableAiAppearance', union_mode='left_to_right')

class Searchbox(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    fusion_searchbox_renderer: FusionSearchboxRenderer | Any = Field(None, alias='fusionSearchboxRenderer', union_mode='left_to_right')

class WebCommandMetadata18(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    send_post: bool | Any = Field(None, alias='sendPost', union_mode='left_to_right')
    api_url: str | Any = Field(None, alias='apiUrl', union_mode='left_to_right')

class CommandMetadata18(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    web_command_metadata: WebCommandMetadata18 | Any = Field(None, alias='webCommandMetadata', union_mode='left_to_right')

class MultiPageMenuRenderer(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    tracking_params: str | Any = Field(None, alias='trackingParams', union_mode='left_to_right')
    style: str | Any = Field(default=None, union_mode='left_to_right')
    show_loading_spinner: bool | Any = Field(None, alias='showLoadingSpinner', union_mode='left_to_right')

class Popup(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    multi_page_menu_renderer: MultiPageMenuRenderer | Any = Field(None, alias='multiPageMenuRenderer', union_mode='left_to_right')

class OpenPopupAction(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    popup: Popup | Any = Field(default=None, union_mode='left_to_right')
    popup_type: str | Any = Field(None, alias='popupType', union_mode='left_to_right')
    be_reused: bool | Any = Field(None, alias='beReused', union_mode='left_to_right')

class Action(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    click_tracking_params: str | Any = Field(None, alias='clickTrackingParams', union_mode='left_to_right')
    open_popup_action: OpenPopupAction | Any = Field(None, alias='openPopupAction', union_mode='left_to_right')

class SignalServiceEndpoint(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    signal: str | Any = Field(default=None, union_mode='left_to_right')
    actions: list[Action] | Any = Field(default=None, union_mode='left_to_right')

class MenuRequest(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    click_tracking_params: str | Any = Field(None, alias='clickTrackingParams', union_mode='left_to_right')
    command_metadata: CommandMetadata18 | Any = Field(None, alias='commandMetadata', union_mode='left_to_right')
    signal_service_endpoint: SignalServiceEndpoint | Any = Field(None, alias='signalServiceEndpoint', union_mode='left_to_right')

class AccessibilityData12(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    label: str | Any = Field(default=None, union_mode='left_to_right')

class Accessibility6(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    accessibility_data: AccessibilityData12 | Any = Field(None, alias='accessibilityData', union_mode='left_to_right')

class TopbarMenuButtonRenderer(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    icon: Icon6 | Any = Field(default=None, union_mode='left_to_right')
    menu_request: MenuRequest | Any = Field(None, alias='menuRequest', union_mode='left_to_right')
    tracking_params: str | Any = Field(None, alias='trackingParams', union_mode='left_to_right')
    accessibility: Accessibility6 | Any = Field(default=None, union_mode='left_to_right')
    tooltip: str | Any = Field(default=None, union_mode='left_to_right')
    style: str | Any = Field(default=None, union_mode='left_to_right')

class Text10(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    runs: list[Run9] | Any = Field(default=None, union_mode='left_to_right')

class WebCommandMetadata19(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    url: str | Any = Field(default=None, union_mode='left_to_right')
    web_page_type: str | Any = Field(None, alias='webPageType', union_mode='left_to_right')
    root_ve: int | Any = Field(None, alias='rootVe', union_mode='left_to_right')

class CommandMetadata19(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    web_command_metadata: WebCommandMetadata19 | Any = Field(None, alias='webCommandMetadata', union_mode='left_to_right')

class SignInEndpoint(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    idam_tag: str | Any = Field(None, alias='idamTag', union_mode='left_to_right')

class NavigationEndpoint7(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    click_tracking_params: str | Any = Field(None, alias='clickTrackingParams', union_mode='left_to_right')
    command_metadata: CommandMetadata19 | Any = Field(None, alias='commandMetadata', union_mode='left_to_right')
    sign_in_endpoint: SignInEndpoint | Any = Field(None, alias='signInEndpoint', union_mode='left_to_right')

class ButtonRenderer8(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    style: str | Any = Field(default=None, union_mode='left_to_right')
    size: str | Any = Field(default=None, union_mode='left_to_right')
    text: Text10 | Any = Field(default=None, union_mode='left_to_right')
    icon: Icon6 | Any = Field(default=None, union_mode='left_to_right')
    navigation_endpoint: NavigationEndpoint7 | Any = Field(None, alias='navigationEndpoint', union_mode='left_to_right')
    tracking_params: str | Any = Field(None, alias='trackingParams', union_mode='left_to_right')
    target_id: str | Any = Field(None, alias='targetId', union_mode='left_to_right')

class TopbarButton(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    topbar_menu_button_renderer: TopbarMenuButtonRenderer | Any = Field(None, alias='topbarMenuButtonRenderer', union_mode='left_to_right')
    button_renderer: ButtonRenderer8 | Any = Field(None, alias='buttonRenderer', union_mode='left_to_right')

class Title8(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    runs: list[Run9] | Any = Field(default=None, union_mode='left_to_right')

class Title9(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    runs: list[Run9] | Any = Field(default=None, union_mode='left_to_right')

class Label(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    runs: list[Run9] | Any = Field(default=None, union_mode='left_to_right')

class HotkeyAccessibilityLabel(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    accessibility_data: AccessibilityData12 | Any = Field(None, alias='accessibilityData', union_mode='left_to_right')

class HotkeyDialogSectionOptionRenderer(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    label: Label | Any = Field(default=None, union_mode='left_to_right')
    hotkey: str | Any = Field(default=None, union_mode='left_to_right')
    hotkey_accessibility_label: HotkeyAccessibilityLabel | Any = Field(None, alias='hotkeyAccessibilityLabel', union_mode='left_to_right')

class Option(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    hotkey_dialog_section_option_renderer: HotkeyDialogSectionOptionRenderer | Any = Field(None, alias='hotkeyDialogSectionOptionRenderer', union_mode='left_to_right')

class HotkeyDialogSectionRenderer(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    title: Title9 | Any = Field(default=None, union_mode='left_to_right')
    options: list[Option] | Any = Field(default=None, union_mode='left_to_right')

class Section(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    hotkey_dialog_section_renderer: HotkeyDialogSectionRenderer | Any = Field(None, alias='hotkeyDialogSectionRenderer', union_mode='left_to_right')

class Text11(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    runs: list[Run9] | Any = Field(default=None, union_mode='left_to_right')

class ButtonRenderer9(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    style: str | Any = Field(default=None, union_mode='left_to_right')
    size: str | Any = Field(default=None, union_mode='left_to_right')
    is_disabled: bool | Any = Field(None, alias='isDisabled', union_mode='left_to_right')
    text: Text11 | Any = Field(default=None, union_mode='left_to_right')
    tracking_params: str | Any = Field(None, alias='trackingParams', union_mode='left_to_right')

class DismissButton(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    button_renderer: ButtonRenderer9 | Any = Field(None, alias='buttonRenderer', union_mode='left_to_right')

class HotkeyDialogRenderer(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    title: Title8 | Any = Field(default=None, union_mode='left_to_right')
    sections: list[Section] | Any = Field(default=None, union_mode='left_to_right')
    dismiss_button: DismissButton | Any = Field(None, alias='dismissButton', union_mode='left_to_right')
    tracking_params: str | Any = Field(None, alias='trackingParams', union_mode='left_to_right')

class HotkeyDialog(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    hotkey_dialog_renderer: HotkeyDialogRenderer | Any = Field(None, alias='hotkeyDialogRenderer', union_mode='left_to_right')

class WebCommandMetadata20(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    send_post: bool | Any = Field(None, alias='sendPost', union_mode='left_to_right')

class CommandMetadata20(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    web_command_metadata: WebCommandMetadata20 | Any = Field(None, alias='webCommandMetadata', union_mode='left_to_right')

class SignalAction(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    signal: str | Any = Field(default=None, union_mode='left_to_right')

class Action1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    click_tracking_params: str | Any = Field(None, alias='clickTrackingParams', union_mode='left_to_right')
    signal_action: SignalAction | Any = Field(None, alias='signalAction', union_mode='left_to_right')

class SignalServiceEndpoint1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    signal: str | Any = Field(default=None, union_mode='left_to_right')
    actions: list[Action1] | Any = Field(default=None, union_mode='left_to_right')

class Command4(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    click_tracking_params: str | Any = Field(None, alias='clickTrackingParams', union_mode='left_to_right')
    command_metadata: CommandMetadata20 | Any = Field(None, alias='commandMetadata', union_mode='left_to_right')
    signal_service_endpoint: SignalServiceEndpoint1 | Any = Field(None, alias='signalServiceEndpoint', union_mode='left_to_right')

class ButtonRenderer10(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    tracking_params: str | Any = Field(None, alias='trackingParams', union_mode='left_to_right')
    command: Command4 | Any = Field(default=None, union_mode='left_to_right')

class BackButton(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    button_renderer: ButtonRenderer10 | Any = Field(None, alias='buttonRenderer', union_mode='left_to_right')

class CommandMetadata21(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    web_command_metadata: WebCommandMetadata20 | Any = Field(None, alias='webCommandMetadata', union_mode='left_to_right')

class Action2(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    click_tracking_params: str | Any = Field(None, alias='clickTrackingParams', union_mode='left_to_right')
    signal_action: SignalAction | Any = Field(None, alias='signalAction', union_mode='left_to_right')

class SignalServiceEndpoint2(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    signal: str | Any = Field(default=None, union_mode='left_to_right')
    actions: list[Action2] | Any = Field(default=None, union_mode='left_to_right')

class Command5(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    click_tracking_params: str | Any = Field(None, alias='clickTrackingParams', union_mode='left_to_right')
    command_metadata: CommandMetadata21 | Any = Field(None, alias='commandMetadata', union_mode='left_to_right')
    signal_service_endpoint: SignalServiceEndpoint2 | Any = Field(None, alias='signalServiceEndpoint', union_mode='left_to_right')

class ButtonRenderer11(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    tracking_params: str | Any = Field(None, alias='trackingParams', union_mode='left_to_right')
    command: Command5 | Any = Field(default=None, union_mode='left_to_right')

class ForwardButton(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    button_renderer: ButtonRenderer11 | Any = Field(None, alias='buttonRenderer', union_mode='left_to_right')

class Text12(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    runs: list[Run9] | Any = Field(default=None, union_mode='left_to_right')

class CommandMetadata22(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    web_command_metadata: WebCommandMetadata20 | Any = Field(None, alias='webCommandMetadata', union_mode='left_to_right')

class Action3(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    click_tracking_params: str | Any = Field(None, alias='clickTrackingParams', union_mode='left_to_right')
    signal_action: SignalAction | Any = Field(None, alias='signalAction', union_mode='left_to_right')

class SignalServiceEndpoint3(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    signal: str | Any = Field(default=None, union_mode='left_to_right')
    actions: list[Action3] | Any = Field(default=None, union_mode='left_to_right')

class Command6(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    click_tracking_params: str | Any = Field(None, alias='clickTrackingParams', union_mode='left_to_right')
    command_metadata: CommandMetadata22 | Any = Field(None, alias='commandMetadata', union_mode='left_to_right')
    signal_service_endpoint: SignalServiceEndpoint3 | Any = Field(None, alias='signalServiceEndpoint', union_mode='left_to_right')

class ButtonRenderer12(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    style: str | Any = Field(default=None, union_mode='left_to_right')
    size: str | Any = Field(default=None, union_mode='left_to_right')
    is_disabled: bool | Any = Field(None, alias='isDisabled', union_mode='left_to_right')
    text: Text12 | Any = Field(default=None, union_mode='left_to_right')
    tracking_params: str | Any = Field(None, alias='trackingParams', union_mode='left_to_right')
    command: Command6 | Any = Field(default=None, union_mode='left_to_right')

class A11ySkipNavigationButton(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    button_renderer: ButtonRenderer12 | Any = Field(None, alias='buttonRenderer', union_mode='left_to_right')

class CommandMetadata23(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    web_command_metadata: WebCommandMetadata20 | Any = Field(None, alias='webCommandMetadata', union_mode='left_to_right')

class PlaceholderHeader(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    runs: list[Run9] | Any = Field(default=None, union_mode='left_to_right')

class PromptHeader(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    runs: list[Run9] | Any = Field(default=None, union_mode='left_to_right')

class ExampleQuery1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    runs: list[Run9] | Any = Field(default=None, union_mode='left_to_right')

class ExampleQuery2(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    runs: list[Run9] | Any = Field(default=None, union_mode='left_to_right')

class PromptMicrophoneLabel(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    runs: list[Run9] | Any = Field(default=None, union_mode='left_to_right')

class LoadingHeader(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    runs: list[Run9] | Any = Field(default=None, union_mode='left_to_right')

class ConnectionErrorHeader(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    runs: list[Run9] | Any = Field(default=None, union_mode='left_to_right')

class ConnectionErrorMicrophoneLabel(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    runs: list[Run9] | Any = Field(default=None, union_mode='left_to_right')

class PermissionsHeader(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    runs: list[Run9] | Any = Field(default=None, union_mode='left_to_right')

class PermissionsSubtext(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    runs: list[Run9] | Any = Field(default=None, union_mode='left_to_right')

class DisabledHeader(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    runs: list[Run9] | Any = Field(default=None, union_mode='left_to_right')

class DisabledSubtext(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    runs: list[Run9] | Any = Field(default=None, union_mode='left_to_right')

class MicrophoneButtonAriaLabel(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    runs: list[Run9] | Any = Field(default=None, union_mode='left_to_right')

class AccessibilityData14(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    accessibility_data: AccessibilityData12 | Any = Field(None, alias='accessibilityData', union_mode='left_to_right')

class ButtonRenderer14(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    style: str | Any = Field(default=None, union_mode='left_to_right')
    size: str | Any = Field(default=None, union_mode='left_to_right')
    is_disabled: bool | Any = Field(None, alias='isDisabled', union_mode='left_to_right')
    icon: Icon6 | Any = Field(default=None, union_mode='left_to_right')
    tracking_params: str | Any = Field(None, alias='trackingParams', union_mode='left_to_right')
    accessibility_data: AccessibilityData14 | Any = Field(None, alias='accessibilityData', union_mode='left_to_right')

class ExitButton(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    button_renderer: ButtonRenderer14 | Any = Field(None, alias='buttonRenderer', union_mode='left_to_right')

class MicrophoneOffPromptHeader(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    runs: list[Run9] | Any = Field(default=None, union_mode='left_to_right')

class VoiceSearchDialogRenderer(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    placeholder_header: PlaceholderHeader | Any = Field(None, alias='placeholderHeader', union_mode='left_to_right')
    prompt_header: PromptHeader | Any = Field(None, alias='promptHeader', union_mode='left_to_right')
    example_query1: ExampleQuery1 | Any = Field(None, alias='exampleQuery1', union_mode='left_to_right')
    example_query2: ExampleQuery2 | Any = Field(None, alias='exampleQuery2', union_mode='left_to_right')
    prompt_microphone_label: PromptMicrophoneLabel | Any = Field(None, alias='promptMicrophoneLabel', union_mode='left_to_right')
    loading_header: LoadingHeader | Any = Field(None, alias='loadingHeader', union_mode='left_to_right')
    connection_error_header: ConnectionErrorHeader | Any = Field(None, alias='connectionErrorHeader', union_mode='left_to_right')
    connection_error_microphone_label: ConnectionErrorMicrophoneLabel | Any = Field(None, alias='connectionErrorMicrophoneLabel', union_mode='left_to_right')
    permissions_header: PermissionsHeader | Any = Field(None, alias='permissionsHeader', union_mode='left_to_right')
    permissions_subtext: PermissionsSubtext | Any = Field(None, alias='permissionsSubtext', union_mode='left_to_right')
    disabled_header: DisabledHeader | Any = Field(None, alias='disabledHeader', union_mode='left_to_right')
    disabled_subtext: DisabledSubtext | Any = Field(None, alias='disabledSubtext', union_mode='left_to_right')
    microphone_button_aria_label: MicrophoneButtonAriaLabel | Any = Field(None, alias='microphoneButtonAriaLabel', union_mode='left_to_right')
    exit_button: ExitButton | Any = Field(None, alias='exitButton', union_mode='left_to_right')
    tracking_params: str | Any = Field(None, alias='trackingParams', union_mode='left_to_right')
    microphone_off_prompt_header: MicrophoneOffPromptHeader | Any = Field(None, alias='microphoneOffPromptHeader', union_mode='left_to_right')

class Popup1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    voice_search_dialog_renderer: VoiceSearchDialogRenderer | Any = Field(None, alias='voiceSearchDialogRenderer', union_mode='left_to_right')

class OpenPopupAction1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    popup: Popup1 | Any = Field(default=None, union_mode='left_to_right')
    popup_type: str | Any = Field(None, alias='popupType', union_mode='left_to_right')

class Action4(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    click_tracking_params: str | Any = Field(None, alias='clickTrackingParams', union_mode='left_to_right')
    open_popup_action: OpenPopupAction1 | Any = Field(None, alias='openPopupAction', union_mode='left_to_right')

class SignalServiceEndpoint4(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    signal: str | Any = Field(default=None, union_mode='left_to_right')
    actions: list[Action4] | Any = Field(default=None, union_mode='left_to_right')

class ServiceEndpoint(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    click_tracking_params: str | Any = Field(None, alias='clickTrackingParams', union_mode='left_to_right')
    command_metadata: CommandMetadata23 | Any = Field(None, alias='commandMetadata', union_mode='left_to_right')
    signal_service_endpoint: SignalServiceEndpoint4 | Any = Field(None, alias='signalServiceEndpoint', union_mode='left_to_right')

class AccessibilityData17(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    label: str | Any = Field(default=None, union_mode='left_to_right')

class AccessibilityData16(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    accessibility_data: AccessibilityData17 | Any = Field(None, alias='accessibilityData', union_mode='left_to_right')

class ButtonRenderer13(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    style: str | Any = Field(default=None, union_mode='left_to_right')
    size: str | Any = Field(default=None, union_mode='left_to_right')
    is_disabled: bool | Any = Field(None, alias='isDisabled', union_mode='left_to_right')
    service_endpoint: ServiceEndpoint | Any = Field(None, alias='serviceEndpoint', union_mode='left_to_right')
    icon: Icon6 | Any = Field(default=None, union_mode='left_to_right')
    tooltip: str | Any = Field(default=None, union_mode='left_to_right')
    tracking_params: str | Any = Field(None, alias='trackingParams', union_mode='left_to_right')
    accessibility_data: AccessibilityData16 | Any = Field(None, alias='accessibilityData', union_mode='left_to_right')

class VoiceSearchButton(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    button_renderer: ButtonRenderer13 | Any = Field(None, alias='buttonRenderer', union_mode='left_to_right')

class DesktopTopbarRenderer(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    logo: Logo | Any = Field(default=None, union_mode='left_to_right')
    searchbox: Searchbox | Any = Field(default=None, union_mode='left_to_right')
    tracking_params: str | Any = Field(None, alias='trackingParams', union_mode='left_to_right')
    topbar_buttons: list[TopbarButton] | Any = Field(None, alias='topbarButtons', union_mode='left_to_right')
    hotkey_dialog: HotkeyDialog | Any = Field(None, alias='hotkeyDialog', union_mode='left_to_right')
    back_button: BackButton | Any = Field(None, alias='backButton', union_mode='left_to_right')
    forward_button: ForwardButton | Any = Field(None, alias='forwardButton', union_mode='left_to_right')
    a11y_skip_navigation_button: A11ySkipNavigationButton | Any = Field(None, alias='a11ySkipNavigationButton', union_mode='left_to_right')
    voice_search_button: VoiceSearchButton | Any = Field(None, alias='voiceSearchButton', union_mode='left_to_right')

class Topbar(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    desktop_topbar_renderer: DesktopTopbarRenderer | Any = Field(None, alias='desktopTopbarRenderer', union_mode='left_to_right')

class Thumbnail6(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    thumbnails: list[Thumbnail5] | Any = Field(default=None, union_mode='left_to_right')

class LinkAlternate(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    href_url: str | Any = Field(None, alias='hrefUrl', union_mode='left_to_right')

class MicroformatDataRenderer(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    url_canonical: str | Any = Field(None, alias='urlCanonical', union_mode='left_to_right')
    title: str | Any = Field(default=None, union_mode='left_to_right')
    description: str | Any = Field(default=None, union_mode='left_to_right')
    thumbnail: Thumbnail6 | Any = Field(default=None, union_mode='left_to_right')
    site_name: str | Any = Field(None, alias='siteName', union_mode='left_to_right')
    app_name: str | Any = Field(None, alias='appName', union_mode='left_to_right')
    android_package: str | Any = Field(None, alias='androidPackage', union_mode='left_to_right')
    ios_app_store_id: str | Any = Field(None, alias='iosAppStoreId', union_mode='left_to_right')
    ios_app_arguments: str | Any = Field(None, alias='iosAppArguments', union_mode='left_to_right')
    og_type: str | Any = Field(None, alias='ogType', union_mode='left_to_right')
    url_applinks_web: str | Any = Field(None, alias='urlApplinksWeb', union_mode='left_to_right')
    url_applinks_ios: str | Any = Field(None, alias='urlApplinksIos', union_mode='left_to_right')
    url_applinks_android: str | Any = Field(None, alias='urlApplinksAndroid', union_mode='left_to_right')
    url_twitter_ios: str | Any = Field(None, alias='urlTwitterIos', union_mode='left_to_right')
    url_twitter_android: str | Any = Field(None, alias='urlTwitterAndroid', union_mode='left_to_right')
    twitter_card_type: str | Any = Field(None, alias='twitterCardType', union_mode='left_to_right')
    twitter_site_handle: str | Any = Field(None, alias='twitterSiteHandle', union_mode='left_to_right')
    schema_dot_org_type: str | Any = Field(None, alias='schemaDotOrgType', union_mode='left_to_right')
    noindex: bool | Any = Field(default=None, union_mode='left_to_right')
    unlisted: bool | Any = Field(default=None, union_mode='left_to_right')
    family_safe: bool | Any = Field(None, alias='familySafe', union_mode='left_to_right')
    available_countries: list[str] | Any = Field(None, alias='availableCountries', union_mode='left_to_right')
    link_alternates: list[LinkAlternate] | Any = Field(None, alias='linkAlternates', union_mode='left_to_right')

class Microformat(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    microformat_data_renderer: MicroformatDataRenderer | Any = Field(None, alias='microformatDataRenderer', union_mode='left_to_right')

class TopicModel(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    response_context: ResponseContext | Any = Field(None, alias='responseContext', union_mode='left_to_right')
    tracking_params: str | Any = Field(None, alias='trackingParams', union_mode='left_to_right')
    on_response_received_endpoints: list[OnResponseReceivedEndpoint] | Any = Field(None, alias='onResponseReceivedEndpoints', union_mode='left_to_right')
    contents: Contents | Any = Field(default=None, union_mode='left_to_right')
    header: Header3 | Any = Field(default=None, union_mode='left_to_right')
    metadata: Metadata3 | Any = Field(default=None, union_mode='left_to_right')
    topbar: Topbar | Any = Field(default=None, union_mode='left_to_right')
    microformat: Microformat | Any = Field(default=None, union_mode='left_to_right')
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
