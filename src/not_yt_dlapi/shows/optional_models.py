from typing import Any, Self
from pydantic import ModelWrapValidatorHandler, PrivateAttr, model_validator
from pydantic import BaseModel, ConfigDict, Field
from datetime import time, timedelta

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

class WebCommandMetadata(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    url: str | None = None
    web_page_type: str | None = Field(None, alias='webPageType')
    root_ve: int | None = Field(None, alias='rootVe')
    api_url: str | None = Field(None, alias='apiUrl')

class CommandMetadata(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    web_command_metadata: WebCommandMetadata | None = Field(None, alias='webCommandMetadata')

class BrowseEndpoint(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    browse_id: str | None = Field(None, alias='browseId')

class Endpoint(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    click_tracking_params: str | None = Field(None, alias='clickTrackingParams')
    command_metadata: CommandMetadata | None = Field(None, alias='commandMetadata')
    browse_endpoint: BrowseEndpoint | None = Field(None, alias='browseEndpoint')

class CommandMetadata1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    web_command_metadata: WebCommandMetadata | None = Field(None, alias='webCommandMetadata')

class BrowseEndpoint1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    browse_id: str | None = Field(None, alias='browseId')
    params: str | None = None

class NavigationEndpoint(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    click_tracking_params: str | None = Field(None, alias='clickTrackingParams')
    command_metadata: CommandMetadata1 | None = Field(None, alias='commandMetadata')
    browse_endpoint: BrowseEndpoint1 | None = Field(None, alias='browseEndpoint')

class AccessibilityData(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    label: str | None = None

class Accessibility(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    accessibility_data: AccessibilityData | None = Field(None, alias='accessibilityData')

class SubMenuItem(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    title: str | None = None
    selected: bool | None = None
    navigation_endpoint: NavigationEndpoint | None = Field(None, alias='navigationEndpoint')
    accessibility: Accessibility | None = None
    tracking_params: str | None = Field(None, alias='trackingParams')

class SortFilterSubMenuRenderer(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    sub_menu_items: list[SubMenuItem] | None = Field(None, alias='subMenuItems')
    tracking_params: str | None = Field(None, alias='trackingParams')

class Collection(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    sort_filter_sub_menu_renderer: SortFilterSubMenuRenderer | None = Field(None, alias='sortFilterSubMenuRenderer')

class Run(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    text: str | None = None

class Description(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    runs: list[Run] | None = None

class PlaylistShowMetadataRenderer(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    collection: Collection | None = None
    description: Description | None = None

class Thumbnail1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    url: str | None = None
    width: int | None = None
    height: int | None = None

class Thumbnail(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    thumbnails: list[Thumbnail1] | None = None

class Accessibility1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    accessibility_data: AccessibilityData | None = Field(None, alias='accessibilityData')

class Title(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    runs: list[Run] | None = None
    accessibility: Accessibility1 | None = None

class Index(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    simple_text: str | None = Field(None, alias='simpleText')

class Accessibility2(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    accessibility_data: AccessibilityData | None = Field(None, alias='accessibilityData')

class LengthText(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    accessibility: Accessibility2 | None = None
    simple_text: time | timedelta | None = Field(None, alias='simpleText')

class WebCommandMetadata2(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    ignore_navigation: bool | None = Field(None, alias='ignoreNavigation')
    url: str | None = None
    web_page_type: str | None = Field(None, alias='webPageType')
    root_ve: int | None = Field(None, alias='rootVe')

class CommandMetadata2(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    web_command_metadata: WebCommandMetadata2 | None = Field(None, alias='webCommandMetadata')

class Title1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    runs: list[Run] | None = None

class Content4(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    runs: list[Run] | None = None

class Text(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    simple_text: str | None = Field(None, alias='simpleText')

class WebCommandMetadata3(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    url: str | None = None
    web_page_type: str | None = Field(None, alias='webPageType')
    root_ve: int | None = Field(None, alias='rootVe')

class CommandMetadata3(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    web_command_metadata: WebCommandMetadata3 | None = Field(None, alias='webCommandMetadata')

class WebCommandMetadata4(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    url: str | None = None
    web_page_type: str | None = Field(None, alias='webPageType')
    root_ve: int | None = Field(None, alias='rootVe')
    api_url: str | None = Field(None, alias='apiUrl')

class CommandMetadata4(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    web_command_metadata: WebCommandMetadata4 | None = Field(None, alias='webCommandMetadata')

class NextEndpoint(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    click_tracking_params: str | None = Field(None, alias='clickTrackingParams')
    command_metadata: CommandMetadata4 | None = Field(None, alias='commandMetadata')
    browse_endpoint: BrowseEndpoint1 | None = Field(None, alias='browseEndpoint')

class SignInEndpoint(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    next_endpoint: NextEndpoint | None = Field(None, alias='nextEndpoint')

class NavigationEndpoint2(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    click_tracking_params: str | None = Field(None, alias='clickTrackingParams')
    command_metadata: CommandMetadata3 | None = Field(None, alias='commandMetadata')
    sign_in_endpoint: SignInEndpoint | None = Field(None, alias='signInEndpoint')

class ButtonRenderer(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    style: str | None = None
    size: str | None = None
    is_disabled: bool | None = Field(None, alias='isDisabled')
    text: Text | None = None
    navigation_endpoint: NavigationEndpoint2 | None = Field(None, alias='navigationEndpoint')
    tracking_params: str | None = Field(None, alias='trackingParams')

class Button(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    button_renderer: ButtonRenderer | None = Field(None, alias='buttonRenderer')

class ModalWithTitleAndButtonRenderer(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    title: Title1 | None = None
    content: Content4 | None = None
    button: Button | None = None

class Modal(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    modal_with_title_and_button_renderer: ModalWithTitleAndButtonRenderer | None = Field(None, alias='modalWithTitleAndButtonRenderer')

class ModalEndpoint(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    modal: Modal | None = None

class VssLoggingContext(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    serialized_context_data: str | None = Field(None, alias='serializedContextData')

class LoggingContext(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    vss_logging_context: VssLoggingContext | None = Field(None, alias='vssLoggingContext')

class WatchEndpoint(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    video_id: str | None = Field(None, alias='videoId')
    playlist_id: str | None = Field(None, alias='playlistId')
    index: int | None = None
    player_params: str | None = Field(None, alias='playerParams')
    logging_context: LoggingContext | None = Field(None, alias='loggingContext')

class NavigationEndpoint1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    click_tracking_params: str | None = Field(None, alias='clickTrackingParams')
    command_metadata: CommandMetadata2 | None = Field(None, alias='commandMetadata')
    modal_endpoint: ModalEndpoint | None = Field(None, alias='modalEndpoint')
    watch_endpoint: WatchEndpoint | None = Field(None, alias='watchEndpoint')

class Text1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    runs: list[Run] | None = None

class Icon(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    icon_type: str | None = Field(None, alias='iconType')

class Title2(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    content: str | None = None

class PanelHeaderViewModel(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    title: Title2 | None = None

class Header(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    panel_header_view_model: PanelHeaderViewModel | None = Field(None, alias='panelHeaderViewModel')

class Subtitle(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    content: str | None = None

class WebCommandMetadata5(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    url: str | None = None
    web_page_type: str | None = Field(None, alias='webPageType')
    root_ve: int | None = Field(None, alias='rootVe')

class CommandMetadata5(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    web_command_metadata: WebCommandMetadata5 | None = Field(None, alias='webCommandMetadata')

class LoggingContext1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    vss_logging_context: VssLoggingContext | None = Field(None, alias='vssLoggingContext')

class WatchEndpoint1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    video_id: str | None = Field(None, alias='videoId')
    playlist_id: str | None = Field(None, alias='playlistId')
    player_params: str | None = Field(None, alias='playerParams')
    logging_context: LoggingContext1 | None = Field(None, alias='loggingContext')

class InnertubeCommand(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    click_tracking_params: str | None = Field(None, alias='clickTrackingParams')
    command_metadata: CommandMetadata5 | None = Field(None, alias='commandMetadata')
    watch_endpoint: WatchEndpoint1 | None = Field(None, alias='watchEndpoint')

class OnTap(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    innertube_command: InnertubeCommand | None = Field(None, alias='innertubeCommand')

class CommandContext(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    on_tap: OnTap | None = Field(None, alias='onTap')

class RendererContext(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    command_context: CommandContext | None = Field(None, alias='commandContext')

class ListItemViewModel(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    title: Title2 | None = None
    subtitle: Subtitle | None = None
    renderer_context: RendererContext | None = Field(None, alias='rendererContext')

class ListItem(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    list_item_view_model: ListItemViewModel | None = Field(None, alias='listItemViewModel')

class ListViewModel(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    list_items: list[ListItem] | None = Field(None, alias='listItems')

class Content5(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    list_view_model: ListViewModel | None = Field(None, alias='listViewModel')

class SheetViewModel(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    header: Header | None = None
    content: Content5 | None = None

class InlineContent(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    sheet_view_model: SheetViewModel | None = Field(None, alias='sheetViewModel')

class PanelLoadingStrategy(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    inline_content: InlineContent | None = Field(None, alias='inlineContent')

class ShowSheetCommand(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    panel_loading_strategy: PanelLoadingStrategy | None = Field(None, alias='panelLoadingStrategy')

class NavigationEndpoint3(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    click_tracking_params: str | None = Field(None, alias='clickTrackingParams')
    show_sheet_command: ShowSheetCommand | None = Field(None, alias='showSheetCommand')

class MenuNavigationItemRenderer(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    text: Text1 | None = None
    icon: Icon | None = None
    navigation_endpoint: NavigationEndpoint3 | None = Field(None, alias='navigationEndpoint')
    tracking_params: str | None = Field(None, alias='trackingParams')

class Item(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    menu_navigation_item_renderer: MenuNavigationItemRenderer | None = Field(None, alias='menuNavigationItemRenderer')

class Accessibility3(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    accessibility_data: AccessibilityData | None = Field(None, alias='accessibilityData')

class MenuRenderer(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    items: list[Item] | None = None
    tracking_params: str | None = Field(None, alias='trackingParams')
    accessibility: Accessibility3 | None = None

class Menu(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    menu_renderer: MenuRenderer | None = Field(None, alias='menuRenderer')

class Accessibility4(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    accessibility_data: AccessibilityData | None = Field(None, alias='accessibilityData')

class Text2(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    accessibility: Accessibility4 | None = None
    simple_text: time | timedelta | None = Field(None, alias='simpleText')

class ThumbnailOverlayTimeStatusRenderer(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    text: Text2 | None = None
    style: str | None = None

class UntoggledIcon(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    icon_type: str | None = Field(None, alias='iconType')

class ToggledIcon(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    icon_type: str | None = Field(None, alias='iconType')

class WebCommandMetadata6(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    send_post: bool | None = Field(None, alias='sendPost')
    api_url: str | None = Field(None, alias='apiUrl')

class CommandMetadata6(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    web_command_metadata: WebCommandMetadata6 | None = Field(None, alias='webCommandMetadata')

class Action(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    added_video_id: str | None = Field(None, alias='addedVideoId')
    action: str | None = None

class PlaylistEditEndpoint(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    playlist_id: str | None = Field(None, alias='playlistId')
    actions: list[Action] | None = None

class CommandMetadata7(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    web_command_metadata: WebCommandMetadata6 | None = Field(None, alias='webCommandMetadata')

class CreatePlaylistServiceEndpoint(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    video_ids: list[str] | None = Field(None, alias='videoIds')
    params: str | None = None

class OnCreateListCommand(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    click_tracking_params: str | None = Field(None, alias='clickTrackingParams')
    command_metadata: CommandMetadata7 | None = Field(None, alias='commandMetadata')
    create_playlist_service_endpoint: CreatePlaylistServiceEndpoint | None = Field(None, alias='createPlaylistServiceEndpoint')

class AddToPlaylistCommand(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    open_miniplayer: bool | None = Field(None, alias='openMiniplayer')
    video_id: str | None = Field(None, alias='videoId')
    list_type: str | None = Field(None, alias='listType')
    on_create_list_command: OnCreateListCommand | None = Field(None, alias='onCreateListCommand')
    video_ids: list[str] | None = Field(None, alias='videoIds')

class Action1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    click_tracking_params: str | None = Field(None, alias='clickTrackingParams')
    add_to_playlist_command: AddToPlaylistCommand | None = Field(None, alias='addToPlaylistCommand')

class SignalServiceEndpoint(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    signal: str | None = None
    actions: list[Action1] | None = None

class UntoggledServiceEndpoint(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    click_tracking_params: str | None = Field(None, alias='clickTrackingParams')
    command_metadata: CommandMetadata6 | None = Field(None, alias='commandMetadata')
    playlist_edit_endpoint: PlaylistEditEndpoint | None = Field(None, alias='playlistEditEndpoint')
    signal_service_endpoint: SignalServiceEndpoint | None = Field(None, alias='signalServiceEndpoint')

class CommandMetadata8(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    web_command_metadata: WebCommandMetadata6 | None = Field(None, alias='webCommandMetadata')

class Action2(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    action: str | None = None
    removed_video_id: str | None = Field(None, alias='removedVideoId')

class PlaylistEditEndpoint1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    playlist_id: str | None = Field(None, alias='playlistId')
    actions: list[Action2] | None = None

class ToggledServiceEndpoint(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    click_tracking_params: str | None = Field(None, alias='clickTrackingParams')
    command_metadata: CommandMetadata8 | None = Field(None, alias='commandMetadata')
    playlist_edit_endpoint: PlaylistEditEndpoint1 | None = Field(None, alias='playlistEditEndpoint')

class UntoggledAccessibility(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    accessibility_data: AccessibilityData | None = Field(None, alias='accessibilityData')

class ToggledAccessibility(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    accessibility_data: AccessibilityData | None = Field(None, alias='accessibilityData')

class ThumbnailOverlayToggleButtonRenderer(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    is_toggled: bool | None = Field(None, alias='isToggled')
    untoggled_icon: UntoggledIcon | None = Field(None, alias='untoggledIcon')
    toggled_icon: ToggledIcon | None = Field(None, alias='toggledIcon')
    untoggled_tooltip: str | None = Field(None, alias='untoggledTooltip')
    toggled_tooltip: str | None = Field(None, alias='toggledTooltip')
    untoggled_service_endpoint: UntoggledServiceEndpoint | None = Field(None, alias='untoggledServiceEndpoint')
    toggled_service_endpoint: ToggledServiceEndpoint | None = Field(None, alias='toggledServiceEndpoint')
    untoggled_accessibility: UntoggledAccessibility | None = Field(None, alias='untoggledAccessibility')
    toggled_accessibility: ToggledAccessibility | None = Field(None, alias='toggledAccessibility')
    tracking_params: str | None = Field(None, alias='trackingParams')

class Text3(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    runs: list[Run] | None = None

class ThumbnailOverlayNowPlayingRenderer(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    text: Text3 | None = None

class ThumbnailOverlay(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    thumbnail_overlay_time_status_renderer: ThumbnailOverlayTimeStatusRenderer | None = Field(None, alias='thumbnailOverlayTimeStatusRenderer')
    thumbnail_overlay_toggle_button_renderer: ThumbnailOverlayToggleButtonRenderer | None = Field(None, alias='thumbnailOverlayToggleButtonRenderer')
    thumbnail_overlay_now_playing_renderer: ThumbnailOverlayNowPlayingRenderer | None = Field(None, alias='thumbnailOverlayNowPlayingRenderer')

class UpcomingEventText(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    simple_text: str | None = Field(None, alias='simpleText')

class UpcomingEventData(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    upcoming_event_text: UpcomingEventText | None = Field(None, alias='upcomingEventText')

class MetadataBadgeRenderer(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    style: str | None = None
    label: str | None = None
    tracking_params: str | None = Field(None, alias='trackingParams')
    accessibility_data: AccessibilityData | None = Field(None, alias='accessibilityData')

class BottomBadge(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    metadata_badge_renderer: MetadataBadgeRenderer | None = Field(None, alias='metadataBadgeRenderer')

class PlaylistVideoRenderer(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    video_id: str | None = Field(None, alias='videoId')
    thumbnail: Thumbnail | None = None
    title: Title | None = None
    index: Index | None = None
    length_text: LengthText | None = Field(None, alias='lengthText')
    navigation_endpoint: NavigationEndpoint1 | None = Field(None, alias='navigationEndpoint')
    length_seconds: str | None = Field(None, alias='lengthSeconds')
    tracking_params: str | None = Field(None, alias='trackingParams')
    is_playable: bool | None = Field(None, alias='isPlayable')
    menu: Menu | None = None
    thumbnail_overlays: list[ThumbnailOverlay] | None = Field(None, alias='thumbnailOverlays')
    upcoming_event_data: UpcomingEventData | None = Field(None, alias='upcomingEventData')
    bottom_badges: list[BottomBadge] | None = Field(None, alias='bottomBadges')

class Content3(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    playlist_video_renderer: PlaylistVideoRenderer | None = Field(None, alias='playlistVideoRenderer')

class PlaylistVideoListRenderer(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    contents: list[Content3] | None = None
    is_editable: bool | None = Field(None, alias='isEditable')
    can_reorder: bool | None = Field(None, alias='canReorder')
    tracking_params: str | None = Field(None, alias='trackingParams')
    target_id: str | None = Field(None, alias='targetId')

class Content2(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    playlist_show_metadata_renderer: PlaylistShowMetadataRenderer | None = Field(None, alias='playlistShowMetadataRenderer')
    playlist_video_list_renderer: PlaylistVideoListRenderer | None = Field(None, alias='playlistVideoListRenderer')

class ItemSectionRenderer(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    contents: list[Content2] | None = None
    tracking_params: str | None = Field(None, alias='trackingParams')

class Content1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    item_section_renderer: ItemSectionRenderer | None = Field(None, alias='itemSectionRenderer')

class SectionListRenderer(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    contents: list[Content1] | None = None
    tracking_params: str | None = Field(None, alias='trackingParams')
    target_id: str | None = Field(None, alias='targetId')

class Content(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    section_list_renderer: SectionListRenderer | None = Field(None, alias='sectionListRenderer')

class Accessibility5(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    accessibility_data: AccessibilityData | None = Field(None, alias='accessibilityData')

class TabRenderer(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    endpoint: Endpoint | None = None
    selected: bool | None = None
    content: Content | None = None
    tab_identifier: str | None = Field(None, alias='tabIdentifier')
    accessibility: Accessibility5 | None = None
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

class IconImage(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    icon_type: str | None = Field(None, alias='iconType')

class TooltipText(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    runs: list[Run] | None = None

class WebCommandMetadata9(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    url: str | None = None
    web_page_type: str | None = Field(None, alias='webPageType')
    root_ve: int | None = Field(None, alias='rootVe')
    api_url: str | None = Field(None, alias='apiUrl')

class CommandMetadata9(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    web_command_metadata: WebCommandMetadata9 | None = Field(None, alias='webCommandMetadata')

class BrowseEndpoint3(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    browse_id: str | None = Field(None, alias='browseId')

class Endpoint1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    click_tracking_params: str | None = Field(None, alias='clickTrackingParams')
    command_metadata: CommandMetadata9 | None = Field(None, alias='commandMetadata')
    browse_endpoint: BrowseEndpoint3 | None = Field(None, alias='browseEndpoint')

class TopbarLogoRenderer(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    icon_image: IconImage | None = Field(None, alias='iconImage')
    tooltip_text: TooltipText | None = Field(None, alias='tooltipText')
    endpoint: Endpoint1 | None = None
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

class Config(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    web_searchbox_config: WebSearchboxConfig | None = Field(None, alias='webSearchboxConfig')

class WebCommandMetadata10(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    url: str | None = None
    web_page_type: str | None = Field(None, alias='webPageType')
    root_ve: int | None = Field(None, alias='rootVe')

class CommandMetadata10(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    web_command_metadata: WebCommandMetadata10 | None = Field(None, alias='webCommandMetadata')

class SearchEndpoint1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    query: str | None = None
    params: str | None = None

class SearchEndpoint(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    click_tracking_params: str | None = Field(None, alias='clickTrackingParams')
    command_metadata: CommandMetadata10 | None = Field(None, alias='commandMetadata')
    search_endpoint: SearchEndpoint1 | None = Field(None, alias='searchEndpoint')

class AccessibilityData9(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    accessibility_data: AccessibilityData | None = Field(None, alias='accessibilityData')

class ButtonRenderer1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    style: str | None = None
    size: str | None = None
    is_disabled: bool | None = Field(None, alias='isDisabled')
    icon: Icon | None = None
    tracking_params: str | None = Field(None, alias='trackingParams')
    accessibility_data: AccessibilityData9 | None = Field(None, alias='accessibilityData')

class ClearButton(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    button_renderer: ButtonRenderer1 | None = Field(None, alias='buttonRenderer')

class Headline(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    content: str | None = None

class DialogHeaderViewModel(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    headline: Headline | None = None

class Header1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    dialog_header_view_model: DialogHeaderViewModel | None = Field(None, alias='dialogHeaderViewModel')

class ButtonViewModel(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    title: str | None = None
    style: str | None = None
    tracking_params: str | None = Field(None, alias='trackingParams')
    is_full_width: bool | None = Field(None, alias='isFullWidth')
    type: str | None = None

class PrimaryButton(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    button_view_model: ButtonViewModel | None = Field(None, alias='buttonViewModel')

class SecondaryButton(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    button_view_model: ButtonViewModel | None = Field(None, alias='buttonViewModel')

class PanelFooterViewModel(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    primary_button: PrimaryButton | None = Field(None, alias='primaryButton')
    secondary_button: SecondaryButton | None = Field(None, alias='secondaryButton')
    should_hide_divider: bool | None = Field(None, alias='shouldHideDivider')

class Footer(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    panel_footer_view_model: PanelFooterViewModel | None = Field(None, alias='panelFooterViewModel')

class Text4(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    content: str | None = None

class Paragraph(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    text: Text4 | None = None

class BasicContentViewModel(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    paragraphs: list[Paragraph] | None = None

class Content6(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    basic_content_view_model: BasicContentViewModel | None = Field(None, alias='basicContentViewModel')

class DialogViewModel(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    header: Header1 | None = None
    footer: Footer | None = None
    content: Content6 | None = None

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
    icon: Icon | None = None
    placeholder_text: PlaceholderText | None = Field(None, alias='placeholderText')
    config: Config | None = None
    tracking_params: str | None = Field(None, alias='trackingParams')
    search_endpoint: SearchEndpoint | None = Field(None, alias='searchEndpoint')
    clear_button: ClearButton | None = Field(None, alias='clearButton')
    show_image_source_dialog: ShowImageSourceDialog | None = Field(None, alias='showImageSourceDialog')
    disable_ai_appearance: bool | None = Field(None, alias='disableAiAppearance')

class Searchbox(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    fusion_searchbox_renderer: FusionSearchboxRenderer | None = Field(None, alias='fusionSearchboxRenderer')

class WebCommandMetadata11(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    send_post: bool | None = Field(None, alias='sendPost')
    api_url: str | None = Field(None, alias='apiUrl')

class CommandMetadata11(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    web_command_metadata: WebCommandMetadata11 | None = Field(None, alias='webCommandMetadata')

class MultiPageMenuRenderer(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    tracking_params: str | None = Field(None, alias='trackingParams')
    style: str | None = None
    show_loading_spinner: bool | None = Field(None, alias='showLoadingSpinner')

class Popup(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    multi_page_menu_renderer: MultiPageMenuRenderer | None = Field(None, alias='multiPageMenuRenderer')

class OpenPopupAction(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    popup: Popup | None = None
    popup_type: str | None = Field(None, alias='popupType')
    be_reused: bool | None = Field(None, alias='beReused')

class Action3(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    click_tracking_params: str | None = Field(None, alias='clickTrackingParams')
    open_popup_action: OpenPopupAction | None = Field(None, alias='openPopupAction')

class SignalServiceEndpoint1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    signal: str | None = None
    actions: list[Action3] | None = None

class MenuRequest(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    click_tracking_params: str | None = Field(None, alias='clickTrackingParams')
    command_metadata: CommandMetadata11 | None = Field(None, alias='commandMetadata')
    signal_service_endpoint: SignalServiceEndpoint1 | None = Field(None, alias='signalServiceEndpoint')

class AccessibilityData11(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    label: str | None = None

class Accessibility6(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    accessibility_data: AccessibilityData11 | None = Field(None, alias='accessibilityData')

class TopbarMenuButtonRenderer(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    icon: Icon | None = None
    menu_request: MenuRequest | None = Field(None, alias='menuRequest')
    tracking_params: str | None = Field(None, alias='trackingParams')
    accessibility: Accessibility6 | None = None
    tooltip: str | None = None
    style: str | None = None

class Text5(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    runs: list[Run] | None = None

class WebCommandMetadata12(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    url: str | None = None
    web_page_type: str | None = Field(None, alias='webPageType')
    root_ve: int | None = Field(None, alias='rootVe')

class CommandMetadata12(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    web_command_metadata: WebCommandMetadata12 | None = Field(None, alias='webCommandMetadata')

class SignInEndpoint1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    idam_tag: str | None = Field(None, alias='idamTag')

class NavigationEndpoint4(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    click_tracking_params: str | None = Field(None, alias='clickTrackingParams')
    command_metadata: CommandMetadata12 | None = Field(None, alias='commandMetadata')
    sign_in_endpoint: SignInEndpoint1 | None = Field(None, alias='signInEndpoint')

class ButtonRenderer2(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    style: str | None = None
    size: str | None = None
    text: Text5 | None = None
    icon: Icon | None = None
    navigation_endpoint: NavigationEndpoint4 | None = Field(None, alias='navigationEndpoint')
    tracking_params: str | None = Field(None, alias='trackingParams')
    target_id: str | None = Field(None, alias='targetId')

class TopbarButton(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    topbar_menu_button_renderer: TopbarMenuButtonRenderer | None = Field(None, alias='topbarMenuButtonRenderer')
    button_renderer: ButtonRenderer2 | None = Field(None, alias='buttonRenderer')

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
    accessibility_data: AccessibilityData11 | None = Field(None, alias='accessibilityData')

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

class Text6(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    runs: list[Run] | None = None

class ButtonRenderer3(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    style: str | None = None
    size: str | None = None
    is_disabled: bool | None = Field(None, alias='isDisabled')
    text: Text6 | None = None
    tracking_params: str | None = Field(None, alias='trackingParams')

class DismissButton(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    button_renderer: ButtonRenderer3 | None = Field(None, alias='buttonRenderer')

class HotkeyDialogRenderer(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    title: Title4 | None = None
    sections: list[Section] | None = None
    dismiss_button: DismissButton | None = Field(None, alias='dismissButton')
    tracking_params: str | None = Field(None, alias='trackingParams')

class HotkeyDialog(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    hotkey_dialog_renderer: HotkeyDialogRenderer | None = Field(None, alias='hotkeyDialogRenderer')

class WebCommandMetadata13(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    send_post: bool | None = Field(None, alias='sendPost')

class CommandMetadata13(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    web_command_metadata: WebCommandMetadata13 | None = Field(None, alias='webCommandMetadata')

class SignalAction(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    signal: str | None = None

class Action4(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    click_tracking_params: str | None = Field(None, alias='clickTrackingParams')
    signal_action: SignalAction | None = Field(None, alias='signalAction')

class SignalServiceEndpoint2(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    signal: str | None = None
    actions: list[Action4] | None = None

class Command(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    click_tracking_params: str | None = Field(None, alias='clickTrackingParams')
    command_metadata: CommandMetadata13 | None = Field(None, alias='commandMetadata')
    signal_service_endpoint: SignalServiceEndpoint2 | None = Field(None, alias='signalServiceEndpoint')

class ButtonRenderer4(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    tracking_params: str | None = Field(None, alias='trackingParams')
    command: Command | None = None

class BackButton(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    button_renderer: ButtonRenderer4 | None = Field(None, alias='buttonRenderer')

class CommandMetadata14(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    web_command_metadata: WebCommandMetadata13 | None = Field(None, alias='webCommandMetadata')

class Action5(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    click_tracking_params: str | None = Field(None, alias='clickTrackingParams')
    signal_action: SignalAction | None = Field(None, alias='signalAction')

class SignalServiceEndpoint3(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    signal: str | None = None
    actions: list[Action5] | None = None

class Command1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    click_tracking_params: str | None = Field(None, alias='clickTrackingParams')
    command_metadata: CommandMetadata14 | None = Field(None, alias='commandMetadata')
    signal_service_endpoint: SignalServiceEndpoint3 | None = Field(None, alias='signalServiceEndpoint')

class ButtonRenderer5(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    tracking_params: str | None = Field(None, alias='trackingParams')
    command: Command1 | None = None

class ForwardButton(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    button_renderer: ButtonRenderer5 | None = Field(None, alias='buttonRenderer')

class Text7(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    runs: list[Run] | None = None

class CommandMetadata15(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    web_command_metadata: WebCommandMetadata13 | None = Field(None, alias='webCommandMetadata')

class Action6(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    click_tracking_params: str | None = Field(None, alias='clickTrackingParams')
    signal_action: SignalAction | None = Field(None, alias='signalAction')

class SignalServiceEndpoint4(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    signal: str | None = None
    actions: list[Action6] | None = None

class Command2(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    click_tracking_params: str | None = Field(None, alias='clickTrackingParams')
    command_metadata: CommandMetadata15 | None = Field(None, alias='commandMetadata')
    signal_service_endpoint: SignalServiceEndpoint4 | None = Field(None, alias='signalServiceEndpoint')

class ButtonRenderer6(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    style: str | None = None
    size: str | None = None
    is_disabled: bool | None = Field(None, alias='isDisabled')
    text: Text7 | None = None
    tracking_params: str | None = Field(None, alias='trackingParams')
    command: Command2 | None = None

class A11ySkipNavigationButton(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    button_renderer: ButtonRenderer6 | None = Field(None, alias='buttonRenderer')

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

class Topbar(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    desktop_topbar_renderer: DesktopTopbarRenderer | None = Field(None, alias='desktopTopbarRenderer')

class Thumbnail3(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    url: str | None = None
    width: int | None = None
    height: int | None = None

class Thumbnail2(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    thumbnails: list[Thumbnail3] | None = None

class PlaylistVideoThumbnailRenderer(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    thumbnail: Thumbnail2 | None = None
    tracking_params: str | None = Field(None, alias='trackingParams')

class ThumbnailRenderer(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    playlist_video_thumbnail_renderer: PlaylistVideoThumbnailRenderer | None = Field(None, alias='playlistVideoThumbnailRenderer')

class Title6(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    simple_text: str | None = Field(None, alias='simpleText')

class Accessibility7(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    accessibility_data: AccessibilityData11 | None = Field(None, alias='accessibilityData')

class Stat(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    accessibility: Accessibility7 | None = None
    simple_text: str | None = Field(None, alias='simpleText')

class MetadataBadgeRenderer1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    style: str | None = None
    label: str | None = None
    tracking_params: str | None = Field(None, alias='trackingParams')
    accessibility_data: AccessibilityData11 | None = Field(None, alias='accessibilityData')

class Badge(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    metadata_badge_renderer: MetadataBadgeRenderer1 | None = Field(None, alias='metadataBadgeRenderer')

class Description1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    simple_text: str | None = Field(None, alias='simpleText')

class Accessibility8(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    accessibility_data: AccessibilityData11 | None = Field(None, alias='accessibilityData')

class Header2(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    accessibility: Accessibility8 | None = None
    simple_text: str | None = Field(None, alias='simpleText')

class Accessibility9(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    accessibility_data: AccessibilityData11 | None = Field(None, alias='accessibilityData')

class Subtitle1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    accessibility: Accessibility9 | None = None
    simple_text: str | None = Field(None, alias='simpleText')

class Text8(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    runs: list[Run] | None = None

class WebCommandMetadata16(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    url: str | None = None
    web_page_type: str | None = Field(None, alias='webPageType')
    root_ve: int | None = Field(None, alias='rootVe')

class CommandMetadata16(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    web_command_metadata: WebCommandMetadata16 | None = Field(None, alias='webCommandMetadata')

class LoggingContext2(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    vss_logging_context: VssLoggingContext | None = Field(None, alias='vssLoggingContext')

class WatchEndpoint2(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    video_id: str | None = Field(None, alias='videoId')
    playlist_id: str | None = Field(None, alias='playlistId')
    logging_context: LoggingContext2 | None = Field(None, alias='loggingContext')

class Command3(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    click_tracking_params: str | None = Field(None, alias='clickTrackingParams')
    command_metadata: CommandMetadata16 | None = Field(None, alias='commandMetadata')
    watch_endpoint: WatchEndpoint2 | None = Field(None, alias='watchEndpoint')

class ButtonRenderer7(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    style: str | None = None
    size: str | None = None
    is_disabled: bool | None = Field(None, alias='isDisabled')
    text: Text8 | None = None
    icon: Icon | None = None
    tracking_params: str | None = Field(None, alias='trackingParams')
    command: Command3 | None = None

class PrimaryActionButton(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    button_renderer: ButtonRenderer7 | None = Field(None, alias='buttonRenderer')

class TvfilmShowWatchForwardOverlayRenderer(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    header: Header2 | None = None
    title: Title6 | None = None
    subtitle: Subtitle1 | None = None
    primary_action_button: PrimaryActionButton | None = Field(None, alias='primaryActionButton')
    tracking_params: str | None = Field(None, alias='trackingParams')

class ThumbnailOverlay1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    tvfilm_show_watch_forward_overlay_renderer: TvfilmShowWatchForwardOverlayRenderer | None = Field(None, alias='tvfilmShowWatchForwardOverlayRenderer')

class PlaylistSidebarPrimaryInfoRenderer(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    thumbnail_renderer: ThumbnailRenderer | None = Field(None, alias='thumbnailRenderer')
    title: Title6 | None = None
    stats: list[Stat] | None = None
    badges: list[Badge] | None = None
    description: Description1 | None = None
    style: str | None = None
    thumbnail_overlays: list[ThumbnailOverlay1] | None = Field(None, alias='thumbnailOverlays')

class Item1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    playlist_sidebar_primary_info_renderer: PlaylistSidebarPrimaryInfoRenderer | None = Field(None, alias='playlistSidebarPrimaryInfoRenderer')

class PlaylistSidebarRenderer(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    items: list[Item1] | None = None
    tracking_params: str | None = Field(None, alias='trackingParams')

class Sidebar(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    playlist_sidebar_renderer: PlaylistSidebarRenderer | None = Field(None, alias='playlistSidebarRenderer')

class ShowsModel(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    response_context: ResponseContext | None = Field(None, alias='responseContext')
    contents: Contents | None = None
    tracking_params: str | None = Field(None, alias='trackingParams')
    topbar: Topbar | None = None
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
