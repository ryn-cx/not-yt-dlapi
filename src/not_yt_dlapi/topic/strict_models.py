from typing import Any, Self
from pydantic import ModelWrapValidatorHandler, PrivateAttr, model_validator
from pydantic import BaseModel, Field
from uuid import UUID

class Param(BaseModel):
    key: str
    value: str

class ServiceTrackingParam(BaseModel):
    service: str
    params: list[Param]

class MainAppWebResponseContext(BaseModel):
    logged_out: bool = Field(..., alias='loggedOut')
    tracking_param: str = Field(..., alias='trackingParam')

class WebResponseContextPreloadData(BaseModel):
    preload_message_names: list[str] = Field(..., alias='preloadMessageNames')

class WebResponseContextExtensionData(BaseModel):
    web_response_context_preload_data: WebResponseContextPreloadData = Field(..., alias='webResponseContextPreloadData')
    has_decorated: bool = Field(..., alias='hasDecorated')

class ResponseContext(BaseModel):
    visitor_data: str = Field(..., alias='visitorData')
    service_tracking_params: list[ServiceTrackingParam] = Field(..., alias='serviceTrackingParams')
    max_age_seconds: int = Field(..., alias='maxAgeSeconds')
    main_app_web_response_context: MainAppWebResponseContext = Field(..., alias='mainAppWebResponseContext')
    response_id: str = Field(..., alias='responseId')
    web_response_context_extension_data: WebResponseContextExtensionData = Field(..., alias='webResponseContextExtensionData')

class WebCommandMetadata(BaseModel):
    url: str
    web_page_type: str = Field(..., alias='webPageType')
    root_ve: int = Field(..., alias='rootVe')
    api_url: str = Field(..., alias='apiUrl')

class CommandMetadata(BaseModel):
    web_command_metadata: WebCommandMetadata = Field(..., alias='webCommandMetadata')

class BrowseEndpoint(BaseModel):
    browse_id: str = Field(..., alias='browseId')
    params: str
    canonical_base_url: str = Field(..., alias='canonicalBaseUrl')

class Endpoint(BaseModel):
    click_tracking_params: str = Field(..., alias='clickTrackingParams')
    command_metadata: CommandMetadata = Field(..., alias='commandMetadata')
    browse_endpoint: BrowseEndpoint = Field(..., alias='browseEndpoint')

class Title1(BaseModel):
    simple_text: str = Field(..., alias='simpleText')

class Icon(BaseModel):
    icon_type: str = Field(..., alias='iconType')

class Accessibility(BaseModel):
    label: str

class AccessibilityData1(BaseModel):
    label: str

class AccessibilityData(BaseModel):
    accessibility_data: AccessibilityData1 = Field(..., alias='accessibilityData')

class ChangeEngagementPanelVisibilityAction(BaseModel):
    target_id: UUID = Field(..., alias='targetId')
    visibility: str

class Command(BaseModel):
    click_tracking_params: str = Field(..., alias='clickTrackingParams')
    change_engagement_panel_visibility_action: ChangeEngagementPanelVisibilityAction = Field(..., alias='changeEngagementPanelVisibilityAction')

class ButtonRenderer(BaseModel):
    style: str
    size: str
    is_disabled: bool = Field(..., alias='isDisabled')
    icon: Icon
    accessibility: Accessibility
    tracking_params: str = Field(..., alias='trackingParams')
    accessibility_data: AccessibilityData = Field(..., alias='accessibilityData')
    command: Command

class VisibilityButton(BaseModel):
    button_renderer: ButtonRenderer = Field(..., alias='buttonRenderer')

class EngagementPanelTitleHeaderRenderer(BaseModel):
    title: Title1
    visibility_button: VisibilityButton = Field(..., alias='visibilityButton')
    tracking_params: str = Field(..., alias='trackingParams')

class Header(BaseModel):
    engagement_panel_title_header_renderer: EngagementPanelTitleHeaderRenderer = Field(..., alias='engagementPanelTitleHeaderRenderer')

class WebCommandMetadata1(BaseModel):
    send_post: bool = Field(..., alias='sendPost')
    api_url: str = Field(..., alias='apiUrl')

class CommandMetadata1(BaseModel):
    web_command_metadata: WebCommandMetadata1 = Field(..., alias='webCommandMetadata')

class ContinuationCommand(BaseModel):
    token: str
    request: str

class ContinuationEndpoint(BaseModel):
    click_tracking_params: str = Field(..., alias='clickTrackingParams')
    command_metadata: CommandMetadata1 = Field(..., alias='commandMetadata')
    continuation_command: ContinuationCommand = Field(..., alias='continuationCommand')

class ContinuationItemRenderer(BaseModel):
    trigger: str
    continuation_endpoint: ContinuationEndpoint = Field(..., alias='continuationEndpoint')

class Content5(BaseModel):
    continuation_item_renderer: ContinuationItemRenderer = Field(..., alias='continuationItemRenderer')

class ItemSectionRenderer1(BaseModel):
    contents: list[Content5]
    tracking_params: str = Field(..., alias='trackingParams')
    section_identifier: UUID = Field(..., alias='sectionIdentifier')
    target_id: UUID = Field(..., alias='targetId')

class Content4(BaseModel):
    item_section_renderer: ItemSectionRenderer1 = Field(..., alias='itemSectionRenderer')

class ScrollPaneStyle(BaseModel):
    scrollable: bool

class SectionListRenderer1(BaseModel):
    contents: list[Content4]
    tracking_params: str = Field(..., alias='trackingParams')
    scroll_pane_style: ScrollPaneStyle = Field(..., alias='scrollPaneStyle')

class Content3(BaseModel):
    section_list_renderer: SectionListRenderer1 = Field(..., alias='sectionListRenderer')

class Identifier(BaseModel):
    surface: str
    tag: UUID

class EngagementPanelSectionListRenderer(BaseModel):
    header: Header
    content: Content3
    target_id: UUID = Field(..., alias='targetId')
    identifier: Identifier
    size: str

class EngagementPanel(BaseModel):
    engagement_panel_section_list_renderer: EngagementPanelSectionListRenderer = Field(..., alias='engagementPanelSectionListRenderer')

class EngagementPanelPopupPresentationConfig(BaseModel):
    popup_type: str = Field(..., alias='popupType')

class EngagementPanelPresentationConfigs(BaseModel):
    engagement_panel_popup_presentation_config: EngagementPanelPopupPresentationConfig = Field(..., alias='engagementPanelPopupPresentationConfig')

class ShowEngagementPanelEndpoint(BaseModel):
    engagement_panel: EngagementPanel = Field(..., alias='engagementPanel')
    identifier: Identifier
    engagement_panel_presentation_configs: EngagementPanelPresentationConfigs = Field(..., alias='engagementPanelPresentationConfigs')

class NavigationEndpoint(BaseModel):
    click_tracking_params: str = Field(..., alias='clickTrackingParams')
    show_engagement_panel_endpoint: ShowEngagementPanelEndpoint = Field(..., alias='showEngagementPanelEndpoint')

class Run(BaseModel):
    text: str
    navigation_endpoint: NavigationEndpoint = Field(..., alias='navigationEndpoint')

class Title(BaseModel):
    runs: list[Run]

class Title2(BaseModel):
    simple_text: str = Field(..., alias='simpleText')

class AccessibilityData3(BaseModel):
    label: str

class AccessibilityData2(BaseModel):
    accessibility_data: AccessibilityData3 = Field(..., alias='accessibilityData')

class Command1(BaseModel):
    click_tracking_params: str = Field(..., alias='clickTrackingParams')
    change_engagement_panel_visibility_action: ChangeEngagementPanelVisibilityAction = Field(..., alias='changeEngagementPanelVisibilityAction')

class ButtonRenderer1(BaseModel):
    style: str
    size: str
    is_disabled: bool = Field(..., alias='isDisabled')
    icon: Icon
    accessibility: Accessibility
    tracking_params: str = Field(..., alias='trackingParams')
    accessibility_data: AccessibilityData2 = Field(..., alias='accessibilityData')
    command: Command1

class VisibilityButton1(BaseModel):
    button_renderer: ButtonRenderer1 = Field(..., alias='buttonRenderer')

class EngagementPanelTitleHeaderRenderer1(BaseModel):
    title: Title2
    visibility_button: VisibilityButton1 = Field(..., alias='visibilityButton')
    tracking_params: str = Field(..., alias='trackingParams')

class Header1(BaseModel):
    engagement_panel_title_header_renderer: EngagementPanelTitleHeaderRenderer1 = Field(..., alias='engagementPanelTitleHeaderRenderer')

class CommandMetadata2(BaseModel):
    web_command_metadata: WebCommandMetadata1 = Field(..., alias='webCommandMetadata')

class ContinuationEndpoint1(BaseModel):
    click_tracking_params: str = Field(..., alias='clickTrackingParams')
    command_metadata: CommandMetadata2 = Field(..., alias='commandMetadata')
    continuation_command: ContinuationCommand = Field(..., alias='continuationCommand')

class ContinuationItemRenderer1(BaseModel):
    trigger: str
    continuation_endpoint: ContinuationEndpoint1 = Field(..., alias='continuationEndpoint')

class Content8(BaseModel):
    continuation_item_renderer: ContinuationItemRenderer1 = Field(..., alias='continuationItemRenderer')

class ItemSectionRenderer2(BaseModel):
    contents: list[Content8]
    tracking_params: str = Field(..., alias='trackingParams')
    section_identifier: UUID = Field(..., alias='sectionIdentifier')
    target_id: UUID = Field(..., alias='targetId')

class Content7(BaseModel):
    item_section_renderer: ItemSectionRenderer2 = Field(..., alias='itemSectionRenderer')

class SectionListRenderer2(BaseModel):
    contents: list[Content7]
    tracking_params: str = Field(..., alias='trackingParams')
    scroll_pane_style: ScrollPaneStyle = Field(..., alias='scrollPaneStyle')

class Content6(BaseModel):
    section_list_renderer: SectionListRenderer2 = Field(..., alias='sectionListRenderer')

class EngagementPanelSectionListRenderer1(BaseModel):
    header: Header1
    content: Content6
    target_id: UUID = Field(..., alias='targetId')
    identifier: Identifier
    size: str

class EngagementPanel1(BaseModel):
    engagement_panel_section_list_renderer: EngagementPanelSectionListRenderer1 = Field(..., alias='engagementPanelSectionListRenderer')

class EngagementPanelPresentationConfigs1(BaseModel):
    engagement_panel_popup_presentation_config: EngagementPanelPopupPresentationConfig = Field(..., alias='engagementPanelPopupPresentationConfig')

class ShowEngagementPanelEndpoint1(BaseModel):
    engagement_panel: EngagementPanel1 = Field(..., alias='engagementPanel')
    identifier: Identifier
    engagement_panel_presentation_configs: EngagementPanelPresentationConfigs1 = Field(..., alias='engagementPanelPresentationConfigs')

class Endpoint1(BaseModel):
    click_tracking_params: str = Field(..., alias='clickTrackingParams')
    show_engagement_panel_endpoint: ShowEngagementPanelEndpoint1 = Field(..., alias='showEngagementPanelEndpoint')

class Source(BaseModel):
    url: str
    width: int
    height: int

class Image(BaseModel):
    sources: list[Source]

class ClientResource(BaseModel):
    image_name: str = Field(..., alias='imageName')

class Source1(BaseModel):
    client_resource: ClientResource = Field(..., alias='clientResource')

class Icon2(BaseModel):
    sources: list[Source1]

class BackgroundColor(BaseModel):
    light_theme: int = Field(..., alias='lightTheme')
    dark_theme: int = Field(..., alias='darkTheme')

class ThumbnailBadgeViewModel(BaseModel):
    icon: Icon2
    text: str
    badge_style: str = Field(..., alias='badgeStyle')
    background_color: BackgroundColor = Field(..., alias='backgroundColor')

class ThumbnailBadge(BaseModel):
    thumbnail_badge_view_model: ThumbnailBadgeViewModel = Field(..., alias='thumbnailBadgeViewModel')

class ThumbnailOverlayBadgeViewModel(BaseModel):
    thumbnail_badges: list[ThumbnailBadge] = Field(..., alias='thumbnailBadges')
    position: str

class Source2(BaseModel):
    client_resource: ClientResource = Field(..., alias='clientResource')

class Icon3(BaseModel):
    sources: list[Source2]

class StyleRun(BaseModel):
    start_index: int = Field(..., alias='startIndex')
    length: int

class Text(BaseModel):
    content: str
    style_runs: list[StyleRun] = Field(..., alias='styleRuns')

class ThumbnailHoverOverlayViewModel(BaseModel):
    icon: Icon3
    text: Text
    style: str

class Overlay(BaseModel):
    thumbnail_overlay_badge_view_model: ThumbnailOverlayBadgeViewModel | None = Field(None, alias='thumbnailOverlayBadgeViewModel')
    thumbnail_hover_overlay_view_model: ThumbnailHoverOverlayViewModel | None = Field(None, alias='thumbnailHoverOverlayViewModel')

class ThumbnailViewModel(BaseModel):
    image: Image
    overlays: list[Overlay]
    background_color: BackgroundColor = Field(..., alias='backgroundColor')

class PrimaryThumbnail(BaseModel):
    thumbnail_view_model: ThumbnailViewModel = Field(..., alias='thumbnailViewModel')

class StackColor(BaseModel):
    light_theme: int = Field(..., alias='lightTheme')
    dark_theme: int = Field(..., alias='darkTheme')

class CollectionThumbnailViewModel(BaseModel):
    primary_thumbnail: PrimaryThumbnail = Field(..., alias='primaryThumbnail')
    stack_color: StackColor = Field(..., alias='stackColor')

class ContentImage(BaseModel):
    collection_thumbnail_view_model: CollectionThumbnailViewModel = Field(..., alias='collectionThumbnailViewModel')

class Title3(BaseModel):
    content: str

class WebCommandMetadata3(BaseModel):
    url: str
    web_page_type: str = Field(..., alias='webPageType')
    root_ve: int = Field(..., alias='rootVe')
    api_url: str = Field(..., alias='apiUrl')

class CommandMetadata3(BaseModel):
    web_command_metadata: WebCommandMetadata3 = Field(..., alias='webCommandMetadata')

class BrowseEndpoint1(BaseModel):
    browse_id: str = Field(..., alias='browseId')
    canonical_base_url: str | None = Field(None, alias='canonicalBaseUrl')

class InnertubeCommand(BaseModel):
    click_tracking_params: str = Field(..., alias='clickTrackingParams')
    command_metadata: CommandMetadata3 = Field(..., alias='commandMetadata')
    browse_endpoint: BrowseEndpoint1 = Field(..., alias='browseEndpoint')

class OnTap(BaseModel):
    innertube_command: InnertubeCommand = Field(..., alias='innertubeCommand')

class CommandRun(BaseModel):
    start_index: int = Field(..., alias='startIndex')
    length: int
    on_tap: OnTap = Field(..., alias='onTap')

class StyleRun1(BaseModel):
    start_index: int = Field(..., alias='startIndex')
    length: int
    weight_label: str = Field(..., alias='weightLabel')

class Text1(BaseModel):
    content: str
    command_runs: list[CommandRun] | None = Field(None, alias='commandRuns')
    style_runs: list[StyleRun1] | None = Field(None, alias='styleRuns')

class MetadataPart(BaseModel):
    text: Text1

class MetadataRow(BaseModel):
    metadata_parts: list[MetadataPart] = Field(..., alias='metadataParts')

class ContentMetadataViewModel(BaseModel):
    metadata_rows: list[MetadataRow] = Field(..., alias='metadataRows')
    delimiter: str

class Metadata1(BaseModel):
    content_metadata_view_model: ContentMetadataViewModel = Field(..., alias='contentMetadataViewModel')

class LockupMetadataViewModel(BaseModel):
    title: Title3
    metadata: Metadata1

class Metadata(BaseModel):
    lockup_metadata_view_model: LockupMetadataViewModel = Field(..., alias='lockupMetadataViewModel')

class WebCommandMetadata4(BaseModel):
    url: str
    web_page_type: str = Field(..., alias='webPageType')
    root_ve: int = Field(..., alias='rootVe')

class CommandMetadata4(BaseModel):
    web_command_metadata: WebCommandMetadata4 = Field(..., alias='webCommandMetadata')

class VssLoggingContext(BaseModel):
    serialized_context_data: str = Field(..., alias='serializedContextData')

class LoggingContext(BaseModel):
    vss_logging_context: VssLoggingContext = Field(..., alias='vssLoggingContext')

class CommonConfig(BaseModel):
    url: str

class Html5PlaybackOnesieConfig(BaseModel):
    common_config: CommonConfig = Field(..., alias='commonConfig')

class WatchEndpointSupportedOnesieConfig(BaseModel):
    html5_playback_onesie_config: Html5PlaybackOnesieConfig = Field(..., alias='html5PlaybackOnesieConfig')

class WatchEndpoint(BaseModel):
    video_id: str = Field(..., alias='videoId')
    playlist_id: str = Field(..., alias='playlistId')
    params: str
    logging_context: LoggingContext = Field(..., alias='loggingContext')
    watch_endpoint_supported_onesie_config: WatchEndpointSupportedOnesieConfig = Field(..., alias='watchEndpointSupportedOnesieConfig')
    player_params: str | None = Field(None, alias='playerParams')

class InnertubeCommand1(BaseModel):
    click_tracking_params: str = Field(..., alias='clickTrackingParams')
    command_metadata: CommandMetadata4 = Field(..., alias='commandMetadata')
    watch_endpoint: WatchEndpoint = Field(..., alias='watchEndpoint')

class OnSelect(BaseModel):
    innertube_command: InnertubeCommand1 = Field(..., alias='innertubeCommand')

class CommandMetadata5(BaseModel):
    web_command_metadata: WebCommandMetadata4 = Field(..., alias='webCommandMetadata')

class LoggingContext1(BaseModel):
    vss_logging_context: VssLoggingContext = Field(..., alias='vssLoggingContext')

class Html5PlaybackOnesieConfig1(BaseModel):
    common_config: CommonConfig = Field(..., alias='commonConfig')

class WatchEndpointSupportedOnesieConfig1(BaseModel):
    html5_playback_onesie_config: Html5PlaybackOnesieConfig1 = Field(..., alias='html5PlaybackOnesieConfig')

class WatchEndpoint1(BaseModel):
    video_id: str = Field(..., alias='videoId')
    playlist_id: str = Field(..., alias='playlistId')
    player_params: str = Field(..., alias='playerParams')
    logging_context: LoggingContext1 = Field(..., alias='loggingContext')
    watch_endpoint_supported_onesie_config: WatchEndpointSupportedOnesieConfig1 = Field(..., alias='watchEndpointSupportedOnesieConfig')

class InnertubeCommand2(BaseModel):
    click_tracking_params: str = Field(..., alias='clickTrackingParams')
    command_metadata: CommandMetadata5 = Field(..., alias='commandMetadata')
    watch_endpoint: WatchEndpoint1 = Field(..., alias='watchEndpoint')

class OnVisible(BaseModel):
    innertube_command: InnertubeCommand2 = Field(..., alias='innertubeCommand')

class InlinePlayerData(BaseModel):
    on_select: OnSelect = Field(..., alias='onSelect')
    on_visible: OnVisible = Field(..., alias='onVisible')

class ItemPlayback(BaseModel):
    inline_player_data: InlinePlayerData = Field(..., alias='inlinePlayerData')

class Visibility(BaseModel):
    types: str

class LoggingDirectives(BaseModel):
    tracking_params: str = Field(..., alias='trackingParams')
    visibility: Visibility

class LoggingContext2(BaseModel):
    logging_directives: LoggingDirectives = Field(..., alias='loggingDirectives')

class CommandMetadata6(BaseModel):
    web_command_metadata: WebCommandMetadata4 = Field(..., alias='webCommandMetadata')

class LoggingContext3(BaseModel):
    vss_logging_context: VssLoggingContext = Field(..., alias='vssLoggingContext')

class Html5PlaybackOnesieConfig2(BaseModel):
    common_config: CommonConfig = Field(..., alias='commonConfig')

class WatchEndpointSupportedOnesieConfig2(BaseModel):
    html5_playback_onesie_config: Html5PlaybackOnesieConfig2 = Field(..., alias='html5PlaybackOnesieConfig')

class WatchEndpoint2(BaseModel):
    video_id: str = Field(..., alias='videoId')
    playlist_id: str = Field(..., alias='playlistId')
    params: str
    logging_context: LoggingContext3 = Field(..., alias='loggingContext')
    watch_endpoint_supported_onesie_config: WatchEndpointSupportedOnesieConfig2 = Field(..., alias='watchEndpointSupportedOnesieConfig')
    player_params: str | None = Field(None, alias='playerParams')

class InnertubeCommand3(BaseModel):
    click_tracking_params: str = Field(..., alias='clickTrackingParams')
    command_metadata: CommandMetadata6 = Field(..., alias='commandMetadata')
    watch_endpoint: WatchEndpoint2 = Field(..., alias='watchEndpoint')

class OnTap1(BaseModel):
    innertube_command: InnertubeCommand3 = Field(..., alias='innertubeCommand')

class CommandContext(BaseModel):
    on_tap: OnTap1 = Field(..., alias='onTap')

class RendererContext(BaseModel):
    logging_context: LoggingContext2 = Field(..., alias='loggingContext')
    command_context: CommandContext = Field(..., alias='commandContext')

class LockupViewModel(BaseModel):
    content_image: ContentImage = Field(..., alias='contentImage')
    metadata: Metadata
    content_id: str = Field(..., alias='contentId')
    content_type: str = Field(..., alias='contentType')
    item_playback: ItemPlayback = Field(..., alias='itemPlayback')
    renderer_context: RendererContext = Field(..., alias='rendererContext')

class Item(BaseModel):
    lockup_view_model: LockupViewModel = Field(..., alias='lockupViewModel')

class Icon4(BaseModel):
    icon_type: str = Field(..., alias='iconType')

class ButtonRenderer2(BaseModel):
    style: str
    size: str
    is_disabled: bool = Field(..., alias='isDisabled')
    icon: Icon4
    accessibility: Accessibility
    tracking_params: str = Field(..., alias='trackingParams')

class NextButton(BaseModel):
    button_renderer: ButtonRenderer2 = Field(..., alias='buttonRenderer')

class ButtonRenderer3(BaseModel):
    style: str
    size: str
    is_disabled: bool = Field(..., alias='isDisabled')
    icon: Icon4
    accessibility: Accessibility
    tracking_params: str = Field(..., alias='trackingParams')

class PreviousButton(BaseModel):
    button_renderer: ButtonRenderer3 = Field(..., alias='buttonRenderer')

class HorizontalListRenderer(BaseModel):
    items: list[Item]
    tracking_params: str = Field(..., alias='trackingParams')
    visible_item_count: int = Field(..., alias='visibleItemCount')
    next_button: NextButton = Field(..., alias='nextButton')
    previous_button: PreviousButton = Field(..., alias='previousButton')
    force16_by9_thumbnail_aspect_ratio: bool = Field(..., alias='force16By9ThumbnailAspectRatio')

class Content9(BaseModel):
    horizontal_list_renderer: HorizontalListRenderer = Field(..., alias='horizontalListRenderer')

class Text2(BaseModel):
    simple_text: str = Field(..., alias='simpleText')

class Title4(BaseModel):
    simple_text: str = Field(..., alias='simpleText')

class AccessibilityData5(BaseModel):
    label: str

class AccessibilityData4(BaseModel):
    accessibility_data: AccessibilityData5 = Field(..., alias='accessibilityData')

class Command2(BaseModel):
    click_tracking_params: str = Field(..., alias='clickTrackingParams')
    change_engagement_panel_visibility_action: ChangeEngagementPanelVisibilityAction = Field(..., alias='changeEngagementPanelVisibilityAction')

class ButtonRenderer5(BaseModel):
    style: str
    size: str
    is_disabled: bool = Field(..., alias='isDisabled')
    icon: Icon4
    accessibility: Accessibility
    tracking_params: str = Field(..., alias='trackingParams')
    accessibility_data: AccessibilityData4 = Field(..., alias='accessibilityData')
    command: Command2

class VisibilityButton2(BaseModel):
    button_renderer: ButtonRenderer5 = Field(..., alias='buttonRenderer')

class EngagementPanelTitleHeaderRenderer2(BaseModel):
    title: Title4
    visibility_button: VisibilityButton2 = Field(..., alias='visibilityButton')
    tracking_params: str = Field(..., alias='trackingParams')

class Header2(BaseModel):
    engagement_panel_title_header_renderer: EngagementPanelTitleHeaderRenderer2 = Field(..., alias='engagementPanelTitleHeaderRenderer')

class WebCommandMetadata7(BaseModel):
    send_post: bool = Field(..., alias='sendPost')
    api_url: str = Field(..., alias='apiUrl')

class CommandMetadata7(BaseModel):
    web_command_metadata: WebCommandMetadata7 = Field(..., alias='webCommandMetadata')

class ContinuationEndpoint2(BaseModel):
    click_tracking_params: str = Field(..., alias='clickTrackingParams')
    command_metadata: CommandMetadata7 = Field(..., alias='commandMetadata')
    continuation_command: ContinuationCommand = Field(..., alias='continuationCommand')

class ContinuationItemRenderer2(BaseModel):
    trigger: str
    continuation_endpoint: ContinuationEndpoint2 = Field(..., alias='continuationEndpoint')

class Content12(BaseModel):
    continuation_item_renderer: ContinuationItemRenderer2 = Field(..., alias='continuationItemRenderer')

class ItemSectionRenderer3(BaseModel):
    contents: list[Content12]
    tracking_params: str = Field(..., alias='trackingParams')
    section_identifier: UUID = Field(..., alias='sectionIdentifier')
    target_id: UUID = Field(..., alias='targetId')

class Content11(BaseModel):
    item_section_renderer: ItemSectionRenderer3 = Field(..., alias='itemSectionRenderer')

class SectionListRenderer3(BaseModel):
    contents: list[Content11]
    tracking_params: str = Field(..., alias='trackingParams')
    scroll_pane_style: ScrollPaneStyle = Field(..., alias='scrollPaneStyle')

class Content10(BaseModel):
    section_list_renderer: SectionListRenderer3 = Field(..., alias='sectionListRenderer')

class EngagementPanelSectionListRenderer2(BaseModel):
    header: Header2
    content: Content10
    target_id: UUID = Field(..., alias='targetId')
    identifier: Identifier
    size: str

class EngagementPanel2(BaseModel):
    engagement_panel_section_list_renderer: EngagementPanelSectionListRenderer2 = Field(..., alias='engagementPanelSectionListRenderer')

class EngagementPanelPresentationConfigs2(BaseModel):
    engagement_panel_popup_presentation_config: EngagementPanelPopupPresentationConfig = Field(..., alias='engagementPanelPopupPresentationConfig')

class ShowEngagementPanelEndpoint2(BaseModel):
    engagement_panel: EngagementPanel2 = Field(..., alias='engagementPanel')
    identifier: Identifier
    engagement_panel_presentation_configs: EngagementPanelPresentationConfigs2 = Field(..., alias='engagementPanelPresentationConfigs')

class NavigationEndpoint1(BaseModel):
    click_tracking_params: str = Field(..., alias='clickTrackingParams')
    show_engagement_panel_endpoint: ShowEngagementPanelEndpoint2 = Field(..., alias='showEngagementPanelEndpoint')

class AccessibilityData7(BaseModel):
    label: str

class AccessibilityData6(BaseModel):
    accessibility_data: AccessibilityData7 = Field(..., alias='accessibilityData')

class ButtonRenderer4(BaseModel):
    style: str
    size: str
    is_disabled: bool = Field(..., alias='isDisabled')
    text: Text2
    navigation_endpoint: NavigationEndpoint1 = Field(..., alias='navigationEndpoint')
    tracking_params: str = Field(..., alias='trackingParams')
    accessibility_data: AccessibilityData6 = Field(..., alias='accessibilityData')

class TopLevelButton(BaseModel):
    button_renderer: ButtonRenderer4 = Field(..., alias='buttonRenderer')

class MenuRenderer(BaseModel):
    tracking_params: str = Field(..., alias='trackingParams')
    top_level_buttons: list[TopLevelButton] = Field(..., alias='topLevelButtons')

class Menu(BaseModel):
    menu_renderer: MenuRenderer = Field(..., alias='menuRenderer')

class ShelfRenderer(BaseModel):
    title: Title
    endpoint: Endpoint1
    content: Content9
    tracking_params: str = Field(..., alias='trackingParams')
    menu: Menu

class Content2(BaseModel):
    shelf_renderer: ShelfRenderer = Field(..., alias='shelfRenderer')

class ItemSectionRenderer(BaseModel):
    contents: list[Content2]
    tracking_params: str = Field(..., alias='trackingParams')

class Content1(BaseModel):
    item_section_renderer: ItemSectionRenderer = Field(..., alias='itemSectionRenderer')

class SectionListRenderer(BaseModel):
    contents: list[Content1]
    tracking_params: str = Field(..., alias='trackingParams')
    target_id: str = Field(..., alias='targetId')
    disable_pull_to_refresh: bool = Field(..., alias='disablePullToRefresh')

class Content(BaseModel):
    section_list_renderer: SectionListRenderer = Field(..., alias='sectionListRenderer')

class TabRenderer(BaseModel):
    endpoint: Endpoint
    title: str
    selected: bool
    content: Content
    tracking_params: str = Field(..., alias='trackingParams')

class Tab(BaseModel):
    tab_renderer: TabRenderer = Field(..., alias='tabRenderer')

class TwoColumnBrowseResultsRenderer(BaseModel):
    tabs: list[Tab]

class Contents(BaseModel):
    two_column_browse_results_renderer: TwoColumnBrowseResultsRenderer = Field(..., alias='twoColumnBrowseResultsRenderer')

class Text3(BaseModel):
    content: str

class LoggingDirectives1(BaseModel):
    tracking_params: str = Field(..., alias='trackingParams')
    visibility: Visibility

class LoggingContext4(BaseModel):
    logging_directives: LoggingDirectives1 = Field(..., alias='loggingDirectives')

class RendererContext1(BaseModel):
    logging_context: LoggingContext4 = Field(..., alias='loggingContext')

class DynamicTextViewModel(BaseModel):
    text: Text3
    max_lines: int = Field(..., alias='maxLines')
    renderer_context: RendererContext1 = Field(..., alias='rendererContext')

class Title5(BaseModel):
    dynamic_text_view_model: DynamicTextViewModel = Field(..., alias='dynamicTextViewModel')

class Source3(BaseModel):
    url: str
    width: int
    height: int

class BorderImageProcessor(BaseModel):
    circular: bool

class Processor(BaseModel):
    border_image_processor: BorderImageProcessor = Field(..., alias='borderImageProcessor')

class Image2(BaseModel):
    sources: list[Source3]
    processor: Processor

class LoggingDirectives2(BaseModel):
    tracking_params: str = Field(..., alias='trackingParams')
    visibility: Visibility

class AvatarViewModel(BaseModel):
    image: Image2
    avatar_image_size: str = Field(..., alias='avatarImageSize')
    logging_directives: LoggingDirectives2 = Field(..., alias='loggingDirectives')

class Avatar(BaseModel):
    avatar_view_model: AvatarViewModel = Field(..., alias='avatarViewModel')

class DecoratedAvatarViewModel(BaseModel):
    avatar: Avatar

class Image1(BaseModel):
    decorated_avatar_view_model: DecoratedAvatarViewModel = Field(..., alias='decoratedAvatarViewModel')

class StyleRun2(BaseModel):
    start_index: int = Field(..., alias='startIndex')
    length: int

class Text4(BaseModel):
    content: str
    style_runs: list[StyleRun2] = Field(..., alias='styleRuns')

class MetadataPart1(BaseModel):
    text: Text4

class MetadataRow1(BaseModel):
    metadata_parts: list[MetadataPart1] = Field(..., alias='metadataParts')

class LoggingDirectives3(BaseModel):
    tracking_params: str = Field(..., alias='trackingParams')
    visibility: Visibility

class LoggingContext5(BaseModel):
    logging_directives: LoggingDirectives3 = Field(..., alias='loggingDirectives')

class RendererContext2(BaseModel):
    logging_context: LoggingContext5 = Field(..., alias='loggingContext')

class ContentMetadataViewModel1(BaseModel):
    metadata_rows: list[MetadataRow1] = Field(..., alias='metadataRows')
    delimiter: str
    renderer_context: RendererContext2 = Field(..., alias='rendererContext')

class Metadata2(BaseModel):
    content_metadata_view_model: ContentMetadataViewModel1 = Field(..., alias='contentMetadataViewModel')

class Description1(BaseModel):
    content: str

class StyleRun3(BaseModel):
    start_index: int = Field(..., alias='startIndex')
    length: int
    weight: int

class TruncationText(BaseModel):
    content: str
    style_runs: list[StyleRun3] = Field(..., alias='styleRuns')

class LoggingDirectives4(BaseModel):
    tracking_params: str = Field(..., alias='trackingParams')
    visibility: Visibility

class LoggingContext6(BaseModel):
    logging_directives: LoggingDirectives4 = Field(..., alias='loggingDirectives')

class AccessibilityContext(BaseModel):
    label: str

class Title6(BaseModel):
    simple_text: str = Field(..., alias='simpleText')

class AccessibilityData9(BaseModel):
    label: str

class AccessibilityData8(BaseModel):
    accessibility_data: AccessibilityData9 = Field(..., alias='accessibilityData')

class Command3(BaseModel):
    click_tracking_params: str = Field(..., alias='clickTrackingParams')
    change_engagement_panel_visibility_action: ChangeEngagementPanelVisibilityAction = Field(..., alias='changeEngagementPanelVisibilityAction')

class ButtonRenderer6(BaseModel):
    style: str
    size: str
    is_disabled: bool = Field(..., alias='isDisabled')
    icon: Icon4
    accessibility: Accessibility
    tracking_params: str = Field(..., alias='trackingParams')
    accessibility_data: AccessibilityData8 = Field(..., alias='accessibilityData')
    command: Command3

class VisibilityButton3(BaseModel):
    button_renderer: ButtonRenderer6 = Field(..., alias='buttonRenderer')

class EngagementPanelTitleHeaderRenderer3(BaseModel):
    title: Title6
    visibility_button: VisibilityButton3 = Field(..., alias='visibilityButton')
    tracking_params: str = Field(..., alias='trackingParams')

class Header4(BaseModel):
    engagement_panel_title_header_renderer: EngagementPanelTitleHeaderRenderer3 = Field(..., alias='engagementPanelTitleHeaderRenderer')

class CommandMetadata8(BaseModel):
    web_command_metadata: WebCommandMetadata7 = Field(..., alias='webCommandMetadata')

class ContinuationEndpoint3(BaseModel):
    click_tracking_params: str = Field(..., alias='clickTrackingParams')
    command_metadata: CommandMetadata8 = Field(..., alias='commandMetadata')
    continuation_command: ContinuationCommand = Field(..., alias='continuationCommand')

class ContinuationItemRenderer3(BaseModel):
    trigger: str
    continuation_endpoint: ContinuationEndpoint3 = Field(..., alias='continuationEndpoint')

class Content16(BaseModel):
    continuation_item_renderer: ContinuationItemRenderer3 = Field(..., alias='continuationItemRenderer')

class ItemSectionRenderer4(BaseModel):
    contents: list[Content16]
    tracking_params: str = Field(..., alias='trackingParams')
    section_identifier: UUID = Field(..., alias='sectionIdentifier')
    target_id: UUID = Field(..., alias='targetId')

class Content15(BaseModel):
    item_section_renderer: ItemSectionRenderer4 = Field(..., alias='itemSectionRenderer')

class SectionListRenderer4(BaseModel):
    contents: list[Content15]
    tracking_params: str = Field(..., alias='trackingParams')
    scroll_pane_style: ScrollPaneStyle = Field(..., alias='scrollPaneStyle')

class Content14(BaseModel):
    section_list_renderer: SectionListRenderer4 = Field(..., alias='sectionListRenderer')

class EngagementPanelSectionListRenderer3(BaseModel):
    header: Header4
    content: Content14
    target_id: UUID = Field(..., alias='targetId')
    identifier: Identifier

class EngagementPanel3(BaseModel):
    engagement_panel_section_list_renderer: EngagementPanelSectionListRenderer3 = Field(..., alias='engagementPanelSectionListRenderer')

class EngagementPanelPresentationConfigs3(BaseModel):
    engagement_panel_popup_presentation_config: EngagementPanelPopupPresentationConfig = Field(..., alias='engagementPanelPopupPresentationConfig')

class ShowEngagementPanelEndpoint3(BaseModel):
    engagement_panel: EngagementPanel3 = Field(..., alias='engagementPanel')
    identifier: Identifier
    engagement_panel_presentation_configs: EngagementPanelPresentationConfigs3 = Field(..., alias='engagementPanelPresentationConfigs')

class InnertubeCommand4(BaseModel):
    click_tracking_params: str = Field(..., alias='clickTrackingParams')
    show_engagement_panel_endpoint: ShowEngagementPanelEndpoint3 = Field(..., alias='showEngagementPanelEndpoint')

class OnTap2(BaseModel):
    innertube_command: InnertubeCommand4 = Field(..., alias='innertubeCommand')

class CommandContext1(BaseModel):
    on_tap: OnTap2 = Field(..., alias='onTap')

class RendererContext3(BaseModel):
    logging_context: LoggingContext6 = Field(..., alias='loggingContext')
    accessibility_context: AccessibilityContext = Field(..., alias='accessibilityContext')
    command_context: CommandContext1 = Field(..., alias='commandContext')

class DescriptionPreviewViewModel(BaseModel):
    description: Description1
    max_lines: int = Field(..., alias='maxLines')
    truncation_text: TruncationText = Field(..., alias='truncationText')
    always_show_truncation_text: bool = Field(..., alias='alwaysShowTruncationText')
    renderer_context: RendererContext3 = Field(..., alias='rendererContext')

class Description(BaseModel):
    description_preview_view_model: DescriptionPreviewViewModel = Field(..., alias='descriptionPreviewViewModel')

class WebCommandMetadata9(BaseModel):
    url: str
    web_page_type: str = Field(..., alias='webPageType')
    root_ve: int = Field(..., alias='rootVe')

class CommandMetadata9(BaseModel):
    web_command_metadata: WebCommandMetadata9 = Field(..., alias='webCommandMetadata')

class UrlEndpoint(BaseModel):
    url: str
    target: str

class InnertubeCommand5(BaseModel):
    click_tracking_params: str = Field(..., alias='clickTrackingParams')
    command_metadata: CommandMetadata9 = Field(..., alias='commandMetadata')
    url_endpoint: UrlEndpoint = Field(..., alias='urlEndpoint')

class OnTap3(BaseModel):
    innertube_command: InnertubeCommand5 = Field(..., alias='innertubeCommand')

class LoggingDirectives5(BaseModel):
    tracking_params: str = Field(..., alias='trackingParams')
    visibility: Visibility

class CommandRun1(BaseModel):
    start_index: int = Field(..., alias='startIndex')
    length: int
    on_tap: OnTap3 = Field(..., alias='onTap')
    logging_directives: LoggingDirectives5 = Field(..., alias='loggingDirectives')

class ColorMapItem(BaseModel):
    key: str
    value: int

class StyleRunColorMapExtension(BaseModel):
    color_map: list[ColorMapItem] = Field(..., alias='colorMap')

class StyleRunExtensions(BaseModel):
    style_run_color_map_extension: StyleRunColorMapExtension = Field(..., alias='styleRunColorMapExtension')

class StyleRun4(BaseModel):
    weight_label: str = Field(..., alias='weightLabel')
    style_run_extensions: StyleRunExtensions = Field(..., alias='styleRunExtensions')

class ClientResource2(BaseModel):
    icon: str

class YoutubeIconSource(BaseModel):
    client_resource: ClientResource2 = Field(..., alias='clientResource')

class CustomImageSource(BaseModel):
    youtube_icon_source: YoutubeIconSource = Field(..., alias='youtubeIconSource')

class Source4(BaseModel):
    custom_image_source: CustomImageSource = Field(..., alias='customImageSource')

class Image3(BaseModel):
    sources: list[Source4]

class ImageType(BaseModel):
    image: Image3

class Type(BaseModel):
    image_type: ImageType = Field(..., alias='imageType')

class Height(BaseModel):
    value: int
    unit: str

class Width(BaseModel):
    value: int
    unit: str

class LayoutProperties(BaseModel):
    height: Height
    width: Width

class Properties(BaseModel):
    layout_properties: LayoutProperties = Field(..., alias='layoutProperties')

class Element(BaseModel):
    type: Type
    properties: Properties

class AttachmentRun(BaseModel):
    start_index: int = Field(..., alias='startIndex')
    length: int
    element: Element
    alignment: str

class Text5(BaseModel):
    content: str
    command_runs: list[CommandRun1] = Field(..., alias='commandRuns')
    style_runs: list[StyleRun4] = Field(..., alias='styleRuns')
    attachment_runs: list[AttachmentRun] = Field(..., alias='attachmentRuns')

class LoggingDirectives6(BaseModel):
    tracking_params: str = Field(..., alias='trackingParams')
    visibility: Visibility

class LoggingContext7(BaseModel):
    logging_directives: LoggingDirectives6 = Field(..., alias='loggingDirectives')

class RendererContext4(BaseModel):
    logging_context: LoggingContext7 = Field(..., alias='loggingContext')

class AttributionViewModel(BaseModel):
    text: Text5
    renderer_context: RendererContext4 = Field(..., alias='rendererContext')

class Attribution(BaseModel):
    attribution_view_model: AttributionViewModel = Field(..., alias='attributionViewModel')

class Source5(BaseModel):
    url: str
    width: int
    height: int

class Image4(BaseModel):
    sources: list[Source5]

class LoggingDirectives7(BaseModel):
    tracking_params: str = Field(..., alias='trackingParams')
    visibility: Visibility

class LoggingContext8(BaseModel):
    logging_directives: LoggingDirectives7 = Field(..., alias='loggingDirectives')

class RendererContext5(BaseModel):
    logging_context: LoggingContext8 = Field(..., alias='loggingContext')

class ImageBannerViewModel(BaseModel):
    image: Image4
    style: str
    renderer_context: RendererContext5 = Field(..., alias='rendererContext')

class Banner(BaseModel):
    image_banner_view_model: ImageBannerViewModel = Field(..., alias='imageBannerViewModel')

class LoggingDirectives8(BaseModel):
    tracking_params: str = Field(..., alias='trackingParams')
    visibility: Visibility

class LoggingContext9(BaseModel):
    logging_directives: LoggingDirectives8 = Field(..., alias='loggingDirectives')

class RendererContext6(BaseModel):
    logging_context: LoggingContext9 = Field(..., alias='loggingContext')

class PageHeaderViewModel(BaseModel):
    title: Title5
    image: Image1
    metadata: Metadata2
    description: Description
    attribution: Attribution
    banner: Banner
    renderer_context: RendererContext6 = Field(..., alias='rendererContext')

class Content13(BaseModel):
    page_header_view_model: PageHeaderViewModel = Field(..., alias='pageHeaderViewModel')

class PageHeaderRenderer(BaseModel):
    page_title: str = Field(..., alias='pageTitle')
    content: Content13

class Header3(BaseModel):
    page_header_renderer: PageHeaderRenderer = Field(..., alias='pageHeaderRenderer')

class Thumbnail(BaseModel):
    url: str
    width: int
    height: int

class Avatar1(BaseModel):
    thumbnails: list[Thumbnail]

class ChannelMetadataRenderer(BaseModel):
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
    channel_metadata_renderer: ChannelMetadataRenderer = Field(..., alias='channelMetadataRenderer')

class IconImage(BaseModel):
    icon_type: str = Field(..., alias='iconType')

class Run1(BaseModel):
    text: str

class TooltipText(BaseModel):
    runs: list[Run1]

class WebCommandMetadata10(BaseModel):
    url: str
    web_page_type: str = Field(..., alias='webPageType')
    root_ve: int = Field(..., alias='rootVe')
    api_url: str = Field(..., alias='apiUrl')

class CommandMetadata10(BaseModel):
    web_command_metadata: WebCommandMetadata10 = Field(..., alias='webCommandMetadata')

class BrowseEndpoint2(BaseModel):
    browse_id: str = Field(..., alias='browseId')

class Endpoint2(BaseModel):
    click_tracking_params: str = Field(..., alias='clickTrackingParams')
    command_metadata: CommandMetadata10 = Field(..., alias='commandMetadata')
    browse_endpoint: BrowseEndpoint2 = Field(..., alias='browseEndpoint')

class TopbarLogoRenderer(BaseModel):
    icon_image: IconImage = Field(..., alias='iconImage')
    tooltip_text: TooltipText = Field(..., alias='tooltipText')
    endpoint: Endpoint2
    tracking_params: str = Field(..., alias='trackingParams')
    override_entity_key: str = Field(..., alias='overrideEntityKey')

class Logo(BaseModel):
    topbar_logo_renderer: TopbarLogoRenderer = Field(..., alias='topbarLogoRenderer')

class PlaceholderText(BaseModel):
    runs: list[Run1]

class WebSearchboxConfig(BaseModel):
    request_language: str = Field(..., alias='requestLanguage')
    request_domain: str = Field(..., alias='requestDomain')
    has_onscreen_keyboard: bool = Field(..., alias='hasOnscreenKeyboard')
    focus_searchbox: bool = Field(..., alias='focusSearchbox')

class Config(BaseModel):
    web_searchbox_config: WebSearchboxConfig = Field(..., alias='webSearchboxConfig')

class WebCommandMetadata11(BaseModel):
    url: str
    web_page_type: str = Field(..., alias='webPageType')
    root_ve: int = Field(..., alias='rootVe')

class CommandMetadata11(BaseModel):
    web_command_metadata: WebCommandMetadata11 = Field(..., alias='webCommandMetadata')

class SearchEndpoint1(BaseModel):
    query: str

class SearchEndpoint(BaseModel):
    click_tracking_params: str = Field(..., alias='clickTrackingParams')
    command_metadata: CommandMetadata11 = Field(..., alias='commandMetadata')
    search_endpoint: SearchEndpoint1 = Field(..., alias='searchEndpoint')

class AccessibilityData11(BaseModel):
    label: str

class AccessibilityData10(BaseModel):
    accessibility_data: AccessibilityData11 = Field(..., alias='accessibilityData')

class ButtonRenderer7(BaseModel):
    style: str
    size: str
    is_disabled: bool = Field(..., alias='isDisabled')
    icon: Icon4
    tracking_params: str = Field(..., alias='trackingParams')
    accessibility_data: AccessibilityData10 = Field(..., alias='accessibilityData')

class ClearButton(BaseModel):
    button_renderer: ButtonRenderer7 = Field(..., alias='buttonRenderer')

class Headline(BaseModel):
    content: str

class DialogHeaderViewModel(BaseModel):
    headline: Headline

class Header5(BaseModel):
    dialog_header_view_model: DialogHeaderViewModel = Field(..., alias='dialogHeaderViewModel')

class ButtonViewModel(BaseModel):
    title: str
    style: str
    tracking_params: str = Field(..., alias='trackingParams')
    is_full_width: bool = Field(..., alias='isFullWidth')
    type: str

class PrimaryButton(BaseModel):
    button_view_model: ButtonViewModel = Field(..., alias='buttonViewModel')

class SecondaryButton(BaseModel):
    button_view_model: ButtonViewModel = Field(..., alias='buttonViewModel')

class PanelFooterViewModel(BaseModel):
    primary_button: PrimaryButton = Field(..., alias='primaryButton')
    secondary_button: SecondaryButton = Field(..., alias='secondaryButton')
    should_hide_divider: bool = Field(..., alias='shouldHideDivider')

class Footer(BaseModel):
    panel_footer_view_model: PanelFooterViewModel = Field(..., alias='panelFooterViewModel')

class Text6(BaseModel):
    content: str

class Paragraph(BaseModel):
    text: Text6

class BasicContentViewModel(BaseModel):
    paragraphs: list[Paragraph]

class Content17(BaseModel):
    basic_content_view_model: BasicContentViewModel = Field(..., alias='basicContentViewModel')

class DialogViewModel(BaseModel):
    header: Header5
    footer: Footer
    content: Content17

class InlineContent(BaseModel):
    dialog_view_model: DialogViewModel = Field(..., alias='dialogViewModel')

class PanelLoadingStrategy(BaseModel):
    inline_content: InlineContent = Field(..., alias='inlineContent')

class ShowDialogCommand(BaseModel):
    panel_loading_strategy: PanelLoadingStrategy = Field(..., alias='panelLoadingStrategy')

class ShowImageSourceDialog(BaseModel):
    click_tracking_params: str = Field(..., alias='clickTrackingParams')
    show_dialog_command: ShowDialogCommand = Field(..., alias='showDialogCommand')

class FusionSearchboxRenderer(BaseModel):
    icon: Icon4
    placeholder_text: PlaceholderText = Field(..., alias='placeholderText')
    config: Config
    tracking_params: str = Field(..., alias='trackingParams')
    search_endpoint: SearchEndpoint = Field(..., alias='searchEndpoint')
    clear_button: ClearButton = Field(..., alias='clearButton')
    show_image_source_dialog: ShowImageSourceDialog = Field(..., alias='showImageSourceDialog')
    disable_ai_appearance: bool = Field(..., alias='disableAiAppearance')

class Searchbox(BaseModel):
    fusion_searchbox_renderer: FusionSearchboxRenderer = Field(..., alias='fusionSearchboxRenderer')

class WebCommandMetadata12(BaseModel):
    send_post: bool = Field(..., alias='sendPost')
    api_url: str = Field(..., alias='apiUrl')

class CommandMetadata12(BaseModel):
    web_command_metadata: WebCommandMetadata12 = Field(..., alias='webCommandMetadata')

class MultiPageMenuRenderer(BaseModel):
    tracking_params: str = Field(..., alias='trackingParams')
    style: str
    show_loading_spinner: bool = Field(..., alias='showLoadingSpinner')

class Popup(BaseModel):
    multi_page_menu_renderer: MultiPageMenuRenderer = Field(..., alias='multiPageMenuRenderer')

class OpenPopupAction(BaseModel):
    popup: Popup
    popup_type: str = Field(..., alias='popupType')
    be_reused: bool = Field(..., alias='beReused')

class Action(BaseModel):
    click_tracking_params: str = Field(..., alias='clickTrackingParams')
    open_popup_action: OpenPopupAction = Field(..., alias='openPopupAction')

class SignalServiceEndpoint(BaseModel):
    signal: str
    actions: list[Action]

class MenuRequest(BaseModel):
    click_tracking_params: str = Field(..., alias='clickTrackingParams')
    command_metadata: CommandMetadata12 = Field(..., alias='commandMetadata')
    signal_service_endpoint: SignalServiceEndpoint = Field(..., alias='signalServiceEndpoint')

class AccessibilityData12(BaseModel):
    label: str

class Accessibility6(BaseModel):
    accessibility_data: AccessibilityData12 = Field(..., alias='accessibilityData')

class TopbarMenuButtonRenderer(BaseModel):
    icon: Icon4
    menu_request: MenuRequest = Field(..., alias='menuRequest')
    tracking_params: str = Field(..., alias='trackingParams')
    accessibility: Accessibility6
    tooltip: str
    style: str

class Text7(BaseModel):
    runs: list[Run1]

class WebCommandMetadata13(BaseModel):
    url: str
    web_page_type: str = Field(..., alias='webPageType')
    root_ve: int = Field(..., alias='rootVe')

class CommandMetadata13(BaseModel):
    web_command_metadata: WebCommandMetadata13 = Field(..., alias='webCommandMetadata')

class SignInEndpoint(BaseModel):
    idam_tag: str = Field(..., alias='idamTag')

class NavigationEndpoint2(BaseModel):
    click_tracking_params: str = Field(..., alias='clickTrackingParams')
    command_metadata: CommandMetadata13 = Field(..., alias='commandMetadata')
    sign_in_endpoint: SignInEndpoint = Field(..., alias='signInEndpoint')

class ButtonRenderer8(BaseModel):
    style: str
    size: str
    text: Text7
    icon: Icon4
    navigation_endpoint: NavigationEndpoint2 = Field(..., alias='navigationEndpoint')
    tracking_params: str = Field(..., alias='trackingParams')
    target_id: str = Field(..., alias='targetId')

class TopbarButton(BaseModel):
    topbar_menu_button_renderer: TopbarMenuButtonRenderer | None = Field(None, alias='topbarMenuButtonRenderer')
    button_renderer: ButtonRenderer8 | None = Field(None, alias='buttonRenderer')

class Title7(BaseModel):
    runs: list[Run1]

class Title8(BaseModel):
    runs: list[Run1]

class Label(BaseModel):
    runs: list[Run1]

class HotkeyAccessibilityLabel(BaseModel):
    accessibility_data: AccessibilityData12 = Field(..., alias='accessibilityData')

class HotkeyDialogSectionOptionRenderer(BaseModel):
    label: Label
    hotkey: str
    hotkey_accessibility_label: HotkeyAccessibilityLabel | None = Field(None, alias='hotkeyAccessibilityLabel')

class Option(BaseModel):
    hotkey_dialog_section_option_renderer: HotkeyDialogSectionOptionRenderer = Field(..., alias='hotkeyDialogSectionOptionRenderer')

class HotkeyDialogSectionRenderer(BaseModel):
    title: Title8
    options: list[Option]

class Section(BaseModel):
    hotkey_dialog_section_renderer: HotkeyDialogSectionRenderer = Field(..., alias='hotkeyDialogSectionRenderer')

class Text8(BaseModel):
    runs: list[Run1]

class ButtonRenderer9(BaseModel):
    style: str
    size: str
    is_disabled: bool = Field(..., alias='isDisabled')
    text: Text8
    tracking_params: str = Field(..., alias='trackingParams')

class DismissButton(BaseModel):
    button_renderer: ButtonRenderer9 = Field(..., alias='buttonRenderer')

class HotkeyDialogRenderer(BaseModel):
    title: Title7
    sections: list[Section]
    dismiss_button: DismissButton = Field(..., alias='dismissButton')
    tracking_params: str = Field(..., alias='trackingParams')

class HotkeyDialog(BaseModel):
    hotkey_dialog_renderer: HotkeyDialogRenderer = Field(..., alias='hotkeyDialogRenderer')

class WebCommandMetadata14(BaseModel):
    send_post: bool = Field(..., alias='sendPost')

class CommandMetadata14(BaseModel):
    web_command_metadata: WebCommandMetadata14 = Field(..., alias='webCommandMetadata')

class SignalAction(BaseModel):
    signal: str

class Action1(BaseModel):
    click_tracking_params: str = Field(..., alias='clickTrackingParams')
    signal_action: SignalAction = Field(..., alias='signalAction')

class SignalServiceEndpoint1(BaseModel):
    signal: str
    actions: list[Action1]

class Command4(BaseModel):
    click_tracking_params: str = Field(..., alias='clickTrackingParams')
    command_metadata: CommandMetadata14 = Field(..., alias='commandMetadata')
    signal_service_endpoint: SignalServiceEndpoint1 = Field(..., alias='signalServiceEndpoint')

class ButtonRenderer10(BaseModel):
    tracking_params: str = Field(..., alias='trackingParams')
    command: Command4

class BackButton(BaseModel):
    button_renderer: ButtonRenderer10 = Field(..., alias='buttonRenderer')

class CommandMetadata15(BaseModel):
    web_command_metadata: WebCommandMetadata14 = Field(..., alias='webCommandMetadata')

class Action2(BaseModel):
    click_tracking_params: str = Field(..., alias='clickTrackingParams')
    signal_action: SignalAction = Field(..., alias='signalAction')

class SignalServiceEndpoint2(BaseModel):
    signal: str
    actions: list[Action2]

class Command5(BaseModel):
    click_tracking_params: str = Field(..., alias='clickTrackingParams')
    command_metadata: CommandMetadata15 = Field(..., alias='commandMetadata')
    signal_service_endpoint: SignalServiceEndpoint2 = Field(..., alias='signalServiceEndpoint')

class ButtonRenderer11(BaseModel):
    tracking_params: str = Field(..., alias='trackingParams')
    command: Command5

class ForwardButton(BaseModel):
    button_renderer: ButtonRenderer11 = Field(..., alias='buttonRenderer')

class Text9(BaseModel):
    runs: list[Run1]

class CommandMetadata16(BaseModel):
    web_command_metadata: WebCommandMetadata14 = Field(..., alias='webCommandMetadata')

class Action3(BaseModel):
    click_tracking_params: str = Field(..., alias='clickTrackingParams')
    signal_action: SignalAction = Field(..., alias='signalAction')

class SignalServiceEndpoint3(BaseModel):
    signal: str
    actions: list[Action3]

class Command6(BaseModel):
    click_tracking_params: str = Field(..., alias='clickTrackingParams')
    command_metadata: CommandMetadata16 = Field(..., alias='commandMetadata')
    signal_service_endpoint: SignalServiceEndpoint3 = Field(..., alias='signalServiceEndpoint')

class ButtonRenderer12(BaseModel):
    style: str
    size: str
    is_disabled: bool = Field(..., alias='isDisabled')
    text: Text9
    tracking_params: str = Field(..., alias='trackingParams')
    command: Command6

class A11ySkipNavigationButton(BaseModel):
    button_renderer: ButtonRenderer12 = Field(..., alias='buttonRenderer')

class CommandMetadata17(BaseModel):
    web_command_metadata: WebCommandMetadata14 = Field(..., alias='webCommandMetadata')

class PlaceholderHeader(BaseModel):
    runs: list[Run1]

class PromptHeader(BaseModel):
    runs: list[Run1]

class ExampleQuery1(BaseModel):
    runs: list[Run1]

class ExampleQuery2(BaseModel):
    runs: list[Run1]

class PromptMicrophoneLabel(BaseModel):
    runs: list[Run1]

class LoadingHeader(BaseModel):
    runs: list[Run1]

class ConnectionErrorHeader(BaseModel):
    runs: list[Run1]

class ConnectionErrorMicrophoneLabel(BaseModel):
    runs: list[Run1]

class PermissionsHeader(BaseModel):
    runs: list[Run1]

class PermissionsSubtext(BaseModel):
    runs: list[Run1]

class DisabledHeader(BaseModel):
    runs: list[Run1]

class DisabledSubtext(BaseModel):
    runs: list[Run1]

class MicrophoneButtonAriaLabel(BaseModel):
    runs: list[Run1]

class AccessibilityData14(BaseModel):
    accessibility_data: AccessibilityData12 = Field(..., alias='accessibilityData')

class ButtonRenderer14(BaseModel):
    style: str
    size: str
    is_disabled: bool = Field(..., alias='isDisabled')
    icon: Icon4
    tracking_params: str = Field(..., alias='trackingParams')
    accessibility_data: AccessibilityData14 = Field(..., alias='accessibilityData')

class ExitButton(BaseModel):
    button_renderer: ButtonRenderer14 = Field(..., alias='buttonRenderer')

class MicrophoneOffPromptHeader(BaseModel):
    runs: list[Run1]

class VoiceSearchDialogRenderer(BaseModel):
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
    voice_search_dialog_renderer: VoiceSearchDialogRenderer = Field(..., alias='voiceSearchDialogRenderer')

class OpenPopupAction1(BaseModel):
    popup: Popup1
    popup_type: str = Field(..., alias='popupType')

class Action4(BaseModel):
    click_tracking_params: str = Field(..., alias='clickTrackingParams')
    open_popup_action: OpenPopupAction1 = Field(..., alias='openPopupAction')

class SignalServiceEndpoint4(BaseModel):
    signal: str
    actions: list[Action4]

class ServiceEndpoint(BaseModel):
    click_tracking_params: str = Field(..., alias='clickTrackingParams')
    command_metadata: CommandMetadata17 = Field(..., alias='commandMetadata')
    signal_service_endpoint: SignalServiceEndpoint4 = Field(..., alias='signalServiceEndpoint')

class AccessibilityData17(BaseModel):
    label: str

class AccessibilityData16(BaseModel):
    accessibility_data: AccessibilityData17 = Field(..., alias='accessibilityData')

class ButtonRenderer13(BaseModel):
    style: str
    size: str
    is_disabled: bool = Field(..., alias='isDisabled')
    service_endpoint: ServiceEndpoint = Field(..., alias='serviceEndpoint')
    icon: Icon4
    tooltip: str
    tracking_params: str = Field(..., alias='trackingParams')
    accessibility_data: AccessibilityData16 = Field(..., alias='accessibilityData')

class VoiceSearchButton(BaseModel):
    button_renderer: ButtonRenderer13 = Field(..., alias='buttonRenderer')

class DesktopTopbarRenderer(BaseModel):
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
    desktop_topbar_renderer: DesktopTopbarRenderer = Field(..., alias='desktopTopbarRenderer')

class Thumbnail1(BaseModel):
    thumbnails: list[Thumbnail]

class LinkAlternate(BaseModel):
    href_url: str = Field(..., alias='hrefUrl')

class MicroformatDataRenderer(BaseModel):
    url_canonical: str = Field(..., alias='urlCanonical')
    title: str
    description: str
    thumbnail: Thumbnail1
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
    microformat_data_renderer: MicroformatDataRenderer = Field(..., alias='microformatDataRenderer')

class Thumbnail4(BaseModel):
    url: str
    width: int
    height: int

class SampledThumbnailColor(BaseModel):
    red: int
    green: int
    blue: int

class DarkColorPalette(BaseModel):
    section2_color: int = Field(..., alias='section2Color')
    icon_inactive_color: int = Field(..., alias='iconInactiveColor')
    icon_disabled_color: int = Field(..., alias='iconDisabledColor')

class VibrantColorPalette(BaseModel):
    icon_inactive_color: int = Field(..., alias='iconInactiveColor')

class Thumbnail3(BaseModel):
    thumbnails: list[Thumbnail4]
    sampled_thumbnail_color: SampledThumbnailColor = Field(..., alias='sampledThumbnailColor')
    dark_color_palette: DarkColorPalette = Field(..., alias='darkColorPalette')
    vibrant_color_palette: VibrantColorPalette = Field(..., alias='vibrantColorPalette')

class WebCommandMetadata18(BaseModel):
    url: str
    web_page_type: str = Field(..., alias='webPageType')
    root_ve: int = Field(..., alias='rootVe')

class CommandMetadata18(BaseModel):
    web_command_metadata: WebCommandMetadata18 = Field(..., alias='webCommandMetadata')

class LoggingContext10(BaseModel):
    vss_logging_context: VssLoggingContext = Field(..., alias='vssLoggingContext')

class Html5PlaybackOnesieConfig3(BaseModel):
    common_config: CommonConfig = Field(..., alias='commonConfig')

class WatchEndpointSupportedOnesieConfig3(BaseModel):
    html5_playback_onesie_config: Html5PlaybackOnesieConfig3 = Field(..., alias='html5PlaybackOnesieConfig')

class WatchEndpoint3(BaseModel):
    video_id: str = Field(..., alias='videoId')
    playlist_id: str = Field(..., alias='playlistId')
    params: str
    logging_context: LoggingContext10 = Field(..., alias='loggingContext')
    watch_endpoint_supported_onesie_config: WatchEndpointSupportedOnesieConfig3 = Field(..., alias='watchEndpointSupportedOnesieConfig')
    player_params: str | None = Field(None, alias='playerParams')

class NavigationEndpoint3(BaseModel):
    click_tracking_params: str = Field(..., alias='clickTrackingParams')
    command_metadata: CommandMetadata18 = Field(..., alias='commandMetadata')
    watch_endpoint: WatchEndpoint3 = Field(..., alias='watchEndpoint')

class Run23(BaseModel):
    text: str
    navigation_endpoint: NavigationEndpoint3 = Field(..., alias='navigationEndpoint')

class Title9(BaseModel):
    runs: list[Run23]

class WebCommandMetadata19(BaseModel):
    url: str
    web_page_type: str = Field(..., alias='webPageType')
    root_ve: int = Field(..., alias='rootVe')
    api_url: str = Field(..., alias='apiUrl')

class CommandMetadata19(BaseModel):
    web_command_metadata: WebCommandMetadata19 = Field(..., alias='webCommandMetadata')

class BrowseEndpoint3(BaseModel):
    browse_id: str = Field(..., alias='browseId')
    canonical_base_url: str = Field(..., alias='canonicalBaseUrl')

class NavigationEndpoint4(BaseModel):
    click_tracking_params: str = Field(..., alias='clickTrackingParams')
    command_metadata: CommandMetadata19 = Field(..., alias='commandMetadata')
    browse_endpoint: BrowseEndpoint3 = Field(..., alias='browseEndpoint')

class Run24(BaseModel):
    text: str
    navigation_endpoint: NavigationEndpoint4 | None = Field(None, alias='navigationEndpoint')

class ShortBylineText(BaseModel):
    runs: list[Run24]

class Run25(BaseModel):
    text: str

class VideoCountText(BaseModel):
    runs: list[Run25]

class WebCommandMetadata20(BaseModel):
    url: str
    web_page_type: str = Field(..., alias='webPageType')
    root_ve: int = Field(..., alias='rootVe')

class CommandMetadata20(BaseModel):
    web_command_metadata: WebCommandMetadata20 = Field(..., alias='webCommandMetadata')

class LoggingContext11(BaseModel):
    vss_logging_context: VssLoggingContext = Field(..., alias='vssLoggingContext')

class Html5PlaybackOnesieConfig4(BaseModel):
    common_config: CommonConfig = Field(..., alias='commonConfig')

class WatchEndpointSupportedOnesieConfig4(BaseModel):
    html5_playback_onesie_config: Html5PlaybackOnesieConfig4 = Field(..., alias='html5PlaybackOnesieConfig')

class WatchEndpoint4(BaseModel):
    video_id: str = Field(..., alias='videoId')
    playlist_id: str = Field(..., alias='playlistId')
    params: str
    logging_context: LoggingContext11 = Field(..., alias='loggingContext')
    watch_endpoint_supported_onesie_config: WatchEndpointSupportedOnesieConfig4 = Field(..., alias='watchEndpointSupportedOnesieConfig')
    player_params: str | None = Field(None, alias='playerParams')

class NavigationEndpoint5(BaseModel):
    click_tracking_params: str = Field(..., alias='clickTrackingParams')
    command_metadata: CommandMetadata20 = Field(..., alias='commandMetadata')
    watch_endpoint: WatchEndpoint4 = Field(..., alias='watchEndpoint')

class VideoCountShortText(BaseModel):
    simple_text: str = Field(..., alias='simpleText')

class Thumbnail5(BaseModel):
    url: str
    width: int
    height: int

class SidebarThumbnail(BaseModel):
    thumbnails: list[Thumbnail5]

class Run26(BaseModel):
    text: str
    bold: bool | None = None

class ThumbnailText(BaseModel):
    runs: list[Run26]

class Thumbnail6(BaseModel):
    thumbnails: list[Thumbnail5]
    sampled_thumbnail_color: SampledThumbnailColor = Field(..., alias='sampledThumbnailColor')
    dark_color_palette: DarkColorPalette = Field(..., alias='darkColorPalette')
    vibrant_color_palette: VibrantColorPalette = Field(..., alias='vibrantColorPalette')

class PlaylistCustomThumbnailRenderer(BaseModel):
    thumbnail: Thumbnail6

class ThumbnailRenderer(BaseModel):
    playlist_custom_thumbnail_renderer: PlaylistCustomThumbnailRenderer = Field(..., alias='playlistCustomThumbnailRenderer')

class WebCommandMetadata21(BaseModel):
    url: str
    web_page_type: str = Field(..., alias='webPageType')
    root_ve: int = Field(..., alias='rootVe')
    api_url: str = Field(..., alias='apiUrl')

class CommandMetadata21(BaseModel):
    web_command_metadata: WebCommandMetadata21 = Field(..., alias='webCommandMetadata')

class NavigationEndpoint6(BaseModel):
    click_tracking_params: str = Field(..., alias='clickTrackingParams')
    command_metadata: CommandMetadata21 = Field(..., alias='commandMetadata')
    browse_endpoint: BrowseEndpoint3 = Field(..., alias='browseEndpoint')

class Run27(BaseModel):
    text: str
    navigation_endpoint: NavigationEndpoint6 | None = Field(None, alias='navigationEndpoint')

class LongBylineText(BaseModel):
    runs: list[Run27]

class Text10(BaseModel):
    simple_text: str = Field(..., alias='simpleText')

class ThumbnailOverlayBottomPanelRenderer(BaseModel):
    text: Text10
    icon: Icon4

class Run28(BaseModel):
    text: str

class Text11(BaseModel):
    runs: list[Run28]

class ThumbnailOverlayHoverTextRenderer(BaseModel):
    text: Text11
    icon: Icon4

class Text12(BaseModel):
    runs: list[Run28]

class ThumbnailOverlayNowPlayingRenderer(BaseModel):
    text: Text12

class ThumbnailOverlay(BaseModel):
    thumbnail_overlay_bottom_panel_renderer: ThumbnailOverlayBottomPanelRenderer | None = Field(None, alias='thumbnailOverlayBottomPanelRenderer')
    thumbnail_overlay_hover_text_renderer: ThumbnailOverlayHoverTextRenderer | None = Field(None, alias='thumbnailOverlayHoverTextRenderer')
    thumbnail_overlay_now_playing_renderer: ThumbnailOverlayNowPlayingRenderer | None = Field(None, alias='thumbnailOverlayNowPlayingRenderer')

class CommandMetadata22(BaseModel):
    web_command_metadata: WebCommandMetadata21 = Field(..., alias='webCommandMetadata')

class BrowseEndpoint5(BaseModel):
    browse_id: str = Field(..., alias='browseId')

class NavigationEndpoint7(BaseModel):
    click_tracking_params: str = Field(..., alias='clickTrackingParams')
    command_metadata: CommandMetadata22 = Field(..., alias='commandMetadata')
    browse_endpoint: BrowseEndpoint5 = Field(..., alias='browseEndpoint')

class Run30(BaseModel):
    text: str
    navigation_endpoint: NavigationEndpoint7 = Field(..., alias='navigationEndpoint')

class ViewPlaylistText(BaseModel):
    runs: list[Run30]

class PublishedTimeText(BaseModel):
    simple_text: str = Field(..., alias='simpleText')

class GridPlaylistRenderer(BaseModel):
    playlist_id: str = Field(..., alias='playlistId')
    thumbnail: Thumbnail3
    title: Title9
    short_byline_text: ShortBylineText = Field(..., alias='shortBylineText')
    video_count_text: VideoCountText = Field(..., alias='videoCountText')
    navigation_endpoint: NavigationEndpoint5 = Field(..., alias='navigationEndpoint')
    video_count_short_text: VideoCountShortText = Field(..., alias='videoCountShortText')
    tracking_params: str = Field(..., alias='trackingParams')
    sidebar_thumbnails: list[SidebarThumbnail] | None = Field(None, alias='sidebarThumbnails')
    thumbnail_text: ThumbnailText = Field(..., alias='thumbnailText')
    thumbnail_renderer: ThumbnailRenderer = Field(..., alias='thumbnailRenderer')
    long_byline_text: LongBylineText = Field(..., alias='longBylineText')
    thumbnail_overlays: list[ThumbnailOverlay] = Field(..., alias='thumbnailOverlays')
    view_playlist_text: ViewPlaylistText = Field(..., alias='viewPlaylistText')
    published_time_text: PublishedTimeText | None = Field(None, alias='publishedTimeText')

class WebCommandMetadata23(BaseModel):
    send_post: bool = Field(..., alias='sendPost')
    api_url: str = Field(..., alias='apiUrl')

class CommandMetadata23(BaseModel):
    web_command_metadata: WebCommandMetadata23 = Field(..., alias='webCommandMetadata')

class ContinuationEndpoint4(BaseModel):
    click_tracking_params: str = Field(..., alias='clickTrackingParams')
    command_metadata: CommandMetadata23 = Field(..., alias='commandMetadata')
    continuation_command: ContinuationCommand = Field(..., alias='continuationCommand')

class ContinuationItemRenderer4(BaseModel):
    trigger: str
    continuation_endpoint: ContinuationEndpoint4 = Field(..., alias='continuationEndpoint')

class Item1(BaseModel):
    grid_playlist_renderer: GridPlaylistRenderer | None = Field(None, alias='gridPlaylistRenderer')
    continuation_item_renderer: ContinuationItemRenderer4 | None = Field(None, alias='continuationItemRenderer')

class GridRenderer(BaseModel):
    items: list[Item1]
    is_collapsible: bool = Field(..., alias='isCollapsible')
    tracking_params: str = Field(..., alias='trackingParams')
    target_id: UUID = Field(..., alias='targetId')

class Thumbnail9(BaseModel):
    url: str
    width: int
    height: int

class Thumbnail8(BaseModel):
    thumbnails: list[Thumbnail9]
    sampled_thumbnail_color: SampledThumbnailColor = Field(..., alias='sampledThumbnailColor')
    dark_color_palette: DarkColorPalette = Field(..., alias='darkColorPalette')
    vibrant_color_palette: VibrantColorPalette = Field(..., alias='vibrantColorPalette')

class WebCommandMetadata24(BaseModel):
    url: str
    web_page_type: str = Field(..., alias='webPageType')
    root_ve: int = Field(..., alias='rootVe')

class CommandMetadata24(BaseModel):
    web_command_metadata: WebCommandMetadata24 = Field(..., alias='webCommandMetadata')

class LoggingContext12(BaseModel):
    vss_logging_context: VssLoggingContext = Field(..., alias='vssLoggingContext')

class Html5PlaybackOnesieConfig5(BaseModel):
    common_config: CommonConfig = Field(..., alias='commonConfig')

class WatchEndpointSupportedOnesieConfig5(BaseModel):
    html5_playback_onesie_config: Html5PlaybackOnesieConfig5 = Field(..., alias='html5PlaybackOnesieConfig')

class WatchEndpoint5(BaseModel):
    video_id: str = Field(..., alias='videoId')
    playlist_id: str = Field(..., alias='playlistId')
    params: str
    player_params: str | None = Field(None, alias='playerParams')
    logging_context: LoggingContext12 = Field(..., alias='loggingContext')
    watch_endpoint_supported_onesie_config: WatchEndpointSupportedOnesieConfig5 = Field(..., alias='watchEndpointSupportedOnesieConfig')

class NavigationEndpoint8(BaseModel):
    click_tracking_params: str = Field(..., alias='clickTrackingParams')
    command_metadata: CommandMetadata24 = Field(..., alias='commandMetadata')
    watch_endpoint: WatchEndpoint5 = Field(..., alias='watchEndpoint')

class Run31(BaseModel):
    text: str
    navigation_endpoint: NavigationEndpoint8 = Field(..., alias='navigationEndpoint')

class Title10(BaseModel):
    runs: list[Run31]

class WebCommandMetadata25(BaseModel):
    url: str
    web_page_type: str = Field(..., alias='webPageType')
    root_ve: int = Field(..., alias='rootVe')
    api_url: str = Field(..., alias='apiUrl')

class CommandMetadata25(BaseModel):
    web_command_metadata: WebCommandMetadata25 = Field(..., alias='webCommandMetadata')

class BrowseEndpoint6(BaseModel):
    browse_id: str = Field(..., alias='browseId')
    canonical_base_url: str = Field(..., alias='canonicalBaseUrl')

class NavigationEndpoint9(BaseModel):
    click_tracking_params: str = Field(..., alias='clickTrackingParams')
    command_metadata: CommandMetadata25 = Field(..., alias='commandMetadata')
    browse_endpoint: BrowseEndpoint6 = Field(..., alias='browseEndpoint')

class Run32(BaseModel):
    text: str
    navigation_endpoint: NavigationEndpoint9 | None = Field(None, alias='navigationEndpoint')

class ShortBylineText1(BaseModel):
    runs: list[Run32]

class Run33(BaseModel):
    text: str

class VideoCountText1(BaseModel):
    runs: list[Run33]

class WebCommandMetadata26(BaseModel):
    url: str
    web_page_type: str = Field(..., alias='webPageType')
    root_ve: int = Field(..., alias='rootVe')

class CommandMetadata26(BaseModel):
    web_command_metadata: WebCommandMetadata26 = Field(..., alias='webCommandMetadata')

class LoggingContext13(BaseModel):
    vss_logging_context: VssLoggingContext = Field(..., alias='vssLoggingContext')

class Html5PlaybackOnesieConfig6(BaseModel):
    common_config: CommonConfig = Field(..., alias='commonConfig')

class WatchEndpointSupportedOnesieConfig6(BaseModel):
    html5_playback_onesie_config: Html5PlaybackOnesieConfig6 = Field(..., alias='html5PlaybackOnesieConfig')

class WatchEndpoint6(BaseModel):
    video_id: str = Field(..., alias='videoId')
    playlist_id: str = Field(..., alias='playlistId')
    params: str
    player_params: str | None = Field(None, alias='playerParams')
    logging_context: LoggingContext13 = Field(..., alias='loggingContext')
    watch_endpoint_supported_onesie_config: WatchEndpointSupportedOnesieConfig6 = Field(..., alias='watchEndpointSupportedOnesieConfig')

class NavigationEndpoint10(BaseModel):
    click_tracking_params: str = Field(..., alias='clickTrackingParams')
    command_metadata: CommandMetadata26 = Field(..., alias='commandMetadata')
    watch_endpoint: WatchEndpoint6 = Field(..., alias='watchEndpoint')

class Thumbnail10(BaseModel):
    url: str
    width: int
    height: int

class SidebarThumbnail1(BaseModel):
    thumbnails: list[Thumbnail10]

class Run34(BaseModel):
    text: str
    bold: bool | None = None

class ThumbnailText1(BaseModel):
    runs: list[Run34]

class Thumbnail11(BaseModel):
    thumbnails: list[Thumbnail10]
    sampled_thumbnail_color: SampledThumbnailColor = Field(..., alias='sampledThumbnailColor')
    dark_color_palette: DarkColorPalette = Field(..., alias='darkColorPalette')
    vibrant_color_palette: VibrantColorPalette = Field(..., alias='vibrantColorPalette')

class PlaylistCustomThumbnailRenderer1(BaseModel):
    thumbnail: Thumbnail11

class ThumbnailRenderer1(BaseModel):
    playlist_custom_thumbnail_renderer: PlaylistCustomThumbnailRenderer1 = Field(..., alias='playlistCustomThumbnailRenderer')

class WebCommandMetadata27(BaseModel):
    url: str
    web_page_type: str = Field(..., alias='webPageType')
    root_ve: int = Field(..., alias='rootVe')
    api_url: str = Field(..., alias='apiUrl')

class CommandMetadata27(BaseModel):
    web_command_metadata: WebCommandMetadata27 = Field(..., alias='webCommandMetadata')

class NavigationEndpoint11(BaseModel):
    click_tracking_params: str = Field(..., alias='clickTrackingParams')
    command_metadata: CommandMetadata27 = Field(..., alias='commandMetadata')
    browse_endpoint: BrowseEndpoint6 = Field(..., alias='browseEndpoint')

class Run35(BaseModel):
    text: str
    navigation_endpoint: NavigationEndpoint11 | None = Field(None, alias='navigationEndpoint')

class LongBylineText1(BaseModel):
    runs: list[Run35]

class Text13(BaseModel):
    simple_text: str = Field(..., alias='simpleText')

class ThumbnailOverlayBottomPanelRenderer1(BaseModel):
    text: Text13
    icon: Icon4

class Run36(BaseModel):
    text: str

class Text14(BaseModel):
    runs: list[Run36]

class ThumbnailOverlayHoverTextRenderer1(BaseModel):
    text: Text14
    icon: Icon4

class Text15(BaseModel):
    runs: list[Run36]

class ThumbnailOverlayNowPlayingRenderer1(BaseModel):
    text: Text15

class ThumbnailOverlay1(BaseModel):
    thumbnail_overlay_bottom_panel_renderer: ThumbnailOverlayBottomPanelRenderer1 | None = Field(None, alias='thumbnailOverlayBottomPanelRenderer')
    thumbnail_overlay_hover_text_renderer: ThumbnailOverlayHoverTextRenderer1 | None = Field(None, alias='thumbnailOverlayHoverTextRenderer')
    thumbnail_overlay_now_playing_renderer: ThumbnailOverlayNowPlayingRenderer1 | None = Field(None, alias='thumbnailOverlayNowPlayingRenderer')

class CommandMetadata28(BaseModel):
    web_command_metadata: WebCommandMetadata27 = Field(..., alias='webCommandMetadata')

class BrowseEndpoint8(BaseModel):
    browse_id: str = Field(..., alias='browseId')

class NavigationEndpoint12(BaseModel):
    click_tracking_params: str = Field(..., alias='clickTrackingParams')
    command_metadata: CommandMetadata28 = Field(..., alias='commandMetadata')
    browse_endpoint: BrowseEndpoint8 = Field(..., alias='browseEndpoint')

class Run38(BaseModel):
    text: str
    navigation_endpoint: NavigationEndpoint12 = Field(..., alias='navigationEndpoint')

class ViewPlaylistText1(BaseModel):
    runs: list[Run38]

class GridPlaylistRenderer1(BaseModel):
    playlist_id: str = Field(..., alias='playlistId')
    thumbnail: Thumbnail8
    title: Title10
    short_byline_text: ShortBylineText1 = Field(..., alias='shortBylineText')
    video_count_text: VideoCountText1 = Field(..., alias='videoCountText')
    navigation_endpoint: NavigationEndpoint10 = Field(..., alias='navigationEndpoint')
    video_count_short_text: VideoCountShortText = Field(..., alias='videoCountShortText')
    tracking_params: str = Field(..., alias='trackingParams')
    sidebar_thumbnails: list[SidebarThumbnail1] | None = Field(None, alias='sidebarThumbnails')
    thumbnail_text: ThumbnailText1 = Field(..., alias='thumbnailText')
    thumbnail_renderer: ThumbnailRenderer1 = Field(..., alias='thumbnailRenderer')
    long_byline_text: LongBylineText1 = Field(..., alias='longBylineText')
    thumbnail_overlays: list[ThumbnailOverlay1] = Field(..., alias='thumbnailOverlays')
    view_playlist_text: ViewPlaylistText1 = Field(..., alias='viewPlaylistText')
    published_time_text: PublishedTimeText | None = Field(None, alias='publishedTimeText')

class ContinuationItem(BaseModel):
    grid_renderer: GridRenderer | None = Field(None, alias='gridRenderer')
    grid_playlist_renderer: GridPlaylistRenderer1 | None = Field(None, alias='gridPlaylistRenderer')

class AppendContinuationItemsAction(BaseModel):
    continuation_items: list[ContinuationItem] = Field(..., alias='continuationItems')
    target_id: UUID = Field(..., alias='targetId')

class OnResponseReceivedEndpoint(BaseModel):
    click_tracking_params: str = Field(..., alias='clickTrackingParams')
    append_continuation_items_action: AppendContinuationItemsAction = Field(..., alias='appendContinuationItemsAction')

class TopicModel(BaseModel):
    response_context: ResponseContext = Field(..., alias='responseContext')
    contents: Contents | None = None
    header: Header3 | None = None
    metadata: Metadata3 | None = None
    tracking_params: str = Field(..., alias='trackingParams')
    topbar: Topbar | None = None
    microformat: Microformat | None = None
    on_response_received_endpoints: list[OnResponseReceivedEndpoint] | None = Field(None, alias='onResponseReceivedEndpoints')
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
