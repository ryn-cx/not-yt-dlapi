from typing import Any, Self
from pydantic import ModelWrapValidatorHandler, PrivateAttr, model_validator
from pydantic import BaseModel, ConfigDict, Field
from datetime import time, timedelta

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

class WebCommandMetadata(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    url: str | Any = Field(default=None, union_mode='left_to_right')
    web_page_type: str | Any = Field(None, alias='webPageType', union_mode='left_to_right')
    root_ve: int | Any = Field(None, alias='rootVe', union_mode='left_to_right')
    api_url: str | Any = Field(None, alias='apiUrl', union_mode='left_to_right')

class CommandMetadata(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    web_command_metadata: WebCommandMetadata | Any = Field(None, alias='webCommandMetadata', union_mode='left_to_right')

class BrowseEndpoint(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    browse_id: str | Any = Field(None, alias='browseId', union_mode='left_to_right')

class Endpoint(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    click_tracking_params: str | Any = Field(None, alias='clickTrackingParams', union_mode='left_to_right')
    command_metadata: CommandMetadata | Any = Field(None, alias='commandMetadata', union_mode='left_to_right')
    browse_endpoint: BrowseEndpoint | Any = Field(None, alias='browseEndpoint', union_mode='left_to_right')

class CommandMetadata1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    web_command_metadata: WebCommandMetadata | Any = Field(None, alias='webCommandMetadata', union_mode='left_to_right')

class BrowseEndpoint1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    browse_id: str | Any = Field(None, alias='browseId', union_mode='left_to_right')
    params: str | Any = Field(default=None, union_mode='left_to_right')

class NavigationEndpoint(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    click_tracking_params: str | Any = Field(None, alias='clickTrackingParams', union_mode='left_to_right')
    command_metadata: CommandMetadata1 | Any = Field(None, alias='commandMetadata', union_mode='left_to_right')
    browse_endpoint: BrowseEndpoint1 | Any = Field(None, alias='browseEndpoint', union_mode='left_to_right')

class AccessibilityData(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    label: str | Any = Field(default=None, union_mode='left_to_right')

class Accessibility(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    accessibility_data: AccessibilityData | Any = Field(None, alias='accessibilityData', union_mode='left_to_right')

class SubMenuItem(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    title: str | Any = Field(default=None, union_mode='left_to_right')
    selected: bool | Any = Field(default=None, union_mode='left_to_right')
    navigation_endpoint: NavigationEndpoint | Any = Field(None, alias='navigationEndpoint', union_mode='left_to_right')
    accessibility: Accessibility | Any = Field(default=None, union_mode='left_to_right')
    tracking_params: str | Any = Field(None, alias='trackingParams', union_mode='left_to_right')

class SortFilterSubMenuRenderer(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    sub_menu_items: list[SubMenuItem] | Any = Field(None, alias='subMenuItems', union_mode='left_to_right')
    tracking_params: str | Any = Field(None, alias='trackingParams', union_mode='left_to_right')

class Collection(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    sort_filter_sub_menu_renderer: SortFilterSubMenuRenderer | Any = Field(None, alias='sortFilterSubMenuRenderer', union_mode='left_to_right')

class Run(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    text: str | Any = Field(default=None, union_mode='left_to_right')

class Description(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    runs: list[Run] | Any = Field(default=None, union_mode='left_to_right')

class PlaylistShowMetadataRenderer(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    collection: Collection | Any = Field(default=None, union_mode='left_to_right')
    description: Description | Any = Field(default=None, union_mode='left_to_right')

class Thumbnail1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    url: str | Any = Field(default=None, union_mode='left_to_right')
    width: int | Any = Field(default=None, union_mode='left_to_right')
    height: int | Any = Field(default=None, union_mode='left_to_right')

class Thumbnail(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    thumbnails: list[Thumbnail1] | Any = Field(default=None, union_mode='left_to_right')

class Accessibility1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    accessibility_data: AccessibilityData | Any = Field(None, alias='accessibilityData', union_mode='left_to_right')

class Title(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    runs: list[Run] | Any = Field(default=None, union_mode='left_to_right')
    accessibility: Accessibility1 | Any = Field(default=None, union_mode='left_to_right')

class Index(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    simple_text: str | Any = Field(None, alias='simpleText', union_mode='left_to_right')

class Accessibility2(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    accessibility_data: AccessibilityData | Any = Field(None, alias='accessibilityData', union_mode='left_to_right')

class LengthText(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    accessibility: Accessibility2 | Any = Field(default=None, union_mode='left_to_right')
    simple_text: time | timedelta | Any = Field(None, alias='simpleText', union_mode='left_to_right')

class WebCommandMetadata2(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    ignore_navigation: bool | Any = Field(None, alias='ignoreNavigation', union_mode='left_to_right')
    url: str | Any = Field(default=None, union_mode='left_to_right')
    web_page_type: str | Any = Field(None, alias='webPageType', union_mode='left_to_right')
    root_ve: int | Any = Field(None, alias='rootVe', union_mode='left_to_right')

class CommandMetadata2(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    web_command_metadata: WebCommandMetadata2 | Any = Field(None, alias='webCommandMetadata', union_mode='left_to_right')

class Title1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    runs: list[Run] | Any = Field(default=None, union_mode='left_to_right')

class Content4(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    runs: list[Run] | Any = Field(default=None, union_mode='left_to_right')

class Text(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    simple_text: str | Any = Field(None, alias='simpleText', union_mode='left_to_right')

class WebCommandMetadata3(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    url: str | Any = Field(default=None, union_mode='left_to_right')
    web_page_type: str | Any = Field(None, alias='webPageType', union_mode='left_to_right')
    root_ve: int | Any = Field(None, alias='rootVe', union_mode='left_to_right')

class CommandMetadata3(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    web_command_metadata: WebCommandMetadata3 | Any = Field(None, alias='webCommandMetadata', union_mode='left_to_right')

class WebCommandMetadata4(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    url: str | Any = Field(default=None, union_mode='left_to_right')
    web_page_type: str | Any = Field(None, alias='webPageType', union_mode='left_to_right')
    root_ve: int | Any = Field(None, alias='rootVe', union_mode='left_to_right')
    api_url: str | Any = Field(None, alias='apiUrl', union_mode='left_to_right')

class CommandMetadata4(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    web_command_metadata: WebCommandMetadata4 | Any = Field(None, alias='webCommandMetadata', union_mode='left_to_right')

class NextEndpoint(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    click_tracking_params: str | Any = Field(None, alias='clickTrackingParams', union_mode='left_to_right')
    command_metadata: CommandMetadata4 | Any = Field(None, alias='commandMetadata', union_mode='left_to_right')
    browse_endpoint: BrowseEndpoint1 | Any = Field(None, alias='browseEndpoint', union_mode='left_to_right')

class SignInEndpoint(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    next_endpoint: NextEndpoint | Any = Field(None, alias='nextEndpoint', union_mode='left_to_right')

class NavigationEndpoint2(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    click_tracking_params: str | Any = Field(None, alias='clickTrackingParams', union_mode='left_to_right')
    command_metadata: CommandMetadata3 | Any = Field(None, alias='commandMetadata', union_mode='left_to_right')
    sign_in_endpoint: SignInEndpoint | Any = Field(None, alias='signInEndpoint', union_mode='left_to_right')

class ButtonRenderer(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    style: str | Any = Field(default=None, union_mode='left_to_right')
    size: str | Any = Field(default=None, union_mode='left_to_right')
    is_disabled: bool | Any = Field(None, alias='isDisabled', union_mode='left_to_right')
    text: Text | Any = Field(default=None, union_mode='left_to_right')
    navigation_endpoint: NavigationEndpoint2 | Any = Field(None, alias='navigationEndpoint', union_mode='left_to_right')
    tracking_params: str | Any = Field(None, alias='trackingParams', union_mode='left_to_right')

class Button(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    button_renderer: ButtonRenderer | Any = Field(None, alias='buttonRenderer', union_mode='left_to_right')

class ModalWithTitleAndButtonRenderer(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    title: Title1 | Any = Field(default=None, union_mode='left_to_right')
    content: Content4 | Any = Field(default=None, union_mode='left_to_right')
    button: Button | Any = Field(default=None, union_mode='left_to_right')

class Modal(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    modal_with_title_and_button_renderer: ModalWithTitleAndButtonRenderer | Any = Field(None, alias='modalWithTitleAndButtonRenderer', union_mode='left_to_right')

class ModalEndpoint(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    modal: Modal | Any = Field(default=None, union_mode='left_to_right')

class VssLoggingContext(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    serialized_context_data: str | Any = Field(None, alias='serializedContextData', union_mode='left_to_right')

class LoggingContext(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    vss_logging_context: VssLoggingContext | Any = Field(None, alias='vssLoggingContext', union_mode='left_to_right')

class WatchEndpoint(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    video_id: str | Any = Field(None, alias='videoId', union_mode='left_to_right')
    playlist_id: str | Any = Field(None, alias='playlistId', union_mode='left_to_right')
    index: int | Any = Field(default=None, union_mode='left_to_right')
    player_params: str | Any = Field(None, alias='playerParams', union_mode='left_to_right')
    logging_context: LoggingContext | Any = Field(None, alias='loggingContext', union_mode='left_to_right')

class NavigationEndpoint1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    click_tracking_params: str | Any = Field(None, alias='clickTrackingParams', union_mode='left_to_right')
    command_metadata: CommandMetadata2 | Any = Field(None, alias='commandMetadata', union_mode='left_to_right')
    modal_endpoint: ModalEndpoint | Any = Field(None, alias='modalEndpoint', union_mode='left_to_right')
    watch_endpoint: WatchEndpoint | Any = Field(None, alias='watchEndpoint', union_mode='left_to_right')

class Text1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    runs: list[Run] | Any = Field(default=None, union_mode='left_to_right')

class Icon(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    icon_type: str | Any = Field(None, alias='iconType', union_mode='left_to_right')

class Title2(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    content: str | Any = Field(default=None, union_mode='left_to_right')

class PanelHeaderViewModel(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    title: Title2 | Any = Field(default=None, union_mode='left_to_right')

class Header(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    panel_header_view_model: PanelHeaderViewModel | Any = Field(None, alias='panelHeaderViewModel', union_mode='left_to_right')

class Subtitle(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    content: str | Any = Field(default=None, union_mode='left_to_right')

class WebCommandMetadata5(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    url: str | Any = Field(default=None, union_mode='left_to_right')
    web_page_type: str | Any = Field(None, alias='webPageType', union_mode='left_to_right')
    root_ve: int | Any = Field(None, alias='rootVe', union_mode='left_to_right')

class CommandMetadata5(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    web_command_metadata: WebCommandMetadata5 | Any = Field(None, alias='webCommandMetadata', union_mode='left_to_right')

class LoggingContext1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    vss_logging_context: VssLoggingContext | Any = Field(None, alias='vssLoggingContext', union_mode='left_to_right')

class WatchEndpoint1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    video_id: str | Any = Field(None, alias='videoId', union_mode='left_to_right')
    playlist_id: str | Any = Field(None, alias='playlistId', union_mode='left_to_right')
    player_params: str | Any = Field(None, alias='playerParams', union_mode='left_to_right')
    logging_context: LoggingContext1 | Any = Field(None, alias='loggingContext', union_mode='left_to_right')

class InnertubeCommand(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    click_tracking_params: str | Any = Field(None, alias='clickTrackingParams', union_mode='left_to_right')
    command_metadata: CommandMetadata5 | Any = Field(None, alias='commandMetadata', union_mode='left_to_right')
    watch_endpoint: WatchEndpoint1 | Any = Field(None, alias='watchEndpoint', union_mode='left_to_right')

class OnTap(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    innertube_command: InnertubeCommand | Any = Field(None, alias='innertubeCommand', union_mode='left_to_right')

class CommandContext(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    on_tap: OnTap | Any = Field(None, alias='onTap', union_mode='left_to_right')

class RendererContext(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    command_context: CommandContext | Any = Field(None, alias='commandContext', union_mode='left_to_right')

class ListItemViewModel(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    title: Title2 | Any = Field(default=None, union_mode='left_to_right')
    subtitle: Subtitle | Any = Field(default=None, union_mode='left_to_right')
    renderer_context: RendererContext | Any = Field(None, alias='rendererContext', union_mode='left_to_right')

class ListItem(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    list_item_view_model: ListItemViewModel | Any = Field(None, alias='listItemViewModel', union_mode='left_to_right')

class ListViewModel(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    list_items: list[ListItem] | Any = Field(None, alias='listItems', union_mode='left_to_right')

class Content5(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    list_view_model: ListViewModel | Any = Field(None, alias='listViewModel', union_mode='left_to_right')

class SheetViewModel(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    header: Header | Any = Field(default=None, union_mode='left_to_right')
    content: Content5 | Any = Field(default=None, union_mode='left_to_right')

class InlineContent(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    sheet_view_model: SheetViewModel | Any = Field(None, alias='sheetViewModel', union_mode='left_to_right')

class PanelLoadingStrategy(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    inline_content: InlineContent | Any = Field(None, alias='inlineContent', union_mode='left_to_right')

class ShowSheetCommand(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    panel_loading_strategy: PanelLoadingStrategy | Any = Field(None, alias='panelLoadingStrategy', union_mode='left_to_right')

class NavigationEndpoint3(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    click_tracking_params: str | Any = Field(None, alias='clickTrackingParams', union_mode='left_to_right')
    show_sheet_command: ShowSheetCommand | Any = Field(None, alias='showSheetCommand', union_mode='left_to_right')

class MenuNavigationItemRenderer(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    text: Text1 | Any = Field(default=None, union_mode='left_to_right')
    icon: Icon | Any = Field(default=None, union_mode='left_to_right')
    navigation_endpoint: NavigationEndpoint3 | Any = Field(None, alias='navigationEndpoint', union_mode='left_to_right')
    tracking_params: str | Any = Field(None, alias='trackingParams', union_mode='left_to_right')

class Item(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    menu_navigation_item_renderer: MenuNavigationItemRenderer | Any = Field(None, alias='menuNavigationItemRenderer', union_mode='left_to_right')

class Accessibility3(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    accessibility_data: AccessibilityData | Any = Field(None, alias='accessibilityData', union_mode='left_to_right')

class MenuRenderer(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    items: list[Item] | Any = Field(default=None, union_mode='left_to_right')
    tracking_params: str | Any = Field(None, alias='trackingParams', union_mode='left_to_right')
    accessibility: Accessibility3 | Any = Field(default=None, union_mode='left_to_right')

class Menu(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    menu_renderer: MenuRenderer | Any = Field(None, alias='menuRenderer', union_mode='left_to_right')

class Accessibility4(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    accessibility_data: AccessibilityData | Any = Field(None, alias='accessibilityData', union_mode='left_to_right')

class Text2(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    accessibility: Accessibility4 | Any = Field(default=None, union_mode='left_to_right')
    simple_text: time | timedelta | Any = Field(None, alias='simpleText', union_mode='left_to_right')

class ThumbnailOverlayTimeStatusRenderer(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    text: Text2 | Any = Field(default=None, union_mode='left_to_right')
    style: str | Any = Field(default=None, union_mode='left_to_right')

class UntoggledIcon(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    icon_type: str | Any = Field(None, alias='iconType', union_mode='left_to_right')

class ToggledIcon(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    icon_type: str | Any = Field(None, alias='iconType', union_mode='left_to_right')

class WebCommandMetadata6(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    send_post: bool | Any = Field(None, alias='sendPost', union_mode='left_to_right')
    api_url: str | Any = Field(None, alias='apiUrl', union_mode='left_to_right')

class CommandMetadata6(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    web_command_metadata: WebCommandMetadata6 | Any = Field(None, alias='webCommandMetadata', union_mode='left_to_right')

class Action(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    added_video_id: str | Any = Field(None, alias='addedVideoId', union_mode='left_to_right')
    action: str | Any = Field(default=None, union_mode='left_to_right')

class PlaylistEditEndpoint(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    playlist_id: str | Any = Field(None, alias='playlistId', union_mode='left_to_right')
    actions: list[Action] | Any = Field(default=None, union_mode='left_to_right')

class CommandMetadata7(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    web_command_metadata: WebCommandMetadata6 | Any = Field(None, alias='webCommandMetadata', union_mode='left_to_right')

class CreatePlaylistServiceEndpoint(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    video_ids: list[str] | Any = Field(None, alias='videoIds', union_mode='left_to_right')
    params: str | Any = Field(default=None, union_mode='left_to_right')

class OnCreateListCommand(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    click_tracking_params: str | Any = Field(None, alias='clickTrackingParams', union_mode='left_to_right')
    command_metadata: CommandMetadata7 | Any = Field(None, alias='commandMetadata', union_mode='left_to_right')
    create_playlist_service_endpoint: CreatePlaylistServiceEndpoint | Any = Field(None, alias='createPlaylistServiceEndpoint', union_mode='left_to_right')

class AddToPlaylistCommand(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    open_miniplayer: bool | Any = Field(None, alias='openMiniplayer', union_mode='left_to_right')
    video_id: str | Any = Field(None, alias='videoId', union_mode='left_to_right')
    list_type: str | Any = Field(None, alias='listType', union_mode='left_to_right')
    on_create_list_command: OnCreateListCommand | Any = Field(None, alias='onCreateListCommand', union_mode='left_to_right')
    video_ids: list[str] | Any = Field(None, alias='videoIds', union_mode='left_to_right')

class Action1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    click_tracking_params: str | Any = Field(None, alias='clickTrackingParams', union_mode='left_to_right')
    add_to_playlist_command: AddToPlaylistCommand | Any = Field(None, alias='addToPlaylistCommand', union_mode='left_to_right')

class SignalServiceEndpoint(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    signal: str | Any = Field(default=None, union_mode='left_to_right')
    actions: list[Action1] | Any = Field(default=None, union_mode='left_to_right')

class UntoggledServiceEndpoint(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    click_tracking_params: str | Any = Field(None, alias='clickTrackingParams', union_mode='left_to_right')
    command_metadata: CommandMetadata6 | Any = Field(None, alias='commandMetadata', union_mode='left_to_right')
    playlist_edit_endpoint: PlaylistEditEndpoint | Any = Field(None, alias='playlistEditEndpoint', union_mode='left_to_right')
    signal_service_endpoint: SignalServiceEndpoint | Any = Field(None, alias='signalServiceEndpoint', union_mode='left_to_right')

class CommandMetadata8(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    web_command_metadata: WebCommandMetadata6 | Any = Field(None, alias='webCommandMetadata', union_mode='left_to_right')

class Action2(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    action: str | Any = Field(default=None, union_mode='left_to_right')
    removed_video_id: str | Any = Field(None, alias='removedVideoId', union_mode='left_to_right')

class PlaylistEditEndpoint1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    playlist_id: str | Any = Field(None, alias='playlistId', union_mode='left_to_right')
    actions: list[Action2] | Any = Field(default=None, union_mode='left_to_right')

class ToggledServiceEndpoint(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    click_tracking_params: str | Any = Field(None, alias='clickTrackingParams', union_mode='left_to_right')
    command_metadata: CommandMetadata8 | Any = Field(None, alias='commandMetadata', union_mode='left_to_right')
    playlist_edit_endpoint: PlaylistEditEndpoint1 | Any = Field(None, alias='playlistEditEndpoint', union_mode='left_to_right')

class UntoggledAccessibility(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    accessibility_data: AccessibilityData | Any = Field(None, alias='accessibilityData', union_mode='left_to_right')

class ToggledAccessibility(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    accessibility_data: AccessibilityData | Any = Field(None, alias='accessibilityData', union_mode='left_to_right')

class ThumbnailOverlayToggleButtonRenderer(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    is_toggled: bool | Any = Field(None, alias='isToggled', union_mode='left_to_right')
    untoggled_icon: UntoggledIcon | Any = Field(None, alias='untoggledIcon', union_mode='left_to_right')
    toggled_icon: ToggledIcon | Any = Field(None, alias='toggledIcon', union_mode='left_to_right')
    untoggled_tooltip: str | Any = Field(None, alias='untoggledTooltip', union_mode='left_to_right')
    toggled_tooltip: str | Any = Field(None, alias='toggledTooltip', union_mode='left_to_right')
    untoggled_service_endpoint: UntoggledServiceEndpoint | Any = Field(None, alias='untoggledServiceEndpoint', union_mode='left_to_right')
    toggled_service_endpoint: ToggledServiceEndpoint | Any = Field(None, alias='toggledServiceEndpoint', union_mode='left_to_right')
    untoggled_accessibility: UntoggledAccessibility | Any = Field(None, alias='untoggledAccessibility', union_mode='left_to_right')
    toggled_accessibility: ToggledAccessibility | Any = Field(None, alias='toggledAccessibility', union_mode='left_to_right')
    tracking_params: str | Any = Field(None, alias='trackingParams', union_mode='left_to_right')

class Text3(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    runs: list[Run] | Any = Field(default=None, union_mode='left_to_right')

class ThumbnailOverlayNowPlayingRenderer(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    text: Text3 | Any = Field(default=None, union_mode='left_to_right')

class ThumbnailOverlay(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    thumbnail_overlay_time_status_renderer: ThumbnailOverlayTimeStatusRenderer | Any = Field(None, alias='thumbnailOverlayTimeStatusRenderer', union_mode='left_to_right')
    thumbnail_overlay_toggle_button_renderer: ThumbnailOverlayToggleButtonRenderer | Any = Field(None, alias='thumbnailOverlayToggleButtonRenderer', union_mode='left_to_right')
    thumbnail_overlay_now_playing_renderer: ThumbnailOverlayNowPlayingRenderer | Any = Field(None, alias='thumbnailOverlayNowPlayingRenderer', union_mode='left_to_right')

class UpcomingEventText(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    simple_text: str | Any = Field(None, alias='simpleText', union_mode='left_to_right')

class UpcomingEventData(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    upcoming_event_text: UpcomingEventText | Any = Field(None, alias='upcomingEventText', union_mode='left_to_right')

class MetadataBadgeRenderer(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    style: str | Any = Field(default=None, union_mode='left_to_right')
    label: str | Any = Field(default=None, union_mode='left_to_right')
    tracking_params: str | Any = Field(None, alias='trackingParams', union_mode='left_to_right')
    accessibility_data: AccessibilityData | Any = Field(None, alias='accessibilityData', union_mode='left_to_right')

class BottomBadge(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    metadata_badge_renderer: MetadataBadgeRenderer | Any = Field(None, alias='metadataBadgeRenderer', union_mode='left_to_right')

class PlaylistVideoRenderer(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    video_id: str | Any = Field(None, alias='videoId', union_mode='left_to_right')
    thumbnail: Thumbnail | Any = Field(default=None, union_mode='left_to_right')
    title: Title | Any = Field(default=None, union_mode='left_to_right')
    index: Index | Any = Field(default=None, union_mode='left_to_right')
    length_text: LengthText | Any = Field(None, alias='lengthText', union_mode='left_to_right')
    navigation_endpoint: NavigationEndpoint1 | Any = Field(None, alias='navigationEndpoint', union_mode='left_to_right')
    length_seconds: str | Any = Field(None, alias='lengthSeconds', union_mode='left_to_right')
    tracking_params: str | Any = Field(None, alias='trackingParams', union_mode='left_to_right')
    is_playable: bool | Any = Field(None, alias='isPlayable', union_mode='left_to_right')
    menu: Menu | Any = Field(default=None, union_mode='left_to_right')
    thumbnail_overlays: list[ThumbnailOverlay] | Any = Field(None, alias='thumbnailOverlays', union_mode='left_to_right')
    upcoming_event_data: UpcomingEventData | Any = Field(None, alias='upcomingEventData', union_mode='left_to_right')
    bottom_badges: list[BottomBadge] | Any = Field(None, alias='bottomBadges', union_mode='left_to_right')

class Content3(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    playlist_video_renderer: PlaylistVideoRenderer | Any = Field(None, alias='playlistVideoRenderer', union_mode='left_to_right')

class PlaylistVideoListRenderer(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    contents: list[Content3] | Any = Field(default=None, union_mode='left_to_right')
    is_editable: bool | Any = Field(None, alias='isEditable', union_mode='left_to_right')
    can_reorder: bool | Any = Field(None, alias='canReorder', union_mode='left_to_right')
    tracking_params: str | Any = Field(None, alias='trackingParams', union_mode='left_to_right')
    target_id: str | Any = Field(None, alias='targetId', union_mode='left_to_right')

class Content2(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    playlist_show_metadata_renderer: PlaylistShowMetadataRenderer | Any = Field(None, alias='playlistShowMetadataRenderer', union_mode='left_to_right')
    playlist_video_list_renderer: PlaylistVideoListRenderer | Any = Field(None, alias='playlistVideoListRenderer', union_mode='left_to_right')

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

class Content(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    section_list_renderer: SectionListRenderer | Any = Field(None, alias='sectionListRenderer', union_mode='left_to_right')

class Accessibility5(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    accessibility_data: AccessibilityData | Any = Field(None, alias='accessibilityData', union_mode='left_to_right')

class TabRenderer(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    endpoint: Endpoint | Any = Field(default=None, union_mode='left_to_right')
    selected: bool | Any = Field(default=None, union_mode='left_to_right')
    content: Content | Any = Field(default=None, union_mode='left_to_right')
    tab_identifier: str | Any = Field(None, alias='tabIdentifier', union_mode='left_to_right')
    accessibility: Accessibility5 | Any = Field(default=None, union_mode='left_to_right')
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

class IconImage(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    icon_type: str | Any = Field(None, alias='iconType', union_mode='left_to_right')

class TooltipText(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    runs: list[Run] | Any = Field(default=None, union_mode='left_to_right')

class WebCommandMetadata9(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    url: str | Any = Field(default=None, union_mode='left_to_right')
    web_page_type: str | Any = Field(None, alias='webPageType', union_mode='left_to_right')
    root_ve: int | Any = Field(None, alias='rootVe', union_mode='left_to_right')
    api_url: str | Any = Field(None, alias='apiUrl', union_mode='left_to_right')

class CommandMetadata9(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    web_command_metadata: WebCommandMetadata9 | Any = Field(None, alias='webCommandMetadata', union_mode='left_to_right')

class BrowseEndpoint3(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    browse_id: str | Any = Field(None, alias='browseId', union_mode='left_to_right')

class Endpoint1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    click_tracking_params: str | Any = Field(None, alias='clickTrackingParams', union_mode='left_to_right')
    command_metadata: CommandMetadata9 | Any = Field(None, alias='commandMetadata', union_mode='left_to_right')
    browse_endpoint: BrowseEndpoint3 | Any = Field(None, alias='browseEndpoint', union_mode='left_to_right')

class TopbarLogoRenderer(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    icon_image: IconImage | Any = Field(None, alias='iconImage', union_mode='left_to_right')
    tooltip_text: TooltipText | Any = Field(None, alias='tooltipText', union_mode='left_to_right')
    endpoint: Endpoint1 | Any = Field(default=None, union_mode='left_to_right')
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

class Config(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    web_searchbox_config: WebSearchboxConfig | Any = Field(None, alias='webSearchboxConfig', union_mode='left_to_right')

class WebCommandMetadata10(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    url: str | Any = Field(default=None, union_mode='left_to_right')
    web_page_type: str | Any = Field(None, alias='webPageType', union_mode='left_to_right')
    root_ve: int | Any = Field(None, alias='rootVe', union_mode='left_to_right')

class CommandMetadata10(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    web_command_metadata: WebCommandMetadata10 | Any = Field(None, alias='webCommandMetadata', union_mode='left_to_right')

class SearchEndpoint1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    query: str | Any = Field(default=None, union_mode='left_to_right')
    params: str | Any = Field(default=None, union_mode='left_to_right')

class SearchEndpoint(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    click_tracking_params: str | Any = Field(None, alias='clickTrackingParams', union_mode='left_to_right')
    command_metadata: CommandMetadata10 | Any = Field(None, alias='commandMetadata', union_mode='left_to_right')
    search_endpoint: SearchEndpoint1 | Any = Field(None, alias='searchEndpoint', union_mode='left_to_right')

class AccessibilityData9(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    accessibility_data: AccessibilityData | Any = Field(None, alias='accessibilityData', union_mode='left_to_right')

class ButtonRenderer1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    style: str | Any = Field(default=None, union_mode='left_to_right')
    size: str | Any = Field(default=None, union_mode='left_to_right')
    is_disabled: bool | Any = Field(None, alias='isDisabled', union_mode='left_to_right')
    icon: Icon | Any = Field(default=None, union_mode='left_to_right')
    tracking_params: str | Any = Field(None, alias='trackingParams', union_mode='left_to_right')
    accessibility_data: AccessibilityData9 | Any = Field(None, alias='accessibilityData', union_mode='left_to_right')

class ClearButton(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    button_renderer: ButtonRenderer1 | Any = Field(None, alias='buttonRenderer', union_mode='left_to_right')

class Headline(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    content: str | Any = Field(default=None, union_mode='left_to_right')

class DialogHeaderViewModel(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    headline: Headline | Any = Field(default=None, union_mode='left_to_right')

class Header1(BaseModel):
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

class Text4(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    content: str | Any = Field(default=None, union_mode='left_to_right')

class Paragraph(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    text: Text4 | Any = Field(default=None, union_mode='left_to_right')

class BasicContentViewModel(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    paragraphs: list[Paragraph] | Any = Field(default=None, union_mode='left_to_right')

class Content6(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    basic_content_view_model: BasicContentViewModel | Any = Field(None, alias='basicContentViewModel', union_mode='left_to_right')

class DialogViewModel(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    header: Header1 | Any = Field(default=None, union_mode='left_to_right')
    footer: Footer | Any = Field(default=None, union_mode='left_to_right')
    content: Content6 | Any = Field(default=None, union_mode='left_to_right')

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
    icon: Icon | Any = Field(default=None, union_mode='left_to_right')
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

class WebCommandMetadata11(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    send_post: bool | Any = Field(None, alias='sendPost', union_mode='left_to_right')
    api_url: str | Any = Field(None, alias='apiUrl', union_mode='left_to_right')

class CommandMetadata11(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    web_command_metadata: WebCommandMetadata11 | Any = Field(None, alias='webCommandMetadata', union_mode='left_to_right')

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

class Action3(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    click_tracking_params: str | Any = Field(None, alias='clickTrackingParams', union_mode='left_to_right')
    open_popup_action: OpenPopupAction | Any = Field(None, alias='openPopupAction', union_mode='left_to_right')

class SignalServiceEndpoint1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    signal: str | Any = Field(default=None, union_mode='left_to_right')
    actions: list[Action3] | Any = Field(default=None, union_mode='left_to_right')

class MenuRequest(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    click_tracking_params: str | Any = Field(None, alias='clickTrackingParams', union_mode='left_to_right')
    command_metadata: CommandMetadata11 | Any = Field(None, alias='commandMetadata', union_mode='left_to_right')
    signal_service_endpoint: SignalServiceEndpoint1 | Any = Field(None, alias='signalServiceEndpoint', union_mode='left_to_right')

class AccessibilityData11(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    label: str | Any = Field(default=None, union_mode='left_to_right')

class Accessibility6(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    accessibility_data: AccessibilityData11 | Any = Field(None, alias='accessibilityData', union_mode='left_to_right')

class TopbarMenuButtonRenderer(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    icon: Icon | Any = Field(default=None, union_mode='left_to_right')
    menu_request: MenuRequest | Any = Field(None, alias='menuRequest', union_mode='left_to_right')
    tracking_params: str | Any = Field(None, alias='trackingParams', union_mode='left_to_right')
    accessibility: Accessibility6 | Any = Field(default=None, union_mode='left_to_right')
    tooltip: str | Any = Field(default=None, union_mode='left_to_right')
    style: str | Any = Field(default=None, union_mode='left_to_right')

class Text5(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    runs: list[Run] | Any = Field(default=None, union_mode='left_to_right')

class WebCommandMetadata12(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    url: str | Any = Field(default=None, union_mode='left_to_right')
    web_page_type: str | Any = Field(None, alias='webPageType', union_mode='left_to_right')
    root_ve: int | Any = Field(None, alias='rootVe', union_mode='left_to_right')

class CommandMetadata12(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    web_command_metadata: WebCommandMetadata12 | Any = Field(None, alias='webCommandMetadata', union_mode='left_to_right')

class SignInEndpoint1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    idam_tag: str | Any = Field(None, alias='idamTag', union_mode='left_to_right')

class NavigationEndpoint4(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    click_tracking_params: str | Any = Field(None, alias='clickTrackingParams', union_mode='left_to_right')
    command_metadata: CommandMetadata12 | Any = Field(None, alias='commandMetadata', union_mode='left_to_right')
    sign_in_endpoint: SignInEndpoint1 | Any = Field(None, alias='signInEndpoint', union_mode='left_to_right')

class ButtonRenderer2(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    style: str | Any = Field(default=None, union_mode='left_to_right')
    size: str | Any = Field(default=None, union_mode='left_to_right')
    text: Text5 | Any = Field(default=None, union_mode='left_to_right')
    icon: Icon | Any = Field(default=None, union_mode='left_to_right')
    navigation_endpoint: NavigationEndpoint4 | Any = Field(None, alias='navigationEndpoint', union_mode='left_to_right')
    tracking_params: str | Any = Field(None, alias='trackingParams', union_mode='left_to_right')
    target_id: str | Any = Field(None, alias='targetId', union_mode='left_to_right')

class TopbarButton(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    topbar_menu_button_renderer: TopbarMenuButtonRenderer | Any = Field(None, alias='topbarMenuButtonRenderer', union_mode='left_to_right')
    button_renderer: ButtonRenderer2 | Any = Field(None, alias='buttonRenderer', union_mode='left_to_right')

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
    accessibility_data: AccessibilityData11 | Any = Field(None, alias='accessibilityData', union_mode='left_to_right')

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

class Text6(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    runs: list[Run] | Any = Field(default=None, union_mode='left_to_right')

class ButtonRenderer3(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    style: str | Any = Field(default=None, union_mode='left_to_right')
    size: str | Any = Field(default=None, union_mode='left_to_right')
    is_disabled: bool | Any = Field(None, alias='isDisabled', union_mode='left_to_right')
    text: Text6 | Any = Field(default=None, union_mode='left_to_right')
    tracking_params: str | Any = Field(None, alias='trackingParams', union_mode='left_to_right')

class DismissButton(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    button_renderer: ButtonRenderer3 | Any = Field(None, alias='buttonRenderer', union_mode='left_to_right')

class HotkeyDialogRenderer(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    title: Title4 | Any = Field(default=None, union_mode='left_to_right')
    sections: list[Section] | Any = Field(default=None, union_mode='left_to_right')
    dismiss_button: DismissButton | Any = Field(None, alias='dismissButton', union_mode='left_to_right')
    tracking_params: str | Any = Field(None, alias='trackingParams', union_mode='left_to_right')

class HotkeyDialog(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    hotkey_dialog_renderer: HotkeyDialogRenderer | Any = Field(None, alias='hotkeyDialogRenderer', union_mode='left_to_right')

class WebCommandMetadata13(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    send_post: bool | Any = Field(None, alias='sendPost', union_mode='left_to_right')

class CommandMetadata13(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    web_command_metadata: WebCommandMetadata13 | Any = Field(None, alias='webCommandMetadata', union_mode='left_to_right')

class SignalAction(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    signal: str | Any = Field(default=None, union_mode='left_to_right')

class Action4(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    click_tracking_params: str | Any = Field(None, alias='clickTrackingParams', union_mode='left_to_right')
    signal_action: SignalAction | Any = Field(None, alias='signalAction', union_mode='left_to_right')

class SignalServiceEndpoint2(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    signal: str | Any = Field(default=None, union_mode='left_to_right')
    actions: list[Action4] | Any = Field(default=None, union_mode='left_to_right')

class Command(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    click_tracking_params: str | Any = Field(None, alias='clickTrackingParams', union_mode='left_to_right')
    command_metadata: CommandMetadata13 | Any = Field(None, alias='commandMetadata', union_mode='left_to_right')
    signal_service_endpoint: SignalServiceEndpoint2 | Any = Field(None, alias='signalServiceEndpoint', union_mode='left_to_right')

class ButtonRenderer4(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    tracking_params: str | Any = Field(None, alias='trackingParams', union_mode='left_to_right')
    command: Command | Any = Field(default=None, union_mode='left_to_right')

class BackButton(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    button_renderer: ButtonRenderer4 | Any = Field(None, alias='buttonRenderer', union_mode='left_to_right')

class CommandMetadata14(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    web_command_metadata: WebCommandMetadata13 | Any = Field(None, alias='webCommandMetadata', union_mode='left_to_right')

class Action5(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    click_tracking_params: str | Any = Field(None, alias='clickTrackingParams', union_mode='left_to_right')
    signal_action: SignalAction | Any = Field(None, alias='signalAction', union_mode='left_to_right')

class SignalServiceEndpoint3(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    signal: str | Any = Field(default=None, union_mode='left_to_right')
    actions: list[Action5] | Any = Field(default=None, union_mode='left_to_right')

class Command1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    click_tracking_params: str | Any = Field(None, alias='clickTrackingParams', union_mode='left_to_right')
    command_metadata: CommandMetadata14 | Any = Field(None, alias='commandMetadata', union_mode='left_to_right')
    signal_service_endpoint: SignalServiceEndpoint3 | Any = Field(None, alias='signalServiceEndpoint', union_mode='left_to_right')

class ButtonRenderer5(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    tracking_params: str | Any = Field(None, alias='trackingParams', union_mode='left_to_right')
    command: Command1 | Any = Field(default=None, union_mode='left_to_right')

class ForwardButton(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    button_renderer: ButtonRenderer5 | Any = Field(None, alias='buttonRenderer', union_mode='left_to_right')

class Text7(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    runs: list[Run] | Any = Field(default=None, union_mode='left_to_right')

class CommandMetadata15(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    web_command_metadata: WebCommandMetadata13 | Any = Field(None, alias='webCommandMetadata', union_mode='left_to_right')

class Action6(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    click_tracking_params: str | Any = Field(None, alias='clickTrackingParams', union_mode='left_to_right')
    signal_action: SignalAction | Any = Field(None, alias='signalAction', union_mode='left_to_right')

class SignalServiceEndpoint4(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    signal: str | Any = Field(default=None, union_mode='left_to_right')
    actions: list[Action6] | Any = Field(default=None, union_mode='left_to_right')

class Command2(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    click_tracking_params: str | Any = Field(None, alias='clickTrackingParams', union_mode='left_to_right')
    command_metadata: CommandMetadata15 | Any = Field(None, alias='commandMetadata', union_mode='left_to_right')
    signal_service_endpoint: SignalServiceEndpoint4 | Any = Field(None, alias='signalServiceEndpoint', union_mode='left_to_right')

class ButtonRenderer6(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    style: str | Any = Field(default=None, union_mode='left_to_right')
    size: str | Any = Field(default=None, union_mode='left_to_right')
    is_disabled: bool | Any = Field(None, alias='isDisabled', union_mode='left_to_right')
    text: Text7 | Any = Field(default=None, union_mode='left_to_right')
    tracking_params: str | Any = Field(None, alias='trackingParams', union_mode='left_to_right')
    command: Command2 | Any = Field(default=None, union_mode='left_to_right')

class A11ySkipNavigationButton(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    button_renderer: ButtonRenderer6 | Any = Field(None, alias='buttonRenderer', union_mode='left_to_right')

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

class Topbar(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    desktop_topbar_renderer: DesktopTopbarRenderer | Any = Field(None, alias='desktopTopbarRenderer', union_mode='left_to_right')

class Thumbnail3(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    url: str | Any = Field(default=None, union_mode='left_to_right')
    width: int | Any = Field(default=None, union_mode='left_to_right')
    height: int | Any = Field(default=None, union_mode='left_to_right')

class Thumbnail2(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    thumbnails: list[Thumbnail3] | Any = Field(default=None, union_mode='left_to_right')

class PlaylistVideoThumbnailRenderer(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    thumbnail: Thumbnail2 | Any = Field(default=None, union_mode='left_to_right')
    tracking_params: str | Any = Field(None, alias='trackingParams', union_mode='left_to_right')

class ThumbnailRenderer(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    playlist_video_thumbnail_renderer: PlaylistVideoThumbnailRenderer | Any = Field(None, alias='playlistVideoThumbnailRenderer', union_mode='left_to_right')

class Title6(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    simple_text: str | Any = Field(None, alias='simpleText', union_mode='left_to_right')

class Accessibility7(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    accessibility_data: AccessibilityData11 | Any = Field(None, alias='accessibilityData', union_mode='left_to_right')

class Stat(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    accessibility: Accessibility7 | Any = Field(default=None, union_mode='left_to_right')
    simple_text: str | Any = Field(None, alias='simpleText', union_mode='left_to_right')

class MetadataBadgeRenderer1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    style: str | Any = Field(default=None, union_mode='left_to_right')
    label: str | Any = Field(default=None, union_mode='left_to_right')
    tracking_params: str | Any = Field(None, alias='trackingParams', union_mode='left_to_right')
    accessibility_data: AccessibilityData11 | Any = Field(None, alias='accessibilityData', union_mode='left_to_right')

class Badge(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    metadata_badge_renderer: MetadataBadgeRenderer1 | Any = Field(None, alias='metadataBadgeRenderer', union_mode='left_to_right')

class Description1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    simple_text: str | Any = Field(None, alias='simpleText', union_mode='left_to_right')

class Accessibility8(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    accessibility_data: AccessibilityData11 | Any = Field(None, alias='accessibilityData', union_mode='left_to_right')

class Header2(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    accessibility: Accessibility8 | Any = Field(default=None, union_mode='left_to_right')
    simple_text: str | Any = Field(None, alias='simpleText', union_mode='left_to_right')

class Accessibility9(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    accessibility_data: AccessibilityData11 | Any = Field(None, alias='accessibilityData', union_mode='left_to_right')

class Subtitle1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    accessibility: Accessibility9 | Any = Field(default=None, union_mode='left_to_right')
    simple_text: str | Any = Field(None, alias='simpleText', union_mode='left_to_right')

class Text8(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    runs: list[Run] | Any = Field(default=None, union_mode='left_to_right')

class WebCommandMetadata16(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    url: str | Any = Field(default=None, union_mode='left_to_right')
    web_page_type: str | Any = Field(None, alias='webPageType', union_mode='left_to_right')
    root_ve: int | Any = Field(None, alias='rootVe', union_mode='left_to_right')

class CommandMetadata16(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    web_command_metadata: WebCommandMetadata16 | Any = Field(None, alias='webCommandMetadata', union_mode='left_to_right')

class LoggingContext2(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    vss_logging_context: VssLoggingContext | Any = Field(None, alias='vssLoggingContext', union_mode='left_to_right')

class WatchEndpoint2(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    video_id: str | Any = Field(None, alias='videoId', union_mode='left_to_right')
    playlist_id: str | Any = Field(None, alias='playlistId', union_mode='left_to_right')
    logging_context: LoggingContext2 | Any = Field(None, alias='loggingContext', union_mode='left_to_right')

class Command3(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    click_tracking_params: str | Any = Field(None, alias='clickTrackingParams', union_mode='left_to_right')
    command_metadata: CommandMetadata16 | Any = Field(None, alias='commandMetadata', union_mode='left_to_right')
    watch_endpoint: WatchEndpoint2 | Any = Field(None, alias='watchEndpoint', union_mode='left_to_right')

class ButtonRenderer7(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    style: str | Any = Field(default=None, union_mode='left_to_right')
    size: str | Any = Field(default=None, union_mode='left_to_right')
    is_disabled: bool | Any = Field(None, alias='isDisabled', union_mode='left_to_right')
    text: Text8 | Any = Field(default=None, union_mode='left_to_right')
    icon: Icon | Any = Field(default=None, union_mode='left_to_right')
    tracking_params: str | Any = Field(None, alias='trackingParams', union_mode='left_to_right')
    command: Command3 | Any = Field(default=None, union_mode='left_to_right')

class PrimaryActionButton(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    button_renderer: ButtonRenderer7 | Any = Field(None, alias='buttonRenderer', union_mode='left_to_right')

class TvfilmShowWatchForwardOverlayRenderer(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    header: Header2 | Any = Field(default=None, union_mode='left_to_right')
    title: Title6 | Any = Field(default=None, union_mode='left_to_right')
    subtitle: Subtitle1 | Any = Field(default=None, union_mode='left_to_right')
    primary_action_button: PrimaryActionButton | Any = Field(None, alias='primaryActionButton', union_mode='left_to_right')
    tracking_params: str | Any = Field(None, alias='trackingParams', union_mode='left_to_right')

class ThumbnailOverlay1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    tvfilm_show_watch_forward_overlay_renderer: TvfilmShowWatchForwardOverlayRenderer | Any = Field(None, alias='tvfilmShowWatchForwardOverlayRenderer', union_mode='left_to_right')

class PlaylistSidebarPrimaryInfoRenderer(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    thumbnail_renderer: ThumbnailRenderer | Any = Field(None, alias='thumbnailRenderer', union_mode='left_to_right')
    title: Title6 | Any = Field(default=None, union_mode='left_to_right')
    stats: list[Stat] | Any = Field(default=None, union_mode='left_to_right')
    badges: list[Badge] | Any = Field(default=None, union_mode='left_to_right')
    description: Description1 | Any = Field(default=None, union_mode='left_to_right')
    style: str | Any = Field(default=None, union_mode='left_to_right')
    thumbnail_overlays: list[ThumbnailOverlay1] | Any = Field(None, alias='thumbnailOverlays', union_mode='left_to_right')

class Item1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    playlist_sidebar_primary_info_renderer: PlaylistSidebarPrimaryInfoRenderer | Any = Field(None, alias='playlistSidebarPrimaryInfoRenderer', union_mode='left_to_right')

class PlaylistSidebarRenderer(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    items: list[Item1] | Any = Field(default=None, union_mode='left_to_right')
    tracking_params: str | Any = Field(None, alias='trackingParams', union_mode='left_to_right')

class Sidebar(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    playlist_sidebar_renderer: PlaylistSidebarRenderer | Any = Field(None, alias='playlistSidebarRenderer', union_mode='left_to_right')

class ShowsModel(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    response_context: ResponseContext | Any = Field(None, alias='responseContext', union_mode='left_to_right')
    contents: Contents | Any = Field(default=None, union_mode='left_to_right')
    tracking_params: str | Any = Field(None, alias='trackingParams', union_mode='left_to_right')
    topbar: Topbar | Any = Field(default=None, union_mode='left_to_right')
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
