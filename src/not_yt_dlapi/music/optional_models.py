from typing import Any, Self
from pydantic import ModelWrapValidatorHandler, PrivateAttr, model_validator
from pydantic import BaseModel, ConfigDict, Field

class Param(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    key: str | None = None
    value: str | None = None

class ServiceTrackingParam(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    service: str | None = None
    params: list[Param] | None = None

class MainAppWebResponseContext(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    logged_out: bool | None = Field(None, alias='loggedOut')
    tracking_param: str | None = Field(None, alias='trackingParam')

class WebResponseContextPreloadData(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    preload_message_names: list[str] | None = Field(None, alias='preloadMessageNames')

class WebResponseContextExtensionData(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    web_response_context_preload_data: WebResponseContextPreloadData | None = Field(None, alias='webResponseContextPreloadData')
    has_decorated: bool | None = Field(None, alias='hasDecorated')

class ResponseContext(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    visitor_data: str | None = Field(None, alias='visitorData')
    service_tracking_params: list[ServiceTrackingParam] | None = Field(None, alias='serviceTrackingParams')
    main_app_web_response_context: MainAppWebResponseContext | None = Field(None, alias='mainAppWebResponseContext')
    response_id: str | None = Field(None, alias='responseId')
    web_response_context_extension_data: WebResponseContextExtensionData | None = Field(None, alias='webResponseContextExtensionData')

class Source(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    url: str | None = None
    width: int | None = None
    height: int | None = None

class Image(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    sources: list[Source] | None = None

class ClientResource(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    image_name: str | None = Field(None, alias='imageName')

class Source1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    client_resource: ClientResource | None = Field(None, alias='clientResource')

class Icon(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    sources: list[Source1] | None = None

class Settings(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    loop: bool | None = None
    autoplay: bool | None = None

class LottieData(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    url: str | None = None
    settings: Settings | None = None

class AccessibilityContext(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    label: str | None = None

class RendererContext(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    accessibility_context: AccessibilityContext | None = Field(None, alias='accessibilityContext')

class ThumbnailBadgeViewModel(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    icon: Icon | None = None
    text: str | None = None
    badge_style: str | None = Field(None, alias='badgeStyle')
    animation_activation_target_id: str | None = Field(None, alias='animationActivationTargetId')
    animation_activation_entity_key: str | None = Field(None, alias='animationActivationEntityKey')
    lottie_data: LottieData | None = Field(None, alias='lottieData')
    animated_text: str | None = Field(None, alias='animatedText')
    animation_activation_entity_selector_type: str | None = Field(None, alias='animationActivationEntitySelectorType')
    renderer_context: RendererContext | None = Field(None, alias='rendererContext')

class Badge(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    thumbnail_badge_view_model: ThumbnailBadgeViewModel | None = Field(None, alias='thumbnailBadgeViewModel')

class ThumbnailBottomOverlayViewModel(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    badges: list[Badge] | None = None

class WebCommandMetadata(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    send_post: bool | None = Field(None, alias='sendPost')
    api_url: str | None = Field(None, alias='apiUrl')

class CommandMetadata(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    web_command_metadata: WebCommandMetadata | None = Field(None, alias='webCommandMetadata')

class Action(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    added_video_id: str | None = Field(None, alias='addedVideoId')
    action: str | None = None

class PlaylistEditEndpoint(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    playlist_id: str | None = Field(None, alias='playlistId')
    actions: list[Action] | None = None

class CommandMetadata1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    web_command_metadata: WebCommandMetadata | None = Field(None, alias='webCommandMetadata')

class CreatePlaylistServiceEndpoint(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    video_ids: list[str] | None = Field(None, alias='videoIds')
    params: str | None = None

class OnCreateListCommand(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    click_tracking_params: str | None = Field(None, alias='clickTrackingParams')
    command_metadata: CommandMetadata1 | None = Field(None, alias='commandMetadata')
    create_playlist_service_endpoint: CreatePlaylistServiceEndpoint | None = Field(None, alias='createPlaylistServiceEndpoint')

class WebCommandMetadata2(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    url: str | None = None
    web_page_type: str | None = Field(None, alias='webPageType')
    root_ve: int | None = Field(None, alias='rootVe')

class CommandMetadata2(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    web_command_metadata: WebCommandMetadata2 | None = Field(None, alias='webCommandMetadata')

class CommonConfig(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    url: str | None = None

class Html5PlaybackOnesieConfig(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    common_config: CommonConfig | None = Field(None, alias='commonConfig')

class WatchEndpointSupportedOnesieConfig(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    html5_playback_onesie_config: Html5PlaybackOnesieConfig | None = Field(None, alias='html5PlaybackOnesieConfig')

class WatchEndpoint(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    video_id: str | None = Field(None, alias='videoId')
    watch_endpoint_supported_onesie_config: WatchEndpointSupportedOnesieConfig | None = Field(None, alias='watchEndpointSupportedOnesieConfig')
    player_params: str | None = Field(None, alias='playerParams')

class VideoCommand(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    click_tracking_params: str | None = Field(None, alias='clickTrackingParams')
    command_metadata: CommandMetadata2 | None = Field(None, alias='commandMetadata')
    watch_endpoint: WatchEndpoint | None = Field(None, alias='watchEndpoint')

class AddToPlaylistCommand(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    open_miniplayer: bool | None = Field(None, alias='openMiniplayer')
    video_id: str | None = Field(None, alias='videoId')
    list_type: str | None = Field(None, alias='listType')
    on_create_list_command: OnCreateListCommand | None = Field(None, alias='onCreateListCommand')
    video_ids: list[str] | None = Field(None, alias='videoIds')
    video_command: VideoCommand | None = Field(None, alias='videoCommand')

class Action1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    click_tracking_params: str | None = Field(None, alias='clickTrackingParams')
    add_to_playlist_command: AddToPlaylistCommand | None = Field(None, alias='addToPlaylistCommand')

class SignalServiceEndpoint(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    signal: str | None = None
    actions: list[Action1] | None = None

class InnertubeCommand(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    click_tracking_params: str | None = Field(None, alias='clickTrackingParams')
    command_metadata: CommandMetadata | None = Field(None, alias='commandMetadata')
    playlist_edit_endpoint: PlaylistEditEndpoint | None = Field(None, alias='playlistEditEndpoint')
    signal_service_endpoint: SignalServiceEndpoint | None = Field(None, alias='signalServiceEndpoint')

class OnTap(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    innertube_command: InnertubeCommand | None = Field(None, alias='innertubeCommand')

class ButtonViewModel(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    icon_name: str | None = Field(None, alias='iconName')
    on_tap: OnTap | None = Field(None, alias='onTap')
    accessibility_text: str | None = Field(None, alias='accessibilityText')
    style: str | None = None
    tracking_params: str | None = Field(None, alias='trackingParams')
    type: str | None = None
    button_size: str | None = Field(None, alias='buttonSize')
    state: str | None = None

class DefaultButtonViewModel(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    button_view_model: ButtonViewModel | None = Field(None, alias='buttonViewModel')

class WebCommandMetadata3(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    send_post: bool | None = Field(None, alias='sendPost')
    api_url: str | None = Field(None, alias='apiUrl')

class CommandMetadata3(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    web_command_metadata: WebCommandMetadata3 | None = Field(None, alias='webCommandMetadata')

class Action2(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    action: str | None = None
    removed_video_id: str | None = Field(None, alias='removedVideoId')

class PlaylistEditEndpoint1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    playlist_id: str | None = Field(None, alias='playlistId')
    actions: list[Action2] | None = None

class InnertubeCommand1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    click_tracking_params: str | None = Field(None, alias='clickTrackingParams')
    command_metadata: CommandMetadata3 | None = Field(None, alias='commandMetadata')
    playlist_edit_endpoint: PlaylistEditEndpoint1 | None = Field(None, alias='playlistEditEndpoint')

class OnTap1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    innertube_command: InnertubeCommand1 | None = Field(None, alias='innertubeCommand')

class ButtonViewModel1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    icon_name: str | None = Field(None, alias='iconName')
    on_tap: OnTap1 | None = Field(None, alias='onTap')
    accessibility_text: str | None = Field(None, alias='accessibilityText')
    style: str | None = None
    tracking_params: str | None = Field(None, alias='trackingParams')
    type: str | None = None
    button_size: str | None = Field(None, alias='buttonSize')
    state: str | None = None

class ToggledButtonViewModel(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    button_view_model: ButtonViewModel1 | None = Field(None, alias='buttonViewModel')

class ToggleButtonViewModel(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    default_button_view_model: DefaultButtonViewModel | None = Field(None, alias='defaultButtonViewModel')
    toggled_button_view_model: ToggledButtonViewModel | None = Field(None, alias='toggledButtonViewModel')
    is_toggled: bool | None = Field(None, alias='isToggled')
    tracking_params: str | None = Field(None, alias='trackingParams')

class Button(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    toggle_button_view_model: ToggleButtonViewModel | None = Field(None, alias='toggleButtonViewModel')

class ThumbnailHoverOverlayToggleActionsViewModel(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    buttons: list[Button] | None = None

class Overlay(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    thumbnail_bottom_overlay_view_model: ThumbnailBottomOverlayViewModel | None = Field(None, alias='thumbnailBottomOverlayViewModel')
    thumbnail_hover_overlay_toggle_actions_view_model: ThumbnailHoverOverlayToggleActionsViewModel | None = Field(None, alias='thumbnailHoverOverlayToggleActionsViewModel')

class ThumbnailViewModel(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    image: Image | None = None
    overlays: list[Overlay] | None = None

class ContentImage(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    thumbnail_view_model: ThumbnailViewModel | None = Field(None, alias='thumbnailViewModel')

class Title(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    content: str | None = None

class Source2(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    url: str | None = None
    width: int | None = None
    height: int | None = None

class Image2(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    sources: list[Source2] | None = None

class AvatarViewModel(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    image: Image2 | None = None
    avatar_image_size: str | None = Field(None, alias='avatarImageSize')

class Avatar(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    avatar_view_model: AvatarViewModel | None = Field(None, alias='avatarViewModel')

class WebCommandMetadata4(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    url: str | None = None
    web_page_type: str | None = Field(None, alias='webPageType')
    root_ve: int | None = Field(None, alias='rootVe')
    api_url: str | None = Field(None, alias='apiUrl')

class CommandMetadata4(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    web_command_metadata: WebCommandMetadata4 | None = Field(None, alias='webCommandMetadata')

class BrowseEndpoint(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    browse_id: str | None = Field(None, alias='browseId')
    canonical_base_url: str | None = Field(None, alias='canonicalBaseUrl')

class InnertubeCommand2(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    click_tracking_params: str | None = Field(None, alias='clickTrackingParams')
    command_metadata: CommandMetadata4 | None = Field(None, alias='commandMetadata')
    browse_endpoint: BrowseEndpoint | None = Field(None, alias='browseEndpoint')

class OnTap2(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    innertube_command: InnertubeCommand2 | None = Field(None, alias='innertubeCommand')

class CommandContext(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    on_tap: OnTap2 | None = Field(None, alias='onTap')

class RendererContext1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    command_context: CommandContext | None = Field(None, alias='commandContext')

class DecoratedAvatarViewModel(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    avatar: Avatar | None = None
    a11y_label: str | None = Field(None, alias='a11yLabel')
    renderer_context: RendererContext1 | None = Field(None, alias='rendererContext')

class Image1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    decorated_avatar_view_model: DecoratedAvatarViewModel | None = Field(None, alias='decoratedAvatarViewModel')

class CommandMetadata5(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    web_command_metadata: WebCommandMetadata4 | None = Field(None, alias='webCommandMetadata')

class InnertubeCommand3(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    click_tracking_params: str | None = Field(None, alias='clickTrackingParams')
    command_metadata: CommandMetadata5 | None = Field(None, alias='commandMetadata')
    browse_endpoint: BrowseEndpoint | None = Field(None, alias='browseEndpoint')

class OnTap3(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    innertube_command: InnertubeCommand3 | None = Field(None, alias='innertubeCommand')

class CommandRun(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    start_index: int | None = Field(None, alias='startIndex')
    length: int | None = None
    on_tap: OnTap3 | None = Field(None, alias='onTap')

class ColorMapItem(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    key: str | None = None
    value: int | None = None

class StyleRunColorMapExtension(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    color_map: list[ColorMapItem] | None = Field(None, alias='colorMap')

class StyleRunExtensions(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    style_run_color_map_extension: StyleRunColorMapExtension | None = Field(None, alias='styleRunColorMapExtension')

class StyleRun(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    start_index: int | None = Field(None, alias='startIndex')
    length: int | None = None
    weight_label: str | None = Field(None, alias='weightLabel')
    style_run_extensions: StyleRunExtensions | None = Field(None, alias='styleRunExtensions')

class Source3(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    client_resource: ClientResource | None = Field(None, alias='clientResource')
    width: int | None = None
    height: int | None = None

class Image3(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    sources: list[Source3] | None = None

class ImageType(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    image: Image3 | None = None

class Type(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    image_type: ImageType | None = Field(None, alias='imageType')

class Height(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    value: int | None = None
    unit: str | None = None

class Width(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    value: int | None = None
    unit: str | None = None

class Left(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    value: int | None = None
    unit: str | None = None

class Margin(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    left: Left | None = None

class LayoutProperties(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    height: Height | None = None
    width: Width | None = None
    margin: Margin | None = None

class Properties(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    layout_properties: LayoutProperties | None = Field(None, alias='layoutProperties')

class Element(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    type: Type | None = None
    properties: Properties | None = None

class AttachmentRun(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    start_index: int | None = Field(None, alias='startIndex')
    length: int | None = None
    element: Element | None = None
    alignment: str | None = None

class Text(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    content: str | None = None
    command_runs: list[CommandRun] | None = Field(None, alias='commandRuns')
    style_runs: list[StyleRun] | None = Field(None, alias='styleRuns')
    attachment_runs: list[AttachmentRun] | None = Field(None, alias='attachmentRuns')

class MetadataPart(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    text: Text | None = None
    accessibility_label: str | None = Field(None, alias='accessibilityLabel')

class MetadataRow(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    metadata_parts: list[MetadataPart] | None = Field(None, alias='metadataParts')

class ContentMetadataViewModel(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    metadata_rows: list[MetadataRow] | None = Field(None, alias='metadataRows')
    delimiter: str | None = None

class Metadata1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    content_metadata_view_model: ContentMetadataViewModel | None = Field(None, alias='contentMetadataViewModel')

class Source4(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    client_resource: ClientResource | None = Field(None, alias='clientResource')

class LeadingImage(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    sources: list[Source4] | None = None

class Visibility(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    types: str | None = None

class LoggingDirectives(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    tracking_params: str | None = Field(None, alias='trackingParams')
    visibility: Visibility | None = None

class LoggingContext(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    logging_directives: LoggingDirectives | None = Field(None, alias='loggingDirectives')

class WebCommandMetadata6(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    send_post: bool | None = Field(None, alias='sendPost')
    api_url: str | None = Field(None, alias='apiUrl')

class CommandMetadata6(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    web_command_metadata: WebCommandMetadata6 | None = Field(None, alias='webCommandMetadata')

class CommandMetadata7(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    web_command_metadata: WebCommandMetadata6 | None = Field(None, alias='webCommandMetadata')

class OnCreateListCommand1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    click_tracking_params: str | None = Field(None, alias='clickTrackingParams')
    command_metadata: CommandMetadata7 | None = Field(None, alias='commandMetadata')
    create_playlist_service_endpoint: CreatePlaylistServiceEndpoint | None = Field(None, alias='createPlaylistServiceEndpoint')

class WebCommandMetadata8(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    url: str | None = None
    web_page_type: str | None = Field(None, alias='webPageType')
    root_ve: int | None = Field(None, alias='rootVe')

class CommandMetadata8(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    web_command_metadata: WebCommandMetadata8 | None = Field(None, alias='webCommandMetadata')

class Html5PlaybackOnesieConfig1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    common_config: CommonConfig | None = Field(None, alias='commonConfig')

class WatchEndpointSupportedOnesieConfig1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    html5_playback_onesie_config: Html5PlaybackOnesieConfig1 | None = Field(None, alias='html5PlaybackOnesieConfig')

class WatchEndpoint1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    video_id: str | None = Field(None, alias='videoId')
    watch_endpoint_supported_onesie_config: WatchEndpointSupportedOnesieConfig1 | None = Field(None, alias='watchEndpointSupportedOnesieConfig')
    player_params: str | None = Field(None, alias='playerParams')

class VideoCommand1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    click_tracking_params: str | None = Field(None, alias='clickTrackingParams')
    command_metadata: CommandMetadata8 | None = Field(None, alias='commandMetadata')
    watch_endpoint: WatchEndpoint1 | None = Field(None, alias='watchEndpoint')

class AddToPlaylistCommand1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    open_miniplayer: bool | None = Field(None, alias='openMiniplayer')
    video_id: str | None = Field(None, alias='videoId')
    list_type: str | None = Field(None, alias='listType')
    on_create_list_command: OnCreateListCommand1 | None = Field(None, alias='onCreateListCommand')
    video_ids: list[str] | None = Field(None, alias='videoIds')
    video_command: VideoCommand1 | None = Field(None, alias='videoCommand')

class Action3(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    click_tracking_params: str | None = Field(None, alias='clickTrackingParams')
    add_to_playlist_command: AddToPlaylistCommand1 | None = Field(None, alias='addToPlaylistCommand')

class SignalServiceEndpoint1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    signal: str | None = None
    actions: list[Action3] | None = None

class UnifiedSharePanelRenderer(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    tracking_params: str | None = Field(None, alias='trackingParams')
    show_loading_spinner: bool | None = Field(None, alias='showLoadingSpinner')

class Popup(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    unified_share_panel_renderer: UnifiedSharePanelRenderer | None = Field(None, alias='unifiedSharePanelRenderer')

class OpenPopupAction(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    popup: Popup | None = None
    popup_type: str | None = Field(None, alias='popupType')
    be_reused: bool | None = Field(None, alias='beReused')

class Command(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    click_tracking_params: str | None = Field(None, alias='clickTrackingParams')
    open_popup_action: OpenPopupAction | None = Field(None, alias='openPopupAction')

class ShareEntityServiceEndpoint(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    serialized_share_entity: str | None = Field(None, alias='serializedShareEntity')
    commands: list[Command] | None = None

class InnertubeCommand5(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    click_tracking_params: str | None = Field(None, alias='clickTrackingParams')
    command_metadata: CommandMetadata6 | None = Field(None, alias='commandMetadata')
    signal_service_endpoint: SignalServiceEndpoint1 | None = Field(None, alias='signalServiceEndpoint')
    share_entity_service_endpoint: ShareEntityServiceEndpoint | None = Field(None, alias='shareEntityServiceEndpoint')

class OnTap5(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    innertube_command: InnertubeCommand5 | None = Field(None, alias='innertubeCommand')

class CommandContext1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    on_tap: OnTap5 | None = Field(None, alias='onTap')

class RendererContext2(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    logging_context: LoggingContext | None = Field(None, alias='loggingContext')
    command_context: CommandContext1 | None = Field(None, alias='commandContext')

class ListItemViewModel(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    title: Title | None = None
    leading_image: LeadingImage | None = Field(None, alias='leadingImage')
    renderer_context: RendererContext2 | None = Field(None, alias='rendererContext')

class ListItem(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    list_item_view_model: ListItemViewModel | None = Field(None, alias='listItemViewModel')

class ListViewModel(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    list_items: list[ListItem] | None = Field(None, alias='listItems')

class Content3(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    list_view_model: ListViewModel | None = Field(None, alias='listViewModel')

class SheetViewModel(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    content: Content3 | None = None

class InlineContent(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    sheet_view_model: SheetViewModel | None = Field(None, alias='sheetViewModel')

class PanelLoadingStrategy(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    inline_content: InlineContent | None = Field(None, alias='inlineContent')

class ShowSheetCommand(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    panel_loading_strategy: PanelLoadingStrategy | None = Field(None, alias='panelLoadingStrategy')

class InnertubeCommand4(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    click_tracking_params: str | None = Field(None, alias='clickTrackingParams')
    show_sheet_command: ShowSheetCommand | None = Field(None, alias='showSheetCommand')

class OnTap4(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    innertube_command: InnertubeCommand4 | None = Field(None, alias='innertubeCommand')

class ButtonViewModel2(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    icon_name: str | None = Field(None, alias='iconName')
    on_tap: OnTap4 | None = Field(None, alias='onTap')
    accessibility_text: str | None = Field(None, alias='accessibilityText')
    style: str | None = None
    tracking_params: str | None = Field(None, alias='trackingParams')
    type: str | None = None
    button_size: str | None = Field(None, alias='buttonSize')
    state: str | None = None

class MenuButton(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    button_view_model: ButtonViewModel2 | None = Field(None, alias='buttonViewModel')

class LockupMetadataViewModel(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    title: Title | None = None
    image: Image1 | None = None
    metadata: Metadata1 | None = None
    menu_button: MenuButton | None = Field(None, alias='menuButton')

class Metadata(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    lockup_metadata_view_model: LockupMetadataViewModel | None = Field(None, alias='lockupMetadataViewModel')

class LoggingDirectives1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    tracking_params: str | None = Field(None, alias='trackingParams')
    visibility: Visibility | None = None

class LoggingContext1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    logging_directives: LoggingDirectives1 | None = Field(None, alias='loggingDirectives')

class CommandMetadata9(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    web_command_metadata: WebCommandMetadata8 | None = Field(None, alias='webCommandMetadata')

class VssLoggingContext(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    serialized_context_data: str | None = Field(None, alias='serializedContextData')

class LoggingContext2(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    vss_logging_context: VssLoggingContext | None = Field(None, alias='vssLoggingContext')

class Html5PlaybackOnesieConfig2(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    common_config: CommonConfig | None = Field(None, alias='commonConfig')

class WatchEndpointSupportedOnesieConfig2(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    html5_playback_onesie_config: Html5PlaybackOnesieConfig2 | None = Field(None, alias='html5PlaybackOnesieConfig')

class WatchEndpoint2(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    video_id: str | None = Field(None, alias='videoId')
    playlist_id: str | None = Field(None, alias='playlistId')
    index: int | None = None
    params: str | None = None
    player_params: str | None = Field(None, alias='playerParams')
    logging_context: LoggingContext2 | None = Field(None, alias='loggingContext')
    watch_endpoint_supported_onesie_config: WatchEndpointSupportedOnesieConfig2 | None = Field(None, alias='watchEndpointSupportedOnesieConfig')

class InnertubeCommand6(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    click_tracking_params: str | None = Field(None, alias='clickTrackingParams')
    command_metadata: CommandMetadata9 | None = Field(None, alias='commandMetadata')
    watch_endpoint: WatchEndpoint2 | None = Field(None, alias='watchEndpoint')

class OnTap6(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    innertube_command: InnertubeCommand6 | None = Field(None, alias='innertubeCommand')

class CommandContext2(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    on_tap: OnTap6 | None = Field(None, alias='onTap')

class RendererContext3(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    logging_context: LoggingContext1 | None = Field(None, alias='loggingContext')
    accessibility_context: AccessibilityContext | None = Field(None, alias='accessibilityContext')
    command_context: CommandContext2 | None = Field(None, alias='commandContext')

class LockupViewModel(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    content_image: ContentImage | None = Field(None, alias='contentImage')
    metadata: Metadata | None = None
    content_id: str | None = Field(None, alias='contentId')
    content_type: str | None = Field(None, alias='contentType')
    renderer_context: RendererContext3 | None = Field(None, alias='rendererContext')

class Content2(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    lockup_view_model: LockupViewModel | None = Field(None, alias='lockupViewModel')

class ItemSectionRenderer(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    contents: list[Content2] | None = None
    tracking_params: str | None = Field(None, alias='trackingParams')
    target_id: str | None = Field(None, alias='targetId')

class Content1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    item_section_renderer: ItemSectionRenderer | None = Field(None, alias='itemSectionRenderer')

class SpacingConfiguration(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    column_gap: int | None = Field(None, alias='columnGap')
    row_gap: int | None = Field(None, alias='rowGap')

class ResponsiveMapItem(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    container_size: str | None = Field(None, alias='containerSize')
    container_type: str | None = Field(None, alias='containerType')
    max_width: int | None = Field(None, alias='maxWidth')
    min_column_size: int | None = Field(None, alias='minColumnSize')
    min_column_count: int | None = Field(None, alias='minColumnCount')
    max_column_count: int | None = Field(None, alias='maxColumnCount')
    spacing_configuration: SpacingConfiguration | None = Field(None, alias='spacingConfiguration')
    column_multiplier: int | None = Field(None, alias='columnMultiplier')
    column_adder: int | None = Field(None, alias='columnAdder')

class ResponsiveContainerConfiguration(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    responsive_size: str | None = Field(None, alias='responsiveSize')
    responsive_map: list[ResponsiveMapItem] | None = Field(None, alias='responsiveMap')

class LayoutConfiguration(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    responsive_container_configuration: ResponsiveContainerConfiguration | None = Field(None, alias='responsiveContainerConfiguration')

class SectionListLayoutConfiguration(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    layout_configuration: LayoutConfiguration | None = Field(None, alias='layoutConfiguration')

class SectionListRenderer(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    contents: list[Content1] | None = None
    tracking_params: str | None = Field(None, alias='trackingParams')
    section_list_layout_configuration: SectionListLayoutConfiguration | None = Field(None, alias='sectionListLayoutConfiguration')

class Content(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    section_list_renderer: SectionListRenderer | None = Field(None, alias='sectionListRenderer')

class TabRenderer(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    selected: bool | None = None
    content: Content | None = None
    tab_identifier: str | None = Field(None, alias='tabIdentifier')
    tracking_params: str | None = Field(None, alias='trackingParams')

class Tab(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    tab_renderer: TabRenderer | None = Field(None, alias='tabRenderer')

class TwoColumnBrowseResultsRenderer(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    tabs: list[Tab] | None = None

class Contents(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    two_column_browse_results_renderer: TwoColumnBrowseResultsRenderer | None = Field(None, alias='twoColumnBrowseResultsRenderer')

class Title2(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    simple_text: str | None = Field(None, alias='simpleText')

class Run(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    text: str | None = None

class NumVideosText(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    runs: list[Run] | None = None

class ViewCountText(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    simple_text: str | None = Field(None, alias='simpleText')

class ShareData(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    can_share: bool | None = Field(None, alias='canShare')

class EditableDetails(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    can_delete: bool | None = Field(None, alias='canDelete')

class WebCommandMetadata10(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    send_post: bool | None = Field(None, alias='sendPost')
    api_url: str | None = Field(None, alias='apiUrl')

class CommandMetadata10(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    web_command_metadata: WebCommandMetadata10 | None = Field(None, alias='webCommandMetadata')

class Action4(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    action: str | None = None
    source_playlist_id: str | None = Field(None, alias='sourcePlaylistId')

class PlaylistEditEndpoint2(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    actions: list[Action4] | None = None

class ServiceEndpoint(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    click_tracking_params: str | None = Field(None, alias='clickTrackingParams')
    command_metadata: CommandMetadata10 | None = Field(None, alias='commandMetadata')
    playlist_edit_endpoint: PlaylistEditEndpoint2 | None = Field(None, alias='playlistEditEndpoint')

class Stat(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    runs: list[Run] | None = None
    simple_text: str | None = Field(None, alias='simpleText')

class BriefStat(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    runs: list[Run] | None = None

class Thumbnail1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    url: str | None = None
    width: int | None = None
    height: int | None = None

class SampledThumbnailColor(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    red: int | None = None
    green: int | None = None
    blue: int | None = None

class DarkColorPalette(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    section2_color: int | None = Field(None, alias='section2Color')
    icon_inactive_color: int | None = Field(None, alias='iconInactiveColor')
    icon_disabled_color: int | None = Field(None, alias='iconDisabledColor')

class VibrantColorPalette(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    icon_inactive_color: int | None = Field(None, alias='iconInactiveColor')

class Thumbnail(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    thumbnails: list[Thumbnail1] | None = None
    sampled_thumbnail_color: SampledThumbnailColor | None = Field(None, alias='sampledThumbnailColor')
    dark_color_palette: DarkColorPalette | None = Field(None, alias='darkColorPalette')
    vibrant_color_palette: VibrantColorPalette | None = Field(None, alias='vibrantColorPalette')

class WebCommandMetadata11(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    url: str | None = None
    web_page_type: str | None = Field(None, alias='webPageType')
    root_ve: int | None = Field(None, alias='rootVe')

class CommandMetadata11(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    web_command_metadata: WebCommandMetadata11 | None = Field(None, alias='webCommandMetadata')

class LoggingContext3(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    vss_logging_context: VssLoggingContext | None = Field(None, alias='vssLoggingContext')

class Html5PlaybackOnesieConfig3(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    common_config: CommonConfig | None = Field(None, alias='commonConfig')

class WatchEndpointSupportedOnesieConfig3(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    html5_playback_onesie_config: Html5PlaybackOnesieConfig3 | None = Field(None, alias='html5PlaybackOnesieConfig')

class WatchEndpoint3(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    video_id: str | None = Field(None, alias='videoId')
    playlist_id: str | None = Field(None, alias='playlistId')
    player_params: str | None = Field(None, alias='playerParams')
    logging_context: LoggingContext3 | None = Field(None, alias='loggingContext')
    watch_endpoint_supported_onesie_config: WatchEndpointSupportedOnesieConfig3 | None = Field(None, alias='watchEndpointSupportedOnesieConfig')

class OnTap7(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    click_tracking_params: str | None = Field(None, alias='clickTrackingParams')
    command_metadata: CommandMetadata11 | None = Field(None, alias='commandMetadata')
    watch_endpoint: WatchEndpoint3 | None = Field(None, alias='watchEndpoint')

class Text1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    simple_text: str | None = Field(None, alias='simpleText')

class Icon1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    icon_type: str | None = Field(None, alias='iconType')

class ThumbnailOverlayHoverTextRenderer(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    text: Text1 | None = None
    icon: Icon1 | None = None

class ThumbnailOverlays(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    thumbnail_overlay_hover_text_renderer: ThumbnailOverlayHoverTextRenderer | None = Field(None, alias='thumbnailOverlayHoverTextRenderer')

class HeroPlaylistThumbnailRenderer(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    thumbnail: Thumbnail | None = None
    max_ratio: float | None = Field(None, alias='maxRatio')
    tracking_params: str | None = Field(None, alias='trackingParams')
    on_tap: OnTap7 | None = Field(None, alias='onTap')
    thumbnail_overlays: ThumbnailOverlays | None = Field(None, alias='thumbnailOverlays')

class PlaylistHeaderBanner(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    hero_playlist_thumbnail_renderer: HeroPlaylistThumbnailRenderer | None = Field(None, alias='heroPlaylistThumbnailRenderer')

class Style(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    style_type: str | None = Field(None, alias='styleType')

class Size(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    size_type: str | None = Field(None, alias='sizeType')

class DefaultIcon(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    icon_type: str | None = Field(None, alias='iconType')

class ToggledIcon(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    icon_type: str | None = Field(None, alias='iconType')

class ToggledStyle(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    style_type: str | None = Field(None, alias='styleType')

class WebCommandMetadata12(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    ignore_navigation: bool | None = Field(None, alias='ignoreNavigation')

class CommandMetadata12(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    web_command_metadata: WebCommandMetadata12 | None = Field(None, alias='webCommandMetadata')

class Content4(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    simple_text: str | None = Field(None, alias='simpleText')

class WebCommandMetadata13(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    url: str | None = None
    web_page_type: str | None = Field(None, alias='webPageType')
    root_ve: int | None = Field(None, alias='rootVe')

class CommandMetadata13(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    web_command_metadata: WebCommandMetadata13 | None = Field(None, alias='webCommandMetadata')

class WebCommandMetadata14(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    url: str | None = None
    web_page_type: str | None = Field(None, alias='webPageType')
    root_ve: int | None = Field(None, alias='rootVe')
    api_url: str | None = Field(None, alias='apiUrl')

class CommandMetadata14(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    web_command_metadata: WebCommandMetadata14 | None = Field(None, alias='webCommandMetadata')

class BrowseEndpoint2(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    browse_id: str | None = Field(None, alias='browseId')

class NextEndpoint(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    click_tracking_params: str | None = Field(None, alias='clickTrackingParams')
    command_metadata: CommandMetadata14 | None = Field(None, alias='commandMetadata')
    browse_endpoint: BrowseEndpoint2 | None = Field(None, alias='browseEndpoint')

class SignInEndpoint(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    next_endpoint: NextEndpoint | None = Field(None, alias='nextEndpoint')
    idam_tag: str | None = Field(None, alias='idamTag')

class NavigationEndpoint(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    click_tracking_params: str | None = Field(None, alias='clickTrackingParams')
    command_metadata: CommandMetadata13 | None = Field(None, alias='commandMetadata')
    sign_in_endpoint: SignInEndpoint | None = Field(None, alias='signInEndpoint')

class ButtonRenderer(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    style: str | None = None
    size: str | None = None
    is_disabled: bool | None = Field(None, alias='isDisabled')
    text: Text1 | None = None
    navigation_endpoint: NavigationEndpoint | None = Field(None, alias='navigationEndpoint')
    tracking_params: str | None = Field(None, alias='trackingParams')

class Button1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    button_renderer: ButtonRenderer | None = Field(None, alias='buttonRenderer')

class ModalWithTitleAndButtonRenderer(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    title: Title2 | None = None
    content: Content4 | None = None
    button: Button1 | None = None

class Modal(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    modal_with_title_and_button_renderer: ModalWithTitleAndButtonRenderer | None = Field(None, alias='modalWithTitleAndButtonRenderer')

class ModalEndpoint(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    modal: Modal | None = None

class DefaultNavigationEndpoint(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    click_tracking_params: str | None = Field(None, alias='clickTrackingParams')
    command_metadata: CommandMetadata12 | None = Field(None, alias='commandMetadata')
    modal_endpoint: ModalEndpoint | None = Field(None, alias='modalEndpoint')

class AccessibilityData1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    label: str | None = None

class AccessibilityData(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    accessibility_data: AccessibilityData1 | None = Field(None, alias='accessibilityData')

class AccessibilityData2(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    label: str | None = None

class ToggledAccessibilityData(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    accessibility_data: AccessibilityData2 | None = Field(None, alias='accessibilityData')

class ToggleButtonRenderer(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    style: Style | None = None
    size: Size | None = None
    is_toggled: bool | None = Field(None, alias='isToggled')
    is_disabled: bool | None = Field(None, alias='isDisabled')
    default_icon: DefaultIcon | None = Field(None, alias='defaultIcon')
    toggled_icon: ToggledIcon | None = Field(None, alias='toggledIcon')
    tracking_params: str | None = Field(None, alias='trackingParams')
    default_tooltip: str | None = Field(None, alias='defaultTooltip')
    toggled_tooltip: str | None = Field(None, alias='toggledTooltip')
    toggled_style: ToggledStyle | None = Field(None, alias='toggledStyle')
    default_navigation_endpoint: DefaultNavigationEndpoint | None = Field(None, alias='defaultNavigationEndpoint')
    accessibility_data: AccessibilityData | None = Field(None, alias='accessibilityData')
    toggled_accessibility_data: ToggledAccessibilityData | None = Field(None, alias='toggledAccessibilityData')

class SaveButton(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    toggle_button_renderer: ToggleButtonRenderer | None = Field(None, alias='toggleButtonRenderer')

class WebCommandMetadata15(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    send_post: bool | None = Field(None, alias='sendPost')
    api_url: str | None = Field(None, alias='apiUrl')

class CommandMetadata15(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    web_command_metadata: WebCommandMetadata15 | None = Field(None, alias='webCommandMetadata')

class Popup1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    unified_share_panel_renderer: UnifiedSharePanelRenderer | None = Field(None, alias='unifiedSharePanelRenderer')

class OpenPopupAction1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    popup: Popup1 | None = None
    popup_type: str | None = Field(None, alias='popupType')
    be_reused: bool | None = Field(None, alias='beReused')

class Command1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    click_tracking_params: str | None = Field(None, alias='clickTrackingParams')
    open_popup_action: OpenPopupAction1 | None = Field(None, alias='openPopupAction')

class ShareEntityServiceEndpoint1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    serialized_share_entity: str | None = Field(None, alias='serializedShareEntity')
    commands: list[Command1] | None = None

class NavigationEndpoint1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    click_tracking_params: str | None = Field(None, alias='clickTrackingParams')
    command_metadata: CommandMetadata15 | None = Field(None, alias='commandMetadata')
    share_entity_service_endpoint: ShareEntityServiceEndpoint1 | None = Field(None, alias='shareEntityServiceEndpoint')

class Accessibility(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    label: str | None = None

class AccessibilityData3(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    accessibility_data: AccessibilityData2 | None = Field(None, alias='accessibilityData')

class ButtonRenderer1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    style: str | None = None
    size: str | None = None
    is_disabled: bool | None = Field(None, alias='isDisabled')
    icon: Icon1 | None = None
    navigation_endpoint: NavigationEndpoint1 | None = Field(None, alias='navigationEndpoint')
    accessibility: Accessibility | None = None
    tooltip: str | None = None
    tracking_params: str | None = Field(None, alias='trackingParams')
    accessibility_data: AccessibilityData3 | None = Field(None, alias='accessibilityData')

class ShareButton(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    button_renderer: ButtonRenderer1 | None = Field(None, alias='buttonRenderer')

class Subtitle(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    simple_text: str | None = Field(None, alias='simpleText')

class WebCommandMetadata16(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    url: str | None = None
    web_page_type: str | None = Field(None, alias='webPageType')
    root_ve: int | None = Field(None, alias='rootVe')

class CommandMetadata16(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    web_command_metadata: WebCommandMetadata16 | None = Field(None, alias='webCommandMetadata')

class LoggingContext4(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    vss_logging_context: VssLoggingContext | None = Field(None, alias='vssLoggingContext')

class Html5PlaybackOnesieConfig4(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    common_config: CommonConfig | None = Field(None, alias='commonConfig')

class WatchEndpointSupportedOnesieConfig4(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    html5_playback_onesie_config: Html5PlaybackOnesieConfig4 | None = Field(None, alias='html5PlaybackOnesieConfig')

class WatchEndpoint4(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    video_id: str | None = Field(None, alias='videoId')
    playlist_id: str | None = Field(None, alias='playlistId')
    player_params: str | None = Field(None, alias='playerParams')
    logging_context: LoggingContext4 | None = Field(None, alias='loggingContext')
    watch_endpoint_supported_onesie_config: WatchEndpointSupportedOnesieConfig4 | None = Field(None, alias='watchEndpointSupportedOnesieConfig')

class NavigationEndpoint2(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    click_tracking_params: str | None = Field(None, alias='clickTrackingParams')
    command_metadata: CommandMetadata16 | None = Field(None, alias='commandMetadata')
    watch_endpoint: WatchEndpoint4 | None = Field(None, alias='watchEndpoint')

class ButtonRenderer2(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    style: str | None = None
    size: str | None = None
    is_disabled: bool | None = Field(None, alias='isDisabled')
    text: Text1 | None = None
    icon: Icon1 | None = None
    navigation_endpoint: NavigationEndpoint2 | None = Field(None, alias='navigationEndpoint')
    tracking_params: str | None = Field(None, alias='trackingParams')

class PlayButton(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    button_renderer: ButtonRenderer2 | None = Field(None, alias='buttonRenderer')

class CommandMetadata17(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    web_command_metadata: WebCommandMetadata16 | None = Field(None, alias='webCommandMetadata')

class LoggingContext5(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    vss_logging_context: VssLoggingContext | None = Field(None, alias='vssLoggingContext')

class Html5PlaybackOnesieConfig5(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    common_config: CommonConfig | None = Field(None, alias='commonConfig')

class WatchEndpointSupportedOnesieConfig5(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    html5_playback_onesie_config: Html5PlaybackOnesieConfig5 | None = Field(None, alias='html5PlaybackOnesieConfig')

class WatchEndpoint5(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    video_id: str | None = Field(None, alias='videoId')
    playlist_id: str | None = Field(None, alias='playlistId')
    params: str | None = None
    player_params: str | None = Field(None, alias='playerParams')
    logging_context: LoggingContext5 | None = Field(None, alias='loggingContext')
    watch_endpoint_supported_onesie_config: WatchEndpointSupportedOnesieConfig5 | None = Field(None, alias='watchEndpointSupportedOnesieConfig')

class NavigationEndpoint3(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    click_tracking_params: str | None = Field(None, alias='clickTrackingParams')
    command_metadata: CommandMetadata17 | None = Field(None, alias='commandMetadata')
    watch_endpoint: WatchEndpoint5 | None = Field(None, alias='watchEndpoint')

class ButtonRenderer3(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    style: str | None = None
    size: str | None = None
    is_disabled: bool | None = Field(None, alias='isDisabled')
    text: Text1 | None = None
    icon: Icon1 | None = None
    navigation_endpoint: NavigationEndpoint3 | None = Field(None, alias='navigationEndpoint')
    tracking_params: str | None = Field(None, alias='trackingParams')

class ShufflePlayButton(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    button_renderer: ButtonRenderer3 | None = Field(None, alias='buttonRenderer')

class Thumbnail3(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    url: str | None = None
    width: int | None = None
    height: int | None = None

class Thumbnail2(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    thumbnails: list[Thumbnail3] | None = None

class BackgroundImageConfig(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    thumbnail: Thumbnail2 | None = None

class GradientColorConfigItem(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    light_theme_color: int | None = Field(None, alias='lightThemeColor')
    dark_theme_color: int | None = Field(None, alias='darkThemeColor')
    start_location: int | float | None = Field(None, alias='startLocation')

class Config(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    light_theme_background_color: int | None = Field(None, alias='lightThemeBackgroundColor')
    dark_theme_background_color: int | None = Field(None, alias='darkThemeBackgroundColor')
    color_source_size_multiplier: int | None = Field(None, alias='colorSourceSizeMultiplier')
    apply_client_image_blur: bool | None = Field(None, alias='applyClientImageBlur')

class CinematicContainerRenderer(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    background_image_config: BackgroundImageConfig | None = Field(None, alias='backgroundImageConfig')
    gradient_color_config: list[GradientColorConfigItem] | None = Field(None, alias='gradientColorConfig')
    config: Config | None = None

class CinematicContainer(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    cinematic_container_renderer: CinematicContainerRenderer | None = Field(None, alias='cinematicContainerRenderer')

class Text5(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    runs: list[Run] | None = None
    simple_text: str | None = Field(None, alias='simpleText')

class PlaylistBylineRenderer(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    text: Text5 | None = None

class BylineItem(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    playlist_byline_renderer: PlaylistBylineRenderer | None = Field(None, alias='playlistBylineRenderer')

class PlaylistHeaderRenderer(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    playlist_id: str | None = Field(None, alias='playlistId')
    title: Title2 | None = None
    num_videos_text: NumVideosText | None = Field(None, alias='numVideosText')
    view_count_text: ViewCountText | None = Field(None, alias='viewCountText')
    share_data: ShareData | None = Field(None, alias='shareData')
    is_editable: bool | None = Field(None, alias='isEditable')
    editable_details: EditableDetails | None = Field(None, alias='editableDetails')
    tracking_params: str | None = Field(None, alias='trackingParams')
    service_endpoints: list[ServiceEndpoint] | None = Field(None, alias='serviceEndpoints')
    stats: list[Stat] | None = None
    brief_stats: list[BriefStat] | None = Field(None, alias='briefStats')
    playlist_header_banner: PlaylistHeaderBanner | None = Field(None, alias='playlistHeaderBanner')
    save_button: SaveButton | None = Field(None, alias='saveButton')
    share_button: ShareButton | None = Field(None, alias='shareButton')
    subtitle: Subtitle | None = None
    play_button: PlayButton | None = Field(None, alias='playButton')
    shuffle_play_button: ShufflePlayButton | None = Field(None, alias='shufflePlayButton')
    cinematic_container: CinematicContainer | None = Field(None, alias='cinematicContainer')
    byline: list[BylineItem] | None = None

class Header(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    playlist_header_renderer: PlaylistHeaderRenderer | None = Field(None, alias='playlistHeaderRenderer')

class PlaylistMetadataRenderer(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    title: str | None = None
    play_url: str | None = Field(None, alias='playUrl')
    android_play_url: str | None = Field(None, alias='androidPlayUrl')
    album_name: str | None = Field(None, alias='albumName')
    android_appindexing_link: str | None = Field(None, alias='androidAppindexingLink')
    ios_appindexing_link: str | None = Field(None, alias='iosAppindexingLink')

class Metadata2(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    playlist_metadata_renderer: PlaylistMetadataRenderer | None = Field(None, alias='playlistMetadataRenderer')

class IconImage(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    icon_type: str | None = Field(None, alias='iconType')

class TooltipText(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    runs: list[Run] | None = None

class WebCommandMetadata18(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    url: str | None = None
    web_page_type: str | None = Field(None, alias='webPageType')
    root_ve: int | None = Field(None, alias='rootVe')
    api_url: str | None = Field(None, alias='apiUrl')

class CommandMetadata18(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    web_command_metadata: WebCommandMetadata18 | None = Field(None, alias='webCommandMetadata')

class Endpoint(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    click_tracking_params: str | None = Field(None, alias='clickTrackingParams')
    command_metadata: CommandMetadata18 | None = Field(None, alias='commandMetadata')
    browse_endpoint: BrowseEndpoint2 | None = Field(None, alias='browseEndpoint')

class TopbarLogoRenderer(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    icon_image: IconImage | None = Field(None, alias='iconImage')
    tooltip_text: TooltipText | None = Field(None, alias='tooltipText')
    endpoint: Endpoint | None = None
    tracking_params: str | None = Field(None, alias='trackingParams')
    override_entity_key: str | None = Field(None, alias='overrideEntityKey')

class Logo(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    topbar_logo_renderer: TopbarLogoRenderer | None = Field(None, alias='topbarLogoRenderer')

class PlaceholderText(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    runs: list[Run] | None = None

class WebSearchboxConfig(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    request_language: str | None = Field(None, alias='requestLanguage')
    request_domain: str | None = Field(None, alias='requestDomain')
    has_onscreen_keyboard: bool | None = Field(None, alias='hasOnscreenKeyboard')
    focus_searchbox: bool | None = Field(None, alias='focusSearchbox')

class Config1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    web_searchbox_config: WebSearchboxConfig | None = Field(None, alias='webSearchboxConfig')

class WebCommandMetadata19(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    url: str | None = None
    web_page_type: str | None = Field(None, alias='webPageType')
    root_ve: int | None = Field(None, alias='rootVe')

class CommandMetadata19(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    web_command_metadata: WebCommandMetadata19 | None = Field(None, alias='webCommandMetadata')

class SearchEndpoint1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    query: str | None = None

class SearchEndpoint(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    click_tracking_params: str | None = Field(None, alias='clickTrackingParams')
    command_metadata: CommandMetadata19 | None = Field(None, alias='commandMetadata')
    search_endpoint: SearchEndpoint1 | None = Field(None, alias='searchEndpoint')

class AccessibilityData6(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    label: str | None = None

class AccessibilityData5(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    accessibility_data: AccessibilityData6 | None = Field(None, alias='accessibilityData')

class ButtonRenderer4(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    style: str | None = None
    size: str | None = None
    is_disabled: bool | None = Field(None, alias='isDisabled')
    icon: Icon1 | None = None
    tracking_params: str | None = Field(None, alias='trackingParams')
    accessibility_data: AccessibilityData5 | None = Field(None, alias='accessibilityData')

class ClearButton(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    button_renderer: ButtonRenderer4 | None = Field(None, alias='buttonRenderer')

class Headline(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    content: str | None = None

class DialogHeaderViewModel(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    headline: Headline | None = None

class Header1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    dialog_header_view_model: DialogHeaderViewModel | None = Field(None, alias='dialogHeaderViewModel')

class ButtonViewModel3(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    title: str | None = None
    style: str | None = None
    tracking_params: str | None = Field(None, alias='trackingParams')
    is_full_width: bool | None = Field(None, alias='isFullWidth')
    type: str | None = None

class PrimaryButton(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    button_view_model: ButtonViewModel3 | None = Field(None, alias='buttonViewModel')

class SecondaryButton(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    button_view_model: ButtonViewModel3 | None = Field(None, alias='buttonViewModel')

class PanelFooterViewModel(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    primary_button: PrimaryButton | None = Field(None, alias='primaryButton')
    secondary_button: SecondaryButton | None = Field(None, alias='secondaryButton')
    should_hide_divider: bool | None = Field(None, alias='shouldHideDivider')

class Footer(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    panel_footer_view_model: PanelFooterViewModel | None = Field(None, alias='panelFooterViewModel')

class Text6(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    content: str | None = None

class Paragraph(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    text: Text6 | None = None

class BasicContentViewModel(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    paragraphs: list[Paragraph] | None = None

class Content5(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    basic_content_view_model: BasicContentViewModel | None = Field(None, alias='basicContentViewModel')

class DialogViewModel(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    header: Header1 | None = None
    footer: Footer | None = None
    content: Content5 | None = None

class InlineContent1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    dialog_view_model: DialogViewModel | None = Field(None, alias='dialogViewModel')

class PanelLoadingStrategy1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    inline_content: InlineContent1 | None = Field(None, alias='inlineContent')

class ShowDialogCommand(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    panel_loading_strategy: PanelLoadingStrategy1 | None = Field(None, alias='panelLoadingStrategy')

class ShowImageSourceDialog(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    click_tracking_params: str | None = Field(None, alias='clickTrackingParams')
    show_dialog_command: ShowDialogCommand | None = Field(None, alias='showDialogCommand')

class FusionSearchboxRenderer(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    icon: Icon1 | None = None
    placeholder_text: PlaceholderText | None = Field(None, alias='placeholderText')
    config: Config1 | None = None
    tracking_params: str | None = Field(None, alias='trackingParams')
    search_endpoint: SearchEndpoint | None = Field(None, alias='searchEndpoint')
    clear_button: ClearButton | None = Field(None, alias='clearButton')
    show_image_source_dialog: ShowImageSourceDialog | None = Field(None, alias='showImageSourceDialog')
    disable_ai_appearance: bool | None = Field(None, alias='disableAiAppearance')

class Searchbox(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    fusion_searchbox_renderer: FusionSearchboxRenderer | None = Field(None, alias='fusionSearchboxRenderer')

class WebCommandMetadata20(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    send_post: bool | None = Field(None, alias='sendPost')
    api_url: str | None = Field(None, alias='apiUrl')

class CommandMetadata20(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    web_command_metadata: WebCommandMetadata20 | None = Field(None, alias='webCommandMetadata')

class MultiPageMenuRenderer(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    tracking_params: str | None = Field(None, alias='trackingParams')
    style: str | None = None
    show_loading_spinner: bool | None = Field(None, alias='showLoadingSpinner')

class Popup2(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    multi_page_menu_renderer: MultiPageMenuRenderer | None = Field(None, alias='multiPageMenuRenderer')

class OpenPopupAction2(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    popup: Popup2 | None = None
    popup_type: str | None = Field(None, alias='popupType')
    be_reused: bool | None = Field(None, alias='beReused')

class Action5(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    click_tracking_params: str | None = Field(None, alias='clickTrackingParams')
    open_popup_action: OpenPopupAction2 | None = Field(None, alias='openPopupAction')

class SignalServiceEndpoint2(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    signal: str | None = None
    actions: list[Action5] | None = None

class MenuRequest(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    click_tracking_params: str | None = Field(None, alias='clickTrackingParams')
    command_metadata: CommandMetadata20 | None = Field(None, alias='commandMetadata')
    signal_service_endpoint: SignalServiceEndpoint2 | None = Field(None, alias='signalServiceEndpoint')

class AccessibilityData7(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    label: str | None = None

class Accessibility1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    accessibility_data: AccessibilityData7 | None = Field(None, alias='accessibilityData')

class TopbarMenuButtonRenderer(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    icon: Icon1 | None = None
    menu_request: MenuRequest | None = Field(None, alias='menuRequest')
    tracking_params: str | None = Field(None, alias='trackingParams')
    accessibility: Accessibility1 | None = None
    tooltip: str | None = None
    style: str | None = None

class Text7(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    runs: list[Run] | None = None

class WebCommandMetadata21(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    url: str | None = None
    web_page_type: str | None = Field(None, alias='webPageType')
    root_ve: int | None = Field(None, alias='rootVe')

class CommandMetadata21(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    web_command_metadata: WebCommandMetadata21 | None = Field(None, alias='webCommandMetadata')

class SignInEndpoint1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    idam_tag: str | None = Field(None, alias='idamTag')

class NavigationEndpoint4(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    click_tracking_params: str | None = Field(None, alias='clickTrackingParams')
    command_metadata: CommandMetadata21 | None = Field(None, alias='commandMetadata')
    sign_in_endpoint: SignInEndpoint1 | None = Field(None, alias='signInEndpoint')

class ButtonRenderer5(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    style: str | None = None
    size: str | None = None
    text: Text7 | None = None
    icon: Icon1 | None = None
    navigation_endpoint: NavigationEndpoint4 | None = Field(None, alias='navigationEndpoint')
    tracking_params: str | None = Field(None, alias='trackingParams')
    target_id: str | None = Field(None, alias='targetId')

class TopbarButton(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    topbar_menu_button_renderer: TopbarMenuButtonRenderer | None = Field(None, alias='topbarMenuButtonRenderer')
    button_renderer: ButtonRenderer5 | None = Field(None, alias='buttonRenderer')

class Title4(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    runs: list[Run] | None = None

class Title5(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    runs: list[Run] | None = None

class Label(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    runs: list[Run] | None = None

class HotkeyAccessibilityLabel(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    accessibility_data: AccessibilityData7 | None = Field(None, alias='accessibilityData')

class HotkeyDialogSectionOptionRenderer(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    label: Label | None = None
    hotkey: str | None = None
    hotkey_accessibility_label: HotkeyAccessibilityLabel | None = Field(None, alias='hotkeyAccessibilityLabel')

class Option(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    hotkey_dialog_section_option_renderer: HotkeyDialogSectionOptionRenderer | None = Field(None, alias='hotkeyDialogSectionOptionRenderer')

class HotkeyDialogSectionRenderer(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    title: Title5 | None = None
    options: list[Option] | None = None

class Section(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    hotkey_dialog_section_renderer: HotkeyDialogSectionRenderer | None = Field(None, alias='hotkeyDialogSectionRenderer')

class Text8(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    runs: list[Run] | None = None

class ButtonRenderer6(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    style: str | None = None
    size: str | None = None
    is_disabled: bool | None = Field(None, alias='isDisabled')
    text: Text8 | None = None
    tracking_params: str | None = Field(None, alias='trackingParams')

class DismissButton(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    button_renderer: ButtonRenderer6 | None = Field(None, alias='buttonRenderer')

class HotkeyDialogRenderer(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    title: Title4 | None = None
    sections: list[Section] | None = None
    dismiss_button: DismissButton | None = Field(None, alias='dismissButton')
    tracking_params: str | None = Field(None, alias='trackingParams')

class HotkeyDialog(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    hotkey_dialog_renderer: HotkeyDialogRenderer | None = Field(None, alias='hotkeyDialogRenderer')

class WebCommandMetadata22(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    send_post: bool | None = Field(None, alias='sendPost')

class CommandMetadata22(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    web_command_metadata: WebCommandMetadata22 | None = Field(None, alias='webCommandMetadata')

class SignalAction(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    signal: str | None = None

class Action6(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    click_tracking_params: str | None = Field(None, alias='clickTrackingParams')
    signal_action: SignalAction | None = Field(None, alias='signalAction')

class SignalServiceEndpoint3(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    signal: str | None = None
    actions: list[Action6] | None = None

class Command2(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    click_tracking_params: str | None = Field(None, alias='clickTrackingParams')
    command_metadata: CommandMetadata22 | None = Field(None, alias='commandMetadata')
    signal_service_endpoint: SignalServiceEndpoint3 | None = Field(None, alias='signalServiceEndpoint')

class ButtonRenderer7(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    tracking_params: str | None = Field(None, alias='trackingParams')
    command: Command2 | None = None

class BackButton(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    button_renderer: ButtonRenderer7 | None = Field(None, alias='buttonRenderer')

class CommandMetadata23(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    web_command_metadata: WebCommandMetadata22 | None = Field(None, alias='webCommandMetadata')

class Action7(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    click_tracking_params: str | None = Field(None, alias='clickTrackingParams')
    signal_action: SignalAction | None = Field(None, alias='signalAction')

class SignalServiceEndpoint4(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    signal: str | None = None
    actions: list[Action7] | None = None

class Command3(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    click_tracking_params: str | None = Field(None, alias='clickTrackingParams')
    command_metadata: CommandMetadata23 | None = Field(None, alias='commandMetadata')
    signal_service_endpoint: SignalServiceEndpoint4 | None = Field(None, alias='signalServiceEndpoint')

class ButtonRenderer8(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    tracking_params: str | None = Field(None, alias='trackingParams')
    command: Command3 | None = None

class ForwardButton(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    button_renderer: ButtonRenderer8 | None = Field(None, alias='buttonRenderer')

class Text9(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    runs: list[Run] | None = None

class CommandMetadata24(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    web_command_metadata: WebCommandMetadata22 | None = Field(None, alias='webCommandMetadata')

class Action8(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    click_tracking_params: str | None = Field(None, alias='clickTrackingParams')
    signal_action: SignalAction | None = Field(None, alias='signalAction')

class SignalServiceEndpoint5(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    signal: str | None = None
    actions: list[Action8] | None = None

class Command4(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    click_tracking_params: str | None = Field(None, alias='clickTrackingParams')
    command_metadata: CommandMetadata24 | None = Field(None, alias='commandMetadata')
    signal_service_endpoint: SignalServiceEndpoint5 | None = Field(None, alias='signalServiceEndpoint')

class ButtonRenderer9(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    style: str | None = None
    size: str | None = None
    is_disabled: bool | None = Field(None, alias='isDisabled')
    text: Text9 | None = None
    tracking_params: str | None = Field(None, alias='trackingParams')
    command: Command4 | None = None

class A11ySkipNavigationButton(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    button_renderer: ButtonRenderer9 | None = Field(None, alias='buttonRenderer')

class CommandMetadata25(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    web_command_metadata: WebCommandMetadata22 | None = Field(None, alias='webCommandMetadata')

class PlaceholderHeader(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    runs: list[Run] | None = None

class PromptHeader(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    runs: list[Run] | None = None

class ExampleQuery1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    runs: list[Run] | None = None

class ExampleQuery2(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    runs: list[Run] | None = None

class PromptMicrophoneLabel(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    runs: list[Run] | None = None

class LoadingHeader(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    runs: list[Run] | None = None

class ConnectionErrorHeader(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    runs: list[Run] | None = None

class ConnectionErrorMicrophoneLabel(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    runs: list[Run] | None = None

class PermissionsHeader(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    runs: list[Run] | None = None

class PermissionsSubtext(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    runs: list[Run] | None = None

class DisabledHeader(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    runs: list[Run] | None = None

class DisabledSubtext(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    runs: list[Run] | None = None

class MicrophoneButtonAriaLabel(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    runs: list[Run] | None = None

class AccessibilityData9(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    accessibility_data: AccessibilityData7 | None = Field(None, alias='accessibilityData')

class ButtonRenderer11(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    style: str | None = None
    size: str | None = None
    is_disabled: bool | None = Field(None, alias='isDisabled')
    icon: Icon1 | None = None
    tracking_params: str | None = Field(None, alias='trackingParams')
    accessibility_data: AccessibilityData9 | None = Field(None, alias='accessibilityData')

class ExitButton(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    button_renderer: ButtonRenderer11 | None = Field(None, alias='buttonRenderer')

class MicrophoneOffPromptHeader(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    runs: list[Run] | None = None

class VoiceSearchDialogRenderer(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    placeholder_header: PlaceholderHeader | None = Field(None, alias='placeholderHeader')
    prompt_header: PromptHeader | None = Field(None, alias='promptHeader')
    example_query1: ExampleQuery1 | None = Field(None, alias='exampleQuery1')
    example_query2: ExampleQuery2 | None = Field(None, alias='exampleQuery2')
    prompt_microphone_label: PromptMicrophoneLabel | None = Field(None, alias='promptMicrophoneLabel')
    loading_header: LoadingHeader | None = Field(None, alias='loadingHeader')
    connection_error_header: ConnectionErrorHeader | None = Field(None, alias='connectionErrorHeader')
    connection_error_microphone_label: ConnectionErrorMicrophoneLabel | None = Field(None, alias='connectionErrorMicrophoneLabel')
    permissions_header: PermissionsHeader | None = Field(None, alias='permissionsHeader')
    permissions_subtext: PermissionsSubtext | None = Field(None, alias='permissionsSubtext')
    disabled_header: DisabledHeader | None = Field(None, alias='disabledHeader')
    disabled_subtext: DisabledSubtext | None = Field(None, alias='disabledSubtext')
    microphone_button_aria_label: MicrophoneButtonAriaLabel | None = Field(None, alias='microphoneButtonAriaLabel')
    exit_button: ExitButton | None = Field(None, alias='exitButton')
    tracking_params: str | None = Field(None, alias='trackingParams')
    microphone_off_prompt_header: MicrophoneOffPromptHeader | None = Field(None, alias='microphoneOffPromptHeader')

class Popup3(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    voice_search_dialog_renderer: VoiceSearchDialogRenderer | None = Field(None, alias='voiceSearchDialogRenderer')

class OpenPopupAction3(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    popup: Popup3 | None = None
    popup_type: str | None = Field(None, alias='popupType')

class Action9(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    click_tracking_params: str | None = Field(None, alias='clickTrackingParams')
    open_popup_action: OpenPopupAction3 | None = Field(None, alias='openPopupAction')

class SignalServiceEndpoint6(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    signal: str | None = None
    actions: list[Action9] | None = None

class ServiceEndpoint1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    click_tracking_params: str | None = Field(None, alias='clickTrackingParams')
    command_metadata: CommandMetadata25 | None = Field(None, alias='commandMetadata')
    signal_service_endpoint: SignalServiceEndpoint6 | None = Field(None, alias='signalServiceEndpoint')

class AccessibilityData12(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    label: str | None = None

class AccessibilityData11(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    accessibility_data: AccessibilityData12 | None = Field(None, alias='accessibilityData')

class ButtonRenderer10(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    style: str | None = None
    size: str | None = None
    is_disabled: bool | None = Field(None, alias='isDisabled')
    service_endpoint: ServiceEndpoint1 | None = Field(None, alias='serviceEndpoint')
    icon: Icon1 | None = None
    tooltip: str | None = None
    tracking_params: str | None = Field(None, alias='trackingParams')
    accessibility_data: AccessibilityData11 | None = Field(None, alias='accessibilityData')

class VoiceSearchButton(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    button_renderer: ButtonRenderer10 | None = Field(None, alias='buttonRenderer')

class DesktopTopbarRenderer(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    logo: Logo | None = None
    searchbox: Searchbox | None = None
    tracking_params: str | None = Field(None, alias='trackingParams')
    topbar_buttons: list[TopbarButton] | None = Field(None, alias='topbarButtons')
    hotkey_dialog: HotkeyDialog | None = Field(None, alias='hotkeyDialog')
    back_button: BackButton | None = Field(None, alias='backButton')
    forward_button: ForwardButton | None = Field(None, alias='forwardButton')
    a11y_skip_navigation_button: A11ySkipNavigationButton | None = Field(None, alias='a11ySkipNavigationButton')
    voice_search_button: VoiceSearchButton | None = Field(None, alias='voiceSearchButton')

class Topbar(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    desktop_topbar_renderer: DesktopTopbarRenderer | None = Field(None, alias='desktopTopbarRenderer')

class Thumbnail5(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    url: str | None = None
    width: int | None = None
    height: int | None = None

class Thumbnail4(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    thumbnails: list[Thumbnail5] | None = None
    sampled_thumbnail_color: SampledThumbnailColor | None = Field(None, alias='sampledThumbnailColor')
    dark_color_palette: DarkColorPalette | None = Field(None, alias='darkColorPalette')
    vibrant_color_palette: VibrantColorPalette | None = Field(None, alias='vibrantColorPalette')

class LinkAlternate(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    href_url: str | None = Field(None, alias='hrefUrl')

class MicroformatDataRenderer(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    url_canonical: str | None = Field(None, alias='urlCanonical')
    title: str | None = None
    description: str | None = None
    thumbnail: Thumbnail4 | None = None
    site_name: str | None = Field(None, alias='siteName')
    app_name: str | None = Field(None, alias='appName')
    android_package: str | None = Field(None, alias='androidPackage')
    ios_app_store_id: str | None = Field(None, alias='iosAppStoreId')
    ios_app_arguments: str | None = Field(None, alias='iosAppArguments')
    og_type: str | None = Field(None, alias='ogType')
    url_applinks_web: str | None = Field(None, alias='urlApplinksWeb')
    url_applinks_ios: str | None = Field(None, alias='urlApplinksIos')
    url_applinks_android: str | None = Field(None, alias='urlApplinksAndroid')
    url_twitter_ios: str | None = Field(None, alias='urlTwitterIos')
    url_twitter_android: str | None = Field(None, alias='urlTwitterAndroid')
    twitter_card_type: str | None = Field(None, alias='twitterCardType')
    twitter_site_handle: str | None = Field(None, alias='twitterSiteHandle')
    schema_dot_org_type: str | None = Field(None, alias='schemaDotOrgType')
    noindex: bool | None = None
    unlisted: bool | None = None
    link_alternates: list[LinkAlternate] | None = Field(None, alias='linkAlternates')

class Microformat(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    microformat_data_renderer: MicroformatDataRenderer | None = Field(None, alias='microformatDataRenderer')

class Thumbnail7(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    url: str | None = None
    width: int | None = None
    height: int | None = None

class Thumbnail6(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    thumbnails: list[Thumbnail7] | None = None
    sampled_thumbnail_color: SampledThumbnailColor | None = Field(None, alias='sampledThumbnailColor')
    dark_color_palette: DarkColorPalette | None = Field(None, alias='darkColorPalette')
    vibrant_color_palette: VibrantColorPalette | None = Field(None, alias='vibrantColorPalette')

class PlaylistCustomThumbnailRenderer(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    thumbnail: Thumbnail6 | None = None

class ThumbnailRenderer(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    playlist_custom_thumbnail_renderer: PlaylistCustomThumbnailRenderer | None = Field(None, alias='playlistCustomThumbnailRenderer')

class WebCommandMetadata26(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    url: str | None = None
    web_page_type: str | None = Field(None, alias='webPageType')
    root_ve: int | None = Field(None, alias='rootVe')

class CommandMetadata26(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    web_command_metadata: WebCommandMetadata26 | None = Field(None, alias='webCommandMetadata')

class LoggingContext6(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    vss_logging_context: VssLoggingContext | None = Field(None, alias='vssLoggingContext')

class Html5PlaybackOnesieConfig6(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    common_config: CommonConfig | None = Field(None, alias='commonConfig')

class WatchEndpointSupportedOnesieConfig6(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    html5_playback_onesie_config: Html5PlaybackOnesieConfig6 | None = Field(None, alias='html5PlaybackOnesieConfig')

class WatchEndpoint6(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    video_id: str | None = Field(None, alias='videoId')
    playlist_id: str | None = Field(None, alias='playlistId')
    player_params: str | None = Field(None, alias='playerParams')
    logging_context: LoggingContext6 | None = Field(None, alias='loggingContext')
    watch_endpoint_supported_onesie_config: WatchEndpointSupportedOnesieConfig6 | None = Field(None, alias='watchEndpointSupportedOnesieConfig')

class NavigationEndpoint5(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    click_tracking_params: str | None = Field(None, alias='clickTrackingParams')
    command_metadata: CommandMetadata26 | None = Field(None, alias='commandMetadata')
    watch_endpoint: WatchEndpoint6 | None = Field(None, alias='watchEndpoint')

class Run26(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    text: str | None = None
    navigation_endpoint: NavigationEndpoint5 | None = Field(None, alias='navigationEndpoint')

class Title6(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    runs: list[Run26] | None = None

class Run27(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    text: str | None = None

class Stat1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    runs: list[Run27] | None = None
    simple_text: str | None = Field(None, alias='simpleText')

class Text10(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    simple_text: str | None = Field(None, alias='simpleText')

class WebCommandMetadata27(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    ignore_navigation: bool | None = Field(None, alias='ignoreNavigation')

class CommandMetadata27(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    web_command_metadata: WebCommandMetadata27 | None = Field(None, alias='webCommandMetadata')

class Title7(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    simple_text: str | None = Field(None, alias='simpleText')

class Content6(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    simple_text: str | None = Field(None, alias='simpleText')

class Text11(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    runs: list[Run27] | None = None

class WebCommandMetadata28(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    url: str | None = None
    web_page_type: str | None = Field(None, alias='webPageType')
    root_ve: int | None = Field(None, alias='rootVe')

class CommandMetadata28(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    web_command_metadata: WebCommandMetadata28 | None = Field(None, alias='webCommandMetadata')

class WebCommandMetadata29(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    url: str | None = None
    web_page_type: str | None = Field(None, alias='webPageType')
    root_ve: int | None = Field(None, alias='rootVe')
    api_url: str | None = Field(None, alias='apiUrl')

class CommandMetadata29(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    web_command_metadata: WebCommandMetadata29 | None = Field(None, alias='webCommandMetadata')

class NextEndpoint1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    click_tracking_params: str | None = Field(None, alias='clickTrackingParams')
    command_metadata: CommandMetadata29 | None = Field(None, alias='commandMetadata')
    browse_endpoint: BrowseEndpoint2 | None = Field(None, alias='browseEndpoint')

class SignInEndpoint2(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    next_endpoint: NextEndpoint1 | None = Field(None, alias='nextEndpoint')

class NavigationEndpoint7(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    click_tracking_params: str | None = Field(None, alias='clickTrackingParams')
    command_metadata: CommandMetadata28 | None = Field(None, alias='commandMetadata')
    sign_in_endpoint: SignInEndpoint2 | None = Field(None, alias='signInEndpoint')

class ButtonRenderer12(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    style: str | None = None
    size: str | None = None
    is_disabled: bool | None = Field(None, alias='isDisabled')
    text: Text11 | None = None
    navigation_endpoint: NavigationEndpoint7 | None = Field(None, alias='navigationEndpoint')
    tracking_params: str | None = Field(None, alias='trackingParams')

class Button2(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    button_renderer: ButtonRenderer12 | None = Field(None, alias='buttonRenderer')

class ModalWithTitleAndButtonRenderer1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    title: Title7 | None = None
    content: Content6 | None = None
    button: Button2 | None = None

class Modal1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    modal_with_title_and_button_renderer: ModalWithTitleAndButtonRenderer1 | None = Field(None, alias='modalWithTitleAndButtonRenderer')

class ModalEndpoint1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    modal: Modal1 | None = None

class NavigationEndpoint6(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    click_tracking_params: str | None = Field(None, alias='clickTrackingParams')
    command_metadata: CommandMetadata27 | None = Field(None, alias='commandMetadata')
    modal_endpoint: ModalEndpoint1 | None = Field(None, alias='modalEndpoint')

class MenuNavigationItemRenderer(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    text: Text10 | None = None
    icon: Icon1 | None = None
    navigation_endpoint: NavigationEndpoint6 | None = Field(None, alias='navigationEndpoint')
    tracking_params: str | None = Field(None, alias='trackingParams')

class Item1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    menu_navigation_item_renderer: MenuNavigationItemRenderer | None = Field(None, alias='menuNavigationItemRenderer')

class WebCommandMetadata30(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    ignore_navigation: bool | None = Field(None, alias='ignoreNavigation')

class CommandMetadata30(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    web_command_metadata: WebCommandMetadata30 | None = Field(None, alias='webCommandMetadata')

class Text12(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    simple_text: str | None = Field(None, alias='simpleText')

class WebCommandMetadata31(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    url: str | None = None
    web_page_type: str | None = Field(None, alias='webPageType')
    root_ve: int | None = Field(None, alias='rootVe')

class CommandMetadata31(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    web_command_metadata: WebCommandMetadata31 | None = Field(None, alias='webCommandMetadata')

class WebCommandMetadata32(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    url: str | None = None
    web_page_type: str | None = Field(None, alias='webPageType')
    root_ve: int | None = Field(None, alias='rootVe')
    api_url: str | None = Field(None, alias='apiUrl')

class CommandMetadata32(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    web_command_metadata: WebCommandMetadata32 | None = Field(None, alias='webCommandMetadata')

class NextEndpoint2(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    click_tracking_params: str | None = Field(None, alias='clickTrackingParams')
    command_metadata: CommandMetadata32 | None = Field(None, alias='commandMetadata')
    browse_endpoint: BrowseEndpoint2 | None = Field(None, alias='browseEndpoint')

class SignInEndpoint3(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    next_endpoint: NextEndpoint2 | None = Field(None, alias='nextEndpoint')
    idam_tag: str | None = Field(None, alias='idamTag')

class NavigationEndpoint8(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    click_tracking_params: str | None = Field(None, alias='clickTrackingParams')
    command_metadata: CommandMetadata31 | None = Field(None, alias='commandMetadata')
    sign_in_endpoint: SignInEndpoint3 | None = Field(None, alias='signInEndpoint')

class ButtonRenderer13(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    style: str | None = None
    size: str | None = None
    is_disabled: bool | None = Field(None, alias='isDisabled')
    text: Text12 | None = None
    navigation_endpoint: NavigationEndpoint8 | None = Field(None, alias='navigationEndpoint')
    tracking_params: str | None = Field(None, alias='trackingParams')

class Button3(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    button_renderer: ButtonRenderer13 | None = Field(None, alias='buttonRenderer')

class ModalWithTitleAndButtonRenderer2(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    title: Title7 | None = None
    content: Content6 | None = None
    button: Button3 | None = None

class Modal2(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    modal_with_title_and_button_renderer: ModalWithTitleAndButtonRenderer2 | None = Field(None, alias='modalWithTitleAndButtonRenderer')

class ModalEndpoint2(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    modal: Modal2 | None = None

class DefaultNavigationEndpoint1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    click_tracking_params: str | None = Field(None, alias='clickTrackingParams')
    command_metadata: CommandMetadata30 | None = Field(None, alias='commandMetadata')
    modal_endpoint: ModalEndpoint2 | None = Field(None, alias='modalEndpoint')

class AccessibilityData14(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    label: str | None = None

class AccessibilityData13(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    accessibility_data: AccessibilityData14 | None = Field(None, alias='accessibilityData')

class AccessibilityData15(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    label: str | None = None

class ToggledAccessibilityData1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    accessibility_data: AccessibilityData15 | None = Field(None, alias='accessibilityData')

class ToggleButtonRenderer1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    style: Style | None = None
    size: Size | None = None
    is_toggled: bool | None = Field(None, alias='isToggled')
    is_disabled: bool | None = Field(None, alias='isDisabled')
    default_icon: DefaultIcon | None = Field(None, alias='defaultIcon')
    toggled_icon: ToggledIcon | None = Field(None, alias='toggledIcon')
    tracking_params: str | None = Field(None, alias='trackingParams')
    default_tooltip: str | None = Field(None, alias='defaultTooltip')
    toggled_tooltip: str | None = Field(None, alias='toggledTooltip')
    default_navigation_endpoint: DefaultNavigationEndpoint1 | None = Field(None, alias='defaultNavigationEndpoint')
    accessibility_data: AccessibilityData13 | None = Field(None, alias='accessibilityData')
    toggled_accessibility_data: ToggledAccessibilityData1 | None = Field(None, alias='toggledAccessibilityData')

class WebCommandMetadata33(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    url: str | None = None
    web_page_type: str | None = Field(None, alias='webPageType')
    root_ve: int | None = Field(None, alias='rootVe')

class CommandMetadata33(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    web_command_metadata: WebCommandMetadata33 | None = Field(None, alias='webCommandMetadata')

class LoggingContext7(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    vss_logging_context: VssLoggingContext | None = Field(None, alias='vssLoggingContext')

class Html5PlaybackOnesieConfig7(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    common_config: CommonConfig | None = Field(None, alias='commonConfig')

class WatchEndpointSupportedOnesieConfig7(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    html5_playback_onesie_config: Html5PlaybackOnesieConfig7 | None = Field(None, alias='html5PlaybackOnesieConfig')

class WatchEndpoint7(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    video_id: str | None = Field(None, alias='videoId')
    playlist_id: str | None = Field(None, alias='playlistId')
    params: str | None = None
    player_params: str | None = Field(None, alias='playerParams')
    logging_context: LoggingContext7 | None = Field(None, alias='loggingContext')
    watch_endpoint_supported_onesie_config: WatchEndpointSupportedOnesieConfig7 | None = Field(None, alias='watchEndpointSupportedOnesieConfig')

class NavigationEndpoint9(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    click_tracking_params: str | None = Field(None, alias='clickTrackingParams')
    command_metadata: CommandMetadata33 | None = Field(None, alias='commandMetadata')
    watch_endpoint: WatchEndpoint7 | None = Field(None, alias='watchEndpoint')

class Accessibility2(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    label: str | None = None

class WebCommandMetadata34(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    send_post: bool | None = Field(None, alias='sendPost')
    api_url: str | None = Field(None, alias='apiUrl')

class CommandMetadata34(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    web_command_metadata: WebCommandMetadata34 | None = Field(None, alias='webCommandMetadata')

class Popup4(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    unified_share_panel_renderer: UnifiedSharePanelRenderer | None = Field(None, alias='unifiedSharePanelRenderer')

class OpenPopupAction4(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    popup: Popup4 | None = None
    popup_type: str | None = Field(None, alias='popupType')
    be_reused: bool | None = Field(None, alias='beReused')

class Command5(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    click_tracking_params: str | None = Field(None, alias='clickTrackingParams')
    open_popup_action: OpenPopupAction4 | None = Field(None, alias='openPopupAction')

class ShareEntityServiceEndpoint2(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    serialized_share_entity: str | None = Field(None, alias='serializedShareEntity')
    commands: list[Command5] | None = None

class ServiceEndpoint2(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    click_tracking_params: str | None = Field(None, alias='clickTrackingParams')
    command_metadata: CommandMetadata34 | None = Field(None, alias='commandMetadata')
    share_entity_service_endpoint: ShareEntityServiceEndpoint2 | None = Field(None, alias='shareEntityServiceEndpoint')

class ButtonRenderer14(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    style: str | None = None
    size: str | None = None
    is_disabled: bool | None = Field(None, alias='isDisabled')
    icon: Icon1 | None = None
    navigation_endpoint: NavigationEndpoint9 | None = Field(None, alias='navigationEndpoint')
    accessibility: Accessibility2 | None = None
    tooltip: str | None = None
    tracking_params: str | None = Field(None, alias='trackingParams')
    service_endpoint: ServiceEndpoint2 | None = Field(None, alias='serviceEndpoint')

class TopLevelButton(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    toggle_button_renderer: ToggleButtonRenderer1 | None = Field(None, alias='toggleButtonRenderer')
    button_renderer: ButtonRenderer14 | None = Field(None, alias='buttonRenderer')

class Accessibility3(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    accessibility_data: AccessibilityData15 | None = Field(None, alias='accessibilityData')

class MenuRenderer(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    items: list[Item1] | None = None
    tracking_params: str | None = Field(None, alias='trackingParams')
    top_level_buttons: list[TopLevelButton] | None = Field(None, alias='topLevelButtons')
    accessibility: Accessibility3 | None = None

class Menu(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    menu_renderer: MenuRenderer | None = Field(None, alias='menuRenderer')

class ThumbnailOverlaySidePanelRenderer(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    text: Text12 | None = None
    icon: Icon1 | None = None

class ThumbnailOverlay(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    thumbnail_overlay_side_panel_renderer: ThumbnailOverlaySidePanelRenderer | None = Field(None, alias='thumbnailOverlaySidePanelRenderer')

class WebCommandMetadata35(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    url: str | None = None
    web_page_type: str | None = Field(None, alias='webPageType')
    root_ve: int | None = Field(None, alias='rootVe')

class CommandMetadata35(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    web_command_metadata: WebCommandMetadata35 | None = Field(None, alias='webCommandMetadata')

class LoggingContext8(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    vss_logging_context: VssLoggingContext | None = Field(None, alias='vssLoggingContext')

class Html5PlaybackOnesieConfig8(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    common_config: CommonConfig | None = Field(None, alias='commonConfig')

class WatchEndpointSupportedOnesieConfig8(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    html5_playback_onesie_config: Html5PlaybackOnesieConfig8 | None = Field(None, alias='html5PlaybackOnesieConfig')

class WatchEndpoint8(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    video_id: str | None = Field(None, alias='videoId')
    playlist_id: str | None = Field(None, alias='playlistId')
    player_params: str | None = Field(None, alias='playerParams')
    logging_context: LoggingContext8 | None = Field(None, alias='loggingContext')
    watch_endpoint_supported_onesie_config: WatchEndpointSupportedOnesieConfig8 | None = Field(None, alias='watchEndpointSupportedOnesieConfig')

class NavigationEndpoint10(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    click_tracking_params: str | None = Field(None, alias='clickTrackingParams')
    command_metadata: CommandMetadata35 | None = Field(None, alias='commandMetadata')
    watch_endpoint: WatchEndpoint8 | None = Field(None, alias='watchEndpoint')

class ShowMoreText(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    runs: list[Run27] | None = None

class PlaylistSidebarPrimaryInfoRenderer(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    thumbnail_renderer: ThumbnailRenderer | None = Field(None, alias='thumbnailRenderer')
    title: Title6 | None = None
    stats: list[Stat1] | None = None
    menu: Menu | None = None
    thumbnail_overlays: list[ThumbnailOverlay] | None = Field(None, alias='thumbnailOverlays')
    navigation_endpoint: NavigationEndpoint10 | None = Field(None, alias='navigationEndpoint')
    show_more_text: ShowMoreText | None = Field(None, alias='showMoreText')

class Item(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    playlist_sidebar_primary_info_renderer: PlaylistSidebarPrimaryInfoRenderer | None = Field(None, alias='playlistSidebarPrimaryInfoRenderer')

class PlaylistSidebarRenderer(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    items: list[Item] | None = None
    tracking_params: str | None = Field(None, alias='trackingParams')

class Sidebar(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    playlist_sidebar_renderer: PlaylistSidebarRenderer | None = Field(None, alias='playlistSidebarRenderer')

class MusicModel(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    response_context: ResponseContext | None = Field(None, alias='responseContext')
    contents: Contents | None = None
    header: Header | None = None
    metadata: Metadata2 | None = None
    tracking_params: str | None = Field(None, alias='trackingParams')
    topbar: Topbar | None = None
    microformat: Microformat | None = None
    sidebar: Sidebar | None = None
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
