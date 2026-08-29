from typing import Any, Self
from pydantic import ModelWrapValidatorHandler, PrivateAttr, model_validator
from pydantic import ConfigDict
from pydantic import BaseModel, Field

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
    main_app_web_response_context: MainAppWebResponseContext = Field(..., alias='mainAppWebResponseContext')
    response_id: str = Field(..., alias='responseId')
    web_response_context_extension_data: WebResponseContextExtensionData = Field(..., alias='webResponseContextExtensionData')

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

class Icon(BaseModel):
    model_config = ConfigDict(defer_build=True)
    sources: list[Source1]

class Settings(BaseModel):
    model_config = ConfigDict(defer_build=True)
    loop: bool
    autoplay: bool

class LottieData(BaseModel):
    model_config = ConfigDict(defer_build=True)
    url: str
    settings: Settings

class AccessibilityContext(BaseModel):
    model_config = ConfigDict(defer_build=True)
    label: str

class RendererContext(BaseModel):
    model_config = ConfigDict(defer_build=True)
    accessibility_context: AccessibilityContext = Field(..., alias='accessibilityContext')

class ThumbnailBadgeViewModel(BaseModel):
    model_config = ConfigDict(defer_build=True)
    icon: Icon
    text: str
    badge_style: str = Field(..., alias='badgeStyle')
    animation_activation_target_id: str = Field(..., alias='animationActivationTargetId')
    animation_activation_entity_key: str = Field(..., alias='animationActivationEntityKey')
    lottie_data: LottieData = Field(..., alias='lottieData')
    animated_text: str = Field(..., alias='animatedText')
    animation_activation_entity_selector_type: str = Field(..., alias='animationActivationEntitySelectorType')
    renderer_context: RendererContext = Field(..., alias='rendererContext')

class Badge(BaseModel):
    model_config = ConfigDict(defer_build=True)
    thumbnail_badge_view_model: ThumbnailBadgeViewModel = Field(..., alias='thumbnailBadgeViewModel')

class ThumbnailBottomOverlayViewModel(BaseModel):
    model_config = ConfigDict(defer_build=True)
    badges: list[Badge]

class WebCommandMetadata(BaseModel):
    model_config = ConfigDict(defer_build=True)
    send_post: bool = Field(..., alias='sendPost')
    api_url: str | None = Field(None, alias='apiUrl')

class CommandMetadata(BaseModel):
    model_config = ConfigDict(defer_build=True)
    web_command_metadata: WebCommandMetadata = Field(..., alias='webCommandMetadata')

class Action(BaseModel):
    model_config = ConfigDict(defer_build=True)
    added_video_id: str = Field(..., alias='addedVideoId')
    action: str

class PlaylistEditEndpoint(BaseModel):
    model_config = ConfigDict(defer_build=True)
    playlist_id: str = Field(..., alias='playlistId')
    actions: list[Action]

class WebCommandMetadata1(BaseModel):
    model_config = ConfigDict(defer_build=True)
    send_post: bool = Field(..., alias='sendPost')
    api_url: str = Field(..., alias='apiUrl')

class CommandMetadata1(BaseModel):
    model_config = ConfigDict(defer_build=True)
    web_command_metadata: WebCommandMetadata1 = Field(..., alias='webCommandMetadata')

class CreatePlaylistServiceEndpoint(BaseModel):
    model_config = ConfigDict(defer_build=True)
    video_ids: list[str] = Field(..., alias='videoIds')
    params: str

class OnCreateListCommand(BaseModel):
    model_config = ConfigDict(defer_build=True)
    click_tracking_params: str = Field(..., alias='clickTrackingParams')
    command_metadata: CommandMetadata1 = Field(..., alias='commandMetadata')
    create_playlist_service_endpoint: CreatePlaylistServiceEndpoint = Field(..., alias='createPlaylistServiceEndpoint')

class WebCommandMetadata2(BaseModel):
    model_config = ConfigDict(defer_build=True)
    url: str
    web_page_type: str = Field(..., alias='webPageType')
    root_ve: int = Field(..., alias='rootVe')

class CommandMetadata2(BaseModel):
    model_config = ConfigDict(defer_build=True)
    web_command_metadata: WebCommandMetadata2 = Field(..., alias='webCommandMetadata')

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
    watch_endpoint_supported_onesie_config: WatchEndpointSupportedOnesieConfig = Field(..., alias='watchEndpointSupportedOnesieConfig')
    player_params: str | None = Field(None, alias='playerParams')

class VideoCommand(BaseModel):
    model_config = ConfigDict(defer_build=True)
    click_tracking_params: str = Field(..., alias='clickTrackingParams')
    command_metadata: CommandMetadata2 = Field(..., alias='commandMetadata')
    watch_endpoint: WatchEndpoint = Field(..., alias='watchEndpoint')

class AddToPlaylistCommand(BaseModel):
    model_config = ConfigDict(defer_build=True)
    open_miniplayer: bool = Field(..., alias='openMiniplayer')
    video_id: str = Field(..., alias='videoId')
    list_type: str = Field(..., alias='listType')
    on_create_list_command: OnCreateListCommand = Field(..., alias='onCreateListCommand')
    video_ids: list[str] = Field(..., alias='videoIds')
    video_command: VideoCommand = Field(..., alias='videoCommand')

class Action1(BaseModel):
    model_config = ConfigDict(defer_build=True)
    click_tracking_params: str = Field(..., alias='clickTrackingParams')
    add_to_playlist_command: AddToPlaylistCommand = Field(..., alias='addToPlaylistCommand')

class SignalServiceEndpoint(BaseModel):
    model_config = ConfigDict(defer_build=True)
    signal: str
    actions: list[Action1]

class InnertubeCommand(BaseModel):
    model_config = ConfigDict(defer_build=True)
    click_tracking_params: str = Field(..., alias='clickTrackingParams')
    command_metadata: CommandMetadata = Field(..., alias='commandMetadata')
    playlist_edit_endpoint: PlaylistEditEndpoint | None = Field(None, alias='playlistEditEndpoint')
    signal_service_endpoint: SignalServiceEndpoint | None = Field(None, alias='signalServiceEndpoint')

class OnTap(BaseModel):
    model_config = ConfigDict(defer_build=True)
    innertube_command: InnertubeCommand = Field(..., alias='innertubeCommand')

class ButtonViewModel(BaseModel):
    model_config = ConfigDict(defer_build=True)
    icon_name: str = Field(..., alias='iconName')
    on_tap: OnTap = Field(..., alias='onTap')
    accessibility_text: str = Field(..., alias='accessibilityText')
    style: str
    tracking_params: str = Field(..., alias='trackingParams')
    type: str
    button_size: str = Field(..., alias='buttonSize')
    state: str

class DefaultButtonViewModel(BaseModel):
    model_config = ConfigDict(defer_build=True)
    button_view_model: ButtonViewModel = Field(..., alias='buttonViewModel')

class WebCommandMetadata3(BaseModel):
    model_config = ConfigDict(defer_build=True)
    send_post: bool = Field(..., alias='sendPost')
    api_url: str = Field(..., alias='apiUrl')

class CommandMetadata3(BaseModel):
    model_config = ConfigDict(defer_build=True)
    web_command_metadata: WebCommandMetadata3 = Field(..., alias='webCommandMetadata')

class Action2(BaseModel):
    model_config = ConfigDict(defer_build=True)
    action: str
    removed_video_id: str = Field(..., alias='removedVideoId')

class PlaylistEditEndpoint1(BaseModel):
    model_config = ConfigDict(defer_build=True)
    playlist_id: str = Field(..., alias='playlistId')
    actions: list[Action2]

class InnertubeCommand1(BaseModel):
    model_config = ConfigDict(defer_build=True)
    click_tracking_params: str = Field(..., alias='clickTrackingParams')
    command_metadata: CommandMetadata3 = Field(..., alias='commandMetadata')
    playlist_edit_endpoint: PlaylistEditEndpoint1 = Field(..., alias='playlistEditEndpoint')

class OnTap1(BaseModel):
    model_config = ConfigDict(defer_build=True)
    innertube_command: InnertubeCommand1 = Field(..., alias='innertubeCommand')

class ButtonViewModel1(BaseModel):
    model_config = ConfigDict(defer_build=True)
    icon_name: str = Field(..., alias='iconName')
    on_tap: OnTap1 | None = Field(None, alias='onTap')
    accessibility_text: str = Field(..., alias='accessibilityText')
    style: str
    tracking_params: str = Field(..., alias='trackingParams')
    type: str
    button_size: str = Field(..., alias='buttonSize')
    state: str

class ToggledButtonViewModel(BaseModel):
    model_config = ConfigDict(defer_build=True)
    button_view_model: ButtonViewModel1 = Field(..., alias='buttonViewModel')

class ToggleButtonViewModel(BaseModel):
    model_config = ConfigDict(defer_build=True)
    default_button_view_model: DefaultButtonViewModel = Field(..., alias='defaultButtonViewModel')
    toggled_button_view_model: ToggledButtonViewModel = Field(..., alias='toggledButtonViewModel')
    is_toggled: bool = Field(..., alias='isToggled')
    tracking_params: str = Field(..., alias='trackingParams')

class Button(BaseModel):
    model_config = ConfigDict(defer_build=True)
    toggle_button_view_model: ToggleButtonViewModel = Field(..., alias='toggleButtonViewModel')

class ThumbnailHoverOverlayToggleActionsViewModel(BaseModel):
    model_config = ConfigDict(defer_build=True)
    buttons: list[Button]

class Overlay(BaseModel):
    model_config = ConfigDict(defer_build=True)
    thumbnail_bottom_overlay_view_model: ThumbnailBottomOverlayViewModel | None = Field(None, alias='thumbnailBottomOverlayViewModel')
    thumbnail_hover_overlay_toggle_actions_view_model: ThumbnailHoverOverlayToggleActionsViewModel | None = Field(None, alias='thumbnailHoverOverlayToggleActionsViewModel')

class ThumbnailViewModel(BaseModel):
    model_config = ConfigDict(defer_build=True)
    image: Image
    overlays: list[Overlay]

class ContentImage(BaseModel):
    model_config = ConfigDict(defer_build=True)
    thumbnail_view_model: ThumbnailViewModel = Field(..., alias='thumbnailViewModel')

class Title(BaseModel):
    model_config = ConfigDict(defer_build=True)
    content: str

class Source2(BaseModel):
    model_config = ConfigDict(defer_build=True)
    url: str
    width: int
    height: int

class Image2(BaseModel):
    model_config = ConfigDict(defer_build=True)
    sources: list[Source2]

class AvatarViewModel(BaseModel):
    model_config = ConfigDict(defer_build=True)
    image: Image2
    avatar_image_size: str = Field(..., alias='avatarImageSize')

class Avatar(BaseModel):
    model_config = ConfigDict(defer_build=True)
    avatar_view_model: AvatarViewModel = Field(..., alias='avatarViewModel')

class WebCommandMetadata4(BaseModel):
    model_config = ConfigDict(defer_build=True)
    url: str
    web_page_type: str = Field(..., alias='webPageType')
    root_ve: int = Field(..., alias='rootVe')
    api_url: str = Field(..., alias='apiUrl')

class CommandMetadata4(BaseModel):
    model_config = ConfigDict(defer_build=True)
    web_command_metadata: WebCommandMetadata4 = Field(..., alias='webCommandMetadata')

class BrowseEndpoint(BaseModel):
    model_config = ConfigDict(defer_build=True)
    browse_id: str = Field(..., alias='browseId')
    canonical_base_url: str | None = Field(None, alias='canonicalBaseUrl')

class InnertubeCommand2(BaseModel):
    model_config = ConfigDict(defer_build=True)
    click_tracking_params: str = Field(..., alias='clickTrackingParams')
    command_metadata: CommandMetadata4 = Field(..., alias='commandMetadata')
    browse_endpoint: BrowseEndpoint = Field(..., alias='browseEndpoint')

class OnTap2(BaseModel):
    model_config = ConfigDict(defer_build=True)
    innertube_command: InnertubeCommand2 = Field(..., alias='innertubeCommand')

class CommandContext(BaseModel):
    model_config = ConfigDict(defer_build=True)
    on_tap: OnTap2 = Field(..., alias='onTap')

class RendererContext1(BaseModel):
    model_config = ConfigDict(defer_build=True)
    command_context: CommandContext = Field(..., alias='commandContext')

class DecoratedAvatarViewModel(BaseModel):
    model_config = ConfigDict(defer_build=True)
    avatar: Avatar
    a11y_label: str = Field(..., alias='a11yLabel')
    renderer_context: RendererContext1 = Field(..., alias='rendererContext')

class Image1(BaseModel):
    model_config = ConfigDict(defer_build=True)
    decorated_avatar_view_model: DecoratedAvatarViewModel = Field(..., alias='decoratedAvatarViewModel')

class CommandMetadata5(BaseModel):
    model_config = ConfigDict(defer_build=True)
    web_command_metadata: WebCommandMetadata4 = Field(..., alias='webCommandMetadata')

class BrowseEndpoint1(BaseModel):
    model_config = ConfigDict(defer_build=True)
    browse_id: str = Field(..., alias='browseId')
    canonical_base_url: str = Field(..., alias='canonicalBaseUrl')

class InnertubeCommand3(BaseModel):
    model_config = ConfigDict(defer_build=True)
    click_tracking_params: str = Field(..., alias='clickTrackingParams')
    command_metadata: CommandMetadata5 = Field(..., alias='commandMetadata')
    browse_endpoint: BrowseEndpoint1 = Field(..., alias='browseEndpoint')

class OnTap3(BaseModel):
    model_config = ConfigDict(defer_build=True)
    innertube_command: InnertubeCommand3 = Field(..., alias='innertubeCommand')

class CommandRun(BaseModel):
    model_config = ConfigDict(defer_build=True)
    start_index: int = Field(..., alias='startIndex')
    length: int
    on_tap: OnTap3 = Field(..., alias='onTap')

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

class StyleRun(BaseModel):
    model_config = ConfigDict(defer_build=True)
    start_index: int = Field(..., alias='startIndex')
    length: int | None = None
    weight_label: str | None = Field(None, alias='weightLabel')
    style_run_extensions: StyleRunExtensions | None = Field(None, alias='styleRunExtensions')

class Source3(BaseModel):
    model_config = ConfigDict(defer_build=True)
    client_resource: ClientResource = Field(..., alias='clientResource')
    width: int
    height: int

class Image3(BaseModel):
    model_config = ConfigDict(defer_build=True)
    sources: list[Source3]

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

class Left(BaseModel):
    model_config = ConfigDict(defer_build=True)
    value: int
    unit: str

class Margin(BaseModel):
    model_config = ConfigDict(defer_build=True)
    left: Left

class LayoutProperties(BaseModel):
    model_config = ConfigDict(defer_build=True)
    height: Height
    width: Width
    margin: Margin

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

class Text(BaseModel):
    model_config = ConfigDict(defer_build=True)
    content: str
    command_runs: list[CommandRun] | None = Field(None, alias='commandRuns')
    style_runs: list[StyleRun] | None = Field(None, alias='styleRuns')
    attachment_runs: list[AttachmentRun] | None = Field(None, alias='attachmentRuns')

class MetadataPart(BaseModel):
    model_config = ConfigDict(defer_build=True)
    text: Text
    accessibility_label: str | None = Field(None, alias='accessibilityLabel')

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

class Source4(BaseModel):
    model_config = ConfigDict(defer_build=True)
    client_resource: ClientResource = Field(..., alias='clientResource')

class LeadingImage(BaseModel):
    model_config = ConfigDict(defer_build=True)
    sources: list[Source4]

class Visibility(BaseModel):
    model_config = ConfigDict(defer_build=True)
    types: str

class LoggingDirectives(BaseModel):
    model_config = ConfigDict(defer_build=True)
    tracking_params: str = Field(..., alias='trackingParams')
    visibility: Visibility

class LoggingContext(BaseModel):
    model_config = ConfigDict(defer_build=True)
    logging_directives: LoggingDirectives = Field(..., alias='loggingDirectives')

class WebCommandMetadata6(BaseModel):
    model_config = ConfigDict(defer_build=True)
    send_post: bool = Field(..., alias='sendPost')
    api_url: str | None = Field(None, alias='apiUrl')

class CommandMetadata6(BaseModel):
    model_config = ConfigDict(defer_build=True)
    web_command_metadata: WebCommandMetadata6 = Field(..., alias='webCommandMetadata')

class WebCommandMetadata7(BaseModel):
    model_config = ConfigDict(defer_build=True)
    send_post: bool = Field(..., alias='sendPost')
    api_url: str = Field(..., alias='apiUrl')

class CommandMetadata7(BaseModel):
    model_config = ConfigDict(defer_build=True)
    web_command_metadata: WebCommandMetadata7 = Field(..., alias='webCommandMetadata')

class OnCreateListCommand1(BaseModel):
    model_config = ConfigDict(defer_build=True)
    click_tracking_params: str = Field(..., alias='clickTrackingParams')
    command_metadata: CommandMetadata7 = Field(..., alias='commandMetadata')
    create_playlist_service_endpoint: CreatePlaylistServiceEndpoint = Field(..., alias='createPlaylistServiceEndpoint')

class WebCommandMetadata8(BaseModel):
    model_config = ConfigDict(defer_build=True)
    url: str
    web_page_type: str = Field(..., alias='webPageType')
    root_ve: int = Field(..., alias='rootVe')

class CommandMetadata8(BaseModel):
    model_config = ConfigDict(defer_build=True)
    web_command_metadata: WebCommandMetadata8 = Field(..., alias='webCommandMetadata')

class Html5PlaybackOnesieConfig1(BaseModel):
    model_config = ConfigDict(defer_build=True)
    common_config: CommonConfig = Field(..., alias='commonConfig')

class WatchEndpointSupportedOnesieConfig1(BaseModel):
    model_config = ConfigDict(defer_build=True)
    html5_playback_onesie_config: Html5PlaybackOnesieConfig1 = Field(..., alias='html5PlaybackOnesieConfig')

class WatchEndpoint1(BaseModel):
    model_config = ConfigDict(defer_build=True)
    video_id: str = Field(..., alias='videoId')
    watch_endpoint_supported_onesie_config: WatchEndpointSupportedOnesieConfig1 = Field(..., alias='watchEndpointSupportedOnesieConfig')
    player_params: str | None = Field(None, alias='playerParams')

class VideoCommand1(BaseModel):
    model_config = ConfigDict(defer_build=True)
    click_tracking_params: str = Field(..., alias='clickTrackingParams')
    command_metadata: CommandMetadata8 = Field(..., alias='commandMetadata')
    watch_endpoint: WatchEndpoint1 = Field(..., alias='watchEndpoint')

class AddToPlaylistCommand1(BaseModel):
    model_config = ConfigDict(defer_build=True)
    open_miniplayer: bool = Field(..., alias='openMiniplayer')
    video_id: str = Field(..., alias='videoId')
    list_type: str = Field(..., alias='listType')
    on_create_list_command: OnCreateListCommand1 = Field(..., alias='onCreateListCommand')
    video_ids: list[str] = Field(..., alias='videoIds')
    video_command: VideoCommand1 = Field(..., alias='videoCommand')

class Action3(BaseModel):
    model_config = ConfigDict(defer_build=True)
    click_tracking_params: str = Field(..., alias='clickTrackingParams')
    add_to_playlist_command: AddToPlaylistCommand1 = Field(..., alias='addToPlaylistCommand')

class SignalServiceEndpoint1(BaseModel):
    model_config = ConfigDict(defer_build=True)
    signal: str
    actions: list[Action3]

class UnifiedSharePanelRenderer(BaseModel):
    model_config = ConfigDict(defer_build=True)
    tracking_params: str = Field(..., alias='trackingParams')
    show_loading_spinner: bool = Field(..., alias='showLoadingSpinner')

class Popup(BaseModel):
    model_config = ConfigDict(defer_build=True)
    unified_share_panel_renderer: UnifiedSharePanelRenderer = Field(..., alias='unifiedSharePanelRenderer')

class OpenPopupAction(BaseModel):
    model_config = ConfigDict(defer_build=True)
    popup: Popup
    popup_type: str = Field(..., alias='popupType')
    be_reused: bool = Field(..., alias='beReused')

class Command(BaseModel):
    model_config = ConfigDict(defer_build=True)
    click_tracking_params: str = Field(..., alias='clickTrackingParams')
    open_popup_action: OpenPopupAction = Field(..., alias='openPopupAction')

class ShareEntityServiceEndpoint(BaseModel):
    model_config = ConfigDict(defer_build=True)
    serialized_share_entity: str = Field(..., alias='serializedShareEntity')
    commands: list[Command]

class InnertubeCommand5(BaseModel):
    model_config = ConfigDict(defer_build=True)
    click_tracking_params: str = Field(..., alias='clickTrackingParams')
    command_metadata: CommandMetadata6 = Field(..., alias='commandMetadata')
    signal_service_endpoint: SignalServiceEndpoint1 | None = Field(None, alias='signalServiceEndpoint')
    share_entity_service_endpoint: ShareEntityServiceEndpoint | None = Field(None, alias='shareEntityServiceEndpoint')

class OnTap5(BaseModel):
    model_config = ConfigDict(defer_build=True)
    innertube_command: InnertubeCommand5 = Field(..., alias='innertubeCommand')

class CommandContext1(BaseModel):
    model_config = ConfigDict(defer_build=True)
    on_tap: OnTap5 = Field(..., alias='onTap')

class RendererContext2(BaseModel):
    model_config = ConfigDict(defer_build=True)
    logging_context: LoggingContext | None = Field(None, alias='loggingContext')
    command_context: CommandContext1 = Field(..., alias='commandContext')

class ListItemViewModel(BaseModel):
    model_config = ConfigDict(defer_build=True)
    title: Title
    leading_image: LeadingImage = Field(..., alias='leadingImage')
    renderer_context: RendererContext2 = Field(..., alias='rendererContext')

class ListItem(BaseModel):
    model_config = ConfigDict(defer_build=True)
    list_item_view_model: ListItemViewModel = Field(..., alias='listItemViewModel')

class ListViewModel(BaseModel):
    model_config = ConfigDict(defer_build=True)
    list_items: list[ListItem] = Field(..., alias='listItems')

class Content3(BaseModel):
    model_config = ConfigDict(defer_build=True)
    list_view_model: ListViewModel = Field(..., alias='listViewModel')

class SheetViewModel(BaseModel):
    model_config = ConfigDict(defer_build=True)
    content: Content3

class InlineContent(BaseModel):
    model_config = ConfigDict(defer_build=True)
    sheet_view_model: SheetViewModel = Field(..., alias='sheetViewModel')

class PanelLoadingStrategy(BaseModel):
    model_config = ConfigDict(defer_build=True)
    inline_content: InlineContent = Field(..., alias='inlineContent')

class ShowSheetCommand(BaseModel):
    model_config = ConfigDict(defer_build=True)
    panel_loading_strategy: PanelLoadingStrategy = Field(..., alias='panelLoadingStrategy')

class InnertubeCommand4(BaseModel):
    model_config = ConfigDict(defer_build=True)
    click_tracking_params: str = Field(..., alias='clickTrackingParams')
    show_sheet_command: ShowSheetCommand = Field(..., alias='showSheetCommand')

class OnTap4(BaseModel):
    model_config = ConfigDict(defer_build=True)
    innertube_command: InnertubeCommand4 = Field(..., alias='innertubeCommand')

class ButtonViewModel2(BaseModel):
    model_config = ConfigDict(defer_build=True)
    icon_name: str = Field(..., alias='iconName')
    on_tap: OnTap4 = Field(..., alias='onTap')
    accessibility_text: str = Field(..., alias='accessibilityText')
    style: str
    tracking_params: str = Field(..., alias='trackingParams')
    type: str
    button_size: str = Field(..., alias='buttonSize')
    state: str

class MenuButton(BaseModel):
    model_config = ConfigDict(defer_build=True)
    button_view_model: ButtonViewModel2 = Field(..., alias='buttonViewModel')

class LockupMetadataViewModel(BaseModel):
    model_config = ConfigDict(defer_build=True)
    title: Title
    image: Image1
    metadata: Metadata1
    menu_button: MenuButton = Field(..., alias='menuButton')

class Metadata(BaseModel):
    model_config = ConfigDict(defer_build=True)
    lockup_metadata_view_model: LockupMetadataViewModel = Field(..., alias='lockupMetadataViewModel')

class LoggingDirectives1(BaseModel):
    model_config = ConfigDict(defer_build=True)
    tracking_params: str = Field(..., alias='trackingParams')
    visibility: Visibility

class LoggingContext1(BaseModel):
    model_config = ConfigDict(defer_build=True)
    logging_directives: LoggingDirectives1 = Field(..., alias='loggingDirectives')

class CommandMetadata9(BaseModel):
    model_config = ConfigDict(defer_build=True)
    web_command_metadata: WebCommandMetadata8 = Field(..., alias='webCommandMetadata')

class VssLoggingContext(BaseModel):
    model_config = ConfigDict(defer_build=True)
    serialized_context_data: str = Field(..., alias='serializedContextData')

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
    index: int
    params: str
    player_params: str = Field(..., alias='playerParams')
    logging_context: LoggingContext2 = Field(..., alias='loggingContext')
    watch_endpoint_supported_onesie_config: WatchEndpointSupportedOnesieConfig2 = Field(..., alias='watchEndpointSupportedOnesieConfig')

class InnertubeCommand6(BaseModel):
    model_config = ConfigDict(defer_build=True)
    click_tracking_params: str = Field(..., alias='clickTrackingParams')
    command_metadata: CommandMetadata9 = Field(..., alias='commandMetadata')
    watch_endpoint: WatchEndpoint2 = Field(..., alias='watchEndpoint')

class OnTap6(BaseModel):
    model_config = ConfigDict(defer_build=True)
    innertube_command: InnertubeCommand6 = Field(..., alias='innertubeCommand')

class CommandContext2(BaseModel):
    model_config = ConfigDict(defer_build=True)
    on_tap: OnTap6 = Field(..., alias='onTap')

class RendererContext3(BaseModel):
    model_config = ConfigDict(defer_build=True)
    logging_context: LoggingContext1 = Field(..., alias='loggingContext')
    accessibility_context: AccessibilityContext = Field(..., alias='accessibilityContext')
    command_context: CommandContext2 = Field(..., alias='commandContext')

class LockupViewModel(BaseModel):
    model_config = ConfigDict(defer_build=True)
    content_image: ContentImage = Field(..., alias='contentImage')
    metadata: Metadata
    content_id: str = Field(..., alias='contentId')
    content_type: str = Field(..., alias='contentType')
    renderer_context: RendererContext3 = Field(..., alias='rendererContext')

class Content2(BaseModel):
    model_config = ConfigDict(defer_build=True)
    lockup_view_model: LockupViewModel = Field(..., alias='lockupViewModel')

class ItemSectionRenderer(BaseModel):
    model_config = ConfigDict(defer_build=True)
    contents: list[Content2]
    tracking_params: str = Field(..., alias='trackingParams')
    target_id: str = Field(..., alias='targetId')

class Content1(BaseModel):
    model_config = ConfigDict(defer_build=True)
    item_section_renderer: ItemSectionRenderer = Field(..., alias='itemSectionRenderer')

class SpacingConfiguration(BaseModel):
    model_config = ConfigDict(defer_build=True)
    column_gap: int = Field(..., alias='columnGap')
    row_gap: int = Field(..., alias='rowGap')

class ResponsiveMapItem(BaseModel):
    model_config = ConfigDict(defer_build=True)
    container_size: str = Field(..., alias='containerSize')
    container_type: str = Field(..., alias='containerType')
    max_width: int = Field(..., alias='maxWidth')
    min_column_size: int = Field(..., alias='minColumnSize')
    min_column_count: int = Field(..., alias='minColumnCount')
    max_column_count: int = Field(..., alias='maxColumnCount')
    spacing_configuration: SpacingConfiguration = Field(..., alias='spacingConfiguration')
    column_multiplier: int = Field(..., alias='columnMultiplier')
    column_adder: int = Field(..., alias='columnAdder')

class ResponsiveContainerConfiguration(BaseModel):
    model_config = ConfigDict(defer_build=True)
    responsive_size: str = Field(..., alias='responsiveSize')
    responsive_map: list[ResponsiveMapItem] = Field(..., alias='responsiveMap')

class LayoutConfiguration(BaseModel):
    model_config = ConfigDict(defer_build=True)
    responsive_container_configuration: ResponsiveContainerConfiguration = Field(..., alias='responsiveContainerConfiguration')

class SectionListLayoutConfiguration(BaseModel):
    model_config = ConfigDict(defer_build=True)
    layout_configuration: LayoutConfiguration = Field(..., alias='layoutConfiguration')

class SectionListRenderer(BaseModel):
    model_config = ConfigDict(defer_build=True)
    contents: list[Content1]
    tracking_params: str = Field(..., alias='trackingParams')
    section_list_layout_configuration: SectionListLayoutConfiguration = Field(..., alias='sectionListLayoutConfiguration')

class Content(BaseModel):
    model_config = ConfigDict(defer_build=True)
    section_list_renderer: SectionListRenderer = Field(..., alias='sectionListRenderer')

class TabRenderer(BaseModel):
    model_config = ConfigDict(defer_build=True)
    selected: bool
    content: Content
    tab_identifier: str = Field(..., alias='tabIdentifier')
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

class Title2(BaseModel):
    model_config = ConfigDict(defer_build=True)
    simple_text: str = Field(..., alias='simpleText')

class Run(BaseModel):
    model_config = ConfigDict(defer_build=True)
    text: str

class NumVideosText(BaseModel):
    model_config = ConfigDict(defer_build=True)
    runs: list[Run]

class ViewCountText(BaseModel):
    model_config = ConfigDict(defer_build=True)
    simple_text: str = Field(..., alias='simpleText')

class ShareData(BaseModel):
    model_config = ConfigDict(defer_build=True)
    can_share: bool = Field(..., alias='canShare')

class EditableDetails(BaseModel):
    model_config = ConfigDict(defer_build=True)
    can_delete: bool = Field(..., alias='canDelete')

class WebCommandMetadata10(BaseModel):
    model_config = ConfigDict(defer_build=True)
    send_post: bool = Field(..., alias='sendPost')
    api_url: str = Field(..., alias='apiUrl')

class CommandMetadata10(BaseModel):
    model_config = ConfigDict(defer_build=True)
    web_command_metadata: WebCommandMetadata10 = Field(..., alias='webCommandMetadata')

class Action4(BaseModel):
    model_config = ConfigDict(defer_build=True)
    action: str
    source_playlist_id: str = Field(..., alias='sourcePlaylistId')

class PlaylistEditEndpoint2(BaseModel):
    model_config = ConfigDict(defer_build=True)
    actions: list[Action4]

class ServiceEndpoint(BaseModel):
    model_config = ConfigDict(defer_build=True)
    click_tracking_params: str = Field(..., alias='clickTrackingParams')
    command_metadata: CommandMetadata10 = Field(..., alias='commandMetadata')
    playlist_edit_endpoint: PlaylistEditEndpoint2 = Field(..., alias='playlistEditEndpoint')

class Stat(BaseModel):
    model_config = ConfigDict(defer_build=True)
    runs: list[Run] | None = None
    simple_text: str | None = Field(None, alias='simpleText')

class BriefStat(BaseModel):
    model_config = ConfigDict(defer_build=True)
    runs: list[Run]

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

class WebCommandMetadata11(BaseModel):
    model_config = ConfigDict(defer_build=True)
    url: str
    web_page_type: str = Field(..., alias='webPageType')
    root_ve: int = Field(..., alias='rootVe')

class CommandMetadata11(BaseModel):
    model_config = ConfigDict(defer_build=True)
    web_command_metadata: WebCommandMetadata11 = Field(..., alias='webCommandMetadata')

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

class OnTap7(BaseModel):
    model_config = ConfigDict(defer_build=True)
    click_tracking_params: str = Field(..., alias='clickTrackingParams')
    command_metadata: CommandMetadata11 = Field(..., alias='commandMetadata')
    watch_endpoint: WatchEndpoint3 = Field(..., alias='watchEndpoint')

class Text1(BaseModel):
    model_config = ConfigDict(defer_build=True)
    simple_text: str = Field(..., alias='simpleText')

class Icon1(BaseModel):
    model_config = ConfigDict(defer_build=True)
    icon_type: str = Field(..., alias='iconType')

class ThumbnailOverlayHoverTextRenderer(BaseModel):
    model_config = ConfigDict(defer_build=True)
    text: Text1
    icon: Icon1

class ThumbnailOverlays(BaseModel):
    model_config = ConfigDict(defer_build=True)
    thumbnail_overlay_hover_text_renderer: ThumbnailOverlayHoverTextRenderer = Field(..., alias='thumbnailOverlayHoverTextRenderer')

class HeroPlaylistThumbnailRenderer(BaseModel):
    model_config = ConfigDict(defer_build=True)
    thumbnail: Thumbnail
    max_ratio: float = Field(..., alias='maxRatio')
    tracking_params: str = Field(..., alias='trackingParams')
    on_tap: OnTap7 = Field(..., alias='onTap')
    thumbnail_overlays: ThumbnailOverlays = Field(..., alias='thumbnailOverlays')

class PlaylistHeaderBanner(BaseModel):
    model_config = ConfigDict(defer_build=True)
    hero_playlist_thumbnail_renderer: HeroPlaylistThumbnailRenderer = Field(..., alias='heroPlaylistThumbnailRenderer')

class Style(BaseModel):
    model_config = ConfigDict(defer_build=True)
    style_type: str = Field(..., alias='styleType')

class Size(BaseModel):
    model_config = ConfigDict(defer_build=True)
    size_type: str = Field(..., alias='sizeType')

class DefaultIcon(BaseModel):
    model_config = ConfigDict(defer_build=True)
    icon_type: str = Field(..., alias='iconType')

class ToggledIcon(BaseModel):
    model_config = ConfigDict(defer_build=True)
    icon_type: str = Field(..., alias='iconType')

class ToggledStyle(BaseModel):
    model_config = ConfigDict(defer_build=True)
    style_type: str = Field(..., alias='styleType')

class WebCommandMetadata12(BaseModel):
    model_config = ConfigDict(defer_build=True)
    ignore_navigation: bool = Field(..., alias='ignoreNavigation')

class CommandMetadata12(BaseModel):
    model_config = ConfigDict(defer_build=True)
    web_command_metadata: WebCommandMetadata12 = Field(..., alias='webCommandMetadata')

class Content4(BaseModel):
    model_config = ConfigDict(defer_build=True)
    simple_text: str = Field(..., alias='simpleText')

class WebCommandMetadata13(BaseModel):
    model_config = ConfigDict(defer_build=True)
    url: str
    web_page_type: str = Field(..., alias='webPageType')
    root_ve: int = Field(..., alias='rootVe')

class CommandMetadata13(BaseModel):
    model_config = ConfigDict(defer_build=True)
    web_command_metadata: WebCommandMetadata13 = Field(..., alias='webCommandMetadata')

class WebCommandMetadata14(BaseModel):
    model_config = ConfigDict(defer_build=True)
    url: str
    web_page_type: str = Field(..., alias='webPageType')
    root_ve: int = Field(..., alias='rootVe')
    api_url: str = Field(..., alias='apiUrl')

class CommandMetadata14(BaseModel):
    model_config = ConfigDict(defer_build=True)
    web_command_metadata: WebCommandMetadata14 = Field(..., alias='webCommandMetadata')

class BrowseEndpoint2(BaseModel):
    model_config = ConfigDict(defer_build=True)
    browse_id: str = Field(..., alias='browseId')

class NextEndpoint(BaseModel):
    model_config = ConfigDict(defer_build=True)
    click_tracking_params: str = Field(..., alias='clickTrackingParams')
    command_metadata: CommandMetadata14 = Field(..., alias='commandMetadata')
    browse_endpoint: BrowseEndpoint2 = Field(..., alias='browseEndpoint')

class SignInEndpoint(BaseModel):
    model_config = ConfigDict(defer_build=True)
    next_endpoint: NextEndpoint = Field(..., alias='nextEndpoint')
    idam_tag: str = Field(..., alias='idamTag')

class NavigationEndpoint(BaseModel):
    model_config = ConfigDict(defer_build=True)
    click_tracking_params: str = Field(..., alias='clickTrackingParams')
    command_metadata: CommandMetadata13 = Field(..., alias='commandMetadata')
    sign_in_endpoint: SignInEndpoint = Field(..., alias='signInEndpoint')

class ButtonRenderer(BaseModel):
    model_config = ConfigDict(defer_build=True)
    style: str
    size: str
    is_disabled: bool = Field(..., alias='isDisabled')
    text: Text1
    navigation_endpoint: NavigationEndpoint = Field(..., alias='navigationEndpoint')
    tracking_params: str = Field(..., alias='trackingParams')

class Button1(BaseModel):
    model_config = ConfigDict(defer_build=True)
    button_renderer: ButtonRenderer = Field(..., alias='buttonRenderer')

class ModalWithTitleAndButtonRenderer(BaseModel):
    model_config = ConfigDict(defer_build=True)
    title: Title2
    content: Content4
    button: Button1

class Modal(BaseModel):
    model_config = ConfigDict(defer_build=True)
    modal_with_title_and_button_renderer: ModalWithTitleAndButtonRenderer = Field(..., alias='modalWithTitleAndButtonRenderer')

class ModalEndpoint(BaseModel):
    model_config = ConfigDict(defer_build=True)
    modal: Modal

class DefaultNavigationEndpoint(BaseModel):
    model_config = ConfigDict(defer_build=True)
    click_tracking_params: str = Field(..., alias='clickTrackingParams')
    command_metadata: CommandMetadata12 = Field(..., alias='commandMetadata')
    modal_endpoint: ModalEndpoint = Field(..., alias='modalEndpoint')

class AccessibilityData1(BaseModel):
    model_config = ConfigDict(defer_build=True)
    label: str

class AccessibilityData(BaseModel):
    model_config = ConfigDict(defer_build=True)
    accessibility_data: AccessibilityData1 = Field(..., alias='accessibilityData')

class AccessibilityData2(BaseModel):
    model_config = ConfigDict(defer_build=True)
    label: str

class ToggledAccessibilityData(BaseModel):
    model_config = ConfigDict(defer_build=True)
    accessibility_data: AccessibilityData2 = Field(..., alias='accessibilityData')

class ToggleButtonRenderer(BaseModel):
    model_config = ConfigDict(defer_build=True)
    style: Style
    size: Size
    is_toggled: bool = Field(..., alias='isToggled')
    is_disabled: bool = Field(..., alias='isDisabled')
    default_icon: DefaultIcon = Field(..., alias='defaultIcon')
    toggled_icon: ToggledIcon = Field(..., alias='toggledIcon')
    tracking_params: str = Field(..., alias='trackingParams')
    default_tooltip: str = Field(..., alias='defaultTooltip')
    toggled_tooltip: str = Field(..., alias='toggledTooltip')
    toggled_style: ToggledStyle = Field(..., alias='toggledStyle')
    default_navigation_endpoint: DefaultNavigationEndpoint = Field(..., alias='defaultNavigationEndpoint')
    accessibility_data: AccessibilityData = Field(..., alias='accessibilityData')
    toggled_accessibility_data: ToggledAccessibilityData = Field(..., alias='toggledAccessibilityData')

class SaveButton(BaseModel):
    model_config = ConfigDict(defer_build=True)
    toggle_button_renderer: ToggleButtonRenderer = Field(..., alias='toggleButtonRenderer')

class WebCommandMetadata15(BaseModel):
    model_config = ConfigDict(defer_build=True)
    send_post: bool = Field(..., alias='sendPost')
    api_url: str = Field(..., alias='apiUrl')

class CommandMetadata15(BaseModel):
    model_config = ConfigDict(defer_build=True)
    web_command_metadata: WebCommandMetadata15 = Field(..., alias='webCommandMetadata')

class Popup1(BaseModel):
    model_config = ConfigDict(defer_build=True)
    unified_share_panel_renderer: UnifiedSharePanelRenderer = Field(..., alias='unifiedSharePanelRenderer')

class OpenPopupAction1(BaseModel):
    model_config = ConfigDict(defer_build=True)
    popup: Popup1
    popup_type: str = Field(..., alias='popupType')
    be_reused: bool = Field(..., alias='beReused')

class Command1(BaseModel):
    model_config = ConfigDict(defer_build=True)
    click_tracking_params: str = Field(..., alias='clickTrackingParams')
    open_popup_action: OpenPopupAction1 = Field(..., alias='openPopupAction')

class ShareEntityServiceEndpoint1(BaseModel):
    model_config = ConfigDict(defer_build=True)
    serialized_share_entity: str = Field(..., alias='serializedShareEntity')
    commands: list[Command1]

class NavigationEndpoint1(BaseModel):
    model_config = ConfigDict(defer_build=True)
    click_tracking_params: str = Field(..., alias='clickTrackingParams')
    command_metadata: CommandMetadata15 = Field(..., alias='commandMetadata')
    share_entity_service_endpoint: ShareEntityServiceEndpoint1 = Field(..., alias='shareEntityServiceEndpoint')

class Accessibility(BaseModel):
    model_config = ConfigDict(defer_build=True)
    label: str

class AccessibilityData3(BaseModel):
    model_config = ConfigDict(defer_build=True)
    accessibility_data: AccessibilityData2 = Field(..., alias='accessibilityData')

class ButtonRenderer1(BaseModel):
    model_config = ConfigDict(defer_build=True)
    style: str
    size: str
    is_disabled: bool = Field(..., alias='isDisabled')
    icon: Icon1
    navigation_endpoint: NavigationEndpoint1 = Field(..., alias='navigationEndpoint')
    accessibility: Accessibility
    tooltip: str
    tracking_params: str = Field(..., alias='trackingParams')
    accessibility_data: AccessibilityData3 = Field(..., alias='accessibilityData')

class ShareButton(BaseModel):
    model_config = ConfigDict(defer_build=True)
    button_renderer: ButtonRenderer1 = Field(..., alias='buttonRenderer')

class Subtitle(BaseModel):
    model_config = ConfigDict(defer_build=True)
    simple_text: str = Field(..., alias='simpleText')

class WebCommandMetadata16(BaseModel):
    model_config = ConfigDict(defer_build=True)
    url: str
    web_page_type: str = Field(..., alias='webPageType')
    root_ve: int = Field(..., alias='rootVe')

class CommandMetadata16(BaseModel):
    model_config = ConfigDict(defer_build=True)
    web_command_metadata: WebCommandMetadata16 = Field(..., alias='webCommandMetadata')

class LoggingContext4(BaseModel):
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
    player_params: str = Field(..., alias='playerParams')
    logging_context: LoggingContext4 = Field(..., alias='loggingContext')
    watch_endpoint_supported_onesie_config: WatchEndpointSupportedOnesieConfig4 = Field(..., alias='watchEndpointSupportedOnesieConfig')

class NavigationEndpoint2(BaseModel):
    model_config = ConfigDict(defer_build=True)
    click_tracking_params: str = Field(..., alias='clickTrackingParams')
    command_metadata: CommandMetadata16 = Field(..., alias='commandMetadata')
    watch_endpoint: WatchEndpoint4 = Field(..., alias='watchEndpoint')

class ButtonRenderer2(BaseModel):
    model_config = ConfigDict(defer_build=True)
    style: str
    size: str
    is_disabled: bool = Field(..., alias='isDisabled')
    text: Text1
    icon: Icon1
    navigation_endpoint: NavigationEndpoint2 = Field(..., alias='navigationEndpoint')
    tracking_params: str = Field(..., alias='trackingParams')

class PlayButton(BaseModel):
    model_config = ConfigDict(defer_build=True)
    button_renderer: ButtonRenderer2 = Field(..., alias='buttonRenderer')

class CommandMetadata17(BaseModel):
    model_config = ConfigDict(defer_build=True)
    web_command_metadata: WebCommandMetadata16 = Field(..., alias='webCommandMetadata')

class LoggingContext5(BaseModel):
    model_config = ConfigDict(defer_build=True)
    vss_logging_context: VssLoggingContext = Field(..., alias='vssLoggingContext')

class Html5PlaybackOnesieConfig5(BaseModel):
    model_config = ConfigDict(defer_build=True)
    common_config: CommonConfig = Field(..., alias='commonConfig')

class WatchEndpointSupportedOnesieConfig5(BaseModel):
    model_config = ConfigDict(defer_build=True)
    html5_playback_onesie_config: Html5PlaybackOnesieConfig5 = Field(..., alias='html5PlaybackOnesieConfig')

class WatchEndpoint5(BaseModel):
    model_config = ConfigDict(defer_build=True)
    video_id: str = Field(..., alias='videoId')
    playlist_id: str = Field(..., alias='playlistId')
    params: str
    player_params: str = Field(..., alias='playerParams')
    logging_context: LoggingContext5 = Field(..., alias='loggingContext')
    watch_endpoint_supported_onesie_config: WatchEndpointSupportedOnesieConfig5 = Field(..., alias='watchEndpointSupportedOnesieConfig')

class NavigationEndpoint3(BaseModel):
    model_config = ConfigDict(defer_build=True)
    click_tracking_params: str = Field(..., alias='clickTrackingParams')
    command_metadata: CommandMetadata17 = Field(..., alias='commandMetadata')
    watch_endpoint: WatchEndpoint5 = Field(..., alias='watchEndpoint')

class ButtonRenderer3(BaseModel):
    model_config = ConfigDict(defer_build=True)
    style: str
    size: str
    is_disabled: bool = Field(..., alias='isDisabled')
    text: Text1
    icon: Icon1
    navigation_endpoint: NavigationEndpoint3 = Field(..., alias='navigationEndpoint')
    tracking_params: str = Field(..., alias='trackingParams')

class ShufflePlayButton(BaseModel):
    model_config = ConfigDict(defer_build=True)
    button_renderer: ButtonRenderer3 = Field(..., alias='buttonRenderer')

class Thumbnail3(BaseModel):
    model_config = ConfigDict(defer_build=True)
    url: str
    width: int
    height: int

class Thumbnail2(BaseModel):
    model_config = ConfigDict(defer_build=True)
    thumbnails: list[Thumbnail3]

class BackgroundImageConfig(BaseModel):
    model_config = ConfigDict(defer_build=True)
    thumbnail: Thumbnail2

class GradientColorConfigItem(BaseModel):
    model_config = ConfigDict(defer_build=True)
    light_theme_color: int = Field(..., alias='lightThemeColor')
    dark_theme_color: int = Field(..., alias='darkThemeColor')
    start_location: int | float = Field(..., alias='startLocation')

class Config(BaseModel):
    model_config = ConfigDict(defer_build=True)
    light_theme_background_color: int = Field(..., alias='lightThemeBackgroundColor')
    dark_theme_background_color: int = Field(..., alias='darkThemeBackgroundColor')
    color_source_size_multiplier: int = Field(..., alias='colorSourceSizeMultiplier')
    apply_client_image_blur: bool = Field(..., alias='applyClientImageBlur')

class CinematicContainerRenderer(BaseModel):
    model_config = ConfigDict(defer_build=True)
    background_image_config: BackgroundImageConfig = Field(..., alias='backgroundImageConfig')
    gradient_color_config: list[GradientColorConfigItem] = Field(..., alias='gradientColorConfig')
    config: Config

class CinematicContainer(BaseModel):
    model_config = ConfigDict(defer_build=True)
    cinematic_container_renderer: CinematicContainerRenderer = Field(..., alias='cinematicContainerRenderer')

class Text5(BaseModel):
    model_config = ConfigDict(defer_build=True)
    runs: list[Run] | None = None
    simple_text: str | None = Field(None, alias='simpleText')

class PlaylistBylineRenderer(BaseModel):
    model_config = ConfigDict(defer_build=True)
    text: Text5

class BylineItem(BaseModel):
    model_config = ConfigDict(defer_build=True)
    playlist_byline_renderer: PlaylistBylineRenderer = Field(..., alias='playlistBylineRenderer')

class PlaylistHeaderRenderer(BaseModel):
    model_config = ConfigDict(defer_build=True)
    playlist_id: str = Field(..., alias='playlistId')
    title: Title2
    num_videos_text: NumVideosText = Field(..., alias='numVideosText')
    view_count_text: ViewCountText = Field(..., alias='viewCountText')
    share_data: ShareData = Field(..., alias='shareData')
    is_editable: bool = Field(..., alias='isEditable')
    editable_details: EditableDetails = Field(..., alias='editableDetails')
    tracking_params: str = Field(..., alias='trackingParams')
    service_endpoints: list[ServiceEndpoint] = Field(..., alias='serviceEndpoints')
    stats: list[Stat]
    brief_stats: list[BriefStat] = Field(..., alias='briefStats')
    playlist_header_banner: PlaylistHeaderBanner = Field(..., alias='playlistHeaderBanner')
    save_button: SaveButton = Field(..., alias='saveButton')
    share_button: ShareButton = Field(..., alias='shareButton')
    subtitle: Subtitle
    play_button: PlayButton = Field(..., alias='playButton')
    shuffle_play_button: ShufflePlayButton = Field(..., alias='shufflePlayButton')
    cinematic_container: CinematicContainer = Field(..., alias='cinematicContainer')
    byline: list[BylineItem]

class Header(BaseModel):
    model_config = ConfigDict(defer_build=True)
    playlist_header_renderer: PlaylistHeaderRenderer = Field(..., alias='playlistHeaderRenderer')

class PlaylistMetadataRenderer(BaseModel):
    model_config = ConfigDict(defer_build=True)
    title: str
    play_url: str = Field(..., alias='playUrl')
    android_play_url: str = Field(..., alias='androidPlayUrl')
    album_name: str = Field(..., alias='albumName')
    android_appindexing_link: str = Field(..., alias='androidAppindexingLink')
    ios_appindexing_link: str = Field(..., alias='iosAppindexingLink')

class Metadata2(BaseModel):
    model_config = ConfigDict(defer_build=True)
    playlist_metadata_renderer: PlaylistMetadataRenderer = Field(..., alias='playlistMetadataRenderer')

class IconImage(BaseModel):
    model_config = ConfigDict(defer_build=True)
    icon_type: str = Field(..., alias='iconType')

class TooltipText(BaseModel):
    model_config = ConfigDict(defer_build=True)
    runs: list[Run]

class WebCommandMetadata18(BaseModel):
    model_config = ConfigDict(defer_build=True)
    url: str
    web_page_type: str = Field(..., alias='webPageType')
    root_ve: int = Field(..., alias='rootVe')
    api_url: str = Field(..., alias='apiUrl')

class CommandMetadata18(BaseModel):
    model_config = ConfigDict(defer_build=True)
    web_command_metadata: WebCommandMetadata18 = Field(..., alias='webCommandMetadata')

class Endpoint(BaseModel):
    model_config = ConfigDict(defer_build=True)
    click_tracking_params: str = Field(..., alias='clickTrackingParams')
    command_metadata: CommandMetadata18 = Field(..., alias='commandMetadata')
    browse_endpoint: BrowseEndpoint2 = Field(..., alias='browseEndpoint')

class TopbarLogoRenderer(BaseModel):
    model_config = ConfigDict(defer_build=True)
    icon_image: IconImage = Field(..., alias='iconImage')
    tooltip_text: TooltipText = Field(..., alias='tooltipText')
    endpoint: Endpoint
    tracking_params: str = Field(..., alias='trackingParams')
    override_entity_key: str = Field(..., alias='overrideEntityKey')

class Logo(BaseModel):
    model_config = ConfigDict(defer_build=True)
    topbar_logo_renderer: TopbarLogoRenderer = Field(..., alias='topbarLogoRenderer')

class PlaceholderText(BaseModel):
    model_config = ConfigDict(defer_build=True)
    runs: list[Run]

class WebSearchboxConfig(BaseModel):
    model_config = ConfigDict(defer_build=True)
    request_language: str = Field(..., alias='requestLanguage')
    request_domain: str = Field(..., alias='requestDomain')
    has_onscreen_keyboard: bool = Field(..., alias='hasOnscreenKeyboard')
    focus_searchbox: bool = Field(..., alias='focusSearchbox')

class Config1(BaseModel):
    model_config = ConfigDict(defer_build=True)
    web_searchbox_config: WebSearchboxConfig = Field(..., alias='webSearchboxConfig')

class WebCommandMetadata19(BaseModel):
    model_config = ConfigDict(defer_build=True)
    url: str
    web_page_type: str = Field(..., alias='webPageType')
    root_ve: int = Field(..., alias='rootVe')

class CommandMetadata19(BaseModel):
    model_config = ConfigDict(defer_build=True)
    web_command_metadata: WebCommandMetadata19 = Field(..., alias='webCommandMetadata')

class SearchEndpoint1(BaseModel):
    model_config = ConfigDict(defer_build=True)
    query: str

class SearchEndpoint(BaseModel):
    model_config = ConfigDict(defer_build=True)
    click_tracking_params: str = Field(..., alias='clickTrackingParams')
    command_metadata: CommandMetadata19 = Field(..., alias='commandMetadata')
    search_endpoint: SearchEndpoint1 = Field(..., alias='searchEndpoint')

class AccessibilityData6(BaseModel):
    model_config = ConfigDict(defer_build=True)
    label: str

class AccessibilityData5(BaseModel):
    model_config = ConfigDict(defer_build=True)
    accessibility_data: AccessibilityData6 = Field(..., alias='accessibilityData')

class ButtonRenderer4(BaseModel):
    model_config = ConfigDict(defer_build=True)
    style: str
    size: str
    is_disabled: bool = Field(..., alias='isDisabled')
    icon: Icon1
    tracking_params: str = Field(..., alias='trackingParams')
    accessibility_data: AccessibilityData5 = Field(..., alias='accessibilityData')

class ClearButton(BaseModel):
    model_config = ConfigDict(defer_build=True)
    button_renderer: ButtonRenderer4 = Field(..., alias='buttonRenderer')

class Headline(BaseModel):
    model_config = ConfigDict(defer_build=True)
    content: str

class DialogHeaderViewModel(BaseModel):
    model_config = ConfigDict(defer_build=True)
    headline: Headline

class Header1(BaseModel):
    model_config = ConfigDict(defer_build=True)
    dialog_header_view_model: DialogHeaderViewModel = Field(..., alias='dialogHeaderViewModel')

class ButtonViewModel3(BaseModel):
    model_config = ConfigDict(defer_build=True)
    title: str
    style: str
    tracking_params: str = Field(..., alias='trackingParams')
    is_full_width: bool = Field(..., alias='isFullWidth')
    type: str

class PrimaryButton(BaseModel):
    model_config = ConfigDict(defer_build=True)
    button_view_model: ButtonViewModel3 = Field(..., alias='buttonViewModel')

class SecondaryButton(BaseModel):
    model_config = ConfigDict(defer_build=True)
    button_view_model: ButtonViewModel3 = Field(..., alias='buttonViewModel')

class PanelFooterViewModel(BaseModel):
    model_config = ConfigDict(defer_build=True)
    primary_button: PrimaryButton = Field(..., alias='primaryButton')
    secondary_button: SecondaryButton = Field(..., alias='secondaryButton')
    should_hide_divider: bool = Field(..., alias='shouldHideDivider')

class Footer(BaseModel):
    model_config = ConfigDict(defer_build=True)
    panel_footer_view_model: PanelFooterViewModel = Field(..., alias='panelFooterViewModel')

class Text6(BaseModel):
    model_config = ConfigDict(defer_build=True)
    content: str

class Paragraph(BaseModel):
    model_config = ConfigDict(defer_build=True)
    text: Text6

class BasicContentViewModel(BaseModel):
    model_config = ConfigDict(defer_build=True)
    paragraphs: list[Paragraph]

class Content5(BaseModel):
    model_config = ConfigDict(defer_build=True)
    basic_content_view_model: BasicContentViewModel = Field(..., alias='basicContentViewModel')

class DialogViewModel(BaseModel):
    model_config = ConfigDict(defer_build=True)
    header: Header1
    footer: Footer
    content: Content5

class InlineContent1(BaseModel):
    model_config = ConfigDict(defer_build=True)
    dialog_view_model: DialogViewModel = Field(..., alias='dialogViewModel')

class PanelLoadingStrategy1(BaseModel):
    model_config = ConfigDict(defer_build=True)
    inline_content: InlineContent1 = Field(..., alias='inlineContent')

class ShowDialogCommand(BaseModel):
    model_config = ConfigDict(defer_build=True)
    panel_loading_strategy: PanelLoadingStrategy1 = Field(..., alias='panelLoadingStrategy')

class ShowImageSourceDialog(BaseModel):
    model_config = ConfigDict(defer_build=True)
    click_tracking_params: str = Field(..., alias='clickTrackingParams')
    show_dialog_command: ShowDialogCommand = Field(..., alias='showDialogCommand')

class FusionSearchboxRenderer(BaseModel):
    model_config = ConfigDict(defer_build=True)
    icon: Icon1
    placeholder_text: PlaceholderText = Field(..., alias='placeholderText')
    config: Config1
    tracking_params: str = Field(..., alias='trackingParams')
    search_endpoint: SearchEndpoint = Field(..., alias='searchEndpoint')
    clear_button: ClearButton = Field(..., alias='clearButton')
    show_image_source_dialog: ShowImageSourceDialog = Field(..., alias='showImageSourceDialog')
    disable_ai_appearance: bool = Field(..., alias='disableAiAppearance')

class Searchbox(BaseModel):
    model_config = ConfigDict(defer_build=True)
    fusion_searchbox_renderer: FusionSearchboxRenderer = Field(..., alias='fusionSearchboxRenderer')

class WebCommandMetadata20(BaseModel):
    model_config = ConfigDict(defer_build=True)
    send_post: bool = Field(..., alias='sendPost')
    api_url: str = Field(..., alias='apiUrl')

class CommandMetadata20(BaseModel):
    model_config = ConfigDict(defer_build=True)
    web_command_metadata: WebCommandMetadata20 = Field(..., alias='webCommandMetadata')

class MultiPageMenuRenderer(BaseModel):
    model_config = ConfigDict(defer_build=True)
    tracking_params: str = Field(..., alias='trackingParams')
    style: str
    show_loading_spinner: bool = Field(..., alias='showLoadingSpinner')

class Popup2(BaseModel):
    model_config = ConfigDict(defer_build=True)
    multi_page_menu_renderer: MultiPageMenuRenderer = Field(..., alias='multiPageMenuRenderer')

class OpenPopupAction2(BaseModel):
    model_config = ConfigDict(defer_build=True)
    popup: Popup2
    popup_type: str = Field(..., alias='popupType')
    be_reused: bool = Field(..., alias='beReused')

class Action5(BaseModel):
    model_config = ConfigDict(defer_build=True)
    click_tracking_params: str = Field(..., alias='clickTrackingParams')
    open_popup_action: OpenPopupAction2 = Field(..., alias='openPopupAction')

class SignalServiceEndpoint2(BaseModel):
    model_config = ConfigDict(defer_build=True)
    signal: str
    actions: list[Action5]

class MenuRequest(BaseModel):
    model_config = ConfigDict(defer_build=True)
    click_tracking_params: str = Field(..., alias='clickTrackingParams')
    command_metadata: CommandMetadata20 = Field(..., alias='commandMetadata')
    signal_service_endpoint: SignalServiceEndpoint2 = Field(..., alias='signalServiceEndpoint')

class AccessibilityData7(BaseModel):
    model_config = ConfigDict(defer_build=True)
    label: str

class Accessibility1(BaseModel):
    model_config = ConfigDict(defer_build=True)
    accessibility_data: AccessibilityData7 = Field(..., alias='accessibilityData')

class TopbarMenuButtonRenderer(BaseModel):
    model_config = ConfigDict(defer_build=True)
    icon: Icon1
    menu_request: MenuRequest = Field(..., alias='menuRequest')
    tracking_params: str = Field(..., alias='trackingParams')
    accessibility: Accessibility1
    tooltip: str
    style: str

class Text7(BaseModel):
    model_config = ConfigDict(defer_build=True)
    runs: list[Run]

class WebCommandMetadata21(BaseModel):
    model_config = ConfigDict(defer_build=True)
    url: str
    web_page_type: str = Field(..., alias='webPageType')
    root_ve: int = Field(..., alias='rootVe')

class CommandMetadata21(BaseModel):
    model_config = ConfigDict(defer_build=True)
    web_command_metadata: WebCommandMetadata21 = Field(..., alias='webCommandMetadata')

class SignInEndpoint1(BaseModel):
    model_config = ConfigDict(defer_build=True)
    idam_tag: str = Field(..., alias='idamTag')

class NavigationEndpoint4(BaseModel):
    model_config = ConfigDict(defer_build=True)
    click_tracking_params: str = Field(..., alias='clickTrackingParams')
    command_metadata: CommandMetadata21 = Field(..., alias='commandMetadata')
    sign_in_endpoint: SignInEndpoint1 = Field(..., alias='signInEndpoint')

class ButtonRenderer5(BaseModel):
    model_config = ConfigDict(defer_build=True)
    style: str
    size: str
    text: Text7
    icon: Icon1
    navigation_endpoint: NavigationEndpoint4 = Field(..., alias='navigationEndpoint')
    tracking_params: str = Field(..., alias='trackingParams')
    target_id: str = Field(..., alias='targetId')

class TopbarButton(BaseModel):
    model_config = ConfigDict(defer_build=True)
    topbar_menu_button_renderer: TopbarMenuButtonRenderer | None = Field(None, alias='topbarMenuButtonRenderer')
    button_renderer: ButtonRenderer5 | None = Field(None, alias='buttonRenderer')

class Title4(BaseModel):
    model_config = ConfigDict(defer_build=True)
    runs: list[Run]

class Title5(BaseModel):
    model_config = ConfigDict(defer_build=True)
    runs: list[Run]

class Label(BaseModel):
    model_config = ConfigDict(defer_build=True)
    runs: list[Run]

class HotkeyAccessibilityLabel(BaseModel):
    model_config = ConfigDict(defer_build=True)
    accessibility_data: AccessibilityData7 = Field(..., alias='accessibilityData')

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
    title: Title5
    options: list[Option]

class Section(BaseModel):
    model_config = ConfigDict(defer_build=True)
    hotkey_dialog_section_renderer: HotkeyDialogSectionRenderer = Field(..., alias='hotkeyDialogSectionRenderer')

class Text8(BaseModel):
    model_config = ConfigDict(defer_build=True)
    runs: list[Run]

class ButtonRenderer6(BaseModel):
    model_config = ConfigDict(defer_build=True)
    style: str
    size: str
    is_disabled: bool = Field(..., alias='isDisabled')
    text: Text8
    tracking_params: str = Field(..., alias='trackingParams')

class DismissButton(BaseModel):
    model_config = ConfigDict(defer_build=True)
    button_renderer: ButtonRenderer6 = Field(..., alias='buttonRenderer')

class HotkeyDialogRenderer(BaseModel):
    model_config = ConfigDict(defer_build=True)
    title: Title4
    sections: list[Section]
    dismiss_button: DismissButton = Field(..., alias='dismissButton')
    tracking_params: str = Field(..., alias='trackingParams')

class HotkeyDialog(BaseModel):
    model_config = ConfigDict(defer_build=True)
    hotkey_dialog_renderer: HotkeyDialogRenderer = Field(..., alias='hotkeyDialogRenderer')

class WebCommandMetadata22(BaseModel):
    model_config = ConfigDict(defer_build=True)
    send_post: bool = Field(..., alias='sendPost')

class CommandMetadata22(BaseModel):
    model_config = ConfigDict(defer_build=True)
    web_command_metadata: WebCommandMetadata22 = Field(..., alias='webCommandMetadata')

class SignalAction(BaseModel):
    model_config = ConfigDict(defer_build=True)
    signal: str

class Action6(BaseModel):
    model_config = ConfigDict(defer_build=True)
    click_tracking_params: str = Field(..., alias='clickTrackingParams')
    signal_action: SignalAction = Field(..., alias='signalAction')

class SignalServiceEndpoint3(BaseModel):
    model_config = ConfigDict(defer_build=True)
    signal: str
    actions: list[Action6]

class Command2(BaseModel):
    model_config = ConfigDict(defer_build=True)
    click_tracking_params: str = Field(..., alias='clickTrackingParams')
    command_metadata: CommandMetadata22 = Field(..., alias='commandMetadata')
    signal_service_endpoint: SignalServiceEndpoint3 = Field(..., alias='signalServiceEndpoint')

class ButtonRenderer7(BaseModel):
    model_config = ConfigDict(defer_build=True)
    tracking_params: str = Field(..., alias='trackingParams')
    command: Command2

class BackButton(BaseModel):
    model_config = ConfigDict(defer_build=True)
    button_renderer: ButtonRenderer7 = Field(..., alias='buttonRenderer')

class CommandMetadata23(BaseModel):
    model_config = ConfigDict(defer_build=True)
    web_command_metadata: WebCommandMetadata22 = Field(..., alias='webCommandMetadata')

class Action7(BaseModel):
    model_config = ConfigDict(defer_build=True)
    click_tracking_params: str = Field(..., alias='clickTrackingParams')
    signal_action: SignalAction = Field(..., alias='signalAction')

class SignalServiceEndpoint4(BaseModel):
    model_config = ConfigDict(defer_build=True)
    signal: str
    actions: list[Action7]

class Command3(BaseModel):
    model_config = ConfigDict(defer_build=True)
    click_tracking_params: str = Field(..., alias='clickTrackingParams')
    command_metadata: CommandMetadata23 = Field(..., alias='commandMetadata')
    signal_service_endpoint: SignalServiceEndpoint4 = Field(..., alias='signalServiceEndpoint')

class ButtonRenderer8(BaseModel):
    model_config = ConfigDict(defer_build=True)
    tracking_params: str = Field(..., alias='trackingParams')
    command: Command3

class ForwardButton(BaseModel):
    model_config = ConfigDict(defer_build=True)
    button_renderer: ButtonRenderer8 = Field(..., alias='buttonRenderer')

class Text9(BaseModel):
    model_config = ConfigDict(defer_build=True)
    runs: list[Run]

class CommandMetadata24(BaseModel):
    model_config = ConfigDict(defer_build=True)
    web_command_metadata: WebCommandMetadata22 = Field(..., alias='webCommandMetadata')

class Action8(BaseModel):
    model_config = ConfigDict(defer_build=True)
    click_tracking_params: str = Field(..., alias='clickTrackingParams')
    signal_action: SignalAction = Field(..., alias='signalAction')

class SignalServiceEndpoint5(BaseModel):
    model_config = ConfigDict(defer_build=True)
    signal: str
    actions: list[Action8]

class Command4(BaseModel):
    model_config = ConfigDict(defer_build=True)
    click_tracking_params: str = Field(..., alias='clickTrackingParams')
    command_metadata: CommandMetadata24 = Field(..., alias='commandMetadata')
    signal_service_endpoint: SignalServiceEndpoint5 = Field(..., alias='signalServiceEndpoint')

class ButtonRenderer9(BaseModel):
    model_config = ConfigDict(defer_build=True)
    style: str
    size: str
    is_disabled: bool = Field(..., alias='isDisabled')
    text: Text9
    tracking_params: str = Field(..., alias='trackingParams')
    command: Command4

class A11ySkipNavigationButton(BaseModel):
    model_config = ConfigDict(defer_build=True)
    button_renderer: ButtonRenderer9 = Field(..., alias='buttonRenderer')

class CommandMetadata25(BaseModel):
    model_config = ConfigDict(defer_build=True)
    web_command_metadata: WebCommandMetadata22 = Field(..., alias='webCommandMetadata')

class PlaceholderHeader(BaseModel):
    model_config = ConfigDict(defer_build=True)
    runs: list[Run]

class PromptHeader(BaseModel):
    model_config = ConfigDict(defer_build=True)
    runs: list[Run]

class ExampleQuery1(BaseModel):
    model_config = ConfigDict(defer_build=True)
    runs: list[Run]

class ExampleQuery2(BaseModel):
    model_config = ConfigDict(defer_build=True)
    runs: list[Run]

class PromptMicrophoneLabel(BaseModel):
    model_config = ConfigDict(defer_build=True)
    runs: list[Run]

class LoadingHeader(BaseModel):
    model_config = ConfigDict(defer_build=True)
    runs: list[Run]

class ConnectionErrorHeader(BaseModel):
    model_config = ConfigDict(defer_build=True)
    runs: list[Run]

class ConnectionErrorMicrophoneLabel(BaseModel):
    model_config = ConfigDict(defer_build=True)
    runs: list[Run]

class PermissionsHeader(BaseModel):
    model_config = ConfigDict(defer_build=True)
    runs: list[Run]

class PermissionsSubtext(BaseModel):
    model_config = ConfigDict(defer_build=True)
    runs: list[Run]

class DisabledHeader(BaseModel):
    model_config = ConfigDict(defer_build=True)
    runs: list[Run]

class DisabledSubtext(BaseModel):
    model_config = ConfigDict(defer_build=True)
    runs: list[Run]

class MicrophoneButtonAriaLabel(BaseModel):
    model_config = ConfigDict(defer_build=True)
    runs: list[Run]

class AccessibilityData9(BaseModel):
    model_config = ConfigDict(defer_build=True)
    accessibility_data: AccessibilityData7 = Field(..., alias='accessibilityData')

class ButtonRenderer11(BaseModel):
    model_config = ConfigDict(defer_build=True)
    style: str
    size: str
    is_disabled: bool = Field(..., alias='isDisabled')
    icon: Icon1
    tracking_params: str = Field(..., alias='trackingParams')
    accessibility_data: AccessibilityData9 = Field(..., alias='accessibilityData')

class ExitButton(BaseModel):
    model_config = ConfigDict(defer_build=True)
    button_renderer: ButtonRenderer11 = Field(..., alias='buttonRenderer')

class MicrophoneOffPromptHeader(BaseModel):
    model_config = ConfigDict(defer_build=True)
    runs: list[Run]

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

class Popup3(BaseModel):
    model_config = ConfigDict(defer_build=True)
    voice_search_dialog_renderer: VoiceSearchDialogRenderer = Field(..., alias='voiceSearchDialogRenderer')

class OpenPopupAction3(BaseModel):
    model_config = ConfigDict(defer_build=True)
    popup: Popup3
    popup_type: str = Field(..., alias='popupType')

class Action9(BaseModel):
    model_config = ConfigDict(defer_build=True)
    click_tracking_params: str = Field(..., alias='clickTrackingParams')
    open_popup_action: OpenPopupAction3 = Field(..., alias='openPopupAction')

class SignalServiceEndpoint6(BaseModel):
    model_config = ConfigDict(defer_build=True)
    signal: str
    actions: list[Action9]

class ServiceEndpoint1(BaseModel):
    model_config = ConfigDict(defer_build=True)
    click_tracking_params: str = Field(..., alias='clickTrackingParams')
    command_metadata: CommandMetadata25 = Field(..., alias='commandMetadata')
    signal_service_endpoint: SignalServiceEndpoint6 = Field(..., alias='signalServiceEndpoint')

class AccessibilityData12(BaseModel):
    model_config = ConfigDict(defer_build=True)
    label: str

class AccessibilityData11(BaseModel):
    model_config = ConfigDict(defer_build=True)
    accessibility_data: AccessibilityData12 = Field(..., alias='accessibilityData')

class ButtonRenderer10(BaseModel):
    model_config = ConfigDict(defer_build=True)
    style: str
    size: str
    is_disabled: bool = Field(..., alias='isDisabled')
    service_endpoint: ServiceEndpoint1 = Field(..., alias='serviceEndpoint')
    icon: Icon1
    tooltip: str
    tracking_params: str = Field(..., alias='trackingParams')
    accessibility_data: AccessibilityData11 = Field(..., alias='accessibilityData')

class VoiceSearchButton(BaseModel):
    model_config = ConfigDict(defer_build=True)
    button_renderer: ButtonRenderer10 = Field(..., alias='buttonRenderer')

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

class Thumbnail5(BaseModel):
    model_config = ConfigDict(defer_build=True)
    url: str
    width: int
    height: int

class Thumbnail4(BaseModel):
    model_config = ConfigDict(defer_build=True)
    thumbnails: list[Thumbnail5]
    sampled_thumbnail_color: SampledThumbnailColor = Field(..., alias='sampledThumbnailColor')
    dark_color_palette: DarkColorPalette = Field(..., alias='darkColorPalette')
    vibrant_color_palette: VibrantColorPalette = Field(..., alias='vibrantColorPalette')

class LinkAlternate(BaseModel):
    model_config = ConfigDict(defer_build=True)
    href_url: str = Field(..., alias='hrefUrl')

class MicroformatDataRenderer(BaseModel):
    model_config = ConfigDict(defer_build=True)
    url_canonical: str = Field(..., alias='urlCanonical')
    title: str
    description: str
    thumbnail: Thumbnail4
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
    link_alternates: list[LinkAlternate] = Field(..., alias='linkAlternates')

class Microformat(BaseModel):
    model_config = ConfigDict(defer_build=True)
    microformat_data_renderer: MicroformatDataRenderer = Field(..., alias='microformatDataRenderer')

class Thumbnail7(BaseModel):
    model_config = ConfigDict(defer_build=True)
    url: str
    width: int
    height: int

class Thumbnail6(BaseModel):
    model_config = ConfigDict(defer_build=True)
    thumbnails: list[Thumbnail7]
    sampled_thumbnail_color: SampledThumbnailColor = Field(..., alias='sampledThumbnailColor')
    dark_color_palette: DarkColorPalette = Field(..., alias='darkColorPalette')
    vibrant_color_palette: VibrantColorPalette = Field(..., alias='vibrantColorPalette')

class PlaylistCustomThumbnailRenderer(BaseModel):
    model_config = ConfigDict(defer_build=True)
    thumbnail: Thumbnail6

class ThumbnailRenderer(BaseModel):
    model_config = ConfigDict(defer_build=True)
    playlist_custom_thumbnail_renderer: PlaylistCustomThumbnailRenderer = Field(..., alias='playlistCustomThumbnailRenderer')

class WebCommandMetadata26(BaseModel):
    model_config = ConfigDict(defer_build=True)
    url: str
    web_page_type: str = Field(..., alias='webPageType')
    root_ve: int = Field(..., alias='rootVe')

class CommandMetadata26(BaseModel):
    model_config = ConfigDict(defer_build=True)
    web_command_metadata: WebCommandMetadata26 = Field(..., alias='webCommandMetadata')

class LoggingContext6(BaseModel):
    model_config = ConfigDict(defer_build=True)
    vss_logging_context: VssLoggingContext = Field(..., alias='vssLoggingContext')

class Html5PlaybackOnesieConfig6(BaseModel):
    model_config = ConfigDict(defer_build=True)
    common_config: CommonConfig = Field(..., alias='commonConfig')

class WatchEndpointSupportedOnesieConfig6(BaseModel):
    model_config = ConfigDict(defer_build=True)
    html5_playback_onesie_config: Html5PlaybackOnesieConfig6 = Field(..., alias='html5PlaybackOnesieConfig')

class WatchEndpoint6(BaseModel):
    model_config = ConfigDict(defer_build=True)
    video_id: str = Field(..., alias='videoId')
    playlist_id: str = Field(..., alias='playlistId')
    player_params: str = Field(..., alias='playerParams')
    logging_context: LoggingContext6 = Field(..., alias='loggingContext')
    watch_endpoint_supported_onesie_config: WatchEndpointSupportedOnesieConfig6 = Field(..., alias='watchEndpointSupportedOnesieConfig')

class NavigationEndpoint5(BaseModel):
    model_config = ConfigDict(defer_build=True)
    click_tracking_params: str = Field(..., alias='clickTrackingParams')
    command_metadata: CommandMetadata26 = Field(..., alias='commandMetadata')
    watch_endpoint: WatchEndpoint6 = Field(..., alias='watchEndpoint')

class Run26(BaseModel):
    model_config = ConfigDict(defer_build=True)
    text: str
    navigation_endpoint: NavigationEndpoint5 = Field(..., alias='navigationEndpoint')

class Title6(BaseModel):
    model_config = ConfigDict(defer_build=True)
    runs: list[Run26]

class Run27(BaseModel):
    model_config = ConfigDict(defer_build=True)
    text: str

class Stat1(BaseModel):
    model_config = ConfigDict(defer_build=True)
    runs: list[Run27] | None = None
    simple_text: str | None = Field(None, alias='simpleText')

class Text10(BaseModel):
    model_config = ConfigDict(defer_build=True)
    simple_text: str = Field(..., alias='simpleText')

class WebCommandMetadata27(BaseModel):
    model_config = ConfigDict(defer_build=True)
    ignore_navigation: bool = Field(..., alias='ignoreNavigation')

class CommandMetadata27(BaseModel):
    model_config = ConfigDict(defer_build=True)
    web_command_metadata: WebCommandMetadata27 = Field(..., alias='webCommandMetadata')

class Title7(BaseModel):
    model_config = ConfigDict(defer_build=True)
    simple_text: str = Field(..., alias='simpleText')

class Content6(BaseModel):
    model_config = ConfigDict(defer_build=True)
    simple_text: str = Field(..., alias='simpleText')

class Text11(BaseModel):
    model_config = ConfigDict(defer_build=True)
    runs: list[Run27]

class WebCommandMetadata28(BaseModel):
    model_config = ConfigDict(defer_build=True)
    url: str
    web_page_type: str = Field(..., alias='webPageType')
    root_ve: int = Field(..., alias='rootVe')

class CommandMetadata28(BaseModel):
    model_config = ConfigDict(defer_build=True)
    web_command_metadata: WebCommandMetadata28 = Field(..., alias='webCommandMetadata')

class WebCommandMetadata29(BaseModel):
    model_config = ConfigDict(defer_build=True)
    url: str
    web_page_type: str = Field(..., alias='webPageType')
    root_ve: int = Field(..., alias='rootVe')
    api_url: str = Field(..., alias='apiUrl')

class CommandMetadata29(BaseModel):
    model_config = ConfigDict(defer_build=True)
    web_command_metadata: WebCommandMetadata29 = Field(..., alias='webCommandMetadata')

class NextEndpoint1(BaseModel):
    model_config = ConfigDict(defer_build=True)
    click_tracking_params: str = Field(..., alias='clickTrackingParams')
    command_metadata: CommandMetadata29 = Field(..., alias='commandMetadata')
    browse_endpoint: BrowseEndpoint2 = Field(..., alias='browseEndpoint')

class SignInEndpoint2(BaseModel):
    model_config = ConfigDict(defer_build=True)
    next_endpoint: NextEndpoint1 = Field(..., alias='nextEndpoint')

class NavigationEndpoint7(BaseModel):
    model_config = ConfigDict(defer_build=True)
    click_tracking_params: str = Field(..., alias='clickTrackingParams')
    command_metadata: CommandMetadata28 = Field(..., alias='commandMetadata')
    sign_in_endpoint: SignInEndpoint2 = Field(..., alias='signInEndpoint')

class ButtonRenderer12(BaseModel):
    model_config = ConfigDict(defer_build=True)
    style: str
    size: str
    is_disabled: bool = Field(..., alias='isDisabled')
    text: Text11
    navigation_endpoint: NavigationEndpoint7 = Field(..., alias='navigationEndpoint')
    tracking_params: str = Field(..., alias='trackingParams')

class Button2(BaseModel):
    model_config = ConfigDict(defer_build=True)
    button_renderer: ButtonRenderer12 = Field(..., alias='buttonRenderer')

class ModalWithTitleAndButtonRenderer1(BaseModel):
    model_config = ConfigDict(defer_build=True)
    title: Title7
    content: Content6
    button: Button2

class Modal1(BaseModel):
    model_config = ConfigDict(defer_build=True)
    modal_with_title_and_button_renderer: ModalWithTitleAndButtonRenderer1 = Field(..., alias='modalWithTitleAndButtonRenderer')

class ModalEndpoint1(BaseModel):
    model_config = ConfigDict(defer_build=True)
    modal: Modal1

class NavigationEndpoint6(BaseModel):
    model_config = ConfigDict(defer_build=True)
    click_tracking_params: str = Field(..., alias='clickTrackingParams')
    command_metadata: CommandMetadata27 = Field(..., alias='commandMetadata')
    modal_endpoint: ModalEndpoint1 = Field(..., alias='modalEndpoint')

class MenuNavigationItemRenderer(BaseModel):
    model_config = ConfigDict(defer_build=True)
    text: Text10
    icon: Icon1
    navigation_endpoint: NavigationEndpoint6 = Field(..., alias='navigationEndpoint')
    tracking_params: str = Field(..., alias='trackingParams')

class Item1(BaseModel):
    model_config = ConfigDict(defer_build=True)
    menu_navigation_item_renderer: MenuNavigationItemRenderer = Field(..., alias='menuNavigationItemRenderer')

class WebCommandMetadata30(BaseModel):
    model_config = ConfigDict(defer_build=True)
    ignore_navigation: bool = Field(..., alias='ignoreNavigation')

class CommandMetadata30(BaseModel):
    model_config = ConfigDict(defer_build=True)
    web_command_metadata: WebCommandMetadata30 = Field(..., alias='webCommandMetadata')

class Text12(BaseModel):
    model_config = ConfigDict(defer_build=True)
    simple_text: str = Field(..., alias='simpleText')

class WebCommandMetadata31(BaseModel):
    model_config = ConfigDict(defer_build=True)
    url: str
    web_page_type: str = Field(..., alias='webPageType')
    root_ve: int = Field(..., alias='rootVe')

class CommandMetadata31(BaseModel):
    model_config = ConfigDict(defer_build=True)
    web_command_metadata: WebCommandMetadata31 = Field(..., alias='webCommandMetadata')

class WebCommandMetadata32(BaseModel):
    model_config = ConfigDict(defer_build=True)
    url: str
    web_page_type: str = Field(..., alias='webPageType')
    root_ve: int = Field(..., alias='rootVe')
    api_url: str = Field(..., alias='apiUrl')

class CommandMetadata32(BaseModel):
    model_config = ConfigDict(defer_build=True)
    web_command_metadata: WebCommandMetadata32 = Field(..., alias='webCommandMetadata')

class NextEndpoint2(BaseModel):
    model_config = ConfigDict(defer_build=True)
    click_tracking_params: str = Field(..., alias='clickTrackingParams')
    command_metadata: CommandMetadata32 = Field(..., alias='commandMetadata')
    browse_endpoint: BrowseEndpoint2 = Field(..., alias='browseEndpoint')

class SignInEndpoint3(BaseModel):
    model_config = ConfigDict(defer_build=True)
    next_endpoint: NextEndpoint2 = Field(..., alias='nextEndpoint')
    idam_tag: str = Field(..., alias='idamTag')

class NavigationEndpoint8(BaseModel):
    model_config = ConfigDict(defer_build=True)
    click_tracking_params: str = Field(..., alias='clickTrackingParams')
    command_metadata: CommandMetadata31 = Field(..., alias='commandMetadata')
    sign_in_endpoint: SignInEndpoint3 = Field(..., alias='signInEndpoint')

class ButtonRenderer13(BaseModel):
    model_config = ConfigDict(defer_build=True)
    style: str
    size: str
    is_disabled: bool = Field(..., alias='isDisabled')
    text: Text12
    navigation_endpoint: NavigationEndpoint8 = Field(..., alias='navigationEndpoint')
    tracking_params: str = Field(..., alias='trackingParams')

class Button3(BaseModel):
    model_config = ConfigDict(defer_build=True)
    button_renderer: ButtonRenderer13 = Field(..., alias='buttonRenderer')

class ModalWithTitleAndButtonRenderer2(BaseModel):
    model_config = ConfigDict(defer_build=True)
    title: Title7
    content: Content6
    button: Button3

class Modal2(BaseModel):
    model_config = ConfigDict(defer_build=True)
    modal_with_title_and_button_renderer: ModalWithTitleAndButtonRenderer2 = Field(..., alias='modalWithTitleAndButtonRenderer')

class ModalEndpoint2(BaseModel):
    model_config = ConfigDict(defer_build=True)
    modal: Modal2

class DefaultNavigationEndpoint1(BaseModel):
    model_config = ConfigDict(defer_build=True)
    click_tracking_params: str = Field(..., alias='clickTrackingParams')
    command_metadata: CommandMetadata30 = Field(..., alias='commandMetadata')
    modal_endpoint: ModalEndpoint2 = Field(..., alias='modalEndpoint')

class AccessibilityData14(BaseModel):
    model_config = ConfigDict(defer_build=True)
    label: str

class AccessibilityData13(BaseModel):
    model_config = ConfigDict(defer_build=True)
    accessibility_data: AccessibilityData14 = Field(..., alias='accessibilityData')

class AccessibilityData15(BaseModel):
    model_config = ConfigDict(defer_build=True)
    label: str

class ToggledAccessibilityData1(BaseModel):
    model_config = ConfigDict(defer_build=True)
    accessibility_data: AccessibilityData15 = Field(..., alias='accessibilityData')

class ToggleButtonRenderer1(BaseModel):
    model_config = ConfigDict(defer_build=True)
    style: Style
    size: Size
    is_toggled: bool = Field(..., alias='isToggled')
    is_disabled: bool = Field(..., alias='isDisabled')
    default_icon: DefaultIcon = Field(..., alias='defaultIcon')
    toggled_icon: ToggledIcon = Field(..., alias='toggledIcon')
    tracking_params: str = Field(..., alias='trackingParams')
    default_tooltip: str = Field(..., alias='defaultTooltip')
    toggled_tooltip: str = Field(..., alias='toggledTooltip')
    default_navigation_endpoint: DefaultNavigationEndpoint1 = Field(..., alias='defaultNavigationEndpoint')
    accessibility_data: AccessibilityData13 = Field(..., alias='accessibilityData')
    toggled_accessibility_data: ToggledAccessibilityData1 = Field(..., alias='toggledAccessibilityData')

class WebCommandMetadata33(BaseModel):
    model_config = ConfigDict(defer_build=True)
    url: str
    web_page_type: str = Field(..., alias='webPageType')
    root_ve: int = Field(..., alias='rootVe')

class CommandMetadata33(BaseModel):
    model_config = ConfigDict(defer_build=True)
    web_command_metadata: WebCommandMetadata33 = Field(..., alias='webCommandMetadata')

class LoggingContext7(BaseModel):
    model_config = ConfigDict(defer_build=True)
    vss_logging_context: VssLoggingContext = Field(..., alias='vssLoggingContext')

class Html5PlaybackOnesieConfig7(BaseModel):
    model_config = ConfigDict(defer_build=True)
    common_config: CommonConfig = Field(..., alias='commonConfig')

class WatchEndpointSupportedOnesieConfig7(BaseModel):
    model_config = ConfigDict(defer_build=True)
    html5_playback_onesie_config: Html5PlaybackOnesieConfig7 = Field(..., alias='html5PlaybackOnesieConfig')

class WatchEndpoint7(BaseModel):
    model_config = ConfigDict(defer_build=True)
    video_id: str = Field(..., alias='videoId')
    playlist_id: str = Field(..., alias='playlistId')
    params: str
    player_params: str = Field(..., alias='playerParams')
    logging_context: LoggingContext7 = Field(..., alias='loggingContext')
    watch_endpoint_supported_onesie_config: WatchEndpointSupportedOnesieConfig7 = Field(..., alias='watchEndpointSupportedOnesieConfig')

class NavigationEndpoint9(BaseModel):
    model_config = ConfigDict(defer_build=True)
    click_tracking_params: str = Field(..., alias='clickTrackingParams')
    command_metadata: CommandMetadata33 = Field(..., alias='commandMetadata')
    watch_endpoint: WatchEndpoint7 = Field(..., alias='watchEndpoint')

class Accessibility2(BaseModel):
    model_config = ConfigDict(defer_build=True)
    label: str

class WebCommandMetadata34(BaseModel):
    model_config = ConfigDict(defer_build=True)
    send_post: bool = Field(..., alias='sendPost')
    api_url: str = Field(..., alias='apiUrl')

class CommandMetadata34(BaseModel):
    model_config = ConfigDict(defer_build=True)
    web_command_metadata: WebCommandMetadata34 = Field(..., alias='webCommandMetadata')

class Popup4(BaseModel):
    model_config = ConfigDict(defer_build=True)
    unified_share_panel_renderer: UnifiedSharePanelRenderer = Field(..., alias='unifiedSharePanelRenderer')

class OpenPopupAction4(BaseModel):
    model_config = ConfigDict(defer_build=True)
    popup: Popup4
    popup_type: str = Field(..., alias='popupType')
    be_reused: bool = Field(..., alias='beReused')

class Command5(BaseModel):
    model_config = ConfigDict(defer_build=True)
    click_tracking_params: str = Field(..., alias='clickTrackingParams')
    open_popup_action: OpenPopupAction4 = Field(..., alias='openPopupAction')

class ShareEntityServiceEndpoint2(BaseModel):
    model_config = ConfigDict(defer_build=True)
    serialized_share_entity: str = Field(..., alias='serializedShareEntity')
    commands: list[Command5]

class ServiceEndpoint2(BaseModel):
    model_config = ConfigDict(defer_build=True)
    click_tracking_params: str = Field(..., alias='clickTrackingParams')
    command_metadata: CommandMetadata34 = Field(..., alias='commandMetadata')
    share_entity_service_endpoint: ShareEntityServiceEndpoint2 = Field(..., alias='shareEntityServiceEndpoint')

class ButtonRenderer14(BaseModel):
    model_config = ConfigDict(defer_build=True)
    style: str
    size: str
    is_disabled: bool = Field(..., alias='isDisabled')
    icon: Icon1
    navigation_endpoint: NavigationEndpoint9 | None = Field(None, alias='navigationEndpoint')
    accessibility: Accessibility2
    tooltip: str
    tracking_params: str = Field(..., alias='trackingParams')
    service_endpoint: ServiceEndpoint2 | None = Field(None, alias='serviceEndpoint')

class TopLevelButton(BaseModel):
    model_config = ConfigDict(defer_build=True)
    toggle_button_renderer: ToggleButtonRenderer1 | None = Field(None, alias='toggleButtonRenderer')
    button_renderer: ButtonRenderer14 | None = Field(None, alias='buttonRenderer')

class Accessibility3(BaseModel):
    model_config = ConfigDict(defer_build=True)
    accessibility_data: AccessibilityData15 = Field(..., alias='accessibilityData')

class MenuRenderer(BaseModel):
    model_config = ConfigDict(defer_build=True)
    items: list[Item1]
    tracking_params: str = Field(..., alias='trackingParams')
    top_level_buttons: list[TopLevelButton] = Field(..., alias='topLevelButtons')
    accessibility: Accessibility3

class Menu(BaseModel):
    model_config = ConfigDict(defer_build=True)
    menu_renderer: MenuRenderer = Field(..., alias='menuRenderer')

class ThumbnailOverlaySidePanelRenderer(BaseModel):
    model_config = ConfigDict(defer_build=True)
    text: Text12
    icon: Icon1

class ThumbnailOverlay(BaseModel):
    model_config = ConfigDict(defer_build=True)
    thumbnail_overlay_side_panel_renderer: ThumbnailOverlaySidePanelRenderer = Field(..., alias='thumbnailOverlaySidePanelRenderer')

class WebCommandMetadata35(BaseModel):
    model_config = ConfigDict(defer_build=True)
    url: str
    web_page_type: str = Field(..., alias='webPageType')
    root_ve: int = Field(..., alias='rootVe')

class CommandMetadata35(BaseModel):
    model_config = ConfigDict(defer_build=True)
    web_command_metadata: WebCommandMetadata35 = Field(..., alias='webCommandMetadata')

class LoggingContext8(BaseModel):
    model_config = ConfigDict(defer_build=True)
    vss_logging_context: VssLoggingContext = Field(..., alias='vssLoggingContext')

class Html5PlaybackOnesieConfig8(BaseModel):
    model_config = ConfigDict(defer_build=True)
    common_config: CommonConfig = Field(..., alias='commonConfig')

class WatchEndpointSupportedOnesieConfig8(BaseModel):
    model_config = ConfigDict(defer_build=True)
    html5_playback_onesie_config: Html5PlaybackOnesieConfig8 = Field(..., alias='html5PlaybackOnesieConfig')

class WatchEndpoint8(BaseModel):
    model_config = ConfigDict(defer_build=True)
    video_id: str = Field(..., alias='videoId')
    playlist_id: str = Field(..., alias='playlistId')
    player_params: str = Field(..., alias='playerParams')
    logging_context: LoggingContext8 = Field(..., alias='loggingContext')
    watch_endpoint_supported_onesie_config: WatchEndpointSupportedOnesieConfig8 = Field(..., alias='watchEndpointSupportedOnesieConfig')

class NavigationEndpoint10(BaseModel):
    model_config = ConfigDict(defer_build=True)
    click_tracking_params: str = Field(..., alias='clickTrackingParams')
    command_metadata: CommandMetadata35 = Field(..., alias='commandMetadata')
    watch_endpoint: WatchEndpoint8 = Field(..., alias='watchEndpoint')

class ShowMoreText(BaseModel):
    model_config = ConfigDict(defer_build=True)
    runs: list[Run27]

class PlaylistSidebarPrimaryInfoRenderer(BaseModel):
    model_config = ConfigDict(defer_build=True)
    thumbnail_renderer: ThumbnailRenderer = Field(..., alias='thumbnailRenderer')
    title: Title6
    stats: list[Stat1]
    menu: Menu
    thumbnail_overlays: list[ThumbnailOverlay] = Field(..., alias='thumbnailOverlays')
    navigation_endpoint: NavigationEndpoint10 = Field(..., alias='navigationEndpoint')
    show_more_text: ShowMoreText = Field(..., alias='showMoreText')

class Item(BaseModel):
    model_config = ConfigDict(defer_build=True)
    playlist_sidebar_primary_info_renderer: PlaylistSidebarPrimaryInfoRenderer = Field(..., alias='playlistSidebarPrimaryInfoRenderer')

class PlaylistSidebarRenderer(BaseModel):
    model_config = ConfigDict(defer_build=True)
    items: list[Item]
    tracking_params: str = Field(..., alias='trackingParams')

class Sidebar(BaseModel):
    model_config = ConfigDict(defer_build=True)
    playlist_sidebar_renderer: PlaylistSidebarRenderer = Field(..., alias='playlistSidebarRenderer')

class MusicModel(BaseModel):
    model_config = ConfigDict(defer_build=True)
    response_context: ResponseContext = Field(..., alias='responseContext')
    contents: Contents
    header: Header
    metadata: Metadata2
    tracking_params: str = Field(..., alias='trackingParams')
    topbar: Topbar
    microformat: Microformat
    sidebar: Sidebar
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
