from typing import Any, Self
from pydantic import ModelWrapValidatorHandler, PrivateAttr, model_validator
from pydantic import ConfigDict
from pydantic import BaseModel, Field
from datetime import time, timedelta

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

class WebCommandMetadata(BaseModel):
    model_config = ConfigDict(defer_build=True)
    url: str
    web_page_type: str = Field(..., alias='webPageType')
    root_ve: int = Field(..., alias='rootVe')
    api_url: str = Field(..., alias='apiUrl')

class CommandMetadata(BaseModel):
    model_config = ConfigDict(defer_build=True)
    web_command_metadata: WebCommandMetadata = Field(..., alias='webCommandMetadata')

class BrowseEndpoint(BaseModel):
    model_config = ConfigDict(defer_build=True)
    browse_id: str = Field(..., alias='browseId')

class Endpoint(BaseModel):
    model_config = ConfigDict(defer_build=True)
    click_tracking_params: str = Field(..., alias='clickTrackingParams')
    command_metadata: CommandMetadata = Field(..., alias='commandMetadata')
    browse_endpoint: BrowseEndpoint = Field(..., alias='browseEndpoint')

class CommandMetadata1(BaseModel):
    model_config = ConfigDict(defer_build=True)
    web_command_metadata: WebCommandMetadata = Field(..., alias='webCommandMetadata')

class BrowseEndpoint1(BaseModel):
    model_config = ConfigDict(defer_build=True)
    browse_id: str = Field(..., alias='browseId')
    params: str

class NavigationEndpoint(BaseModel):
    model_config = ConfigDict(defer_build=True)
    click_tracking_params: str = Field(..., alias='clickTrackingParams')
    command_metadata: CommandMetadata1 = Field(..., alias='commandMetadata')
    browse_endpoint: BrowseEndpoint1 = Field(..., alias='browseEndpoint')

class AccessibilityData(BaseModel):
    model_config = ConfigDict(defer_build=True)
    label: str

class Accessibility(BaseModel):
    model_config = ConfigDict(defer_build=True)
    accessibility_data: AccessibilityData = Field(..., alias='accessibilityData')

class SubMenuItem(BaseModel):
    model_config = ConfigDict(defer_build=True)
    title: str
    selected: bool | None = None
    navigation_endpoint: NavigationEndpoint = Field(..., alias='navigationEndpoint')
    accessibility: Accessibility
    tracking_params: str = Field(..., alias='trackingParams')

class SortFilterSubMenuRenderer(BaseModel):
    model_config = ConfigDict(defer_build=True)
    sub_menu_items: list[SubMenuItem] = Field(..., alias='subMenuItems')
    tracking_params: str = Field(..., alias='trackingParams')

class Collection(BaseModel):
    model_config = ConfigDict(defer_build=True)
    sort_filter_sub_menu_renderer: SortFilterSubMenuRenderer = Field(..., alias='sortFilterSubMenuRenderer')

class Run(BaseModel):
    model_config = ConfigDict(defer_build=True)
    text: str

class Description(BaseModel):
    model_config = ConfigDict(defer_build=True)
    runs: list[Run]

class PlaylistShowMetadataRenderer(BaseModel):
    model_config = ConfigDict(defer_build=True)
    collection: Collection
    description: Description

class Thumbnail1(BaseModel):
    model_config = ConfigDict(defer_build=True)
    url: str
    width: int
    height: int

class Thumbnail(BaseModel):
    model_config = ConfigDict(defer_build=True)
    thumbnails: list[Thumbnail1]

class Accessibility1(BaseModel):
    model_config = ConfigDict(defer_build=True)
    accessibility_data: AccessibilityData = Field(..., alias='accessibilityData')

class Title(BaseModel):
    model_config = ConfigDict(defer_build=True)
    runs: list[Run]
    accessibility: Accessibility1

class Index(BaseModel):
    model_config = ConfigDict(defer_build=True)
    simple_text: str = Field(..., alias='simpleText')

class Accessibility2(BaseModel):
    model_config = ConfigDict(defer_build=True)
    accessibility_data: AccessibilityData = Field(..., alias='accessibilityData')

class LengthText(BaseModel):
    model_config = ConfigDict(defer_build=True)
    accessibility: Accessibility2
    simple_text: time | timedelta = Field(..., alias='simpleText')

class WebCommandMetadata2(BaseModel):
    model_config = ConfigDict(defer_build=True)
    ignore_navigation: bool | None = Field(None, alias='ignoreNavigation')
    url: str | None = None
    web_page_type: str | None = Field(None, alias='webPageType')
    root_ve: int | None = Field(None, alias='rootVe')

class CommandMetadata2(BaseModel):
    model_config = ConfigDict(defer_build=True)
    web_command_metadata: WebCommandMetadata2 = Field(..., alias='webCommandMetadata')

class Title1(BaseModel):
    model_config = ConfigDict(defer_build=True)
    runs: list[Run]

class Content4(BaseModel):
    model_config = ConfigDict(defer_build=True)
    runs: list[Run]

class Text(BaseModel):
    model_config = ConfigDict(defer_build=True)
    simple_text: str = Field(..., alias='simpleText')

class WebCommandMetadata3(BaseModel):
    model_config = ConfigDict(defer_build=True)
    url: str
    web_page_type: str = Field(..., alias='webPageType')
    root_ve: int = Field(..., alias='rootVe')

class CommandMetadata3(BaseModel):
    model_config = ConfigDict(defer_build=True)
    web_command_metadata: WebCommandMetadata3 = Field(..., alias='webCommandMetadata')

class WebCommandMetadata4(BaseModel):
    model_config = ConfigDict(defer_build=True)
    url: str
    web_page_type: str = Field(..., alias='webPageType')
    root_ve: int = Field(..., alias='rootVe')
    api_url: str = Field(..., alias='apiUrl')

class CommandMetadata4(BaseModel):
    model_config = ConfigDict(defer_build=True)
    web_command_metadata: WebCommandMetadata4 = Field(..., alias='webCommandMetadata')

class BrowseEndpoint2(BaseModel):
    model_config = ConfigDict(defer_build=True)
    browse_id: str = Field(..., alias='browseId')
    params: str | None = None

class NextEndpoint(BaseModel):
    model_config = ConfigDict(defer_build=True)
    click_tracking_params: str = Field(..., alias='clickTrackingParams')
    command_metadata: CommandMetadata4 = Field(..., alias='commandMetadata')
    browse_endpoint: BrowseEndpoint2 = Field(..., alias='browseEndpoint')

class SignInEndpoint(BaseModel):
    model_config = ConfigDict(defer_build=True)
    next_endpoint: NextEndpoint = Field(..., alias='nextEndpoint')

class NavigationEndpoint2(BaseModel):
    model_config = ConfigDict(defer_build=True)
    click_tracking_params: str = Field(..., alias='clickTrackingParams')
    command_metadata: CommandMetadata3 = Field(..., alias='commandMetadata')
    sign_in_endpoint: SignInEndpoint = Field(..., alias='signInEndpoint')

class ButtonRenderer(BaseModel):
    model_config = ConfigDict(defer_build=True)
    style: str
    size: str
    is_disabled: bool = Field(..., alias='isDisabled')
    text: Text
    navigation_endpoint: NavigationEndpoint2 = Field(..., alias='navigationEndpoint')
    tracking_params: str = Field(..., alias='trackingParams')

class Button(BaseModel):
    model_config = ConfigDict(defer_build=True)
    button_renderer: ButtonRenderer = Field(..., alias='buttonRenderer')

class ModalWithTitleAndButtonRenderer(BaseModel):
    model_config = ConfigDict(defer_build=True)
    title: Title1
    content: Content4
    button: Button

class Modal(BaseModel):
    model_config = ConfigDict(defer_build=True)
    modal_with_title_and_button_renderer: ModalWithTitleAndButtonRenderer = Field(..., alias='modalWithTitleAndButtonRenderer')

class ModalEndpoint(BaseModel):
    model_config = ConfigDict(defer_build=True)
    modal: Modal

class VssLoggingContext(BaseModel):
    model_config = ConfigDict(defer_build=True)
    serialized_context_data: str = Field(..., alias='serializedContextData')

class LoggingContext(BaseModel):
    model_config = ConfigDict(defer_build=True)
    vss_logging_context: VssLoggingContext = Field(..., alias='vssLoggingContext')

class WatchEndpoint(BaseModel):
    model_config = ConfigDict(defer_build=True)
    video_id: str = Field(..., alias='videoId')
    playlist_id: str = Field(..., alias='playlistId')
    index: int
    player_params: str = Field(..., alias='playerParams')
    logging_context: LoggingContext = Field(..., alias='loggingContext')

class NavigationEndpoint1(BaseModel):
    model_config = ConfigDict(defer_build=True)
    click_tracking_params: str = Field(..., alias='clickTrackingParams')
    command_metadata: CommandMetadata2 = Field(..., alias='commandMetadata')
    modal_endpoint: ModalEndpoint | None = Field(None, alias='modalEndpoint')
    watch_endpoint: WatchEndpoint | None = Field(None, alias='watchEndpoint')

class Text1(BaseModel):
    model_config = ConfigDict(defer_build=True)
    runs: list[Run]

class Icon(BaseModel):
    model_config = ConfigDict(defer_build=True)
    icon_type: str = Field(..., alias='iconType')

class Title2(BaseModel):
    model_config = ConfigDict(defer_build=True)
    content: str

class PanelHeaderViewModel(BaseModel):
    model_config = ConfigDict(defer_build=True)
    title: Title2

class Header(BaseModel):
    model_config = ConfigDict(defer_build=True)
    panel_header_view_model: PanelHeaderViewModel = Field(..., alias='panelHeaderViewModel')

class Subtitle(BaseModel):
    model_config = ConfigDict(defer_build=True)
    content: str

class WebCommandMetadata5(BaseModel):
    model_config = ConfigDict(defer_build=True)
    url: str
    web_page_type: str = Field(..., alias='webPageType')
    root_ve: int = Field(..., alias='rootVe')

class CommandMetadata5(BaseModel):
    model_config = ConfigDict(defer_build=True)
    web_command_metadata: WebCommandMetadata5 = Field(..., alias='webCommandMetadata')

class LoggingContext1(BaseModel):
    model_config = ConfigDict(defer_build=True)
    vss_logging_context: VssLoggingContext = Field(..., alias='vssLoggingContext')

class WatchEndpoint1(BaseModel):
    model_config = ConfigDict(defer_build=True)
    video_id: str = Field(..., alias='videoId')
    playlist_id: str = Field(..., alias='playlistId')
    player_params: str = Field(..., alias='playerParams')
    logging_context: LoggingContext1 = Field(..., alias='loggingContext')

class InnertubeCommand(BaseModel):
    model_config = ConfigDict(defer_build=True)
    click_tracking_params: str = Field(..., alias='clickTrackingParams')
    command_metadata: CommandMetadata5 = Field(..., alias='commandMetadata')
    watch_endpoint: WatchEndpoint1 = Field(..., alias='watchEndpoint')

class OnTap(BaseModel):
    model_config = ConfigDict(defer_build=True)
    innertube_command: InnertubeCommand = Field(..., alias='innertubeCommand')

class CommandContext(BaseModel):
    model_config = ConfigDict(defer_build=True)
    on_tap: OnTap = Field(..., alias='onTap')

class RendererContext(BaseModel):
    model_config = ConfigDict(defer_build=True)
    command_context: CommandContext = Field(..., alias='commandContext')

class ListItemViewModel(BaseModel):
    model_config = ConfigDict(defer_build=True)
    title: Title2
    subtitle: Subtitle
    renderer_context: RendererContext = Field(..., alias='rendererContext')

class ListItem(BaseModel):
    model_config = ConfigDict(defer_build=True)
    list_item_view_model: ListItemViewModel = Field(..., alias='listItemViewModel')

class ListViewModel(BaseModel):
    model_config = ConfigDict(defer_build=True)
    list_items: list[ListItem] = Field(..., alias='listItems')

class Content5(BaseModel):
    model_config = ConfigDict(defer_build=True)
    list_view_model: ListViewModel = Field(..., alias='listViewModel')

class SheetViewModel(BaseModel):
    model_config = ConfigDict(defer_build=True)
    header: Header
    content: Content5

class InlineContent(BaseModel):
    model_config = ConfigDict(defer_build=True)
    sheet_view_model: SheetViewModel = Field(..., alias='sheetViewModel')

class PanelLoadingStrategy(BaseModel):
    model_config = ConfigDict(defer_build=True)
    inline_content: InlineContent = Field(..., alias='inlineContent')

class ShowSheetCommand(BaseModel):
    model_config = ConfigDict(defer_build=True)
    panel_loading_strategy: PanelLoadingStrategy = Field(..., alias='panelLoadingStrategy')

class NavigationEndpoint3(BaseModel):
    model_config = ConfigDict(defer_build=True)
    click_tracking_params: str = Field(..., alias='clickTrackingParams')
    show_sheet_command: ShowSheetCommand = Field(..., alias='showSheetCommand')

class MenuNavigationItemRenderer(BaseModel):
    model_config = ConfigDict(defer_build=True)
    text: Text1
    icon: Icon
    navigation_endpoint: NavigationEndpoint3 = Field(..., alias='navigationEndpoint')
    tracking_params: str = Field(..., alias='trackingParams')

class Item(BaseModel):
    model_config = ConfigDict(defer_build=True)
    menu_navigation_item_renderer: MenuNavigationItemRenderer = Field(..., alias='menuNavigationItemRenderer')

class Accessibility3(BaseModel):
    model_config = ConfigDict(defer_build=True)
    accessibility_data: AccessibilityData = Field(..., alias='accessibilityData')

class MenuRenderer(BaseModel):
    model_config = ConfigDict(defer_build=True)
    items: list[Item]
    tracking_params: str = Field(..., alias='trackingParams')
    accessibility: Accessibility3

class Menu(BaseModel):
    model_config = ConfigDict(defer_build=True)
    menu_renderer: MenuRenderer = Field(..., alias='menuRenderer')

class Accessibility4(BaseModel):
    model_config = ConfigDict(defer_build=True)
    accessibility_data: AccessibilityData = Field(..., alias='accessibilityData')

class Text2(BaseModel):
    model_config = ConfigDict(defer_build=True)
    accessibility: Accessibility4
    simple_text: time | timedelta = Field(..., alias='simpleText')

class ThumbnailOverlayTimeStatusRenderer(BaseModel):
    model_config = ConfigDict(defer_build=True)
    text: Text2
    style: str

class UntoggledIcon(BaseModel):
    model_config = ConfigDict(defer_build=True)
    icon_type: str = Field(..., alias='iconType')

class ToggledIcon(BaseModel):
    model_config = ConfigDict(defer_build=True)
    icon_type: str = Field(..., alias='iconType')

class WebCommandMetadata6(BaseModel):
    model_config = ConfigDict(defer_build=True)
    send_post: bool = Field(..., alias='sendPost')
    api_url: str | None = Field(None, alias='apiUrl')

class CommandMetadata6(BaseModel):
    model_config = ConfigDict(defer_build=True)
    web_command_metadata: WebCommandMetadata6 = Field(..., alias='webCommandMetadata')

class Action(BaseModel):
    model_config = ConfigDict(defer_build=True)
    added_video_id: str = Field(..., alias='addedVideoId')
    action: str

class PlaylistEditEndpoint(BaseModel):
    model_config = ConfigDict(defer_build=True)
    playlist_id: str = Field(..., alias='playlistId')
    actions: list[Action]

class WebCommandMetadata7(BaseModel):
    model_config = ConfigDict(defer_build=True)
    send_post: bool = Field(..., alias='sendPost')
    api_url: str = Field(..., alias='apiUrl')

class CommandMetadata7(BaseModel):
    model_config = ConfigDict(defer_build=True)
    web_command_metadata: WebCommandMetadata7 = Field(..., alias='webCommandMetadata')

class CreatePlaylistServiceEndpoint(BaseModel):
    model_config = ConfigDict(defer_build=True)
    video_ids: list[str] = Field(..., alias='videoIds')
    params: str

class OnCreateListCommand(BaseModel):
    model_config = ConfigDict(defer_build=True)
    click_tracking_params: str = Field(..., alias='clickTrackingParams')
    command_metadata: CommandMetadata7 = Field(..., alias='commandMetadata')
    create_playlist_service_endpoint: CreatePlaylistServiceEndpoint = Field(..., alias='createPlaylistServiceEndpoint')

class AddToPlaylistCommand(BaseModel):
    model_config = ConfigDict(defer_build=True)
    open_miniplayer: bool = Field(..., alias='openMiniplayer')
    video_id: str = Field(..., alias='videoId')
    list_type: str = Field(..., alias='listType')
    on_create_list_command: OnCreateListCommand = Field(..., alias='onCreateListCommand')
    video_ids: list[str] = Field(..., alias='videoIds')

class Action1(BaseModel):
    model_config = ConfigDict(defer_build=True)
    click_tracking_params: str = Field(..., alias='clickTrackingParams')
    add_to_playlist_command: AddToPlaylistCommand = Field(..., alias='addToPlaylistCommand')

class SignalServiceEndpoint(BaseModel):
    model_config = ConfigDict(defer_build=True)
    signal: str
    actions: list[Action1]

class UntoggledServiceEndpoint(BaseModel):
    model_config = ConfigDict(defer_build=True)
    click_tracking_params: str = Field(..., alias='clickTrackingParams')
    command_metadata: CommandMetadata6 = Field(..., alias='commandMetadata')
    playlist_edit_endpoint: PlaylistEditEndpoint | None = Field(None, alias='playlistEditEndpoint')
    signal_service_endpoint: SignalServiceEndpoint | None = Field(None, alias='signalServiceEndpoint')

class CommandMetadata8(BaseModel):
    model_config = ConfigDict(defer_build=True)
    web_command_metadata: WebCommandMetadata7 = Field(..., alias='webCommandMetadata')

class Action2(BaseModel):
    model_config = ConfigDict(defer_build=True)
    action: str
    removed_video_id: str = Field(..., alias='removedVideoId')

class PlaylistEditEndpoint1(BaseModel):
    model_config = ConfigDict(defer_build=True)
    playlist_id: str = Field(..., alias='playlistId')
    actions: list[Action2]

class ToggledServiceEndpoint(BaseModel):
    model_config = ConfigDict(defer_build=True)
    click_tracking_params: str = Field(..., alias='clickTrackingParams')
    command_metadata: CommandMetadata8 = Field(..., alias='commandMetadata')
    playlist_edit_endpoint: PlaylistEditEndpoint1 = Field(..., alias='playlistEditEndpoint')

class UntoggledAccessibility(BaseModel):
    model_config = ConfigDict(defer_build=True)
    accessibility_data: AccessibilityData = Field(..., alias='accessibilityData')

class ToggledAccessibility(BaseModel):
    model_config = ConfigDict(defer_build=True)
    accessibility_data: AccessibilityData = Field(..., alias='accessibilityData')

class ThumbnailOverlayToggleButtonRenderer(BaseModel):
    model_config = ConfigDict(defer_build=True)
    is_toggled: bool | None = Field(None, alias='isToggled')
    untoggled_icon: UntoggledIcon = Field(..., alias='untoggledIcon')
    toggled_icon: ToggledIcon = Field(..., alias='toggledIcon')
    untoggled_tooltip: str = Field(..., alias='untoggledTooltip')
    toggled_tooltip: str = Field(..., alias='toggledTooltip')
    untoggled_service_endpoint: UntoggledServiceEndpoint = Field(..., alias='untoggledServiceEndpoint')
    toggled_service_endpoint: ToggledServiceEndpoint | None = Field(None, alias='toggledServiceEndpoint')
    untoggled_accessibility: UntoggledAccessibility = Field(..., alias='untoggledAccessibility')
    toggled_accessibility: ToggledAccessibility = Field(..., alias='toggledAccessibility')
    tracking_params: str = Field(..., alias='trackingParams')

class Text3(BaseModel):
    model_config = ConfigDict(defer_build=True)
    runs: list[Run]

class ThumbnailOverlayNowPlayingRenderer(BaseModel):
    model_config = ConfigDict(defer_build=True)
    text: Text3

class ThumbnailOverlay(BaseModel):
    model_config = ConfigDict(defer_build=True)
    thumbnail_overlay_time_status_renderer: ThumbnailOverlayTimeStatusRenderer | None = Field(None, alias='thumbnailOverlayTimeStatusRenderer')
    thumbnail_overlay_toggle_button_renderer: ThumbnailOverlayToggleButtonRenderer | None = Field(None, alias='thumbnailOverlayToggleButtonRenderer')
    thumbnail_overlay_now_playing_renderer: ThumbnailOverlayNowPlayingRenderer | None = Field(None, alias='thumbnailOverlayNowPlayingRenderer')

class UpcomingEventText(BaseModel):
    model_config = ConfigDict(defer_build=True)
    simple_text: str = Field(..., alias='simpleText')

class UpcomingEventData(BaseModel):
    model_config = ConfigDict(defer_build=True)
    upcoming_event_text: UpcomingEventText = Field(..., alias='upcomingEventText')

class MetadataBadgeRenderer(BaseModel):
    model_config = ConfigDict(defer_build=True)
    style: str
    label: str
    tracking_params: str = Field(..., alias='trackingParams')
    accessibility_data: AccessibilityData = Field(..., alias='accessibilityData')

class BottomBadge(BaseModel):
    model_config = ConfigDict(defer_build=True)
    metadata_badge_renderer: MetadataBadgeRenderer = Field(..., alias='metadataBadgeRenderer')

class PlaylistVideoRenderer(BaseModel):
    model_config = ConfigDict(defer_build=True)
    video_id: str = Field(..., alias='videoId')
    thumbnail: Thumbnail
    title: Title
    index: Index
    length_text: LengthText = Field(..., alias='lengthText')
    navigation_endpoint: NavigationEndpoint1 = Field(..., alias='navigationEndpoint')
    length_seconds: str = Field(..., alias='lengthSeconds')
    tracking_params: str = Field(..., alias='trackingParams')
    is_playable: bool = Field(..., alias='isPlayable')
    menu: Menu
    thumbnail_overlays: list[ThumbnailOverlay] = Field(..., alias='thumbnailOverlays')
    upcoming_event_data: UpcomingEventData = Field(..., alias='upcomingEventData')
    bottom_badges: list[BottomBadge] = Field(..., alias='bottomBadges')

class Content3(BaseModel):
    model_config = ConfigDict(defer_build=True)
    playlist_video_renderer: PlaylistVideoRenderer = Field(..., alias='playlistVideoRenderer')

class PlaylistVideoListRenderer(BaseModel):
    model_config = ConfigDict(defer_build=True)
    contents: list[Content3]
    is_editable: bool = Field(..., alias='isEditable')
    can_reorder: bool = Field(..., alias='canReorder')
    tracking_params: str = Field(..., alias='trackingParams')
    target_id: str = Field(..., alias='targetId')

class Content2(BaseModel):
    model_config = ConfigDict(defer_build=True)
    playlist_show_metadata_renderer: PlaylistShowMetadataRenderer | None = Field(None, alias='playlistShowMetadataRenderer')
    playlist_video_list_renderer: PlaylistVideoListRenderer | None = Field(None, alias='playlistVideoListRenderer')

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

class Content(BaseModel):
    model_config = ConfigDict(defer_build=True)
    section_list_renderer: SectionListRenderer = Field(..., alias='sectionListRenderer')

class Accessibility5(BaseModel):
    model_config = ConfigDict(defer_build=True)
    accessibility_data: AccessibilityData = Field(..., alias='accessibilityData')

class TabRenderer(BaseModel):
    model_config = ConfigDict(defer_build=True)
    endpoint: Endpoint
    selected: bool
    content: Content
    tab_identifier: str = Field(..., alias='tabIdentifier')
    accessibility: Accessibility5
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

class IconImage(BaseModel):
    model_config = ConfigDict(defer_build=True)
    icon_type: str = Field(..., alias='iconType')

class TooltipText(BaseModel):
    model_config = ConfigDict(defer_build=True)
    runs: list[Run]

class WebCommandMetadata9(BaseModel):
    model_config = ConfigDict(defer_build=True)
    url: str
    web_page_type: str = Field(..., alias='webPageType')
    root_ve: int = Field(..., alias='rootVe')
    api_url: str = Field(..., alias='apiUrl')

class CommandMetadata9(BaseModel):
    model_config = ConfigDict(defer_build=True)
    web_command_metadata: WebCommandMetadata9 = Field(..., alias='webCommandMetadata')

class BrowseEndpoint3(BaseModel):
    model_config = ConfigDict(defer_build=True)
    browse_id: str = Field(..., alias='browseId')

class Endpoint1(BaseModel):
    model_config = ConfigDict(defer_build=True)
    click_tracking_params: str = Field(..., alias='clickTrackingParams')
    command_metadata: CommandMetadata9 = Field(..., alias='commandMetadata')
    browse_endpoint: BrowseEndpoint3 = Field(..., alias='browseEndpoint')

class TopbarLogoRenderer(BaseModel):
    model_config = ConfigDict(defer_build=True)
    icon_image: IconImage = Field(..., alias='iconImage')
    tooltip_text: TooltipText = Field(..., alias='tooltipText')
    endpoint: Endpoint1
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

class Config(BaseModel):
    model_config = ConfigDict(defer_build=True)
    web_searchbox_config: WebSearchboxConfig = Field(..., alias='webSearchboxConfig')

class WebCommandMetadata10(BaseModel):
    model_config = ConfigDict(defer_build=True)
    url: str
    web_page_type: str = Field(..., alias='webPageType')
    root_ve: int = Field(..., alias='rootVe')

class CommandMetadata10(BaseModel):
    model_config = ConfigDict(defer_build=True)
    web_command_metadata: WebCommandMetadata10 = Field(..., alias='webCommandMetadata')

class SearchEndpoint1(BaseModel):
    model_config = ConfigDict(defer_build=True)
    query: str
    params: str

class SearchEndpoint(BaseModel):
    model_config = ConfigDict(defer_build=True)
    click_tracking_params: str = Field(..., alias='clickTrackingParams')
    command_metadata: CommandMetadata10 = Field(..., alias='commandMetadata')
    search_endpoint: SearchEndpoint1 = Field(..., alias='searchEndpoint')

class AccessibilityData9(BaseModel):
    model_config = ConfigDict(defer_build=True)
    accessibility_data: AccessibilityData = Field(..., alias='accessibilityData')

class ButtonRenderer1(BaseModel):
    model_config = ConfigDict(defer_build=True)
    style: str
    size: str
    is_disabled: bool = Field(..., alias='isDisabled')
    icon: Icon
    tracking_params: str = Field(..., alias='trackingParams')
    accessibility_data: AccessibilityData9 = Field(..., alias='accessibilityData')

class ClearButton(BaseModel):
    model_config = ConfigDict(defer_build=True)
    button_renderer: ButtonRenderer1 = Field(..., alias='buttonRenderer')

class Headline(BaseModel):
    model_config = ConfigDict(defer_build=True)
    content: str

class DialogHeaderViewModel(BaseModel):
    model_config = ConfigDict(defer_build=True)
    headline: Headline

class Header1(BaseModel):
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

class Text4(BaseModel):
    model_config = ConfigDict(defer_build=True)
    content: str

class Paragraph(BaseModel):
    model_config = ConfigDict(defer_build=True)
    text: Text4

class BasicContentViewModel(BaseModel):
    model_config = ConfigDict(defer_build=True)
    paragraphs: list[Paragraph]

class Content6(BaseModel):
    model_config = ConfigDict(defer_build=True)
    basic_content_view_model: BasicContentViewModel = Field(..., alias='basicContentViewModel')

class DialogViewModel(BaseModel):
    model_config = ConfigDict(defer_build=True)
    header: Header1
    footer: Footer
    content: Content6

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
    icon: Icon
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

class WebCommandMetadata11(BaseModel):
    model_config = ConfigDict(defer_build=True)
    send_post: bool = Field(..., alias='sendPost')
    api_url: str = Field(..., alias='apiUrl')

class CommandMetadata11(BaseModel):
    model_config = ConfigDict(defer_build=True)
    web_command_metadata: WebCommandMetadata11 = Field(..., alias='webCommandMetadata')

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

class Action3(BaseModel):
    model_config = ConfigDict(defer_build=True)
    click_tracking_params: str = Field(..., alias='clickTrackingParams')
    open_popup_action: OpenPopupAction = Field(..., alias='openPopupAction')

class SignalServiceEndpoint1(BaseModel):
    model_config = ConfigDict(defer_build=True)
    signal: str
    actions: list[Action3]

class MenuRequest(BaseModel):
    model_config = ConfigDict(defer_build=True)
    click_tracking_params: str = Field(..., alias='clickTrackingParams')
    command_metadata: CommandMetadata11 = Field(..., alias='commandMetadata')
    signal_service_endpoint: SignalServiceEndpoint1 = Field(..., alias='signalServiceEndpoint')

class AccessibilityData11(BaseModel):
    model_config = ConfigDict(defer_build=True)
    label: str

class Accessibility6(BaseModel):
    model_config = ConfigDict(defer_build=True)
    accessibility_data: AccessibilityData11 = Field(..., alias='accessibilityData')

class TopbarMenuButtonRenderer(BaseModel):
    model_config = ConfigDict(defer_build=True)
    icon: Icon
    menu_request: MenuRequest = Field(..., alias='menuRequest')
    tracking_params: str = Field(..., alias='trackingParams')
    accessibility: Accessibility6
    tooltip: str
    style: str

class Text5(BaseModel):
    model_config = ConfigDict(defer_build=True)
    runs: list[Run]

class WebCommandMetadata12(BaseModel):
    model_config = ConfigDict(defer_build=True)
    url: str
    web_page_type: str = Field(..., alias='webPageType')
    root_ve: int = Field(..., alias='rootVe')

class CommandMetadata12(BaseModel):
    model_config = ConfigDict(defer_build=True)
    web_command_metadata: WebCommandMetadata12 = Field(..., alias='webCommandMetadata')

class SignInEndpoint1(BaseModel):
    model_config = ConfigDict(defer_build=True)
    idam_tag: str = Field(..., alias='idamTag')

class NavigationEndpoint4(BaseModel):
    model_config = ConfigDict(defer_build=True)
    click_tracking_params: str = Field(..., alias='clickTrackingParams')
    command_metadata: CommandMetadata12 = Field(..., alias='commandMetadata')
    sign_in_endpoint: SignInEndpoint1 = Field(..., alias='signInEndpoint')

class ButtonRenderer2(BaseModel):
    model_config = ConfigDict(defer_build=True)
    style: str
    size: str
    text: Text5
    icon: Icon
    navigation_endpoint: NavigationEndpoint4 = Field(..., alias='navigationEndpoint')
    tracking_params: str = Field(..., alias='trackingParams')
    target_id: str = Field(..., alias='targetId')

class TopbarButton(BaseModel):
    model_config = ConfigDict(defer_build=True)
    topbar_menu_button_renderer: TopbarMenuButtonRenderer | None = Field(None, alias='topbarMenuButtonRenderer')
    button_renderer: ButtonRenderer2 | None = Field(None, alias='buttonRenderer')

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
    accessibility_data: AccessibilityData11 = Field(..., alias='accessibilityData')

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

class Text6(BaseModel):
    model_config = ConfigDict(defer_build=True)
    runs: list[Run]

class ButtonRenderer3(BaseModel):
    model_config = ConfigDict(defer_build=True)
    style: str
    size: str
    is_disabled: bool = Field(..., alias='isDisabled')
    text: Text6
    tracking_params: str = Field(..., alias='trackingParams')

class DismissButton(BaseModel):
    model_config = ConfigDict(defer_build=True)
    button_renderer: ButtonRenderer3 = Field(..., alias='buttonRenderer')

class HotkeyDialogRenderer(BaseModel):
    model_config = ConfigDict(defer_build=True)
    title: Title4
    sections: list[Section]
    dismiss_button: DismissButton = Field(..., alias='dismissButton')
    tracking_params: str = Field(..., alias='trackingParams')

class HotkeyDialog(BaseModel):
    model_config = ConfigDict(defer_build=True)
    hotkey_dialog_renderer: HotkeyDialogRenderer = Field(..., alias='hotkeyDialogRenderer')

class WebCommandMetadata13(BaseModel):
    model_config = ConfigDict(defer_build=True)
    send_post: bool = Field(..., alias='sendPost')

class CommandMetadata13(BaseModel):
    model_config = ConfigDict(defer_build=True)
    web_command_metadata: WebCommandMetadata13 = Field(..., alias='webCommandMetadata')

class SignalAction(BaseModel):
    model_config = ConfigDict(defer_build=True)
    signal: str

class Action4(BaseModel):
    model_config = ConfigDict(defer_build=True)
    click_tracking_params: str = Field(..., alias='clickTrackingParams')
    signal_action: SignalAction = Field(..., alias='signalAction')

class SignalServiceEndpoint2(BaseModel):
    model_config = ConfigDict(defer_build=True)
    signal: str
    actions: list[Action4]

class Command(BaseModel):
    model_config = ConfigDict(defer_build=True)
    click_tracking_params: str = Field(..., alias='clickTrackingParams')
    command_metadata: CommandMetadata13 = Field(..., alias='commandMetadata')
    signal_service_endpoint: SignalServiceEndpoint2 = Field(..., alias='signalServiceEndpoint')

class ButtonRenderer4(BaseModel):
    model_config = ConfigDict(defer_build=True)
    tracking_params: str = Field(..., alias='trackingParams')
    command: Command

class BackButton(BaseModel):
    model_config = ConfigDict(defer_build=True)
    button_renderer: ButtonRenderer4 = Field(..., alias='buttonRenderer')

class CommandMetadata14(BaseModel):
    model_config = ConfigDict(defer_build=True)
    web_command_metadata: WebCommandMetadata13 = Field(..., alias='webCommandMetadata')

class Action5(BaseModel):
    model_config = ConfigDict(defer_build=True)
    click_tracking_params: str = Field(..., alias='clickTrackingParams')
    signal_action: SignalAction = Field(..., alias='signalAction')

class SignalServiceEndpoint3(BaseModel):
    model_config = ConfigDict(defer_build=True)
    signal: str
    actions: list[Action5]

class Command1(BaseModel):
    model_config = ConfigDict(defer_build=True)
    click_tracking_params: str = Field(..., alias='clickTrackingParams')
    command_metadata: CommandMetadata14 = Field(..., alias='commandMetadata')
    signal_service_endpoint: SignalServiceEndpoint3 = Field(..., alias='signalServiceEndpoint')

class ButtonRenderer5(BaseModel):
    model_config = ConfigDict(defer_build=True)
    tracking_params: str = Field(..., alias='trackingParams')
    command: Command1

class ForwardButton(BaseModel):
    model_config = ConfigDict(defer_build=True)
    button_renderer: ButtonRenderer5 = Field(..., alias='buttonRenderer')

class Text7(BaseModel):
    model_config = ConfigDict(defer_build=True)
    runs: list[Run]

class CommandMetadata15(BaseModel):
    model_config = ConfigDict(defer_build=True)
    web_command_metadata: WebCommandMetadata13 = Field(..., alias='webCommandMetadata')

class Action6(BaseModel):
    model_config = ConfigDict(defer_build=True)
    click_tracking_params: str = Field(..., alias='clickTrackingParams')
    signal_action: SignalAction = Field(..., alias='signalAction')

class SignalServiceEndpoint4(BaseModel):
    model_config = ConfigDict(defer_build=True)
    signal: str
    actions: list[Action6]

class Command2(BaseModel):
    model_config = ConfigDict(defer_build=True)
    click_tracking_params: str = Field(..., alias='clickTrackingParams')
    command_metadata: CommandMetadata15 = Field(..., alias='commandMetadata')
    signal_service_endpoint: SignalServiceEndpoint4 = Field(..., alias='signalServiceEndpoint')

class ButtonRenderer6(BaseModel):
    model_config = ConfigDict(defer_build=True)
    style: str
    size: str
    is_disabled: bool = Field(..., alias='isDisabled')
    text: Text7
    tracking_params: str = Field(..., alias='trackingParams')
    command: Command2

class A11ySkipNavigationButton(BaseModel):
    model_config = ConfigDict(defer_build=True)
    button_renderer: ButtonRenderer6 = Field(..., alias='buttonRenderer')

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

class Topbar(BaseModel):
    model_config = ConfigDict(defer_build=True)
    desktop_topbar_renderer: DesktopTopbarRenderer = Field(..., alias='desktopTopbarRenderer')

class Thumbnail3(BaseModel):
    model_config = ConfigDict(defer_build=True)
    url: str
    width: int
    height: int

class Thumbnail2(BaseModel):
    model_config = ConfigDict(defer_build=True)
    thumbnails: list[Thumbnail3]

class PlaylistVideoThumbnailRenderer(BaseModel):
    model_config = ConfigDict(defer_build=True)
    thumbnail: Thumbnail2
    tracking_params: str = Field(..., alias='trackingParams')

class ThumbnailRenderer(BaseModel):
    model_config = ConfigDict(defer_build=True)
    playlist_video_thumbnail_renderer: PlaylistVideoThumbnailRenderer = Field(..., alias='playlistVideoThumbnailRenderer')

class Title6(BaseModel):
    model_config = ConfigDict(defer_build=True)
    simple_text: str = Field(..., alias='simpleText')

class Accessibility7(BaseModel):
    model_config = ConfigDict(defer_build=True)
    accessibility_data: AccessibilityData11 = Field(..., alias='accessibilityData')

class Stat(BaseModel):
    model_config = ConfigDict(defer_build=True)
    accessibility: Accessibility7
    simple_text: str = Field(..., alias='simpleText')

class MetadataBadgeRenderer1(BaseModel):
    model_config = ConfigDict(defer_build=True)
    style: str
    label: str
    tracking_params: str = Field(..., alias='trackingParams')
    accessibility_data: AccessibilityData11 | None = Field(None, alias='accessibilityData')

class Badge(BaseModel):
    model_config = ConfigDict(defer_build=True)
    metadata_badge_renderer: MetadataBadgeRenderer1 = Field(..., alias='metadataBadgeRenderer')

class Description1(BaseModel):
    model_config = ConfigDict(defer_build=True)
    simple_text: str = Field(..., alias='simpleText')

class Accessibility8(BaseModel):
    model_config = ConfigDict(defer_build=True)
    accessibility_data: AccessibilityData11 = Field(..., alias='accessibilityData')

class Header2(BaseModel):
    model_config = ConfigDict(defer_build=True)
    accessibility: Accessibility8
    simple_text: str = Field(..., alias='simpleText')

class Accessibility9(BaseModel):
    model_config = ConfigDict(defer_build=True)
    accessibility_data: AccessibilityData11 = Field(..., alias='accessibilityData')

class Subtitle1(BaseModel):
    model_config = ConfigDict(defer_build=True)
    accessibility: Accessibility9
    simple_text: str = Field(..., alias='simpleText')

class Text8(BaseModel):
    model_config = ConfigDict(defer_build=True)
    runs: list[Run]

class WebCommandMetadata16(BaseModel):
    model_config = ConfigDict(defer_build=True)
    url: str
    web_page_type: str = Field(..., alias='webPageType')
    root_ve: int = Field(..., alias='rootVe')

class CommandMetadata16(BaseModel):
    model_config = ConfigDict(defer_build=True)
    web_command_metadata: WebCommandMetadata16 = Field(..., alias='webCommandMetadata')

class LoggingContext2(BaseModel):
    model_config = ConfigDict(defer_build=True)
    vss_logging_context: VssLoggingContext = Field(..., alias='vssLoggingContext')

class WatchEndpoint2(BaseModel):
    model_config = ConfigDict(defer_build=True)
    video_id: str = Field(..., alias='videoId')
    playlist_id: str = Field(..., alias='playlistId')
    logging_context: LoggingContext2 = Field(..., alias='loggingContext')

class Command3(BaseModel):
    model_config = ConfigDict(defer_build=True)
    click_tracking_params: str = Field(..., alias='clickTrackingParams')
    command_metadata: CommandMetadata16 = Field(..., alias='commandMetadata')
    watch_endpoint: WatchEndpoint2 = Field(..., alias='watchEndpoint')

class ButtonRenderer7(BaseModel):
    model_config = ConfigDict(defer_build=True)
    style: str
    size: str
    is_disabled: bool = Field(..., alias='isDisabled')
    text: Text8
    icon: Icon
    tracking_params: str = Field(..., alias='trackingParams')
    command: Command3

class PrimaryActionButton(BaseModel):
    model_config = ConfigDict(defer_build=True)
    button_renderer: ButtonRenderer7 = Field(..., alias='buttonRenderer')

class TvfilmShowWatchForwardOverlayRenderer(BaseModel):
    model_config = ConfigDict(defer_build=True)
    header: Header2
    title: Title6
    subtitle: Subtitle1
    primary_action_button: PrimaryActionButton = Field(..., alias='primaryActionButton')
    tracking_params: str = Field(..., alias='trackingParams')

class ThumbnailOverlay1(BaseModel):
    model_config = ConfigDict(defer_build=True)
    tvfilm_show_watch_forward_overlay_renderer: TvfilmShowWatchForwardOverlayRenderer = Field(..., alias='tvfilmShowWatchForwardOverlayRenderer')

class PlaylistSidebarPrimaryInfoRenderer(BaseModel):
    model_config = ConfigDict(defer_build=True)
    thumbnail_renderer: ThumbnailRenderer = Field(..., alias='thumbnailRenderer')
    title: Title6
    stats: list[Stat]
    badges: list[Badge]
    description: Description1
    style: str
    thumbnail_overlays: list[ThumbnailOverlay1] | None = Field(None, alias='thumbnailOverlays')

class Item1(BaseModel):
    model_config = ConfigDict(defer_build=True)
    playlist_sidebar_primary_info_renderer: PlaylistSidebarPrimaryInfoRenderer = Field(..., alias='playlistSidebarPrimaryInfoRenderer')

class PlaylistSidebarRenderer(BaseModel):
    model_config = ConfigDict(defer_build=True)
    items: list[Item1]
    tracking_params: str = Field(..., alias='trackingParams')

class Sidebar(BaseModel):
    model_config = ConfigDict(defer_build=True)
    playlist_sidebar_renderer: PlaylistSidebarRenderer = Field(..., alias='playlistSidebarRenderer')

class ShowsModel(BaseModel):
    model_config = ConfigDict(defer_build=True)
    response_context: ResponseContext = Field(..., alias='responseContext')
    contents: Contents
    tracking_params: str = Field(..., alias='trackingParams')
    topbar: Topbar
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
