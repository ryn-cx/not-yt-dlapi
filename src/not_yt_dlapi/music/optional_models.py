from typing import Any, Self
from pydantic import ModelWrapValidatorHandler, PrivateAttr, model_validator
from pydantic import BaseModel, ConfigDict, Field

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
    main_app_web_response_context: MainAppWebResponseContext | Any = Field(None, alias='mainAppWebResponseContext', union_mode='left_to_right')
    response_id: str | Any = Field(None, alias='responseId', union_mode='left_to_right')
    web_response_context_extension_data: WebResponseContextExtensionData | Any = Field(None, alias='webResponseContextExtensionData', union_mode='left_to_right')

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

class Icon(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    sources: list[Source1] | Any = Field(default=None, union_mode='left_to_right')

class Settings(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    loop: bool | Any = Field(default=None, union_mode='left_to_right')
    autoplay: bool | Any = Field(default=None, union_mode='left_to_right')

class LottieData(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    url: str | Any = Field(default=None, union_mode='left_to_right')
    settings: Settings | Any = Field(default=None, union_mode='left_to_right')

class AccessibilityContext(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    label: str | Any = Field(default=None, union_mode='left_to_right')

class RendererContext(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    accessibility_context: AccessibilityContext | Any = Field(None, alias='accessibilityContext', union_mode='left_to_right')

class ThumbnailBadgeViewModel(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    icon: Icon | Any = Field(default=None, union_mode='left_to_right')
    text: str | Any = Field(default=None, union_mode='left_to_right')
    badge_style: str | Any = Field(None, alias='badgeStyle', union_mode='left_to_right')
    animation_activation_target_id: str | Any = Field(None, alias='animationActivationTargetId', union_mode='left_to_right')
    animation_activation_entity_key: str | Any = Field(None, alias='animationActivationEntityKey', union_mode='left_to_right')
    lottie_data: LottieData | Any = Field(None, alias='lottieData', union_mode='left_to_right')
    animated_text: str | Any = Field(None, alias='animatedText', union_mode='left_to_right')
    animation_activation_entity_selector_type: str | Any = Field(None, alias='animationActivationEntitySelectorType', union_mode='left_to_right')
    renderer_context: RendererContext | Any = Field(None, alias='rendererContext', union_mode='left_to_right')

class Badge(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    thumbnail_badge_view_model: ThumbnailBadgeViewModel | Any = Field(None, alias='thumbnailBadgeViewModel', union_mode='left_to_right')

class ThumbnailBottomOverlayViewModel(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    badges: list[Badge] | Any = Field(default=None, union_mode='left_to_right')

class WebCommandMetadata(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    send_post: bool | Any = Field(None, alias='sendPost', union_mode='left_to_right')
    api_url: str | Any = Field(None, alias='apiUrl', union_mode='left_to_right')

class CommandMetadata(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    web_command_metadata: WebCommandMetadata | Any = Field(None, alias='webCommandMetadata', union_mode='left_to_right')

class Action(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    added_video_id: str | Any = Field(None, alias='addedVideoId', union_mode='left_to_right')
    action: str | Any = Field(default=None, union_mode='left_to_right')

class PlaylistEditEndpoint(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    playlist_id: str | Any = Field(None, alias='playlistId', union_mode='left_to_right')
    actions: list[Action] | Any = Field(default=None, union_mode='left_to_right')

class CommandMetadata1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    web_command_metadata: WebCommandMetadata | Any = Field(None, alias='webCommandMetadata', union_mode='left_to_right')

class CreatePlaylistServiceEndpoint(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    video_ids: list[str] | Any = Field(None, alias='videoIds', union_mode='left_to_right')
    params: str | Any = Field(default=None, union_mode='left_to_right')

class OnCreateListCommand(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    click_tracking_params: str | Any = Field(None, alias='clickTrackingParams', union_mode='left_to_right')
    command_metadata: CommandMetadata1 | Any = Field(None, alias='commandMetadata', union_mode='left_to_right')
    create_playlist_service_endpoint: CreatePlaylistServiceEndpoint | Any = Field(None, alias='createPlaylistServiceEndpoint', union_mode='left_to_right')

class WebCommandMetadata2(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    url: str | Any = Field(default=None, union_mode='left_to_right')
    web_page_type: str | Any = Field(None, alias='webPageType', union_mode='left_to_right')
    root_ve: int | Any = Field(None, alias='rootVe', union_mode='left_to_right')

class CommandMetadata2(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    web_command_metadata: WebCommandMetadata2 | Any = Field(None, alias='webCommandMetadata', union_mode='left_to_right')

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
    watch_endpoint_supported_onesie_config: WatchEndpointSupportedOnesieConfig | Any = Field(None, alias='watchEndpointSupportedOnesieConfig', union_mode='left_to_right')
    player_params: str | Any = Field(None, alias='playerParams', union_mode='left_to_right')

class VideoCommand(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    click_tracking_params: str | Any = Field(None, alias='clickTrackingParams', union_mode='left_to_right')
    command_metadata: CommandMetadata2 | Any = Field(None, alias='commandMetadata', union_mode='left_to_right')
    watch_endpoint: WatchEndpoint | Any = Field(None, alias='watchEndpoint', union_mode='left_to_right')

class AddToPlaylistCommand(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    open_miniplayer: bool | Any = Field(None, alias='openMiniplayer', union_mode='left_to_right')
    video_id: str | Any = Field(None, alias='videoId', union_mode='left_to_right')
    list_type: str | Any = Field(None, alias='listType', union_mode='left_to_right')
    on_create_list_command: OnCreateListCommand | Any = Field(None, alias='onCreateListCommand', union_mode='left_to_right')
    video_ids: list[str] | Any = Field(None, alias='videoIds', union_mode='left_to_right')
    video_command: VideoCommand | Any = Field(None, alias='videoCommand', union_mode='left_to_right')

class Action1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    click_tracking_params: str | Any = Field(None, alias='clickTrackingParams', union_mode='left_to_right')
    add_to_playlist_command: AddToPlaylistCommand | Any = Field(None, alias='addToPlaylistCommand', union_mode='left_to_right')

class SignalServiceEndpoint(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    signal: str | Any = Field(default=None, union_mode='left_to_right')
    actions: list[Action1] | Any = Field(default=None, union_mode='left_to_right')

class InnertubeCommand(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    click_tracking_params: str | Any = Field(None, alias='clickTrackingParams', union_mode='left_to_right')
    command_metadata: CommandMetadata | Any = Field(None, alias='commandMetadata', union_mode='left_to_right')
    playlist_edit_endpoint: PlaylistEditEndpoint | Any = Field(None, alias='playlistEditEndpoint', union_mode='left_to_right')
    signal_service_endpoint: SignalServiceEndpoint | Any = Field(None, alias='signalServiceEndpoint', union_mode='left_to_right')

class OnTap(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    innertube_command: InnertubeCommand | Any = Field(None, alias='innertubeCommand', union_mode='left_to_right')

class ButtonViewModel(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    icon_name: str | Any = Field(None, alias='iconName', union_mode='left_to_right')
    on_tap: OnTap | Any = Field(None, alias='onTap', union_mode='left_to_right')
    accessibility_text: str | Any = Field(None, alias='accessibilityText', union_mode='left_to_right')
    style: str | Any = Field(default=None, union_mode='left_to_right')
    tracking_params: str | Any = Field(None, alias='trackingParams', union_mode='left_to_right')
    type: str | Any = Field(default=None, union_mode='left_to_right')
    button_size: str | Any = Field(None, alias='buttonSize', union_mode='left_to_right')
    state: str | Any = Field(default=None, union_mode='left_to_right')

class DefaultButtonViewModel(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    button_view_model: ButtonViewModel | Any = Field(None, alias='buttonViewModel', union_mode='left_to_right')

class WebCommandMetadata3(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    send_post: bool | Any = Field(None, alias='sendPost', union_mode='left_to_right')
    api_url: str | Any = Field(None, alias='apiUrl', union_mode='left_to_right')

class CommandMetadata3(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    web_command_metadata: WebCommandMetadata3 | Any = Field(None, alias='webCommandMetadata', union_mode='left_to_right')

class Action2(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    action: str | Any = Field(default=None, union_mode='left_to_right')
    removed_video_id: str | Any = Field(None, alias='removedVideoId', union_mode='left_to_right')

class PlaylistEditEndpoint1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    playlist_id: str | Any = Field(None, alias='playlistId', union_mode='left_to_right')
    actions: list[Action2] | Any = Field(default=None, union_mode='left_to_right')

class InnertubeCommand1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    click_tracking_params: str | Any = Field(None, alias='clickTrackingParams', union_mode='left_to_right')
    command_metadata: CommandMetadata3 | Any = Field(None, alias='commandMetadata', union_mode='left_to_right')
    playlist_edit_endpoint: PlaylistEditEndpoint1 | Any = Field(None, alias='playlistEditEndpoint', union_mode='left_to_right')

class OnTap1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    innertube_command: InnertubeCommand1 | Any = Field(None, alias='innertubeCommand', union_mode='left_to_right')

class ButtonViewModel1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    icon_name: str | Any = Field(None, alias='iconName', union_mode='left_to_right')
    on_tap: OnTap1 | Any = Field(None, alias='onTap', union_mode='left_to_right')
    accessibility_text: str | Any = Field(None, alias='accessibilityText', union_mode='left_to_right')
    style: str | Any = Field(default=None, union_mode='left_to_right')
    tracking_params: str | Any = Field(None, alias='trackingParams', union_mode='left_to_right')
    type: str | Any = Field(default=None, union_mode='left_to_right')
    button_size: str | Any = Field(None, alias='buttonSize', union_mode='left_to_right')
    state: str | Any = Field(default=None, union_mode='left_to_right')

class ToggledButtonViewModel(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    button_view_model: ButtonViewModel1 | Any = Field(None, alias='buttonViewModel', union_mode='left_to_right')

class ToggleButtonViewModel(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    default_button_view_model: DefaultButtonViewModel | Any = Field(None, alias='defaultButtonViewModel', union_mode='left_to_right')
    toggled_button_view_model: ToggledButtonViewModel | Any = Field(None, alias='toggledButtonViewModel', union_mode='left_to_right')
    is_toggled: bool | Any = Field(None, alias='isToggled', union_mode='left_to_right')
    tracking_params: str | Any = Field(None, alias='trackingParams', union_mode='left_to_right')

class Button(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    toggle_button_view_model: ToggleButtonViewModel | Any = Field(None, alias='toggleButtonViewModel', union_mode='left_to_right')

class ThumbnailHoverOverlayToggleActionsViewModel(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    buttons: list[Button] | Any = Field(default=None, union_mode='left_to_right')

class Overlay(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    thumbnail_bottom_overlay_view_model: ThumbnailBottomOverlayViewModel | Any = Field(None, alias='thumbnailBottomOverlayViewModel', union_mode='left_to_right')
    thumbnail_hover_overlay_toggle_actions_view_model: ThumbnailHoverOverlayToggleActionsViewModel | Any = Field(None, alias='thumbnailHoverOverlayToggleActionsViewModel', union_mode='left_to_right')

class ThumbnailViewModel(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    image: Image | Any = Field(default=None, union_mode='left_to_right')
    overlays: list[Overlay] | Any = Field(default=None, union_mode='left_to_right')

class ContentImage(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    thumbnail_view_model: ThumbnailViewModel | Any = Field(None, alias='thumbnailViewModel', union_mode='left_to_right')

class Title(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    content: str | Any = Field(default=None, union_mode='left_to_right')

class Source2(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    url: str | Any = Field(default=None, union_mode='left_to_right')
    width: int | Any = Field(default=None, union_mode='left_to_right')
    height: int | Any = Field(default=None, union_mode='left_to_right')

class Image2(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    sources: list[Source2] | Any = Field(default=None, union_mode='left_to_right')

class AvatarViewModel(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    image: Image2 | Any = Field(default=None, union_mode='left_to_right')
    avatar_image_size: str | Any = Field(None, alias='avatarImageSize', union_mode='left_to_right')

class Avatar(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    avatar_view_model: AvatarViewModel | Any = Field(None, alias='avatarViewModel', union_mode='left_to_right')

class WebCommandMetadata4(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    url: str | Any = Field(default=None, union_mode='left_to_right')
    web_page_type: str | Any = Field(None, alias='webPageType', union_mode='left_to_right')
    root_ve: int | Any = Field(None, alias='rootVe', union_mode='left_to_right')
    api_url: str | Any = Field(None, alias='apiUrl', union_mode='left_to_right')

class CommandMetadata4(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    web_command_metadata: WebCommandMetadata4 | Any = Field(None, alias='webCommandMetadata', union_mode='left_to_right')

class BrowseEndpoint(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    browse_id: str | Any = Field(None, alias='browseId', union_mode='left_to_right')
    canonical_base_url: str | Any = Field(None, alias='canonicalBaseUrl', union_mode='left_to_right')

class InnertubeCommand2(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    click_tracking_params: str | Any = Field(None, alias='clickTrackingParams', union_mode='left_to_right')
    command_metadata: CommandMetadata4 | Any = Field(None, alias='commandMetadata', union_mode='left_to_right')
    browse_endpoint: BrowseEndpoint | Any = Field(None, alias='browseEndpoint', union_mode='left_to_right')

class OnTap2(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    innertube_command: InnertubeCommand2 | Any = Field(None, alias='innertubeCommand', union_mode='left_to_right')

class CommandContext(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    on_tap: OnTap2 | Any = Field(None, alias='onTap', union_mode='left_to_right')

class RendererContext1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    command_context: CommandContext | Any = Field(None, alias='commandContext', union_mode='left_to_right')

class DecoratedAvatarViewModel(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    avatar: Avatar | Any = Field(default=None, union_mode='left_to_right')
    a11y_label: str | Any = Field(None, alias='a11yLabel', union_mode='left_to_right')
    renderer_context: RendererContext1 | Any = Field(None, alias='rendererContext', union_mode='left_to_right')

class Image1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    decorated_avatar_view_model: DecoratedAvatarViewModel | Any = Field(None, alias='decoratedAvatarViewModel', union_mode='left_to_right')

class CommandMetadata5(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    web_command_metadata: WebCommandMetadata4 | Any = Field(None, alias='webCommandMetadata', union_mode='left_to_right')

class InnertubeCommand3(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    click_tracking_params: str | Any = Field(None, alias='clickTrackingParams', union_mode='left_to_right')
    command_metadata: CommandMetadata5 | Any = Field(None, alias='commandMetadata', union_mode='left_to_right')
    browse_endpoint: BrowseEndpoint | Any = Field(None, alias='browseEndpoint', union_mode='left_to_right')

class OnTap3(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    innertube_command: InnertubeCommand3 | Any = Field(None, alias='innertubeCommand', union_mode='left_to_right')

class CommandRun(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    start_index: int | Any = Field(None, alias='startIndex', union_mode='left_to_right')
    length: int | Any = Field(default=None, union_mode='left_to_right')
    on_tap: OnTap3 | Any = Field(None, alias='onTap', union_mode='left_to_right')

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

class StyleRun(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    start_index: int | Any = Field(None, alias='startIndex', union_mode='left_to_right')
    length: int | Any = Field(default=None, union_mode='left_to_right')
    weight_label: str | Any = Field(None, alias='weightLabel', union_mode='left_to_right')
    style_run_extensions: StyleRunExtensions | Any = Field(None, alias='styleRunExtensions', union_mode='left_to_right')

class Source3(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    client_resource: ClientResource | Any = Field(None, alias='clientResource', union_mode='left_to_right')
    width: int | Any = Field(default=None, union_mode='left_to_right')
    height: int | Any = Field(default=None, union_mode='left_to_right')

class Image3(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    sources: list[Source3] | Any = Field(default=None, union_mode='left_to_right')

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

class Left(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    value: int | Any = Field(default=None, union_mode='left_to_right')
    unit: str | Any = Field(default=None, union_mode='left_to_right')

class Margin(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    left: Left | Any = Field(default=None, union_mode='left_to_right')

class LayoutProperties(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    height: Height | Any = Field(default=None, union_mode='left_to_right')
    width: Width | Any = Field(default=None, union_mode='left_to_right')
    margin: Margin | Any = Field(default=None, union_mode='left_to_right')

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

class Text(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    content: str | Any = Field(default=None, union_mode='left_to_right')
    command_runs: list[CommandRun] | Any = Field(None, alias='commandRuns', union_mode='left_to_right')
    style_runs: list[StyleRun] | Any = Field(None, alias='styleRuns', union_mode='left_to_right')
    attachment_runs: list[AttachmentRun] | Any = Field(None, alias='attachmentRuns', union_mode='left_to_right')

class MetadataPart(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    text: Text | Any = Field(default=None, union_mode='left_to_right')
    accessibility_label: str | Any = Field(None, alias='accessibilityLabel', union_mode='left_to_right')

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

class Source4(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    client_resource: ClientResource | Any = Field(None, alias='clientResource', union_mode='left_to_right')

class LeadingImage(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    sources: list[Source4] | Any = Field(default=None, union_mode='left_to_right')

class Visibility(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    types: str | Any = Field(default=None, union_mode='left_to_right')

class LoggingDirectives(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    tracking_params: str | Any = Field(None, alias='trackingParams', union_mode='left_to_right')
    visibility: Visibility | Any = Field(default=None, union_mode='left_to_right')

class LoggingContext(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    logging_directives: LoggingDirectives | Any = Field(None, alias='loggingDirectives', union_mode='left_to_right')

class WebCommandMetadata6(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    send_post: bool | Any = Field(None, alias='sendPost', union_mode='left_to_right')
    api_url: str | Any = Field(None, alias='apiUrl', union_mode='left_to_right')

class CommandMetadata6(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    web_command_metadata: WebCommandMetadata6 | Any = Field(None, alias='webCommandMetadata', union_mode='left_to_right')

class CommandMetadata7(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    web_command_metadata: WebCommandMetadata6 | Any = Field(None, alias='webCommandMetadata', union_mode='left_to_right')

class OnCreateListCommand1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    click_tracking_params: str | Any = Field(None, alias='clickTrackingParams', union_mode='left_to_right')
    command_metadata: CommandMetadata7 | Any = Field(None, alias='commandMetadata', union_mode='left_to_right')
    create_playlist_service_endpoint: CreatePlaylistServiceEndpoint | Any = Field(None, alias='createPlaylistServiceEndpoint', union_mode='left_to_right')

class WebCommandMetadata8(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    url: str | Any = Field(default=None, union_mode='left_to_right')
    web_page_type: str | Any = Field(None, alias='webPageType', union_mode='left_to_right')
    root_ve: int | Any = Field(None, alias='rootVe', union_mode='left_to_right')

class CommandMetadata8(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    web_command_metadata: WebCommandMetadata8 | Any = Field(None, alias='webCommandMetadata', union_mode='left_to_right')

class Html5PlaybackOnesieConfig1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    common_config: CommonConfig | Any = Field(None, alias='commonConfig', union_mode='left_to_right')

class WatchEndpointSupportedOnesieConfig1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    html5_playback_onesie_config: Html5PlaybackOnesieConfig1 | Any = Field(None, alias='html5PlaybackOnesieConfig', union_mode='left_to_right')

class WatchEndpoint1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    video_id: str | Any = Field(None, alias='videoId', union_mode='left_to_right')
    watch_endpoint_supported_onesie_config: WatchEndpointSupportedOnesieConfig1 | Any = Field(None, alias='watchEndpointSupportedOnesieConfig', union_mode='left_to_right')
    player_params: str | Any = Field(None, alias='playerParams', union_mode='left_to_right')

class VideoCommand1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    click_tracking_params: str | Any = Field(None, alias='clickTrackingParams', union_mode='left_to_right')
    command_metadata: CommandMetadata8 | Any = Field(None, alias='commandMetadata', union_mode='left_to_right')
    watch_endpoint: WatchEndpoint1 | Any = Field(None, alias='watchEndpoint', union_mode='left_to_right')

class AddToPlaylistCommand1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    open_miniplayer: bool | Any = Field(None, alias='openMiniplayer', union_mode='left_to_right')
    video_id: str | Any = Field(None, alias='videoId', union_mode='left_to_right')
    list_type: str | Any = Field(None, alias='listType', union_mode='left_to_right')
    on_create_list_command: OnCreateListCommand1 | Any = Field(None, alias='onCreateListCommand', union_mode='left_to_right')
    video_ids: list[str] | Any = Field(None, alias='videoIds', union_mode='left_to_right')
    video_command: VideoCommand1 | Any = Field(None, alias='videoCommand', union_mode='left_to_right')

class Action3(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    click_tracking_params: str | Any = Field(None, alias='clickTrackingParams', union_mode='left_to_right')
    add_to_playlist_command: AddToPlaylistCommand1 | Any = Field(None, alias='addToPlaylistCommand', union_mode='left_to_right')

class SignalServiceEndpoint1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    signal: str | Any = Field(default=None, union_mode='left_to_right')
    actions: list[Action3] | Any = Field(default=None, union_mode='left_to_right')

class UnifiedSharePanelRenderer(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    tracking_params: str | Any = Field(None, alias='trackingParams', union_mode='left_to_right')
    show_loading_spinner: bool | Any = Field(None, alias='showLoadingSpinner', union_mode='left_to_right')

class Popup(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    unified_share_panel_renderer: UnifiedSharePanelRenderer | Any = Field(None, alias='unifiedSharePanelRenderer', union_mode='left_to_right')

class OpenPopupAction(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    popup: Popup | Any = Field(default=None, union_mode='left_to_right')
    popup_type: str | Any = Field(None, alias='popupType', union_mode='left_to_right')
    be_reused: bool | Any = Field(None, alias='beReused', union_mode='left_to_right')

class Command(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    click_tracking_params: str | Any = Field(None, alias='clickTrackingParams', union_mode='left_to_right')
    open_popup_action: OpenPopupAction | Any = Field(None, alias='openPopupAction', union_mode='left_to_right')

class ShareEntityServiceEndpoint(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    serialized_share_entity: str | Any = Field(None, alias='serializedShareEntity', union_mode='left_to_right')
    commands: list[Command] | Any = Field(default=None, union_mode='left_to_right')

class InnertubeCommand5(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    click_tracking_params: str | Any = Field(None, alias='clickTrackingParams', union_mode='left_to_right')
    command_metadata: CommandMetadata6 | Any = Field(None, alias='commandMetadata', union_mode='left_to_right')
    signal_service_endpoint: SignalServiceEndpoint1 | Any = Field(None, alias='signalServiceEndpoint', union_mode='left_to_right')
    share_entity_service_endpoint: ShareEntityServiceEndpoint | Any = Field(None, alias='shareEntityServiceEndpoint', union_mode='left_to_right')

class OnTap5(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    innertube_command: InnertubeCommand5 | Any = Field(None, alias='innertubeCommand', union_mode='left_to_right')

class CommandContext1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    on_tap: OnTap5 | Any = Field(None, alias='onTap', union_mode='left_to_right')

class RendererContext2(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    logging_context: LoggingContext | Any = Field(None, alias='loggingContext', union_mode='left_to_right')
    command_context: CommandContext1 | Any = Field(None, alias='commandContext', union_mode='left_to_right')

class ListItemViewModel(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    title: Title | Any = Field(default=None, union_mode='left_to_right')
    leading_image: LeadingImage | Any = Field(None, alias='leadingImage', union_mode='left_to_right')
    renderer_context: RendererContext2 | Any = Field(None, alias='rendererContext', union_mode='left_to_right')

class ListItem(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    list_item_view_model: ListItemViewModel | Any = Field(None, alias='listItemViewModel', union_mode='left_to_right')

class ListViewModel(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    list_items: list[ListItem] | Any = Field(None, alias='listItems', union_mode='left_to_right')

class Content3(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    list_view_model: ListViewModel | Any = Field(None, alias='listViewModel', union_mode='left_to_right')

class SheetViewModel(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    content: Content3 | Any = Field(default=None, union_mode='left_to_right')

class InlineContent(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    sheet_view_model: SheetViewModel | Any = Field(None, alias='sheetViewModel', union_mode='left_to_right')

class PanelLoadingStrategy(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    inline_content: InlineContent | Any = Field(None, alias='inlineContent', union_mode='left_to_right')

class ShowSheetCommand(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    panel_loading_strategy: PanelLoadingStrategy | Any = Field(None, alias='panelLoadingStrategy', union_mode='left_to_right')

class InnertubeCommand4(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    click_tracking_params: str | Any = Field(None, alias='clickTrackingParams', union_mode='left_to_right')
    show_sheet_command: ShowSheetCommand | Any = Field(None, alias='showSheetCommand', union_mode='left_to_right')

class OnTap4(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    innertube_command: InnertubeCommand4 | Any = Field(None, alias='innertubeCommand', union_mode='left_to_right')

class ButtonViewModel2(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    icon_name: str | Any = Field(None, alias='iconName', union_mode='left_to_right')
    on_tap: OnTap4 | Any = Field(None, alias='onTap', union_mode='left_to_right')
    accessibility_text: str | Any = Field(None, alias='accessibilityText', union_mode='left_to_right')
    style: str | Any = Field(default=None, union_mode='left_to_right')
    tracking_params: str | Any = Field(None, alias='trackingParams', union_mode='left_to_right')
    type: str | Any = Field(default=None, union_mode='left_to_right')
    button_size: str | Any = Field(None, alias='buttonSize', union_mode='left_to_right')
    state: str | Any = Field(default=None, union_mode='left_to_right')

class MenuButton(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    button_view_model: ButtonViewModel2 | Any = Field(None, alias='buttonViewModel', union_mode='left_to_right')

class LockupMetadataViewModel(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    title: Title | Any = Field(default=None, union_mode='left_to_right')
    image: Image1 | Any = Field(default=None, union_mode='left_to_right')
    metadata: Metadata1 | Any = Field(default=None, union_mode='left_to_right')
    menu_button: MenuButton | Any = Field(None, alias='menuButton', union_mode='left_to_right')

class Metadata(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    lockup_metadata_view_model: LockupMetadataViewModel | Any = Field(None, alias='lockupMetadataViewModel', union_mode='left_to_right')

class LoggingDirectives1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    tracking_params: str | Any = Field(None, alias='trackingParams', union_mode='left_to_right')
    visibility: Visibility | Any = Field(default=None, union_mode='left_to_right')

class LoggingContext1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    logging_directives: LoggingDirectives1 | Any = Field(None, alias='loggingDirectives', union_mode='left_to_right')

class CommandMetadata9(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    web_command_metadata: WebCommandMetadata8 | Any = Field(None, alias='webCommandMetadata', union_mode='left_to_right')

class VssLoggingContext(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    serialized_context_data: str | Any = Field(None, alias='serializedContextData', union_mode='left_to_right')

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
    index: int | Any = Field(default=None, union_mode='left_to_right')
    params: str | Any = Field(default=None, union_mode='left_to_right')
    player_params: str | Any = Field(None, alias='playerParams', union_mode='left_to_right')
    logging_context: LoggingContext2 | Any = Field(None, alias='loggingContext', union_mode='left_to_right')
    watch_endpoint_supported_onesie_config: WatchEndpointSupportedOnesieConfig2 | Any = Field(None, alias='watchEndpointSupportedOnesieConfig', union_mode='left_to_right')

class InnertubeCommand6(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    click_tracking_params: str | Any = Field(None, alias='clickTrackingParams', union_mode='left_to_right')
    command_metadata: CommandMetadata9 | Any = Field(None, alias='commandMetadata', union_mode='left_to_right')
    watch_endpoint: WatchEndpoint2 | Any = Field(None, alias='watchEndpoint', union_mode='left_to_right')

class OnTap6(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    innertube_command: InnertubeCommand6 | Any = Field(None, alias='innertubeCommand', union_mode='left_to_right')

class CommandContext2(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    on_tap: OnTap6 | Any = Field(None, alias='onTap', union_mode='left_to_right')

class RendererContext3(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    logging_context: LoggingContext1 | Any = Field(None, alias='loggingContext', union_mode='left_to_right')
    accessibility_context: AccessibilityContext | Any = Field(None, alias='accessibilityContext', union_mode='left_to_right')
    command_context: CommandContext2 | Any = Field(None, alias='commandContext', union_mode='left_to_right')

class LockupViewModel(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    content_image: ContentImage | Any = Field(None, alias='contentImage', union_mode='left_to_right')
    metadata: Metadata | Any = Field(default=None, union_mode='left_to_right')
    content_id: str | Any = Field(None, alias='contentId', union_mode='left_to_right')
    content_type: str | Any = Field(None, alias='contentType', union_mode='left_to_right')
    renderer_context: RendererContext3 | Any = Field(None, alias='rendererContext', union_mode='left_to_right')

class Content2(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    lockup_view_model: LockupViewModel | Any = Field(None, alias='lockupViewModel', union_mode='left_to_right')

class ItemSectionRenderer(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    contents: list[Content2] | Any = Field(default=None, union_mode='left_to_right')
    tracking_params: str | Any = Field(None, alias='trackingParams', union_mode='left_to_right')
    target_id: str | Any = Field(None, alias='targetId', union_mode='left_to_right')

class Content1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    item_section_renderer: ItemSectionRenderer | Any = Field(None, alias='itemSectionRenderer', union_mode='left_to_right')

class SpacingConfiguration(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    column_gap: int | Any = Field(None, alias='columnGap', union_mode='left_to_right')
    row_gap: int | Any = Field(None, alias='rowGap', union_mode='left_to_right')

class ResponsiveMapItem(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    container_size: str | Any = Field(None, alias='containerSize', union_mode='left_to_right')
    container_type: str | Any = Field(None, alias='containerType', union_mode='left_to_right')
    max_width: int | Any = Field(None, alias='maxWidth', union_mode='left_to_right')
    min_column_size: int | Any = Field(None, alias='minColumnSize', union_mode='left_to_right')
    min_column_count: int | Any = Field(None, alias='minColumnCount', union_mode='left_to_right')
    max_column_count: int | Any = Field(None, alias='maxColumnCount', union_mode='left_to_right')
    spacing_configuration: SpacingConfiguration | Any = Field(None, alias='spacingConfiguration', union_mode='left_to_right')
    column_multiplier: int | Any = Field(None, alias='columnMultiplier', union_mode='left_to_right')
    column_adder: int | Any = Field(None, alias='columnAdder', union_mode='left_to_right')

class ResponsiveContainerConfiguration(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    responsive_size: str | Any = Field(None, alias='responsiveSize', union_mode='left_to_right')
    responsive_map: list[ResponsiveMapItem] | Any = Field(None, alias='responsiveMap', union_mode='left_to_right')

class LayoutConfiguration(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    responsive_container_configuration: ResponsiveContainerConfiguration | Any = Field(None, alias='responsiveContainerConfiguration', union_mode='left_to_right')

class SectionListLayoutConfiguration(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    layout_configuration: LayoutConfiguration | Any = Field(None, alias='layoutConfiguration', union_mode='left_to_right')

class SectionListRenderer(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    contents: list[Content1] | Any = Field(default=None, union_mode='left_to_right')
    tracking_params: str | Any = Field(None, alias='trackingParams', union_mode='left_to_right')
    section_list_layout_configuration: SectionListLayoutConfiguration | Any = Field(None, alias='sectionListLayoutConfiguration', union_mode='left_to_right')

class Content(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    section_list_renderer: SectionListRenderer | Any = Field(None, alias='sectionListRenderer', union_mode='left_to_right')

class TabRenderer(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    selected: bool | Any = Field(default=None, union_mode='left_to_right')
    content: Content | Any = Field(default=None, union_mode='left_to_right')
    tab_identifier: str | Any = Field(None, alias='tabIdentifier', union_mode='left_to_right')
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

class Title2(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    simple_text: str | Any = Field(None, alias='simpleText', union_mode='left_to_right')

class Run(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    text: str | Any = Field(default=None, union_mode='left_to_right')

class NumVideosText(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    runs: list[Run] | Any = Field(default=None, union_mode='left_to_right')

class ViewCountText(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    simple_text: str | Any = Field(None, alias='simpleText', union_mode='left_to_right')

class ShareData(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    can_share: bool | Any = Field(None, alias='canShare', union_mode='left_to_right')

class EditableDetails(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    can_delete: bool | Any = Field(None, alias='canDelete', union_mode='left_to_right')

class WebCommandMetadata10(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    send_post: bool | Any = Field(None, alias='sendPost', union_mode='left_to_right')
    api_url: str | Any = Field(None, alias='apiUrl', union_mode='left_to_right')

class CommandMetadata10(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    web_command_metadata: WebCommandMetadata10 | Any = Field(None, alias='webCommandMetadata', union_mode='left_to_right')

class Action4(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    action: str | Any = Field(default=None, union_mode='left_to_right')
    source_playlist_id: str | Any = Field(None, alias='sourcePlaylistId', union_mode='left_to_right')

class PlaylistEditEndpoint2(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    actions: list[Action4] | Any = Field(default=None, union_mode='left_to_right')

class ServiceEndpoint(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    click_tracking_params: str | Any = Field(None, alias='clickTrackingParams', union_mode='left_to_right')
    command_metadata: CommandMetadata10 | Any = Field(None, alias='commandMetadata', union_mode='left_to_right')
    playlist_edit_endpoint: PlaylistEditEndpoint2 | Any = Field(None, alias='playlistEditEndpoint', union_mode='left_to_right')

class Stat(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    runs: list[Run] | Any = Field(default=None, union_mode='left_to_right')
    simple_text: str | Any = Field(None, alias='simpleText', union_mode='left_to_right')

class BriefStat(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    runs: list[Run] | Any = Field(default=None, union_mode='left_to_right')

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

class WebCommandMetadata11(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    url: str | Any = Field(default=None, union_mode='left_to_right')
    web_page_type: str | Any = Field(None, alias='webPageType', union_mode='left_to_right')
    root_ve: int | Any = Field(None, alias='rootVe', union_mode='left_to_right')

class CommandMetadata11(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    web_command_metadata: WebCommandMetadata11 | Any = Field(None, alias='webCommandMetadata', union_mode='left_to_right')

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

class OnTap7(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    click_tracking_params: str | Any = Field(None, alias='clickTrackingParams', union_mode='left_to_right')
    command_metadata: CommandMetadata11 | Any = Field(None, alias='commandMetadata', union_mode='left_to_right')
    watch_endpoint: WatchEndpoint3 | Any = Field(None, alias='watchEndpoint', union_mode='left_to_right')

class Text1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    simple_text: str | Any = Field(None, alias='simpleText', union_mode='left_to_right')

class Icon1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    icon_type: str | Any = Field(None, alias='iconType', union_mode='left_to_right')

class ThumbnailOverlayHoverTextRenderer(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    text: Text1 | Any = Field(default=None, union_mode='left_to_right')
    icon: Icon1 | Any = Field(default=None, union_mode='left_to_right')

class ThumbnailOverlays(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    thumbnail_overlay_hover_text_renderer: ThumbnailOverlayHoverTextRenderer | Any = Field(None, alias='thumbnailOverlayHoverTextRenderer', union_mode='left_to_right')

class HeroPlaylistThumbnailRenderer(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    thumbnail: Thumbnail | Any = Field(default=None, union_mode='left_to_right')
    max_ratio: float | Any = Field(None, alias='maxRatio', union_mode='left_to_right')
    tracking_params: str | Any = Field(None, alias='trackingParams', union_mode='left_to_right')
    on_tap: OnTap7 | Any = Field(None, alias='onTap', union_mode='left_to_right')
    thumbnail_overlays: ThumbnailOverlays | Any = Field(None, alias='thumbnailOverlays', union_mode='left_to_right')

class PlaylistHeaderBanner(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    hero_playlist_thumbnail_renderer: HeroPlaylistThumbnailRenderer | Any = Field(None, alias='heroPlaylistThumbnailRenderer', union_mode='left_to_right')

class Style(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    style_type: str | Any = Field(None, alias='styleType', union_mode='left_to_right')

class Size(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    size_type: str | Any = Field(None, alias='sizeType', union_mode='left_to_right')

class DefaultIcon(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    icon_type: str | Any = Field(None, alias='iconType', union_mode='left_to_right')

class ToggledIcon(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    icon_type: str | Any = Field(None, alias='iconType', union_mode='left_to_right')

class ToggledStyle(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    style_type: str | Any = Field(None, alias='styleType', union_mode='left_to_right')

class WebCommandMetadata12(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    ignore_navigation: bool | Any = Field(None, alias='ignoreNavigation', union_mode='left_to_right')

class CommandMetadata12(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    web_command_metadata: WebCommandMetadata12 | Any = Field(None, alias='webCommandMetadata', union_mode='left_to_right')

class Content4(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    simple_text: str | Any = Field(None, alias='simpleText', union_mode='left_to_right')

class WebCommandMetadata13(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    url: str | Any = Field(default=None, union_mode='left_to_right')
    web_page_type: str | Any = Field(None, alias='webPageType', union_mode='left_to_right')
    root_ve: int | Any = Field(None, alias='rootVe', union_mode='left_to_right')

class CommandMetadata13(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    web_command_metadata: WebCommandMetadata13 | Any = Field(None, alias='webCommandMetadata', union_mode='left_to_right')

class WebCommandMetadata14(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    url: str | Any = Field(default=None, union_mode='left_to_right')
    web_page_type: str | Any = Field(None, alias='webPageType', union_mode='left_to_right')
    root_ve: int | Any = Field(None, alias='rootVe', union_mode='left_to_right')
    api_url: str | Any = Field(None, alias='apiUrl', union_mode='left_to_right')

class CommandMetadata14(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    web_command_metadata: WebCommandMetadata14 | Any = Field(None, alias='webCommandMetadata', union_mode='left_to_right')

class BrowseEndpoint2(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    browse_id: str | Any = Field(None, alias='browseId', union_mode='left_to_right')

class NextEndpoint(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    click_tracking_params: str | Any = Field(None, alias='clickTrackingParams', union_mode='left_to_right')
    command_metadata: CommandMetadata14 | Any = Field(None, alias='commandMetadata', union_mode='left_to_right')
    browse_endpoint: BrowseEndpoint2 | Any = Field(None, alias='browseEndpoint', union_mode='left_to_right')

class SignInEndpoint(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    next_endpoint: NextEndpoint | Any = Field(None, alias='nextEndpoint', union_mode='left_to_right')
    idam_tag: str | Any = Field(None, alias='idamTag', union_mode='left_to_right')

class NavigationEndpoint(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    click_tracking_params: str | Any = Field(None, alias='clickTrackingParams', union_mode='left_to_right')
    command_metadata: CommandMetadata13 | Any = Field(None, alias='commandMetadata', union_mode='left_to_right')
    sign_in_endpoint: SignInEndpoint | Any = Field(None, alias='signInEndpoint', union_mode='left_to_right')

class ButtonRenderer(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    style: str | Any = Field(default=None, union_mode='left_to_right')
    size: str | Any = Field(default=None, union_mode='left_to_right')
    is_disabled: bool | Any = Field(None, alias='isDisabled', union_mode='left_to_right')
    text: Text1 | Any = Field(default=None, union_mode='left_to_right')
    navigation_endpoint: NavigationEndpoint | Any = Field(None, alias='navigationEndpoint', union_mode='left_to_right')
    tracking_params: str | Any = Field(None, alias='trackingParams', union_mode='left_to_right')

class Button1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    button_renderer: ButtonRenderer | Any = Field(None, alias='buttonRenderer', union_mode='left_to_right')

class ModalWithTitleAndButtonRenderer(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    title: Title2 | Any = Field(default=None, union_mode='left_to_right')
    content: Content4 | Any = Field(default=None, union_mode='left_to_right')
    button: Button1 | Any = Field(default=None, union_mode='left_to_right')

class Modal(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    modal_with_title_and_button_renderer: ModalWithTitleAndButtonRenderer | Any = Field(None, alias='modalWithTitleAndButtonRenderer', union_mode='left_to_right')

class ModalEndpoint(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    modal: Modal | Any = Field(default=None, union_mode='left_to_right')

class DefaultNavigationEndpoint(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    click_tracking_params: str | Any = Field(None, alias='clickTrackingParams', union_mode='left_to_right')
    command_metadata: CommandMetadata12 | Any = Field(None, alias='commandMetadata', union_mode='left_to_right')
    modal_endpoint: ModalEndpoint | Any = Field(None, alias='modalEndpoint', union_mode='left_to_right')

class AccessibilityData1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    label: str | Any = Field(default=None, union_mode='left_to_right')

class AccessibilityData(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    accessibility_data: AccessibilityData1 | Any = Field(None, alias='accessibilityData', union_mode='left_to_right')

class AccessibilityData2(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    label: str | Any = Field(default=None, union_mode='left_to_right')

class ToggledAccessibilityData(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    accessibility_data: AccessibilityData2 | Any = Field(None, alias='accessibilityData', union_mode='left_to_right')

class ToggleButtonRenderer(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    style: Style | Any = Field(default=None, union_mode='left_to_right')
    size: Size | Any = Field(default=None, union_mode='left_to_right')
    is_toggled: bool | Any = Field(None, alias='isToggled', union_mode='left_to_right')
    is_disabled: bool | Any = Field(None, alias='isDisabled', union_mode='left_to_right')
    default_icon: DefaultIcon | Any = Field(None, alias='defaultIcon', union_mode='left_to_right')
    toggled_icon: ToggledIcon | Any = Field(None, alias='toggledIcon', union_mode='left_to_right')
    tracking_params: str | Any = Field(None, alias='trackingParams', union_mode='left_to_right')
    default_tooltip: str | Any = Field(None, alias='defaultTooltip', union_mode='left_to_right')
    toggled_tooltip: str | Any = Field(None, alias='toggledTooltip', union_mode='left_to_right')
    toggled_style: ToggledStyle | Any = Field(None, alias='toggledStyle', union_mode='left_to_right')
    default_navigation_endpoint: DefaultNavigationEndpoint | Any = Field(None, alias='defaultNavigationEndpoint', union_mode='left_to_right')
    accessibility_data: AccessibilityData | Any = Field(None, alias='accessibilityData', union_mode='left_to_right')
    toggled_accessibility_data: ToggledAccessibilityData | Any = Field(None, alias='toggledAccessibilityData', union_mode='left_to_right')

class SaveButton(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    toggle_button_renderer: ToggleButtonRenderer | Any = Field(None, alias='toggleButtonRenderer', union_mode='left_to_right')

class WebCommandMetadata15(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    send_post: bool | Any = Field(None, alias='sendPost', union_mode='left_to_right')
    api_url: str | Any = Field(None, alias='apiUrl', union_mode='left_to_right')

class CommandMetadata15(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    web_command_metadata: WebCommandMetadata15 | Any = Field(None, alias='webCommandMetadata', union_mode='left_to_right')

class Popup1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    unified_share_panel_renderer: UnifiedSharePanelRenderer | Any = Field(None, alias='unifiedSharePanelRenderer', union_mode='left_to_right')

class OpenPopupAction1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    popup: Popup1 | Any = Field(default=None, union_mode='left_to_right')
    popup_type: str | Any = Field(None, alias='popupType', union_mode='left_to_right')
    be_reused: bool | Any = Field(None, alias='beReused', union_mode='left_to_right')

class Command1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    click_tracking_params: str | Any = Field(None, alias='clickTrackingParams', union_mode='left_to_right')
    open_popup_action: OpenPopupAction1 | Any = Field(None, alias='openPopupAction', union_mode='left_to_right')

class ShareEntityServiceEndpoint1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    serialized_share_entity: str | Any = Field(None, alias='serializedShareEntity', union_mode='left_to_right')
    commands: list[Command1] | Any = Field(default=None, union_mode='left_to_right')

class NavigationEndpoint1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    click_tracking_params: str | Any = Field(None, alias='clickTrackingParams', union_mode='left_to_right')
    command_metadata: CommandMetadata15 | Any = Field(None, alias='commandMetadata', union_mode='left_to_right')
    share_entity_service_endpoint: ShareEntityServiceEndpoint1 | Any = Field(None, alias='shareEntityServiceEndpoint', union_mode='left_to_right')

class Accessibility(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    label: str | Any = Field(default=None, union_mode='left_to_right')

class AccessibilityData3(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    accessibility_data: AccessibilityData2 | Any = Field(None, alias='accessibilityData', union_mode='left_to_right')

class ButtonRenderer1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    style: str | Any = Field(default=None, union_mode='left_to_right')
    size: str | Any = Field(default=None, union_mode='left_to_right')
    is_disabled: bool | Any = Field(None, alias='isDisabled', union_mode='left_to_right')
    icon: Icon1 | Any = Field(default=None, union_mode='left_to_right')
    navigation_endpoint: NavigationEndpoint1 | Any = Field(None, alias='navigationEndpoint', union_mode='left_to_right')
    accessibility: Accessibility | Any = Field(default=None, union_mode='left_to_right')
    tooltip: str | Any = Field(default=None, union_mode='left_to_right')
    tracking_params: str | Any = Field(None, alias='trackingParams', union_mode='left_to_right')
    accessibility_data: AccessibilityData3 | Any = Field(None, alias='accessibilityData', union_mode='left_to_right')

class ShareButton(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    button_renderer: ButtonRenderer1 | Any = Field(None, alias='buttonRenderer', union_mode='left_to_right')

class Subtitle(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    simple_text: str | Any = Field(None, alias='simpleText', union_mode='left_to_right')

class WebCommandMetadata16(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    url: str | Any = Field(default=None, union_mode='left_to_right')
    web_page_type: str | Any = Field(None, alias='webPageType', union_mode='left_to_right')
    root_ve: int | Any = Field(None, alias='rootVe', union_mode='left_to_right')

class CommandMetadata16(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    web_command_metadata: WebCommandMetadata16 | Any = Field(None, alias='webCommandMetadata', union_mode='left_to_right')

class LoggingContext4(BaseModel):
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
    player_params: str | Any = Field(None, alias='playerParams', union_mode='left_to_right')
    logging_context: LoggingContext4 | Any = Field(None, alias='loggingContext', union_mode='left_to_right')
    watch_endpoint_supported_onesie_config: WatchEndpointSupportedOnesieConfig4 | Any = Field(None, alias='watchEndpointSupportedOnesieConfig', union_mode='left_to_right')

class NavigationEndpoint2(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    click_tracking_params: str | Any = Field(None, alias='clickTrackingParams', union_mode='left_to_right')
    command_metadata: CommandMetadata16 | Any = Field(None, alias='commandMetadata', union_mode='left_to_right')
    watch_endpoint: WatchEndpoint4 | Any = Field(None, alias='watchEndpoint', union_mode='left_to_right')

class ButtonRenderer2(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    style: str | Any = Field(default=None, union_mode='left_to_right')
    size: str | Any = Field(default=None, union_mode='left_to_right')
    is_disabled: bool | Any = Field(None, alias='isDisabled', union_mode='left_to_right')
    text: Text1 | Any = Field(default=None, union_mode='left_to_right')
    icon: Icon1 | Any = Field(default=None, union_mode='left_to_right')
    navigation_endpoint: NavigationEndpoint2 | Any = Field(None, alias='navigationEndpoint', union_mode='left_to_right')
    tracking_params: str | Any = Field(None, alias='trackingParams', union_mode='left_to_right')

class PlayButton(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    button_renderer: ButtonRenderer2 | Any = Field(None, alias='buttonRenderer', union_mode='left_to_right')

class CommandMetadata17(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    web_command_metadata: WebCommandMetadata16 | Any = Field(None, alias='webCommandMetadata', union_mode='left_to_right')

class LoggingContext5(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    vss_logging_context: VssLoggingContext | Any = Field(None, alias='vssLoggingContext', union_mode='left_to_right')

class Html5PlaybackOnesieConfig5(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    common_config: CommonConfig | Any = Field(None, alias='commonConfig', union_mode='left_to_right')

class WatchEndpointSupportedOnesieConfig5(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    html5_playback_onesie_config: Html5PlaybackOnesieConfig5 | Any = Field(None, alias='html5PlaybackOnesieConfig', union_mode='left_to_right')

class WatchEndpoint5(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    video_id: str | Any = Field(None, alias='videoId', union_mode='left_to_right')
    playlist_id: str | Any = Field(None, alias='playlistId', union_mode='left_to_right')
    params: str | Any = Field(default=None, union_mode='left_to_right')
    player_params: str | Any = Field(None, alias='playerParams', union_mode='left_to_right')
    logging_context: LoggingContext5 | Any = Field(None, alias='loggingContext', union_mode='left_to_right')
    watch_endpoint_supported_onesie_config: WatchEndpointSupportedOnesieConfig5 | Any = Field(None, alias='watchEndpointSupportedOnesieConfig', union_mode='left_to_right')

class NavigationEndpoint3(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    click_tracking_params: str | Any = Field(None, alias='clickTrackingParams', union_mode='left_to_right')
    command_metadata: CommandMetadata17 | Any = Field(None, alias='commandMetadata', union_mode='left_to_right')
    watch_endpoint: WatchEndpoint5 | Any = Field(None, alias='watchEndpoint', union_mode='left_to_right')

class ButtonRenderer3(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    style: str | Any = Field(default=None, union_mode='left_to_right')
    size: str | Any = Field(default=None, union_mode='left_to_right')
    is_disabled: bool | Any = Field(None, alias='isDisabled', union_mode='left_to_right')
    text: Text1 | Any = Field(default=None, union_mode='left_to_right')
    icon: Icon1 | Any = Field(default=None, union_mode='left_to_right')
    navigation_endpoint: NavigationEndpoint3 | Any = Field(None, alias='navigationEndpoint', union_mode='left_to_right')
    tracking_params: str | Any = Field(None, alias='trackingParams', union_mode='left_to_right')

class ShufflePlayButton(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    button_renderer: ButtonRenderer3 | Any = Field(None, alias='buttonRenderer', union_mode='left_to_right')

class Thumbnail3(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    url: str | Any = Field(default=None, union_mode='left_to_right')
    width: int | Any = Field(default=None, union_mode='left_to_right')
    height: int | Any = Field(default=None, union_mode='left_to_right')

class Thumbnail2(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    thumbnails: list[Thumbnail3] | Any = Field(default=None, union_mode='left_to_right')

class BackgroundImageConfig(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    thumbnail: Thumbnail2 | Any = Field(default=None, union_mode='left_to_right')

class GradientColorConfigItem(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    light_theme_color: int | Any = Field(None, alias='lightThemeColor', union_mode='left_to_right')
    dark_theme_color: int | Any = Field(None, alias='darkThemeColor', union_mode='left_to_right')
    start_location: int | float | Any = Field(None, alias='startLocation', union_mode='left_to_right')

class Config(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    light_theme_background_color: int | Any = Field(None, alias='lightThemeBackgroundColor', union_mode='left_to_right')
    dark_theme_background_color: int | Any = Field(None, alias='darkThemeBackgroundColor', union_mode='left_to_right')
    color_source_size_multiplier: int | Any = Field(None, alias='colorSourceSizeMultiplier', union_mode='left_to_right')
    apply_client_image_blur: bool | Any = Field(None, alias='applyClientImageBlur', union_mode='left_to_right')

class CinematicContainerRenderer(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    background_image_config: BackgroundImageConfig | Any = Field(None, alias='backgroundImageConfig', union_mode='left_to_right')
    gradient_color_config: list[GradientColorConfigItem] | Any = Field(None, alias='gradientColorConfig', union_mode='left_to_right')
    config: Config | Any = Field(default=None, union_mode='left_to_right')

class CinematicContainer(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    cinematic_container_renderer: CinematicContainerRenderer | Any = Field(None, alias='cinematicContainerRenderer', union_mode='left_to_right')

class Text5(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    runs: list[Run] | Any = Field(default=None, union_mode='left_to_right')
    simple_text: str | Any = Field(None, alias='simpleText', union_mode='left_to_right')

class PlaylistBylineRenderer(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    text: Text5 | Any = Field(default=None, union_mode='left_to_right')

class BylineItem(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    playlist_byline_renderer: PlaylistBylineRenderer | Any = Field(None, alias='playlistBylineRenderer', union_mode='left_to_right')

class PlaylistHeaderRenderer(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    playlist_id: str | Any = Field(None, alias='playlistId', union_mode='left_to_right')
    title: Title2 | Any = Field(default=None, union_mode='left_to_right')
    num_videos_text: NumVideosText | Any = Field(None, alias='numVideosText', union_mode='left_to_right')
    view_count_text: ViewCountText | Any = Field(None, alias='viewCountText', union_mode='left_to_right')
    share_data: ShareData | Any = Field(None, alias='shareData', union_mode='left_to_right')
    is_editable: bool | Any = Field(None, alias='isEditable', union_mode='left_to_right')
    editable_details: EditableDetails | Any = Field(None, alias='editableDetails', union_mode='left_to_right')
    tracking_params: str | Any = Field(None, alias='trackingParams', union_mode='left_to_right')
    service_endpoints: list[ServiceEndpoint] | Any = Field(None, alias='serviceEndpoints', union_mode='left_to_right')
    stats: list[Stat] | Any = Field(default=None, union_mode='left_to_right')
    brief_stats: list[BriefStat] | Any = Field(None, alias='briefStats', union_mode='left_to_right')
    playlist_header_banner: PlaylistHeaderBanner | Any = Field(None, alias='playlistHeaderBanner', union_mode='left_to_right')
    save_button: SaveButton | Any = Field(None, alias='saveButton', union_mode='left_to_right')
    share_button: ShareButton | Any = Field(None, alias='shareButton', union_mode='left_to_right')
    subtitle: Subtitle | Any = Field(default=None, union_mode='left_to_right')
    play_button: PlayButton | Any = Field(None, alias='playButton', union_mode='left_to_right')
    shuffle_play_button: ShufflePlayButton | Any = Field(None, alias='shufflePlayButton', union_mode='left_to_right')
    cinematic_container: CinematicContainer | Any = Field(None, alias='cinematicContainer', union_mode='left_to_right')
    byline: list[BylineItem] | Any = Field(default=None, union_mode='left_to_right')

class Header(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    playlist_header_renderer: PlaylistHeaderRenderer | Any = Field(None, alias='playlistHeaderRenderer', union_mode='left_to_right')

class PlaylistMetadataRenderer(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    title: str | Any = Field(default=None, union_mode='left_to_right')
    play_url: str | Any = Field(None, alias='playUrl', union_mode='left_to_right')
    android_play_url: str | Any = Field(None, alias='androidPlayUrl', union_mode='left_to_right')
    album_name: str | Any = Field(None, alias='albumName', union_mode='left_to_right')
    android_appindexing_link: str | Any = Field(None, alias='androidAppindexingLink', union_mode='left_to_right')
    ios_appindexing_link: str | Any = Field(None, alias='iosAppindexingLink', union_mode='left_to_right')

class Metadata2(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    playlist_metadata_renderer: PlaylistMetadataRenderer | Any = Field(None, alias='playlistMetadataRenderer', union_mode='left_to_right')

class IconImage(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    icon_type: str | Any = Field(None, alias='iconType', union_mode='left_to_right')

class TooltipText(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    runs: list[Run] | Any = Field(default=None, union_mode='left_to_right')

class WebCommandMetadata18(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    url: str | Any = Field(default=None, union_mode='left_to_right')
    web_page_type: str | Any = Field(None, alias='webPageType', union_mode='left_to_right')
    root_ve: int | Any = Field(None, alias='rootVe', union_mode='left_to_right')
    api_url: str | Any = Field(None, alias='apiUrl', union_mode='left_to_right')

class CommandMetadata18(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    web_command_metadata: WebCommandMetadata18 | Any = Field(None, alias='webCommandMetadata', union_mode='left_to_right')

class Endpoint(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    click_tracking_params: str | Any = Field(None, alias='clickTrackingParams', union_mode='left_to_right')
    command_metadata: CommandMetadata18 | Any = Field(None, alias='commandMetadata', union_mode='left_to_right')
    browse_endpoint: BrowseEndpoint2 | Any = Field(None, alias='browseEndpoint', union_mode='left_to_right')

class TopbarLogoRenderer(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    icon_image: IconImage | Any = Field(None, alias='iconImage', union_mode='left_to_right')
    tooltip_text: TooltipText | Any = Field(None, alias='tooltipText', union_mode='left_to_right')
    endpoint: Endpoint | Any = Field(default=None, union_mode='left_to_right')
    tracking_params: str | Any = Field(None, alias='trackingParams', union_mode='left_to_right')
    override_entity_key: str | Any = Field(None, alias='overrideEntityKey', union_mode='left_to_right')

class Logo(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    topbar_logo_renderer: TopbarLogoRenderer | Any = Field(None, alias='topbarLogoRenderer', union_mode='left_to_right')

class PlaceholderText(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    runs: list[Run] | Any = Field(default=None, union_mode='left_to_right')

class WebSearchboxConfig(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    request_language: str | Any = Field(None, alias='requestLanguage', union_mode='left_to_right')
    request_domain: str | Any = Field(None, alias='requestDomain', union_mode='left_to_right')
    has_onscreen_keyboard: bool | Any = Field(None, alias='hasOnscreenKeyboard', union_mode='left_to_right')
    focus_searchbox: bool | Any = Field(None, alias='focusSearchbox', union_mode='left_to_right')

class Config1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    web_searchbox_config: WebSearchboxConfig | Any = Field(None, alias='webSearchboxConfig', union_mode='left_to_right')

class WebCommandMetadata19(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    url: str | Any = Field(default=None, union_mode='left_to_right')
    web_page_type: str | Any = Field(None, alias='webPageType', union_mode='left_to_right')
    root_ve: int | Any = Field(None, alias='rootVe', union_mode='left_to_right')

class CommandMetadata19(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    web_command_metadata: WebCommandMetadata19 | Any = Field(None, alias='webCommandMetadata', union_mode='left_to_right')

class SearchEndpoint1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    query: str | Any = Field(default=None, union_mode='left_to_right')

class SearchEndpoint(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    click_tracking_params: str | Any = Field(None, alias='clickTrackingParams', union_mode='left_to_right')
    command_metadata: CommandMetadata19 | Any = Field(None, alias='commandMetadata', union_mode='left_to_right')
    search_endpoint: SearchEndpoint1 | Any = Field(None, alias='searchEndpoint', union_mode='left_to_right')

class AccessibilityData6(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    label: str | Any = Field(default=None, union_mode='left_to_right')

class AccessibilityData5(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    accessibility_data: AccessibilityData6 | Any = Field(None, alias='accessibilityData', union_mode='left_to_right')

class ButtonRenderer4(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    style: str | Any = Field(default=None, union_mode='left_to_right')
    size: str | Any = Field(default=None, union_mode='left_to_right')
    is_disabled: bool | Any = Field(None, alias='isDisabled', union_mode='left_to_right')
    icon: Icon1 | Any = Field(default=None, union_mode='left_to_right')
    tracking_params: str | Any = Field(None, alias='trackingParams', union_mode='left_to_right')
    accessibility_data: AccessibilityData5 | Any = Field(None, alias='accessibilityData', union_mode='left_to_right')

class ClearButton(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    button_renderer: ButtonRenderer4 | Any = Field(None, alias='buttonRenderer', union_mode='left_to_right')

class Headline(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    content: str | Any = Field(default=None, union_mode='left_to_right')

class DialogHeaderViewModel(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    headline: Headline | Any = Field(default=None, union_mode='left_to_right')

class Header1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    dialog_header_view_model: DialogHeaderViewModel | Any = Field(None, alias='dialogHeaderViewModel', union_mode='left_to_right')

class ButtonViewModel3(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    title: str | Any = Field(default=None, union_mode='left_to_right')
    style: str | Any = Field(default=None, union_mode='left_to_right')
    tracking_params: str | Any = Field(None, alias='trackingParams', union_mode='left_to_right')
    is_full_width: bool | Any = Field(None, alias='isFullWidth', union_mode='left_to_right')
    type: str | Any = Field(default=None, union_mode='left_to_right')

class PrimaryButton(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    button_view_model: ButtonViewModel3 | Any = Field(None, alias='buttonViewModel', union_mode='left_to_right')

class SecondaryButton(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    button_view_model: ButtonViewModel3 | Any = Field(None, alias='buttonViewModel', union_mode='left_to_right')

class PanelFooterViewModel(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    primary_button: PrimaryButton | Any = Field(None, alias='primaryButton', union_mode='left_to_right')
    secondary_button: SecondaryButton | Any = Field(None, alias='secondaryButton', union_mode='left_to_right')
    should_hide_divider: bool | Any = Field(None, alias='shouldHideDivider', union_mode='left_to_right')

class Footer(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    panel_footer_view_model: PanelFooterViewModel | Any = Field(None, alias='panelFooterViewModel', union_mode='left_to_right')

class Text6(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    content: str | Any = Field(default=None, union_mode='left_to_right')

class Paragraph(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    text: Text6 | Any = Field(default=None, union_mode='left_to_right')

class BasicContentViewModel(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    paragraphs: list[Paragraph] | Any = Field(default=None, union_mode='left_to_right')

class Content5(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    basic_content_view_model: BasicContentViewModel | Any = Field(None, alias='basicContentViewModel', union_mode='left_to_right')

class DialogViewModel(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    header: Header1 | Any = Field(default=None, union_mode='left_to_right')
    footer: Footer | Any = Field(default=None, union_mode='left_to_right')
    content: Content5 | Any = Field(default=None, union_mode='left_to_right')

class InlineContent1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    dialog_view_model: DialogViewModel | Any = Field(None, alias='dialogViewModel', union_mode='left_to_right')

class PanelLoadingStrategy1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    inline_content: InlineContent1 | Any = Field(None, alias='inlineContent', union_mode='left_to_right')

class ShowDialogCommand(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    panel_loading_strategy: PanelLoadingStrategy1 | Any = Field(None, alias='panelLoadingStrategy', union_mode='left_to_right')

class ShowImageSourceDialog(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    click_tracking_params: str | Any = Field(None, alias='clickTrackingParams', union_mode='left_to_right')
    show_dialog_command: ShowDialogCommand | Any = Field(None, alias='showDialogCommand', union_mode='left_to_right')

class FusionSearchboxRenderer(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    icon: Icon1 | Any = Field(default=None, union_mode='left_to_right')
    placeholder_text: PlaceholderText | Any = Field(None, alias='placeholderText', union_mode='left_to_right')
    config: Config1 | Any = Field(default=None, union_mode='left_to_right')
    tracking_params: str | Any = Field(None, alias='trackingParams', union_mode='left_to_right')
    search_endpoint: SearchEndpoint | Any = Field(None, alias='searchEndpoint', union_mode='left_to_right')
    clear_button: ClearButton | Any = Field(None, alias='clearButton', union_mode='left_to_right')
    show_image_source_dialog: ShowImageSourceDialog | Any = Field(None, alias='showImageSourceDialog', union_mode='left_to_right')
    disable_ai_appearance: bool | Any = Field(None, alias='disableAiAppearance', union_mode='left_to_right')

class Searchbox(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    fusion_searchbox_renderer: FusionSearchboxRenderer | Any = Field(None, alias='fusionSearchboxRenderer', union_mode='left_to_right')

class WebCommandMetadata20(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    send_post: bool | Any = Field(None, alias='sendPost', union_mode='left_to_right')
    api_url: str | Any = Field(None, alias='apiUrl', union_mode='left_to_right')

class CommandMetadata20(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    web_command_metadata: WebCommandMetadata20 | Any = Field(None, alias='webCommandMetadata', union_mode='left_to_right')

class MultiPageMenuRenderer(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    tracking_params: str | Any = Field(None, alias='trackingParams', union_mode='left_to_right')
    style: str | Any = Field(default=None, union_mode='left_to_right')
    show_loading_spinner: bool | Any = Field(None, alias='showLoadingSpinner', union_mode='left_to_right')

class Popup2(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    multi_page_menu_renderer: MultiPageMenuRenderer | Any = Field(None, alias='multiPageMenuRenderer', union_mode='left_to_right')

class OpenPopupAction2(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    popup: Popup2 | Any = Field(default=None, union_mode='left_to_right')
    popup_type: str | Any = Field(None, alias='popupType', union_mode='left_to_right')
    be_reused: bool | Any = Field(None, alias='beReused', union_mode='left_to_right')

class Action5(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    click_tracking_params: str | Any = Field(None, alias='clickTrackingParams', union_mode='left_to_right')
    open_popup_action: OpenPopupAction2 | Any = Field(None, alias='openPopupAction', union_mode='left_to_right')

class SignalServiceEndpoint2(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    signal: str | Any = Field(default=None, union_mode='left_to_right')
    actions: list[Action5] | Any = Field(default=None, union_mode='left_to_right')

class MenuRequest(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    click_tracking_params: str | Any = Field(None, alias='clickTrackingParams', union_mode='left_to_right')
    command_metadata: CommandMetadata20 | Any = Field(None, alias='commandMetadata', union_mode='left_to_right')
    signal_service_endpoint: SignalServiceEndpoint2 | Any = Field(None, alias='signalServiceEndpoint', union_mode='left_to_right')

class AccessibilityData7(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    label: str | Any = Field(default=None, union_mode='left_to_right')

class Accessibility1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    accessibility_data: AccessibilityData7 | Any = Field(None, alias='accessibilityData', union_mode='left_to_right')

class TopbarMenuButtonRenderer(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    icon: Icon1 | Any = Field(default=None, union_mode='left_to_right')
    menu_request: MenuRequest | Any = Field(None, alias='menuRequest', union_mode='left_to_right')
    tracking_params: str | Any = Field(None, alias='trackingParams', union_mode='left_to_right')
    accessibility: Accessibility1 | Any = Field(default=None, union_mode='left_to_right')
    tooltip: str | Any = Field(default=None, union_mode='left_to_right')
    style: str | Any = Field(default=None, union_mode='left_to_right')

class Text7(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    runs: list[Run] | Any = Field(default=None, union_mode='left_to_right')

class WebCommandMetadata21(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    url: str | Any = Field(default=None, union_mode='left_to_right')
    web_page_type: str | Any = Field(None, alias='webPageType', union_mode='left_to_right')
    root_ve: int | Any = Field(None, alias='rootVe', union_mode='left_to_right')

class CommandMetadata21(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    web_command_metadata: WebCommandMetadata21 | Any = Field(None, alias='webCommandMetadata', union_mode='left_to_right')

class SignInEndpoint1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    idam_tag: str | Any = Field(None, alias='idamTag', union_mode='left_to_right')

class NavigationEndpoint4(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    click_tracking_params: str | Any = Field(None, alias='clickTrackingParams', union_mode='left_to_right')
    command_metadata: CommandMetadata21 | Any = Field(None, alias='commandMetadata', union_mode='left_to_right')
    sign_in_endpoint: SignInEndpoint1 | Any = Field(None, alias='signInEndpoint', union_mode='left_to_right')

class ButtonRenderer5(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    style: str | Any = Field(default=None, union_mode='left_to_right')
    size: str | Any = Field(default=None, union_mode='left_to_right')
    text: Text7 | Any = Field(default=None, union_mode='left_to_right')
    icon: Icon1 | Any = Field(default=None, union_mode='left_to_right')
    navigation_endpoint: NavigationEndpoint4 | Any = Field(None, alias='navigationEndpoint', union_mode='left_to_right')
    tracking_params: str | Any = Field(None, alias='trackingParams', union_mode='left_to_right')
    target_id: str | Any = Field(None, alias='targetId', union_mode='left_to_right')

class TopbarButton(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    topbar_menu_button_renderer: TopbarMenuButtonRenderer | Any = Field(None, alias='topbarMenuButtonRenderer', union_mode='left_to_right')
    button_renderer: ButtonRenderer5 | Any = Field(None, alias='buttonRenderer', union_mode='left_to_right')

class Title4(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    runs: list[Run] | Any = Field(default=None, union_mode='left_to_right')

class Title5(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    runs: list[Run] | Any = Field(default=None, union_mode='left_to_right')

class Label(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    runs: list[Run] | Any = Field(default=None, union_mode='left_to_right')

class HotkeyAccessibilityLabel(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    accessibility_data: AccessibilityData7 | Any = Field(None, alias='accessibilityData', union_mode='left_to_right')

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
    title: Title5 | Any = Field(default=None, union_mode='left_to_right')
    options: list[Option] | Any = Field(default=None, union_mode='left_to_right')

class Section(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    hotkey_dialog_section_renderer: HotkeyDialogSectionRenderer | Any = Field(None, alias='hotkeyDialogSectionRenderer', union_mode='left_to_right')

class Text8(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    runs: list[Run] | Any = Field(default=None, union_mode='left_to_right')

class ButtonRenderer6(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    style: str | Any = Field(default=None, union_mode='left_to_right')
    size: str | Any = Field(default=None, union_mode='left_to_right')
    is_disabled: bool | Any = Field(None, alias='isDisabled', union_mode='left_to_right')
    text: Text8 | Any = Field(default=None, union_mode='left_to_right')
    tracking_params: str | Any = Field(None, alias='trackingParams', union_mode='left_to_right')

class DismissButton(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    button_renderer: ButtonRenderer6 | Any = Field(None, alias='buttonRenderer', union_mode='left_to_right')

class HotkeyDialogRenderer(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    title: Title4 | Any = Field(default=None, union_mode='left_to_right')
    sections: list[Section] | Any = Field(default=None, union_mode='left_to_right')
    dismiss_button: DismissButton | Any = Field(None, alias='dismissButton', union_mode='left_to_right')
    tracking_params: str | Any = Field(None, alias='trackingParams', union_mode='left_to_right')

class HotkeyDialog(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    hotkey_dialog_renderer: HotkeyDialogRenderer | Any = Field(None, alias='hotkeyDialogRenderer', union_mode='left_to_right')

class WebCommandMetadata22(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    send_post: bool | Any = Field(None, alias='sendPost', union_mode='left_to_right')

class CommandMetadata22(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    web_command_metadata: WebCommandMetadata22 | Any = Field(None, alias='webCommandMetadata', union_mode='left_to_right')

class SignalAction(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    signal: str | Any = Field(default=None, union_mode='left_to_right')

class Action6(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    click_tracking_params: str | Any = Field(None, alias='clickTrackingParams', union_mode='left_to_right')
    signal_action: SignalAction | Any = Field(None, alias='signalAction', union_mode='left_to_right')

class SignalServiceEndpoint3(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    signal: str | Any = Field(default=None, union_mode='left_to_right')
    actions: list[Action6] | Any = Field(default=None, union_mode='left_to_right')

class Command2(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    click_tracking_params: str | Any = Field(None, alias='clickTrackingParams', union_mode='left_to_right')
    command_metadata: CommandMetadata22 | Any = Field(None, alias='commandMetadata', union_mode='left_to_right')
    signal_service_endpoint: SignalServiceEndpoint3 | Any = Field(None, alias='signalServiceEndpoint', union_mode='left_to_right')

class ButtonRenderer7(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    tracking_params: str | Any = Field(None, alias='trackingParams', union_mode='left_to_right')
    command: Command2 | Any = Field(default=None, union_mode='left_to_right')

class BackButton(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    button_renderer: ButtonRenderer7 | Any = Field(None, alias='buttonRenderer', union_mode='left_to_right')

class CommandMetadata23(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    web_command_metadata: WebCommandMetadata22 | Any = Field(None, alias='webCommandMetadata', union_mode='left_to_right')

class Action7(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    click_tracking_params: str | Any = Field(None, alias='clickTrackingParams', union_mode='left_to_right')
    signal_action: SignalAction | Any = Field(None, alias='signalAction', union_mode='left_to_right')

class SignalServiceEndpoint4(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    signal: str | Any = Field(default=None, union_mode='left_to_right')
    actions: list[Action7] | Any = Field(default=None, union_mode='left_to_right')

class Command3(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    click_tracking_params: str | Any = Field(None, alias='clickTrackingParams', union_mode='left_to_right')
    command_metadata: CommandMetadata23 | Any = Field(None, alias='commandMetadata', union_mode='left_to_right')
    signal_service_endpoint: SignalServiceEndpoint4 | Any = Field(None, alias='signalServiceEndpoint', union_mode='left_to_right')

class ButtonRenderer8(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    tracking_params: str | Any = Field(None, alias='trackingParams', union_mode='left_to_right')
    command: Command3 | Any = Field(default=None, union_mode='left_to_right')

class ForwardButton(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    button_renderer: ButtonRenderer8 | Any = Field(None, alias='buttonRenderer', union_mode='left_to_right')

class Text9(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    runs: list[Run] | Any = Field(default=None, union_mode='left_to_right')

class CommandMetadata24(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    web_command_metadata: WebCommandMetadata22 | Any = Field(None, alias='webCommandMetadata', union_mode='left_to_right')

class Action8(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    click_tracking_params: str | Any = Field(None, alias='clickTrackingParams', union_mode='left_to_right')
    signal_action: SignalAction | Any = Field(None, alias='signalAction', union_mode='left_to_right')

class SignalServiceEndpoint5(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    signal: str | Any = Field(default=None, union_mode='left_to_right')
    actions: list[Action8] | Any = Field(default=None, union_mode='left_to_right')

class Command4(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    click_tracking_params: str | Any = Field(None, alias='clickTrackingParams', union_mode='left_to_right')
    command_metadata: CommandMetadata24 | Any = Field(None, alias='commandMetadata', union_mode='left_to_right')
    signal_service_endpoint: SignalServiceEndpoint5 | Any = Field(None, alias='signalServiceEndpoint', union_mode='left_to_right')

class ButtonRenderer9(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    style: str | Any = Field(default=None, union_mode='left_to_right')
    size: str | Any = Field(default=None, union_mode='left_to_right')
    is_disabled: bool | Any = Field(None, alias='isDisabled', union_mode='left_to_right')
    text: Text9 | Any = Field(default=None, union_mode='left_to_right')
    tracking_params: str | Any = Field(None, alias='trackingParams', union_mode='left_to_right')
    command: Command4 | Any = Field(default=None, union_mode='left_to_right')

class A11ySkipNavigationButton(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    button_renderer: ButtonRenderer9 | Any = Field(None, alias='buttonRenderer', union_mode='left_to_right')

class CommandMetadata25(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    web_command_metadata: WebCommandMetadata22 | Any = Field(None, alias='webCommandMetadata', union_mode='left_to_right')

class PlaceholderHeader(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    runs: list[Run] | Any = Field(default=None, union_mode='left_to_right')

class PromptHeader(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    runs: list[Run] | Any = Field(default=None, union_mode='left_to_right')

class ExampleQuery1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    runs: list[Run] | Any = Field(default=None, union_mode='left_to_right')

class ExampleQuery2(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    runs: list[Run] | Any = Field(default=None, union_mode='left_to_right')

class PromptMicrophoneLabel(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    runs: list[Run] | Any = Field(default=None, union_mode='left_to_right')

class LoadingHeader(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    runs: list[Run] | Any = Field(default=None, union_mode='left_to_right')

class ConnectionErrorHeader(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    runs: list[Run] | Any = Field(default=None, union_mode='left_to_right')

class ConnectionErrorMicrophoneLabel(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    runs: list[Run] | Any = Field(default=None, union_mode='left_to_right')

class PermissionsHeader(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    runs: list[Run] | Any = Field(default=None, union_mode='left_to_right')

class PermissionsSubtext(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    runs: list[Run] | Any = Field(default=None, union_mode='left_to_right')

class DisabledHeader(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    runs: list[Run] | Any = Field(default=None, union_mode='left_to_right')

class DisabledSubtext(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    runs: list[Run] | Any = Field(default=None, union_mode='left_to_right')

class MicrophoneButtonAriaLabel(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    runs: list[Run] | Any = Field(default=None, union_mode='left_to_right')

class AccessibilityData9(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    accessibility_data: AccessibilityData7 | Any = Field(None, alias='accessibilityData', union_mode='left_to_right')

class ButtonRenderer11(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    style: str | Any = Field(default=None, union_mode='left_to_right')
    size: str | Any = Field(default=None, union_mode='left_to_right')
    is_disabled: bool | Any = Field(None, alias='isDisabled', union_mode='left_to_right')
    icon: Icon1 | Any = Field(default=None, union_mode='left_to_right')
    tracking_params: str | Any = Field(None, alias='trackingParams', union_mode='left_to_right')
    accessibility_data: AccessibilityData9 | Any = Field(None, alias='accessibilityData', union_mode='left_to_right')

class ExitButton(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    button_renderer: ButtonRenderer11 | Any = Field(None, alias='buttonRenderer', union_mode='left_to_right')

class MicrophoneOffPromptHeader(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    runs: list[Run] | Any = Field(default=None, union_mode='left_to_right')

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

class Popup3(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    voice_search_dialog_renderer: VoiceSearchDialogRenderer | Any = Field(None, alias='voiceSearchDialogRenderer', union_mode='left_to_right')

class OpenPopupAction3(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    popup: Popup3 | Any = Field(default=None, union_mode='left_to_right')
    popup_type: str | Any = Field(None, alias='popupType', union_mode='left_to_right')

class Action9(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    click_tracking_params: str | Any = Field(None, alias='clickTrackingParams', union_mode='left_to_right')
    open_popup_action: OpenPopupAction3 | Any = Field(None, alias='openPopupAction', union_mode='left_to_right')

class SignalServiceEndpoint6(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    signal: str | Any = Field(default=None, union_mode='left_to_right')
    actions: list[Action9] | Any = Field(default=None, union_mode='left_to_right')

class ServiceEndpoint1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    click_tracking_params: str | Any = Field(None, alias='clickTrackingParams', union_mode='left_to_right')
    command_metadata: CommandMetadata25 | Any = Field(None, alias='commandMetadata', union_mode='left_to_right')
    signal_service_endpoint: SignalServiceEndpoint6 | Any = Field(None, alias='signalServiceEndpoint', union_mode='left_to_right')

class AccessibilityData12(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    label: str | Any = Field(default=None, union_mode='left_to_right')

class AccessibilityData11(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    accessibility_data: AccessibilityData12 | Any = Field(None, alias='accessibilityData', union_mode='left_to_right')

class ButtonRenderer10(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    style: str | Any = Field(default=None, union_mode='left_to_right')
    size: str | Any = Field(default=None, union_mode='left_to_right')
    is_disabled: bool | Any = Field(None, alias='isDisabled', union_mode='left_to_right')
    service_endpoint: ServiceEndpoint1 | Any = Field(None, alias='serviceEndpoint', union_mode='left_to_right')
    icon: Icon1 | Any = Field(default=None, union_mode='left_to_right')
    tooltip: str | Any = Field(default=None, union_mode='left_to_right')
    tracking_params: str | Any = Field(None, alias='trackingParams', union_mode='left_to_right')
    accessibility_data: AccessibilityData11 | Any = Field(None, alias='accessibilityData', union_mode='left_to_right')

class VoiceSearchButton(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    button_renderer: ButtonRenderer10 | Any = Field(None, alias='buttonRenderer', union_mode='left_to_right')

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

class Thumbnail5(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    url: str | Any = Field(default=None, union_mode='left_to_right')
    width: int | Any = Field(default=None, union_mode='left_to_right')
    height: int | Any = Field(default=None, union_mode='left_to_right')

class Thumbnail4(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    thumbnails: list[Thumbnail5] | Any = Field(default=None, union_mode='left_to_right')
    sampled_thumbnail_color: SampledThumbnailColor | Any = Field(None, alias='sampledThumbnailColor', union_mode='left_to_right')
    dark_color_palette: DarkColorPalette | Any = Field(None, alias='darkColorPalette', union_mode='left_to_right')
    vibrant_color_palette: VibrantColorPalette | Any = Field(None, alias='vibrantColorPalette', union_mode='left_to_right')

class LinkAlternate(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    href_url: str | Any = Field(None, alias='hrefUrl', union_mode='left_to_right')

class MicroformatDataRenderer(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    url_canonical: str | Any = Field(None, alias='urlCanonical', union_mode='left_to_right')
    title: str | Any = Field(default=None, union_mode='left_to_right')
    description: str | Any = Field(default=None, union_mode='left_to_right')
    thumbnail: Thumbnail4 | Any = Field(default=None, union_mode='left_to_right')
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
    link_alternates: list[LinkAlternate] | Any = Field(None, alias='linkAlternates', union_mode='left_to_right')

class Microformat(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    microformat_data_renderer: MicroformatDataRenderer | Any = Field(None, alias='microformatDataRenderer', union_mode='left_to_right')

class Thumbnail7(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    url: str | Any = Field(default=None, union_mode='left_to_right')
    width: int | Any = Field(default=None, union_mode='left_to_right')
    height: int | Any = Field(default=None, union_mode='left_to_right')

class Thumbnail6(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    thumbnails: list[Thumbnail7] | Any = Field(default=None, union_mode='left_to_right')
    sampled_thumbnail_color: SampledThumbnailColor | Any = Field(None, alias='sampledThumbnailColor', union_mode='left_to_right')
    dark_color_palette: DarkColorPalette | Any = Field(None, alias='darkColorPalette', union_mode='left_to_right')
    vibrant_color_palette: VibrantColorPalette | Any = Field(None, alias='vibrantColorPalette', union_mode='left_to_right')

class PlaylistCustomThumbnailRenderer(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    thumbnail: Thumbnail6 | Any = Field(default=None, union_mode='left_to_right')

class ThumbnailRenderer(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    playlist_custom_thumbnail_renderer: PlaylistCustomThumbnailRenderer | Any = Field(None, alias='playlistCustomThumbnailRenderer', union_mode='left_to_right')

class WebCommandMetadata26(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    url: str | Any = Field(default=None, union_mode='left_to_right')
    web_page_type: str | Any = Field(None, alias='webPageType', union_mode='left_to_right')
    root_ve: int | Any = Field(None, alias='rootVe', union_mode='left_to_right')

class CommandMetadata26(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    web_command_metadata: WebCommandMetadata26 | Any = Field(None, alias='webCommandMetadata', union_mode='left_to_right')

class LoggingContext6(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    vss_logging_context: VssLoggingContext | Any = Field(None, alias='vssLoggingContext', union_mode='left_to_right')

class Html5PlaybackOnesieConfig6(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    common_config: CommonConfig | Any = Field(None, alias='commonConfig', union_mode='left_to_right')

class WatchEndpointSupportedOnesieConfig6(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    html5_playback_onesie_config: Html5PlaybackOnesieConfig6 | Any = Field(None, alias='html5PlaybackOnesieConfig', union_mode='left_to_right')

class WatchEndpoint6(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    video_id: str | Any = Field(None, alias='videoId', union_mode='left_to_right')
    playlist_id: str | Any = Field(None, alias='playlistId', union_mode='left_to_right')
    player_params: str | Any = Field(None, alias='playerParams', union_mode='left_to_right')
    logging_context: LoggingContext6 | Any = Field(None, alias='loggingContext', union_mode='left_to_right')
    watch_endpoint_supported_onesie_config: WatchEndpointSupportedOnesieConfig6 | Any = Field(None, alias='watchEndpointSupportedOnesieConfig', union_mode='left_to_right')

class NavigationEndpoint5(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    click_tracking_params: str | Any = Field(None, alias='clickTrackingParams', union_mode='left_to_right')
    command_metadata: CommandMetadata26 | Any = Field(None, alias='commandMetadata', union_mode='left_to_right')
    watch_endpoint: WatchEndpoint6 | Any = Field(None, alias='watchEndpoint', union_mode='left_to_right')

class Run26(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    text: str | Any = Field(default=None, union_mode='left_to_right')
    navigation_endpoint: NavigationEndpoint5 | Any = Field(None, alias='navigationEndpoint', union_mode='left_to_right')

class Title6(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    runs: list[Run26] | Any = Field(default=None, union_mode='left_to_right')

class Run27(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    text: str | Any = Field(default=None, union_mode='left_to_right')

class Stat1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    runs: list[Run27] | Any = Field(default=None, union_mode='left_to_right')
    simple_text: str | Any = Field(None, alias='simpleText', union_mode='left_to_right')

class Text10(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    simple_text: str | Any = Field(None, alias='simpleText', union_mode='left_to_right')

class WebCommandMetadata27(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    ignore_navigation: bool | Any = Field(None, alias='ignoreNavigation', union_mode='left_to_right')

class CommandMetadata27(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    web_command_metadata: WebCommandMetadata27 | Any = Field(None, alias='webCommandMetadata', union_mode='left_to_right')

class Title7(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    simple_text: str | Any = Field(None, alias='simpleText', union_mode='left_to_right')

class Content6(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    simple_text: str | Any = Field(None, alias='simpleText', union_mode='left_to_right')

class Text11(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    runs: list[Run27] | Any = Field(default=None, union_mode='left_to_right')

class WebCommandMetadata28(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    url: str | Any = Field(default=None, union_mode='left_to_right')
    web_page_type: str | Any = Field(None, alias='webPageType', union_mode='left_to_right')
    root_ve: int | Any = Field(None, alias='rootVe', union_mode='left_to_right')

class CommandMetadata28(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    web_command_metadata: WebCommandMetadata28 | Any = Field(None, alias='webCommandMetadata', union_mode='left_to_right')

class WebCommandMetadata29(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    url: str | Any = Field(default=None, union_mode='left_to_right')
    web_page_type: str | Any = Field(None, alias='webPageType', union_mode='left_to_right')
    root_ve: int | Any = Field(None, alias='rootVe', union_mode='left_to_right')
    api_url: str | Any = Field(None, alias='apiUrl', union_mode='left_to_right')

class CommandMetadata29(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    web_command_metadata: WebCommandMetadata29 | Any = Field(None, alias='webCommandMetadata', union_mode='left_to_right')

class NextEndpoint1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    click_tracking_params: str | Any = Field(None, alias='clickTrackingParams', union_mode='left_to_right')
    command_metadata: CommandMetadata29 | Any = Field(None, alias='commandMetadata', union_mode='left_to_right')
    browse_endpoint: BrowseEndpoint2 | Any = Field(None, alias='browseEndpoint', union_mode='left_to_right')

class SignInEndpoint2(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    next_endpoint: NextEndpoint1 | Any = Field(None, alias='nextEndpoint', union_mode='left_to_right')

class NavigationEndpoint7(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    click_tracking_params: str | Any = Field(None, alias='clickTrackingParams', union_mode='left_to_right')
    command_metadata: CommandMetadata28 | Any = Field(None, alias='commandMetadata', union_mode='left_to_right')
    sign_in_endpoint: SignInEndpoint2 | Any = Field(None, alias='signInEndpoint', union_mode='left_to_right')

class ButtonRenderer12(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    style: str | Any = Field(default=None, union_mode='left_to_right')
    size: str | Any = Field(default=None, union_mode='left_to_right')
    is_disabled: bool | Any = Field(None, alias='isDisabled', union_mode='left_to_right')
    text: Text11 | Any = Field(default=None, union_mode='left_to_right')
    navigation_endpoint: NavigationEndpoint7 | Any = Field(None, alias='navigationEndpoint', union_mode='left_to_right')
    tracking_params: str | Any = Field(None, alias='trackingParams', union_mode='left_to_right')

class Button2(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    button_renderer: ButtonRenderer12 | Any = Field(None, alias='buttonRenderer', union_mode='left_to_right')

class ModalWithTitleAndButtonRenderer1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    title: Title7 | Any = Field(default=None, union_mode='left_to_right')
    content: Content6 | Any = Field(default=None, union_mode='left_to_right')
    button: Button2 | Any = Field(default=None, union_mode='left_to_right')

class Modal1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    modal_with_title_and_button_renderer: ModalWithTitleAndButtonRenderer1 | Any = Field(None, alias='modalWithTitleAndButtonRenderer', union_mode='left_to_right')

class ModalEndpoint1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    modal: Modal1 | Any = Field(default=None, union_mode='left_to_right')

class NavigationEndpoint6(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    click_tracking_params: str | Any = Field(None, alias='clickTrackingParams', union_mode='left_to_right')
    command_metadata: CommandMetadata27 | Any = Field(None, alias='commandMetadata', union_mode='left_to_right')
    modal_endpoint: ModalEndpoint1 | Any = Field(None, alias='modalEndpoint', union_mode='left_to_right')

class MenuNavigationItemRenderer(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    text: Text10 | Any = Field(default=None, union_mode='left_to_right')
    icon: Icon1 | Any = Field(default=None, union_mode='left_to_right')
    navigation_endpoint: NavigationEndpoint6 | Any = Field(None, alias='navigationEndpoint', union_mode='left_to_right')
    tracking_params: str | Any = Field(None, alias='trackingParams', union_mode='left_to_right')

class Item1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    menu_navigation_item_renderer: MenuNavigationItemRenderer | Any = Field(None, alias='menuNavigationItemRenderer', union_mode='left_to_right')

class WebCommandMetadata30(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    ignore_navigation: bool | Any = Field(None, alias='ignoreNavigation', union_mode='left_to_right')

class CommandMetadata30(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    web_command_metadata: WebCommandMetadata30 | Any = Field(None, alias='webCommandMetadata', union_mode='left_to_right')

class Text12(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    simple_text: str | Any = Field(None, alias='simpleText', union_mode='left_to_right')

class WebCommandMetadata31(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    url: str | Any = Field(default=None, union_mode='left_to_right')
    web_page_type: str | Any = Field(None, alias='webPageType', union_mode='left_to_right')
    root_ve: int | Any = Field(None, alias='rootVe', union_mode='left_to_right')

class CommandMetadata31(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    web_command_metadata: WebCommandMetadata31 | Any = Field(None, alias='webCommandMetadata', union_mode='left_to_right')

class WebCommandMetadata32(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    url: str | Any = Field(default=None, union_mode='left_to_right')
    web_page_type: str | Any = Field(None, alias='webPageType', union_mode='left_to_right')
    root_ve: int | Any = Field(None, alias='rootVe', union_mode='left_to_right')
    api_url: str | Any = Field(None, alias='apiUrl', union_mode='left_to_right')

class CommandMetadata32(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    web_command_metadata: WebCommandMetadata32 | Any = Field(None, alias='webCommandMetadata', union_mode='left_to_right')

class NextEndpoint2(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    click_tracking_params: str | Any = Field(None, alias='clickTrackingParams', union_mode='left_to_right')
    command_metadata: CommandMetadata32 | Any = Field(None, alias='commandMetadata', union_mode='left_to_right')
    browse_endpoint: BrowseEndpoint2 | Any = Field(None, alias='browseEndpoint', union_mode='left_to_right')

class SignInEndpoint3(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    next_endpoint: NextEndpoint2 | Any = Field(None, alias='nextEndpoint', union_mode='left_to_right')
    idam_tag: str | Any = Field(None, alias='idamTag', union_mode='left_to_right')

class NavigationEndpoint8(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    click_tracking_params: str | Any = Field(None, alias='clickTrackingParams', union_mode='left_to_right')
    command_metadata: CommandMetadata31 | Any = Field(None, alias='commandMetadata', union_mode='left_to_right')
    sign_in_endpoint: SignInEndpoint3 | Any = Field(None, alias='signInEndpoint', union_mode='left_to_right')

class ButtonRenderer13(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    style: str | Any = Field(default=None, union_mode='left_to_right')
    size: str | Any = Field(default=None, union_mode='left_to_right')
    is_disabled: bool | Any = Field(None, alias='isDisabled', union_mode='left_to_right')
    text: Text12 | Any = Field(default=None, union_mode='left_to_right')
    navigation_endpoint: NavigationEndpoint8 | Any = Field(None, alias='navigationEndpoint', union_mode='left_to_right')
    tracking_params: str | Any = Field(None, alias='trackingParams', union_mode='left_to_right')

class Button3(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    button_renderer: ButtonRenderer13 | Any = Field(None, alias='buttonRenderer', union_mode='left_to_right')

class ModalWithTitleAndButtonRenderer2(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    title: Title7 | Any = Field(default=None, union_mode='left_to_right')
    content: Content6 | Any = Field(default=None, union_mode='left_to_right')
    button: Button3 | Any = Field(default=None, union_mode='left_to_right')

class Modal2(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    modal_with_title_and_button_renderer: ModalWithTitleAndButtonRenderer2 | Any = Field(None, alias='modalWithTitleAndButtonRenderer', union_mode='left_to_right')

class ModalEndpoint2(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    modal: Modal2 | Any = Field(default=None, union_mode='left_to_right')

class DefaultNavigationEndpoint1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    click_tracking_params: str | Any = Field(None, alias='clickTrackingParams', union_mode='left_to_right')
    command_metadata: CommandMetadata30 | Any = Field(None, alias='commandMetadata', union_mode='left_to_right')
    modal_endpoint: ModalEndpoint2 | Any = Field(None, alias='modalEndpoint', union_mode='left_to_right')

class AccessibilityData14(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    label: str | Any = Field(default=None, union_mode='left_to_right')

class AccessibilityData13(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    accessibility_data: AccessibilityData14 | Any = Field(None, alias='accessibilityData', union_mode='left_to_right')

class AccessibilityData15(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    label: str | Any = Field(default=None, union_mode='left_to_right')

class ToggledAccessibilityData1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    accessibility_data: AccessibilityData15 | Any = Field(None, alias='accessibilityData', union_mode='left_to_right')

class ToggleButtonRenderer1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    style: Style | Any = Field(default=None, union_mode='left_to_right')
    size: Size | Any = Field(default=None, union_mode='left_to_right')
    is_toggled: bool | Any = Field(None, alias='isToggled', union_mode='left_to_right')
    is_disabled: bool | Any = Field(None, alias='isDisabled', union_mode='left_to_right')
    default_icon: DefaultIcon | Any = Field(None, alias='defaultIcon', union_mode='left_to_right')
    toggled_icon: ToggledIcon | Any = Field(None, alias='toggledIcon', union_mode='left_to_right')
    tracking_params: str | Any = Field(None, alias='trackingParams', union_mode='left_to_right')
    default_tooltip: str | Any = Field(None, alias='defaultTooltip', union_mode='left_to_right')
    toggled_tooltip: str | Any = Field(None, alias='toggledTooltip', union_mode='left_to_right')
    default_navigation_endpoint: DefaultNavigationEndpoint1 | Any = Field(None, alias='defaultNavigationEndpoint', union_mode='left_to_right')
    accessibility_data: AccessibilityData13 | Any = Field(None, alias='accessibilityData', union_mode='left_to_right')
    toggled_accessibility_data: ToggledAccessibilityData1 | Any = Field(None, alias='toggledAccessibilityData', union_mode='left_to_right')

class WebCommandMetadata33(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    url: str | Any = Field(default=None, union_mode='left_to_right')
    web_page_type: str | Any = Field(None, alias='webPageType', union_mode='left_to_right')
    root_ve: int | Any = Field(None, alias='rootVe', union_mode='left_to_right')

class CommandMetadata33(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    web_command_metadata: WebCommandMetadata33 | Any = Field(None, alias='webCommandMetadata', union_mode='left_to_right')

class LoggingContext7(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    vss_logging_context: VssLoggingContext | Any = Field(None, alias='vssLoggingContext', union_mode='left_to_right')

class Html5PlaybackOnesieConfig7(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    common_config: CommonConfig | Any = Field(None, alias='commonConfig', union_mode='left_to_right')

class WatchEndpointSupportedOnesieConfig7(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    html5_playback_onesie_config: Html5PlaybackOnesieConfig7 | Any = Field(None, alias='html5PlaybackOnesieConfig', union_mode='left_to_right')

class WatchEndpoint7(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    video_id: str | Any = Field(None, alias='videoId', union_mode='left_to_right')
    playlist_id: str | Any = Field(None, alias='playlistId', union_mode='left_to_right')
    params: str | Any = Field(default=None, union_mode='left_to_right')
    player_params: str | Any = Field(None, alias='playerParams', union_mode='left_to_right')
    logging_context: LoggingContext7 | Any = Field(None, alias='loggingContext', union_mode='left_to_right')
    watch_endpoint_supported_onesie_config: WatchEndpointSupportedOnesieConfig7 | Any = Field(None, alias='watchEndpointSupportedOnesieConfig', union_mode='left_to_right')

class NavigationEndpoint9(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    click_tracking_params: str | Any = Field(None, alias='clickTrackingParams', union_mode='left_to_right')
    command_metadata: CommandMetadata33 | Any = Field(None, alias='commandMetadata', union_mode='left_to_right')
    watch_endpoint: WatchEndpoint7 | Any = Field(None, alias='watchEndpoint', union_mode='left_to_right')

class Accessibility2(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    label: str | Any = Field(default=None, union_mode='left_to_right')

class WebCommandMetadata34(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    send_post: bool | Any = Field(None, alias='sendPost', union_mode='left_to_right')
    api_url: str | Any = Field(None, alias='apiUrl', union_mode='left_to_right')

class CommandMetadata34(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    web_command_metadata: WebCommandMetadata34 | Any = Field(None, alias='webCommandMetadata', union_mode='left_to_right')

class Popup4(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    unified_share_panel_renderer: UnifiedSharePanelRenderer | Any = Field(None, alias='unifiedSharePanelRenderer', union_mode='left_to_right')

class OpenPopupAction4(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    popup: Popup4 | Any = Field(default=None, union_mode='left_to_right')
    popup_type: str | Any = Field(None, alias='popupType', union_mode='left_to_right')
    be_reused: bool | Any = Field(None, alias='beReused', union_mode='left_to_right')

class Command5(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    click_tracking_params: str | Any = Field(None, alias='clickTrackingParams', union_mode='left_to_right')
    open_popup_action: OpenPopupAction4 | Any = Field(None, alias='openPopupAction', union_mode='left_to_right')

class ShareEntityServiceEndpoint2(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    serialized_share_entity: str | Any = Field(None, alias='serializedShareEntity', union_mode='left_to_right')
    commands: list[Command5] | Any = Field(default=None, union_mode='left_to_right')

class ServiceEndpoint2(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    click_tracking_params: str | Any = Field(None, alias='clickTrackingParams', union_mode='left_to_right')
    command_metadata: CommandMetadata34 | Any = Field(None, alias='commandMetadata', union_mode='left_to_right')
    share_entity_service_endpoint: ShareEntityServiceEndpoint2 | Any = Field(None, alias='shareEntityServiceEndpoint', union_mode='left_to_right')

class ButtonRenderer14(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    style: str | Any = Field(default=None, union_mode='left_to_right')
    size: str | Any = Field(default=None, union_mode='left_to_right')
    is_disabled: bool | Any = Field(None, alias='isDisabled', union_mode='left_to_right')
    icon: Icon1 | Any = Field(default=None, union_mode='left_to_right')
    navigation_endpoint: NavigationEndpoint9 | Any = Field(None, alias='navigationEndpoint', union_mode='left_to_right')
    accessibility: Accessibility2 | Any = Field(default=None, union_mode='left_to_right')
    tooltip: str | Any = Field(default=None, union_mode='left_to_right')
    tracking_params: str | Any = Field(None, alias='trackingParams', union_mode='left_to_right')
    service_endpoint: ServiceEndpoint2 | Any = Field(None, alias='serviceEndpoint', union_mode='left_to_right')

class TopLevelButton(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    toggle_button_renderer: ToggleButtonRenderer1 | Any = Field(None, alias='toggleButtonRenderer', union_mode='left_to_right')
    button_renderer: ButtonRenderer14 | Any = Field(None, alias='buttonRenderer', union_mode='left_to_right')

class Accessibility3(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    accessibility_data: AccessibilityData15 | Any = Field(None, alias='accessibilityData', union_mode='left_to_right')

class MenuRenderer(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    items: list[Item1] | Any = Field(default=None, union_mode='left_to_right')
    tracking_params: str | Any = Field(None, alias='trackingParams', union_mode='left_to_right')
    top_level_buttons: list[TopLevelButton] | Any = Field(None, alias='topLevelButtons', union_mode='left_to_right')
    accessibility: Accessibility3 | Any = Field(default=None, union_mode='left_to_right')

class Menu(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    menu_renderer: MenuRenderer | Any = Field(None, alias='menuRenderer', union_mode='left_to_right')

class ThumbnailOverlaySidePanelRenderer(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    text: Text12 | Any = Field(default=None, union_mode='left_to_right')
    icon: Icon1 | Any = Field(default=None, union_mode='left_to_right')

class ThumbnailOverlay(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    thumbnail_overlay_side_panel_renderer: ThumbnailOverlaySidePanelRenderer | Any = Field(None, alias='thumbnailOverlaySidePanelRenderer', union_mode='left_to_right')

class WebCommandMetadata35(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    url: str | Any = Field(default=None, union_mode='left_to_right')
    web_page_type: str | Any = Field(None, alias='webPageType', union_mode='left_to_right')
    root_ve: int | Any = Field(None, alias='rootVe', union_mode='left_to_right')

class CommandMetadata35(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    web_command_metadata: WebCommandMetadata35 | Any = Field(None, alias='webCommandMetadata', union_mode='left_to_right')

class LoggingContext8(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    vss_logging_context: VssLoggingContext | Any = Field(None, alias='vssLoggingContext', union_mode='left_to_right')

class Html5PlaybackOnesieConfig8(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    common_config: CommonConfig | Any = Field(None, alias='commonConfig', union_mode='left_to_right')

class WatchEndpointSupportedOnesieConfig8(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    html5_playback_onesie_config: Html5PlaybackOnesieConfig8 | Any = Field(None, alias='html5PlaybackOnesieConfig', union_mode='left_to_right')

class WatchEndpoint8(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    video_id: str | Any = Field(None, alias='videoId', union_mode='left_to_right')
    playlist_id: str | Any = Field(None, alias='playlistId', union_mode='left_to_right')
    player_params: str | Any = Field(None, alias='playerParams', union_mode='left_to_right')
    logging_context: LoggingContext8 | Any = Field(None, alias='loggingContext', union_mode='left_to_right')
    watch_endpoint_supported_onesie_config: WatchEndpointSupportedOnesieConfig8 | Any = Field(None, alias='watchEndpointSupportedOnesieConfig', union_mode='left_to_right')

class NavigationEndpoint10(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    click_tracking_params: str | Any = Field(None, alias='clickTrackingParams', union_mode='left_to_right')
    command_metadata: CommandMetadata35 | Any = Field(None, alias='commandMetadata', union_mode='left_to_right')
    watch_endpoint: WatchEndpoint8 | Any = Field(None, alias='watchEndpoint', union_mode='left_to_right')

class ShowMoreText(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    runs: list[Run27] | Any = Field(default=None, union_mode='left_to_right')

class PlaylistSidebarPrimaryInfoRenderer(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    thumbnail_renderer: ThumbnailRenderer | Any = Field(None, alias='thumbnailRenderer', union_mode='left_to_right')
    title: Title6 | Any = Field(default=None, union_mode='left_to_right')
    stats: list[Stat1] | Any = Field(default=None, union_mode='left_to_right')
    menu: Menu | Any = Field(default=None, union_mode='left_to_right')
    thumbnail_overlays: list[ThumbnailOverlay] | Any = Field(None, alias='thumbnailOverlays', union_mode='left_to_right')
    navigation_endpoint: NavigationEndpoint10 | Any = Field(None, alias='navigationEndpoint', union_mode='left_to_right')
    show_more_text: ShowMoreText | Any = Field(None, alias='showMoreText', union_mode='left_to_right')

class Item(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    playlist_sidebar_primary_info_renderer: PlaylistSidebarPrimaryInfoRenderer | Any = Field(None, alias='playlistSidebarPrimaryInfoRenderer', union_mode='left_to_right')

class PlaylistSidebarRenderer(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    items: list[Item] | Any = Field(default=None, union_mode='left_to_right')
    tracking_params: str | Any = Field(None, alias='trackingParams', union_mode='left_to_right')

class Sidebar(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    playlist_sidebar_renderer: PlaylistSidebarRenderer | Any = Field(None, alias='playlistSidebarRenderer', union_mode='left_to_right')

class MusicModel(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    response_context: ResponseContext | Any = Field(None, alias='responseContext', union_mode='left_to_right')
    contents: Contents | Any = Field(default=None, union_mode='left_to_right')
    header: Header | Any = Field(default=None, union_mode='left_to_right')
    metadata: Metadata2 | Any = Field(default=None, union_mode='left_to_right')
    tracking_params: str | Any = Field(None, alias='trackingParams', union_mode='left_to_right')
    topbar: Topbar | Any = Field(default=None, union_mode='left_to_right')
    microformat: Microformat | Any = Field(default=None, union_mode='left_to_right')
    sidebar: Sidebar | Any = Field(default=None, union_mode='left_to_right')
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
