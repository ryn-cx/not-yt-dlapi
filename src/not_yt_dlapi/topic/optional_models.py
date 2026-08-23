from typing import Any, Self
from pydantic import ModelWrapValidatorHandler, PrivateAttr, model_validator
from pydantic import BaseModel, ConfigDict, Field
from uuid import UUID

class Param(BaseModel):
    model_config = ConfigDict(extra='ignore')
    key: str | None = None
    value: str | None = None

class ServiceTrackingParam(BaseModel):
    model_config = ConfigDict(extra='ignore')
    service: str | None = None
    params: list[Param] | None = None

class MainAppWebResponseContext(BaseModel):
    model_config = ConfigDict(extra='ignore')
    logged_out: bool | None = Field(None, alias='loggedOut')
    tracking_param: str | None = Field(None, alias='trackingParam')

class WebResponseContextPreloadData(BaseModel):
    model_config = ConfigDict(extra='ignore')
    preload_message_names: list[str] | None = Field(None, alias='preloadMessageNames')

class WebResponseContextExtensionData(BaseModel):
    model_config = ConfigDict(extra='ignore')
    web_response_context_preload_data: WebResponseContextPreloadData | None = Field(None, alias='webResponseContextPreloadData')
    has_decorated: bool | None = Field(None, alias='hasDecorated')

class ResponseContext(BaseModel):
    model_config = ConfigDict(extra='ignore')
    visitor_data: str | None = Field(None, alias='visitorData')
    service_tracking_params: list[ServiceTrackingParam] | None = Field(None, alias='serviceTrackingParams')
    max_age_seconds: int | None = Field(None, alias='maxAgeSeconds')
    main_app_web_response_context: MainAppWebResponseContext | None = Field(None, alias='mainAppWebResponseContext')
    response_id: str | None = Field(None, alias='responseId')
    web_response_context_extension_data: WebResponseContextExtensionData | None = Field(None, alias='webResponseContextExtensionData')

class WebCommandMetadata(BaseModel):
    model_config = ConfigDict(extra='ignore')
    url: str | None = None
    web_page_type: str | None = Field(None, alias='webPageType')
    root_ve: int | None = Field(None, alias='rootVe')
    api_url: str | None = Field(None, alias='apiUrl')

class CommandMetadata(BaseModel):
    model_config = ConfigDict(extra='ignore')
    web_command_metadata: WebCommandMetadata | None = Field(None, alias='webCommandMetadata')

class BrowseEndpoint(BaseModel):
    model_config = ConfigDict(extra='ignore')
    browse_id: str | None = Field(None, alias='browseId')
    params: str | None = None
    canonical_base_url: str | None = Field(None, alias='canonicalBaseUrl')

class Endpoint(BaseModel):
    model_config = ConfigDict(extra='ignore')
    click_tracking_params: str | None = Field(None, alias='clickTrackingParams')
    command_metadata: CommandMetadata | None = Field(None, alias='commandMetadata')
    browse_endpoint: BrowseEndpoint | None = Field(None, alias='browseEndpoint')

class Title1(BaseModel):
    model_config = ConfigDict(extra='ignore')
    simple_text: str | None = Field(None, alias='simpleText')

class Icon(BaseModel):
    model_config = ConfigDict(extra='ignore')
    icon_type: str | None = Field(None, alias='iconType')

class Accessibility(BaseModel):
    model_config = ConfigDict(extra='ignore')
    label: str | None = None

class AccessibilityData1(BaseModel):
    model_config = ConfigDict(extra='ignore')
    label: str | None = None

class AccessibilityData(BaseModel):
    model_config = ConfigDict(extra='ignore')
    accessibility_data: AccessibilityData1 | None = Field(None, alias='accessibilityData')

class ChangeEngagementPanelVisibilityAction(BaseModel):
    model_config = ConfigDict(extra='ignore')
    target_id: UUID | None = Field(None, alias='targetId')
    visibility: str | None = None

class Command(BaseModel):
    model_config = ConfigDict(extra='ignore')
    click_tracking_params: str | None = Field(None, alias='clickTrackingParams')
    change_engagement_panel_visibility_action: ChangeEngagementPanelVisibilityAction | None = Field(None, alias='changeEngagementPanelVisibilityAction')

class ButtonRenderer(BaseModel):
    model_config = ConfigDict(extra='ignore')
    style: str | None = None
    size: str | None = None
    is_disabled: bool | None = Field(None, alias='isDisabled')
    icon: Icon | None = None
    accessibility: Accessibility | None = None
    tracking_params: str | None = Field(None, alias='trackingParams')
    accessibility_data: AccessibilityData | None = Field(None, alias='accessibilityData')
    command: Command | None = None

class VisibilityButton(BaseModel):
    model_config = ConfigDict(extra='ignore')
    button_renderer: ButtonRenderer | None = Field(None, alias='buttonRenderer')

class EngagementPanelTitleHeaderRenderer(BaseModel):
    model_config = ConfigDict(extra='ignore')
    title: Title1 | None = None
    visibility_button: VisibilityButton | None = Field(None, alias='visibilityButton')
    tracking_params: str | None = Field(None, alias='trackingParams')

class Header(BaseModel):
    model_config = ConfigDict(extra='ignore')
    engagement_panel_title_header_renderer: EngagementPanelTitleHeaderRenderer | None = Field(None, alias='engagementPanelTitleHeaderRenderer')

class WebCommandMetadata1(BaseModel):
    model_config = ConfigDict(extra='ignore')
    send_post: bool | None = Field(None, alias='sendPost')
    api_url: str | None = Field(None, alias='apiUrl')

class CommandMetadata1(BaseModel):
    model_config = ConfigDict(extra='ignore')
    web_command_metadata: WebCommandMetadata1 | None = Field(None, alias='webCommandMetadata')

class ContinuationCommand(BaseModel):
    model_config = ConfigDict(extra='ignore')
    token: str | None = None
    request: str | None = None

class ContinuationEndpoint(BaseModel):
    model_config = ConfigDict(extra='ignore')
    click_tracking_params: str | None = Field(None, alias='clickTrackingParams')
    command_metadata: CommandMetadata1 | None = Field(None, alias='commandMetadata')
    continuation_command: ContinuationCommand | None = Field(None, alias='continuationCommand')

class ContinuationItemRenderer(BaseModel):
    model_config = ConfigDict(extra='ignore')
    trigger: str | None = None
    continuation_endpoint: ContinuationEndpoint | None = Field(None, alias='continuationEndpoint')

class Content5(BaseModel):
    model_config = ConfigDict(extra='ignore')
    continuation_item_renderer: ContinuationItemRenderer | None = Field(None, alias='continuationItemRenderer')

class ItemSectionRenderer1(BaseModel):
    model_config = ConfigDict(extra='ignore')
    contents: list[Content5] | None = None
    tracking_params: str | None = Field(None, alias='trackingParams')
    section_identifier: UUID | None = Field(None, alias='sectionIdentifier')
    target_id: UUID | None = Field(None, alias='targetId')

class Content4(BaseModel):
    model_config = ConfigDict(extra='ignore')
    item_section_renderer: ItemSectionRenderer1 | None = Field(None, alias='itemSectionRenderer')

class ScrollPaneStyle(BaseModel):
    model_config = ConfigDict(extra='ignore')
    scrollable: bool | None = None

class SectionListRenderer1(BaseModel):
    model_config = ConfigDict(extra='ignore')
    contents: list[Content4] | None = None
    tracking_params: str | None = Field(None, alias='trackingParams')
    scroll_pane_style: ScrollPaneStyle | None = Field(None, alias='scrollPaneStyle')

class Content3(BaseModel):
    model_config = ConfigDict(extra='ignore')
    section_list_renderer: SectionListRenderer1 | None = Field(None, alias='sectionListRenderer')

class Identifier(BaseModel):
    model_config = ConfigDict(extra='ignore')
    surface: str | None = None
    tag: UUID | None = None

class EngagementPanelSectionListRenderer(BaseModel):
    model_config = ConfigDict(extra='ignore')
    header: Header | None = None
    content: Content3 | None = None
    target_id: UUID | None = Field(None, alias='targetId')
    identifier: Identifier | None = None
    size: str | None = None

class EngagementPanel(BaseModel):
    model_config = ConfigDict(extra='ignore')
    engagement_panel_section_list_renderer: EngagementPanelSectionListRenderer | None = Field(None, alias='engagementPanelSectionListRenderer')

class EngagementPanelPopupPresentationConfig(BaseModel):
    model_config = ConfigDict(extra='ignore')
    popup_type: str | None = Field(None, alias='popupType')

class EngagementPanelPresentationConfigs(BaseModel):
    model_config = ConfigDict(extra='ignore')
    engagement_panel_popup_presentation_config: EngagementPanelPopupPresentationConfig | None = Field(None, alias='engagementPanelPopupPresentationConfig')

class ShowEngagementPanelEndpoint(BaseModel):
    model_config = ConfigDict(extra='ignore')
    engagement_panel: EngagementPanel | None = Field(None, alias='engagementPanel')
    identifier: Identifier | None = None
    engagement_panel_presentation_configs: EngagementPanelPresentationConfigs | None = Field(None, alias='engagementPanelPresentationConfigs')

class NavigationEndpoint(BaseModel):
    model_config = ConfigDict(extra='ignore')
    click_tracking_params: str | None = Field(None, alias='clickTrackingParams')
    show_engagement_panel_endpoint: ShowEngagementPanelEndpoint | None = Field(None, alias='showEngagementPanelEndpoint')

class Run(BaseModel):
    model_config = ConfigDict(extra='ignore')
    text: str | None = None
    navigation_endpoint: NavigationEndpoint | None = Field(None, alias='navigationEndpoint')

class Title(BaseModel):
    model_config = ConfigDict(extra='ignore')
    runs: list[Run] | None = None

class Title2(BaseModel):
    model_config = ConfigDict(extra='ignore')
    simple_text: str | None = Field(None, alias='simpleText')

class AccessibilityData3(BaseModel):
    model_config = ConfigDict(extra='ignore')
    label: str | None = None

class AccessibilityData2(BaseModel):
    model_config = ConfigDict(extra='ignore')
    accessibility_data: AccessibilityData3 | None = Field(None, alias='accessibilityData')

class Command1(BaseModel):
    model_config = ConfigDict(extra='ignore')
    click_tracking_params: str | None = Field(None, alias='clickTrackingParams')
    change_engagement_panel_visibility_action: ChangeEngagementPanelVisibilityAction | None = Field(None, alias='changeEngagementPanelVisibilityAction')

class ButtonRenderer1(BaseModel):
    model_config = ConfigDict(extra='ignore')
    style: str | None = None
    size: str | None = None
    is_disabled: bool | None = Field(None, alias='isDisabled')
    icon: Icon | None = None
    accessibility: Accessibility | None = None
    tracking_params: str | None = Field(None, alias='trackingParams')
    accessibility_data: AccessibilityData2 | None = Field(None, alias='accessibilityData')
    command: Command1 | None = None

class VisibilityButton1(BaseModel):
    model_config = ConfigDict(extra='ignore')
    button_renderer: ButtonRenderer1 | None = Field(None, alias='buttonRenderer')

class EngagementPanelTitleHeaderRenderer1(BaseModel):
    model_config = ConfigDict(extra='ignore')
    title: Title2 | None = None
    visibility_button: VisibilityButton1 | None = Field(None, alias='visibilityButton')
    tracking_params: str | None = Field(None, alias='trackingParams')

class Header1(BaseModel):
    model_config = ConfigDict(extra='ignore')
    engagement_panel_title_header_renderer: EngagementPanelTitleHeaderRenderer1 | None = Field(None, alias='engagementPanelTitleHeaderRenderer')

class CommandMetadata2(BaseModel):
    model_config = ConfigDict(extra='ignore')
    web_command_metadata: WebCommandMetadata1 | None = Field(None, alias='webCommandMetadata')

class ContinuationEndpoint1(BaseModel):
    model_config = ConfigDict(extra='ignore')
    click_tracking_params: str | None = Field(None, alias='clickTrackingParams')
    command_metadata: CommandMetadata2 | None = Field(None, alias='commandMetadata')
    continuation_command: ContinuationCommand | None = Field(None, alias='continuationCommand')

class ContinuationItemRenderer1(BaseModel):
    model_config = ConfigDict(extra='ignore')
    trigger: str | None = None
    continuation_endpoint: ContinuationEndpoint1 | None = Field(None, alias='continuationEndpoint')

class Content8(BaseModel):
    model_config = ConfigDict(extra='ignore')
    continuation_item_renderer: ContinuationItemRenderer1 | None = Field(None, alias='continuationItemRenderer')

class ItemSectionRenderer2(BaseModel):
    model_config = ConfigDict(extra='ignore')
    contents: list[Content8] | None = None
    tracking_params: str | None = Field(None, alias='trackingParams')
    section_identifier: UUID | None = Field(None, alias='sectionIdentifier')
    target_id: UUID | None = Field(None, alias='targetId')

class Content7(BaseModel):
    model_config = ConfigDict(extra='ignore')
    item_section_renderer: ItemSectionRenderer2 | None = Field(None, alias='itemSectionRenderer')

class SectionListRenderer2(BaseModel):
    model_config = ConfigDict(extra='ignore')
    contents: list[Content7] | None = None
    tracking_params: str | None = Field(None, alias='trackingParams')
    scroll_pane_style: ScrollPaneStyle | None = Field(None, alias='scrollPaneStyle')

class Content6(BaseModel):
    model_config = ConfigDict(extra='ignore')
    section_list_renderer: SectionListRenderer2 | None = Field(None, alias='sectionListRenderer')

class EngagementPanelSectionListRenderer1(BaseModel):
    model_config = ConfigDict(extra='ignore')
    header: Header1 | None = None
    content: Content6 | None = None
    target_id: UUID | None = Field(None, alias='targetId')
    identifier: Identifier | None = None
    size: str | None = None

class EngagementPanel1(BaseModel):
    model_config = ConfigDict(extra='ignore')
    engagement_panel_section_list_renderer: EngagementPanelSectionListRenderer1 | None = Field(None, alias='engagementPanelSectionListRenderer')

class EngagementPanelPresentationConfigs1(BaseModel):
    model_config = ConfigDict(extra='ignore')
    engagement_panel_popup_presentation_config: EngagementPanelPopupPresentationConfig | None = Field(None, alias='engagementPanelPopupPresentationConfig')

class ShowEngagementPanelEndpoint1(BaseModel):
    model_config = ConfigDict(extra='ignore')
    engagement_panel: EngagementPanel1 | None = Field(None, alias='engagementPanel')
    identifier: Identifier | None = None
    engagement_panel_presentation_configs: EngagementPanelPresentationConfigs1 | None = Field(None, alias='engagementPanelPresentationConfigs')

class Endpoint1(BaseModel):
    model_config = ConfigDict(extra='ignore')
    click_tracking_params: str | None = Field(None, alias='clickTrackingParams')
    show_engagement_panel_endpoint: ShowEngagementPanelEndpoint1 | None = Field(None, alias='showEngagementPanelEndpoint')

class Source(BaseModel):
    model_config = ConfigDict(extra='ignore')
    url: str | None = None
    width: int | None = None
    height: int | None = None

class Image(BaseModel):
    model_config = ConfigDict(extra='ignore')
    sources: list[Source] | None = None

class ClientResource(BaseModel):
    model_config = ConfigDict(extra='ignore')
    image_name: str | None = Field(None, alias='imageName')

class Source1(BaseModel):
    model_config = ConfigDict(extra='ignore')
    client_resource: ClientResource | None = Field(None, alias='clientResource')

class Icon2(BaseModel):
    model_config = ConfigDict(extra='ignore')
    sources: list[Source1] | None = None

class BackgroundColor(BaseModel):
    model_config = ConfigDict(extra='ignore')
    light_theme: int | None = Field(None, alias='lightTheme')
    dark_theme: int | None = Field(None, alias='darkTheme')

class ThumbnailBadgeViewModel(BaseModel):
    model_config = ConfigDict(extra='ignore')
    icon: Icon2 | None = None
    text: str | None = None
    badge_style: str | None = Field(None, alias='badgeStyle')
    background_color: BackgroundColor | None = Field(None, alias='backgroundColor')

class ThumbnailBadge(BaseModel):
    model_config = ConfigDict(extra='ignore')
    thumbnail_badge_view_model: ThumbnailBadgeViewModel | None = Field(None, alias='thumbnailBadgeViewModel')

class ThumbnailOverlayBadgeViewModel(BaseModel):
    model_config = ConfigDict(extra='ignore')
    thumbnail_badges: list[ThumbnailBadge] | None = Field(None, alias='thumbnailBadges')
    position: str | None = None

class Source2(BaseModel):
    model_config = ConfigDict(extra='ignore')
    client_resource: ClientResource | None = Field(None, alias='clientResource')

class Icon3(BaseModel):
    model_config = ConfigDict(extra='ignore')
    sources: list[Source2] | None = None

class StyleRun(BaseModel):
    model_config = ConfigDict(extra='ignore')
    start_index: int | None = Field(None, alias='startIndex')
    length: int | None = None

class Text(BaseModel):
    model_config = ConfigDict(extra='ignore')
    content: str | None = None
    style_runs: list[StyleRun] | None = Field(None, alias='styleRuns')

class ThumbnailHoverOverlayViewModel(BaseModel):
    model_config = ConfigDict(extra='ignore')
    icon: Icon3 | None = None
    text: Text | None = None
    style: str | None = None

class Overlay(BaseModel):
    model_config = ConfigDict(extra='ignore')
    thumbnail_overlay_badge_view_model: ThumbnailOverlayBadgeViewModel | None = Field(None, alias='thumbnailOverlayBadgeViewModel')
    thumbnail_hover_overlay_view_model: ThumbnailHoverOverlayViewModel | None = Field(None, alias='thumbnailHoverOverlayViewModel')

class ThumbnailViewModel(BaseModel):
    model_config = ConfigDict(extra='ignore')
    image: Image | None = None
    overlays: list[Overlay] | None = None
    background_color: BackgroundColor | None = Field(None, alias='backgroundColor')

class PrimaryThumbnail(BaseModel):
    model_config = ConfigDict(extra='ignore')
    thumbnail_view_model: ThumbnailViewModel | None = Field(None, alias='thumbnailViewModel')

class StackColor(BaseModel):
    model_config = ConfigDict(extra='ignore')
    light_theme: int | None = Field(None, alias='lightTheme')
    dark_theme: int | None = Field(None, alias='darkTheme')

class CollectionThumbnailViewModel(BaseModel):
    model_config = ConfigDict(extra='ignore')
    primary_thumbnail: PrimaryThumbnail | None = Field(None, alias='primaryThumbnail')
    stack_color: StackColor | None = Field(None, alias='stackColor')

class ContentImage(BaseModel):
    model_config = ConfigDict(extra='ignore')
    collection_thumbnail_view_model: CollectionThumbnailViewModel | None = Field(None, alias='collectionThumbnailViewModel')

class Title3(BaseModel):
    model_config = ConfigDict(extra='ignore')
    content: str | None = None

class WebCommandMetadata3(BaseModel):
    model_config = ConfigDict(extra='ignore')
    url: str | None = None
    web_page_type: str | None = Field(None, alias='webPageType')
    root_ve: int | None = Field(None, alias='rootVe')
    api_url: str | None = Field(None, alias='apiUrl')

class CommandMetadata3(BaseModel):
    model_config = ConfigDict(extra='ignore')
    web_command_metadata: WebCommandMetadata3 | None = Field(None, alias='webCommandMetadata')

class BrowseEndpoint1(BaseModel):
    model_config = ConfigDict(extra='ignore')
    browse_id: str | None = Field(None, alias='browseId')
    canonical_base_url: str | None = Field(None, alias='canonicalBaseUrl')

class InnertubeCommand(BaseModel):
    model_config = ConfigDict(extra='ignore')
    click_tracking_params: str | None = Field(None, alias='clickTrackingParams')
    command_metadata: CommandMetadata3 | None = Field(None, alias='commandMetadata')
    browse_endpoint: BrowseEndpoint1 | None = Field(None, alias='browseEndpoint')

class OnTap(BaseModel):
    model_config = ConfigDict(extra='ignore')
    innertube_command: InnertubeCommand | None = Field(None, alias='innertubeCommand')

class CommandRun(BaseModel):
    model_config = ConfigDict(extra='ignore')
    start_index: int | None = Field(None, alias='startIndex')
    length: int | None = None
    on_tap: OnTap | None = Field(None, alias='onTap')

class StyleRun1(BaseModel):
    model_config = ConfigDict(extra='ignore')
    start_index: int | None = Field(None, alias='startIndex')
    length: int | None = None
    weight_label: str | None = Field(None, alias='weightLabel')

class Text1(BaseModel):
    model_config = ConfigDict(extra='ignore')
    content: str | None = None
    command_runs: list[CommandRun] | None = Field(None, alias='commandRuns')
    style_runs: list[StyleRun1] | None = Field(None, alias='styleRuns')

class MetadataPart(BaseModel):
    model_config = ConfigDict(extra='ignore')
    text: Text1 | None = None

class MetadataRow(BaseModel):
    model_config = ConfigDict(extra='ignore')
    metadata_parts: list[MetadataPart] | None = Field(None, alias='metadataParts')

class ContentMetadataViewModel(BaseModel):
    model_config = ConfigDict(extra='ignore')
    metadata_rows: list[MetadataRow] | None = Field(None, alias='metadataRows')
    delimiter: str | None = None

class Metadata1(BaseModel):
    model_config = ConfigDict(extra='ignore')
    content_metadata_view_model: ContentMetadataViewModel | None = Field(None, alias='contentMetadataViewModel')

class LockupMetadataViewModel(BaseModel):
    model_config = ConfigDict(extra='ignore')
    title: Title3 | None = None
    metadata: Metadata1 | None = None

class Metadata(BaseModel):
    model_config = ConfigDict(extra='ignore')
    lockup_metadata_view_model: LockupMetadataViewModel | None = Field(None, alias='lockupMetadataViewModel')

class WebCommandMetadata4(BaseModel):
    model_config = ConfigDict(extra='ignore')
    url: str | None = None
    web_page_type: str | None = Field(None, alias='webPageType')
    root_ve: int | None = Field(None, alias='rootVe')

class CommandMetadata4(BaseModel):
    model_config = ConfigDict(extra='ignore')
    web_command_metadata: WebCommandMetadata4 | None = Field(None, alias='webCommandMetadata')

class VssLoggingContext(BaseModel):
    model_config = ConfigDict(extra='ignore')
    serialized_context_data: str | None = Field(None, alias='serializedContextData')

class LoggingContext(BaseModel):
    model_config = ConfigDict(extra='ignore')
    vss_logging_context: VssLoggingContext | None = Field(None, alias='vssLoggingContext')

class CommonConfig(BaseModel):
    model_config = ConfigDict(extra='ignore')
    url: str | None = None

class Html5PlaybackOnesieConfig(BaseModel):
    model_config = ConfigDict(extra='ignore')
    common_config: CommonConfig | None = Field(None, alias='commonConfig')

class WatchEndpointSupportedOnesieConfig(BaseModel):
    model_config = ConfigDict(extra='ignore')
    html5_playback_onesie_config: Html5PlaybackOnesieConfig | None = Field(None, alias='html5PlaybackOnesieConfig')

class WatchEndpoint(BaseModel):
    model_config = ConfigDict(extra='ignore')
    video_id: str | None = Field(None, alias='videoId')
    playlist_id: str | None = Field(None, alias='playlistId')
    params: str | None = None
    logging_context: LoggingContext | None = Field(None, alias='loggingContext')
    watch_endpoint_supported_onesie_config: WatchEndpointSupportedOnesieConfig | None = Field(None, alias='watchEndpointSupportedOnesieConfig')
    player_params: str | None = Field(None, alias='playerParams')

class InnertubeCommand1(BaseModel):
    model_config = ConfigDict(extra='ignore')
    click_tracking_params: str | None = Field(None, alias='clickTrackingParams')
    command_metadata: CommandMetadata4 | None = Field(None, alias='commandMetadata')
    watch_endpoint: WatchEndpoint | None = Field(None, alias='watchEndpoint')

class OnSelect(BaseModel):
    model_config = ConfigDict(extra='ignore')
    innertube_command: InnertubeCommand1 | None = Field(None, alias='innertubeCommand')

class CommandMetadata5(BaseModel):
    model_config = ConfigDict(extra='ignore')
    web_command_metadata: WebCommandMetadata4 | None = Field(None, alias='webCommandMetadata')

class LoggingContext1(BaseModel):
    model_config = ConfigDict(extra='ignore')
    vss_logging_context: VssLoggingContext | None = Field(None, alias='vssLoggingContext')

class Html5PlaybackOnesieConfig1(BaseModel):
    model_config = ConfigDict(extra='ignore')
    common_config: CommonConfig | None = Field(None, alias='commonConfig')

class WatchEndpointSupportedOnesieConfig1(BaseModel):
    model_config = ConfigDict(extra='ignore')
    html5_playback_onesie_config: Html5PlaybackOnesieConfig1 | None = Field(None, alias='html5PlaybackOnesieConfig')

class WatchEndpoint1(BaseModel):
    model_config = ConfigDict(extra='ignore')
    video_id: str | None = Field(None, alias='videoId')
    playlist_id: str | None = Field(None, alias='playlistId')
    player_params: str | None = Field(None, alias='playerParams')
    logging_context: LoggingContext1 | None = Field(None, alias='loggingContext')
    watch_endpoint_supported_onesie_config: WatchEndpointSupportedOnesieConfig1 | None = Field(None, alias='watchEndpointSupportedOnesieConfig')

class InnertubeCommand2(BaseModel):
    model_config = ConfigDict(extra='ignore')
    click_tracking_params: str | None = Field(None, alias='clickTrackingParams')
    command_metadata: CommandMetadata5 | None = Field(None, alias='commandMetadata')
    watch_endpoint: WatchEndpoint1 | None = Field(None, alias='watchEndpoint')

class OnVisible(BaseModel):
    model_config = ConfigDict(extra='ignore')
    innertube_command: InnertubeCommand2 | None = Field(None, alias='innertubeCommand')

class InlinePlayerData(BaseModel):
    model_config = ConfigDict(extra='ignore')
    on_select: OnSelect | None = Field(None, alias='onSelect')
    on_visible: OnVisible | None = Field(None, alias='onVisible')

class ItemPlayback(BaseModel):
    model_config = ConfigDict(extra='ignore')
    inline_player_data: InlinePlayerData | None = Field(None, alias='inlinePlayerData')

class Visibility(BaseModel):
    model_config = ConfigDict(extra='ignore')
    types: str | None = None

class LoggingDirectives(BaseModel):
    model_config = ConfigDict(extra='ignore')
    tracking_params: str | None = Field(None, alias='trackingParams')
    visibility: Visibility | None = None

class LoggingContext2(BaseModel):
    model_config = ConfigDict(extra='ignore')
    logging_directives: LoggingDirectives | None = Field(None, alias='loggingDirectives')

class CommandMetadata6(BaseModel):
    model_config = ConfigDict(extra='ignore')
    web_command_metadata: WebCommandMetadata4 | None = Field(None, alias='webCommandMetadata')

class LoggingContext3(BaseModel):
    model_config = ConfigDict(extra='ignore')
    vss_logging_context: VssLoggingContext | None = Field(None, alias='vssLoggingContext')

class Html5PlaybackOnesieConfig2(BaseModel):
    model_config = ConfigDict(extra='ignore')
    common_config: CommonConfig | None = Field(None, alias='commonConfig')

class WatchEndpointSupportedOnesieConfig2(BaseModel):
    model_config = ConfigDict(extra='ignore')
    html5_playback_onesie_config: Html5PlaybackOnesieConfig2 | None = Field(None, alias='html5PlaybackOnesieConfig')

class WatchEndpoint2(BaseModel):
    model_config = ConfigDict(extra='ignore')
    video_id: str | None = Field(None, alias='videoId')
    playlist_id: str | None = Field(None, alias='playlistId')
    params: str | None = None
    logging_context: LoggingContext3 | None = Field(None, alias='loggingContext')
    watch_endpoint_supported_onesie_config: WatchEndpointSupportedOnesieConfig2 | None = Field(None, alias='watchEndpointSupportedOnesieConfig')
    player_params: str | None = Field(None, alias='playerParams')

class InnertubeCommand3(BaseModel):
    model_config = ConfigDict(extra='ignore')
    click_tracking_params: str | None = Field(None, alias='clickTrackingParams')
    command_metadata: CommandMetadata6 | None = Field(None, alias='commandMetadata')
    watch_endpoint: WatchEndpoint2 | None = Field(None, alias='watchEndpoint')

class OnTap1(BaseModel):
    model_config = ConfigDict(extra='ignore')
    innertube_command: InnertubeCommand3 | None = Field(None, alias='innertubeCommand')

class CommandContext(BaseModel):
    model_config = ConfigDict(extra='ignore')
    on_tap: OnTap1 | None = Field(None, alias='onTap')

class RendererContext(BaseModel):
    model_config = ConfigDict(extra='ignore')
    logging_context: LoggingContext2 | None = Field(None, alias='loggingContext')
    command_context: CommandContext | None = Field(None, alias='commandContext')

class LockupViewModel(BaseModel):
    model_config = ConfigDict(extra='ignore')
    content_image: ContentImage | None = Field(None, alias='contentImage')
    metadata: Metadata | None = None
    content_id: str | None = Field(None, alias='contentId')
    content_type: str | None = Field(None, alias='contentType')
    item_playback: ItemPlayback | None = Field(None, alias='itemPlayback')
    renderer_context: RendererContext | None = Field(None, alias='rendererContext')

class Item(BaseModel):
    model_config = ConfigDict(extra='ignore')
    lockup_view_model: LockupViewModel | None = Field(None, alias='lockupViewModel')

class Icon4(BaseModel):
    model_config = ConfigDict(extra='ignore')
    icon_type: str | None = Field(None, alias='iconType')

class ButtonRenderer2(BaseModel):
    model_config = ConfigDict(extra='ignore')
    style: str | None = None
    size: str | None = None
    is_disabled: bool | None = Field(None, alias='isDisabled')
    icon: Icon4 | None = None
    accessibility: Accessibility | None = None
    tracking_params: str | None = Field(None, alias='trackingParams')

class NextButton(BaseModel):
    model_config = ConfigDict(extra='ignore')
    button_renderer: ButtonRenderer2 | None = Field(None, alias='buttonRenderer')

class ButtonRenderer3(BaseModel):
    model_config = ConfigDict(extra='ignore')
    style: str | None = None
    size: str | None = None
    is_disabled: bool | None = Field(None, alias='isDisabled')
    icon: Icon4 | None = None
    accessibility: Accessibility | None = None
    tracking_params: str | None = Field(None, alias='trackingParams')

class PreviousButton(BaseModel):
    model_config = ConfigDict(extra='ignore')
    button_renderer: ButtonRenderer3 | None = Field(None, alias='buttonRenderer')

class HorizontalListRenderer(BaseModel):
    model_config = ConfigDict(extra='ignore')
    items: list[Item] | None = None
    tracking_params: str | None = Field(None, alias='trackingParams')
    visible_item_count: int | None = Field(None, alias='visibleItemCount')
    next_button: NextButton | None = Field(None, alias='nextButton')
    previous_button: PreviousButton | None = Field(None, alias='previousButton')
    force16_by9_thumbnail_aspect_ratio: bool | None = Field(None, alias='force16By9ThumbnailAspectRatio')

class Content9(BaseModel):
    model_config = ConfigDict(extra='ignore')
    horizontal_list_renderer: HorizontalListRenderer | None = Field(None, alias='horizontalListRenderer')

class Text2(BaseModel):
    model_config = ConfigDict(extra='ignore')
    simple_text: str | None = Field(None, alias='simpleText')

class Title4(BaseModel):
    model_config = ConfigDict(extra='ignore')
    simple_text: str | None = Field(None, alias='simpleText')

class AccessibilityData5(BaseModel):
    model_config = ConfigDict(extra='ignore')
    label: str | None = None

class AccessibilityData4(BaseModel):
    model_config = ConfigDict(extra='ignore')
    accessibility_data: AccessibilityData5 | None = Field(None, alias='accessibilityData')

class Command2(BaseModel):
    model_config = ConfigDict(extra='ignore')
    click_tracking_params: str | None = Field(None, alias='clickTrackingParams')
    change_engagement_panel_visibility_action: ChangeEngagementPanelVisibilityAction | None = Field(None, alias='changeEngagementPanelVisibilityAction')

class ButtonRenderer5(BaseModel):
    model_config = ConfigDict(extra='ignore')
    style: str | None = None
    size: str | None = None
    is_disabled: bool | None = Field(None, alias='isDisabled')
    icon: Icon4 | None = None
    accessibility: Accessibility | None = None
    tracking_params: str | None = Field(None, alias='trackingParams')
    accessibility_data: AccessibilityData4 | None = Field(None, alias='accessibilityData')
    command: Command2 | None = None

class VisibilityButton2(BaseModel):
    model_config = ConfigDict(extra='ignore')
    button_renderer: ButtonRenderer5 | None = Field(None, alias='buttonRenderer')

class EngagementPanelTitleHeaderRenderer2(BaseModel):
    model_config = ConfigDict(extra='ignore')
    title: Title4 | None = None
    visibility_button: VisibilityButton2 | None = Field(None, alias='visibilityButton')
    tracking_params: str | None = Field(None, alias='trackingParams')

class Header2(BaseModel):
    model_config = ConfigDict(extra='ignore')
    engagement_panel_title_header_renderer: EngagementPanelTitleHeaderRenderer2 | None = Field(None, alias='engagementPanelTitleHeaderRenderer')

class WebCommandMetadata7(BaseModel):
    model_config = ConfigDict(extra='ignore')
    send_post: bool | None = Field(None, alias='sendPost')
    api_url: str | None = Field(None, alias='apiUrl')

class CommandMetadata7(BaseModel):
    model_config = ConfigDict(extra='ignore')
    web_command_metadata: WebCommandMetadata7 | None = Field(None, alias='webCommandMetadata')

class ContinuationEndpoint2(BaseModel):
    model_config = ConfigDict(extra='ignore')
    click_tracking_params: str | None = Field(None, alias='clickTrackingParams')
    command_metadata: CommandMetadata7 | None = Field(None, alias='commandMetadata')
    continuation_command: ContinuationCommand | None = Field(None, alias='continuationCommand')

class ContinuationItemRenderer2(BaseModel):
    model_config = ConfigDict(extra='ignore')
    trigger: str | None = None
    continuation_endpoint: ContinuationEndpoint2 | None = Field(None, alias='continuationEndpoint')

class Content12(BaseModel):
    model_config = ConfigDict(extra='ignore')
    continuation_item_renderer: ContinuationItemRenderer2 | None = Field(None, alias='continuationItemRenderer')

class ItemSectionRenderer3(BaseModel):
    model_config = ConfigDict(extra='ignore')
    contents: list[Content12] | None = None
    tracking_params: str | None = Field(None, alias='trackingParams')
    section_identifier: UUID | None = Field(None, alias='sectionIdentifier')
    target_id: UUID | None = Field(None, alias='targetId')

class Content11(BaseModel):
    model_config = ConfigDict(extra='ignore')
    item_section_renderer: ItemSectionRenderer3 | None = Field(None, alias='itemSectionRenderer')

class SectionListRenderer3(BaseModel):
    model_config = ConfigDict(extra='ignore')
    contents: list[Content11] | None = None
    tracking_params: str | None = Field(None, alias='trackingParams')
    scroll_pane_style: ScrollPaneStyle | None = Field(None, alias='scrollPaneStyle')

class Content10(BaseModel):
    model_config = ConfigDict(extra='ignore')
    section_list_renderer: SectionListRenderer3 | None = Field(None, alias='sectionListRenderer')

class EngagementPanelSectionListRenderer2(BaseModel):
    model_config = ConfigDict(extra='ignore')
    header: Header2 | None = None
    content: Content10 | None = None
    target_id: UUID | None = Field(None, alias='targetId')
    identifier: Identifier | None = None
    size: str | None = None

class EngagementPanel2(BaseModel):
    model_config = ConfigDict(extra='ignore')
    engagement_panel_section_list_renderer: EngagementPanelSectionListRenderer2 | None = Field(None, alias='engagementPanelSectionListRenderer')

class EngagementPanelPresentationConfigs2(BaseModel):
    model_config = ConfigDict(extra='ignore')
    engagement_panel_popup_presentation_config: EngagementPanelPopupPresentationConfig | None = Field(None, alias='engagementPanelPopupPresentationConfig')

class ShowEngagementPanelEndpoint2(BaseModel):
    model_config = ConfigDict(extra='ignore')
    engagement_panel: EngagementPanel2 | None = Field(None, alias='engagementPanel')
    identifier: Identifier | None = None
    engagement_panel_presentation_configs: EngagementPanelPresentationConfigs2 | None = Field(None, alias='engagementPanelPresentationConfigs')

class NavigationEndpoint1(BaseModel):
    model_config = ConfigDict(extra='ignore')
    click_tracking_params: str | None = Field(None, alias='clickTrackingParams')
    show_engagement_panel_endpoint: ShowEngagementPanelEndpoint2 | None = Field(None, alias='showEngagementPanelEndpoint')

class AccessibilityData7(BaseModel):
    model_config = ConfigDict(extra='ignore')
    label: str | None = None

class AccessibilityData6(BaseModel):
    model_config = ConfigDict(extra='ignore')
    accessibility_data: AccessibilityData7 | None = Field(None, alias='accessibilityData')

class ButtonRenderer4(BaseModel):
    model_config = ConfigDict(extra='ignore')
    style: str | None = None
    size: str | None = None
    is_disabled: bool | None = Field(None, alias='isDisabled')
    text: Text2 | None = None
    navigation_endpoint: NavigationEndpoint1 | None = Field(None, alias='navigationEndpoint')
    tracking_params: str | None = Field(None, alias='trackingParams')
    accessibility_data: AccessibilityData6 | None = Field(None, alias='accessibilityData')

class TopLevelButton(BaseModel):
    model_config = ConfigDict(extra='ignore')
    button_renderer: ButtonRenderer4 | None = Field(None, alias='buttonRenderer')

class MenuRenderer(BaseModel):
    model_config = ConfigDict(extra='ignore')
    tracking_params: str | None = Field(None, alias='trackingParams')
    top_level_buttons: list[TopLevelButton] | None = Field(None, alias='topLevelButtons')

class Menu(BaseModel):
    model_config = ConfigDict(extra='ignore')
    menu_renderer: MenuRenderer | None = Field(None, alias='menuRenderer')

class ShelfRenderer(BaseModel):
    model_config = ConfigDict(extra='ignore')
    title: Title | None = None
    endpoint: Endpoint1 | None = None
    content: Content9 | None = None
    tracking_params: str | None = Field(None, alias='trackingParams')
    menu: Menu | None = None

class Content2(BaseModel):
    model_config = ConfigDict(extra='ignore')
    shelf_renderer: ShelfRenderer | None = Field(None, alias='shelfRenderer')

class ItemSectionRenderer(BaseModel):
    model_config = ConfigDict(extra='ignore')
    contents: list[Content2] | None = None
    tracking_params: str | None = Field(None, alias='trackingParams')

class Content1(BaseModel):
    model_config = ConfigDict(extra='ignore')
    item_section_renderer: ItemSectionRenderer | None = Field(None, alias='itemSectionRenderer')

class SectionListRenderer(BaseModel):
    model_config = ConfigDict(extra='ignore')
    contents: list[Content1] | None = None
    tracking_params: str | None = Field(None, alias='trackingParams')
    target_id: str | None = Field(None, alias='targetId')
    disable_pull_to_refresh: bool | None = Field(None, alias='disablePullToRefresh')

class Content(BaseModel):
    model_config = ConfigDict(extra='ignore')
    section_list_renderer: SectionListRenderer | None = Field(None, alias='sectionListRenderer')

class TabRenderer(BaseModel):
    model_config = ConfigDict(extra='ignore')
    endpoint: Endpoint | None = None
    title: str | None = None
    selected: bool | None = None
    content: Content | None = None
    tracking_params: str | None = Field(None, alias='trackingParams')

class Tab(BaseModel):
    model_config = ConfigDict(extra='ignore')
    tab_renderer: TabRenderer | None = Field(None, alias='tabRenderer')

class TwoColumnBrowseResultsRenderer(BaseModel):
    model_config = ConfigDict(extra='ignore')
    tabs: list[Tab] | None = None

class Contents(BaseModel):
    model_config = ConfigDict(extra='ignore')
    two_column_browse_results_renderer: TwoColumnBrowseResultsRenderer | None = Field(None, alias='twoColumnBrowseResultsRenderer')

class Text3(BaseModel):
    model_config = ConfigDict(extra='ignore')
    content: str | None = None

class LoggingDirectives1(BaseModel):
    model_config = ConfigDict(extra='ignore')
    tracking_params: str | None = Field(None, alias='trackingParams')
    visibility: Visibility | None = None

class LoggingContext4(BaseModel):
    model_config = ConfigDict(extra='ignore')
    logging_directives: LoggingDirectives1 | None = Field(None, alias='loggingDirectives')

class RendererContext1(BaseModel):
    model_config = ConfigDict(extra='ignore')
    logging_context: LoggingContext4 | None = Field(None, alias='loggingContext')

class DynamicTextViewModel(BaseModel):
    model_config = ConfigDict(extra='ignore')
    text: Text3 | None = None
    max_lines: int | None = Field(None, alias='maxLines')
    renderer_context: RendererContext1 | None = Field(None, alias='rendererContext')

class Title5(BaseModel):
    model_config = ConfigDict(extra='ignore')
    dynamic_text_view_model: DynamicTextViewModel | None = Field(None, alias='dynamicTextViewModel')

class Source3(BaseModel):
    model_config = ConfigDict(extra='ignore')
    url: str | None = None
    width: int | None = None
    height: int | None = None

class BorderImageProcessor(BaseModel):
    model_config = ConfigDict(extra='ignore')
    circular: bool | None = None

class Processor(BaseModel):
    model_config = ConfigDict(extra='ignore')
    border_image_processor: BorderImageProcessor | None = Field(None, alias='borderImageProcessor')

class Image2(BaseModel):
    model_config = ConfigDict(extra='ignore')
    sources: list[Source3] | None = None
    processor: Processor | None = None

class LoggingDirectives2(BaseModel):
    model_config = ConfigDict(extra='ignore')
    tracking_params: str | None = Field(None, alias='trackingParams')
    visibility: Visibility | None = None

class AvatarViewModel(BaseModel):
    model_config = ConfigDict(extra='ignore')
    image: Image2 | None = None
    avatar_image_size: str | None = Field(None, alias='avatarImageSize')
    logging_directives: LoggingDirectives2 | None = Field(None, alias='loggingDirectives')

class Avatar(BaseModel):
    model_config = ConfigDict(extra='ignore')
    avatar_view_model: AvatarViewModel | None = Field(None, alias='avatarViewModel')

class DecoratedAvatarViewModel(BaseModel):
    model_config = ConfigDict(extra='ignore')
    avatar: Avatar | None = None

class Image1(BaseModel):
    model_config = ConfigDict(extra='ignore')
    decorated_avatar_view_model: DecoratedAvatarViewModel | None = Field(None, alias='decoratedAvatarViewModel')

class StyleRun2(BaseModel):
    model_config = ConfigDict(extra='ignore')
    start_index: int | None = Field(None, alias='startIndex')
    length: int | None = None

class Text4(BaseModel):
    model_config = ConfigDict(extra='ignore')
    content: str | None = None
    style_runs: list[StyleRun2] | None = Field(None, alias='styleRuns')

class MetadataPart1(BaseModel):
    model_config = ConfigDict(extra='ignore')
    text: Text4 | None = None

class MetadataRow1(BaseModel):
    model_config = ConfigDict(extra='ignore')
    metadata_parts: list[MetadataPart1] | None = Field(None, alias='metadataParts')

class LoggingDirectives3(BaseModel):
    model_config = ConfigDict(extra='ignore')
    tracking_params: str | None = Field(None, alias='trackingParams')
    visibility: Visibility | None = None

class LoggingContext5(BaseModel):
    model_config = ConfigDict(extra='ignore')
    logging_directives: LoggingDirectives3 | None = Field(None, alias='loggingDirectives')

class RendererContext2(BaseModel):
    model_config = ConfigDict(extra='ignore')
    logging_context: LoggingContext5 | None = Field(None, alias='loggingContext')

class ContentMetadataViewModel1(BaseModel):
    model_config = ConfigDict(extra='ignore')
    metadata_rows: list[MetadataRow1] | None = Field(None, alias='metadataRows')
    delimiter: str | None = None
    renderer_context: RendererContext2 | None = Field(None, alias='rendererContext')

class Metadata2(BaseModel):
    model_config = ConfigDict(extra='ignore')
    content_metadata_view_model: ContentMetadataViewModel1 | None = Field(None, alias='contentMetadataViewModel')

class Description1(BaseModel):
    model_config = ConfigDict(extra='ignore')
    content: str | None = None

class StyleRun3(BaseModel):
    model_config = ConfigDict(extra='ignore')
    start_index: int | None = Field(None, alias='startIndex')
    length: int | None = None
    weight: int | None = None

class TruncationText(BaseModel):
    model_config = ConfigDict(extra='ignore')
    content: str | None = None
    style_runs: list[StyleRun3] | None = Field(None, alias='styleRuns')

class LoggingDirectives4(BaseModel):
    model_config = ConfigDict(extra='ignore')
    tracking_params: str | None = Field(None, alias='trackingParams')
    visibility: Visibility | None = None

class LoggingContext6(BaseModel):
    model_config = ConfigDict(extra='ignore')
    logging_directives: LoggingDirectives4 | None = Field(None, alias='loggingDirectives')

class AccessibilityContext(BaseModel):
    model_config = ConfigDict(extra='ignore')
    label: str | None = None

class Title6(BaseModel):
    model_config = ConfigDict(extra='ignore')
    simple_text: str | None = Field(None, alias='simpleText')

class AccessibilityData9(BaseModel):
    model_config = ConfigDict(extra='ignore')
    label: str | None = None

class AccessibilityData8(BaseModel):
    model_config = ConfigDict(extra='ignore')
    accessibility_data: AccessibilityData9 | None = Field(None, alias='accessibilityData')

class Command3(BaseModel):
    model_config = ConfigDict(extra='ignore')
    click_tracking_params: str | None = Field(None, alias='clickTrackingParams')
    change_engagement_panel_visibility_action: ChangeEngagementPanelVisibilityAction | None = Field(None, alias='changeEngagementPanelVisibilityAction')

class ButtonRenderer6(BaseModel):
    model_config = ConfigDict(extra='ignore')
    style: str | None = None
    size: str | None = None
    is_disabled: bool | None = Field(None, alias='isDisabled')
    icon: Icon4 | None = None
    accessibility: Accessibility | None = None
    tracking_params: str | None = Field(None, alias='trackingParams')
    accessibility_data: AccessibilityData8 | None = Field(None, alias='accessibilityData')
    command: Command3 | None = None

class VisibilityButton3(BaseModel):
    model_config = ConfigDict(extra='ignore')
    button_renderer: ButtonRenderer6 | None = Field(None, alias='buttonRenderer')

class EngagementPanelTitleHeaderRenderer3(BaseModel):
    model_config = ConfigDict(extra='ignore')
    title: Title6 | None = None
    visibility_button: VisibilityButton3 | None = Field(None, alias='visibilityButton')
    tracking_params: str | None = Field(None, alias='trackingParams')

class Header4(BaseModel):
    model_config = ConfigDict(extra='ignore')
    engagement_panel_title_header_renderer: EngagementPanelTitleHeaderRenderer3 | None = Field(None, alias='engagementPanelTitleHeaderRenderer')

class CommandMetadata8(BaseModel):
    model_config = ConfigDict(extra='ignore')
    web_command_metadata: WebCommandMetadata7 | None = Field(None, alias='webCommandMetadata')

class ContinuationEndpoint3(BaseModel):
    model_config = ConfigDict(extra='ignore')
    click_tracking_params: str | None = Field(None, alias='clickTrackingParams')
    command_metadata: CommandMetadata8 | None = Field(None, alias='commandMetadata')
    continuation_command: ContinuationCommand | None = Field(None, alias='continuationCommand')

class ContinuationItemRenderer3(BaseModel):
    model_config = ConfigDict(extra='ignore')
    trigger: str | None = None
    continuation_endpoint: ContinuationEndpoint3 | None = Field(None, alias='continuationEndpoint')

class Content16(BaseModel):
    model_config = ConfigDict(extra='ignore')
    continuation_item_renderer: ContinuationItemRenderer3 | None = Field(None, alias='continuationItemRenderer')

class ItemSectionRenderer4(BaseModel):
    model_config = ConfigDict(extra='ignore')
    contents: list[Content16] | None = None
    tracking_params: str | None = Field(None, alias='trackingParams')
    section_identifier: UUID | None = Field(None, alias='sectionIdentifier')
    target_id: UUID | None = Field(None, alias='targetId')

class Content15(BaseModel):
    model_config = ConfigDict(extra='ignore')
    item_section_renderer: ItemSectionRenderer4 | None = Field(None, alias='itemSectionRenderer')

class SectionListRenderer4(BaseModel):
    model_config = ConfigDict(extra='ignore')
    contents: list[Content15] | None = None
    tracking_params: str | None = Field(None, alias='trackingParams')
    scroll_pane_style: ScrollPaneStyle | None = Field(None, alias='scrollPaneStyle')

class Content14(BaseModel):
    model_config = ConfigDict(extra='ignore')
    section_list_renderer: SectionListRenderer4 | None = Field(None, alias='sectionListRenderer')

class EngagementPanelSectionListRenderer3(BaseModel):
    model_config = ConfigDict(extra='ignore')
    header: Header4 | None = None
    content: Content14 | None = None
    target_id: UUID | None = Field(None, alias='targetId')
    identifier: Identifier | None = None

class EngagementPanel3(BaseModel):
    model_config = ConfigDict(extra='ignore')
    engagement_panel_section_list_renderer: EngagementPanelSectionListRenderer3 | None = Field(None, alias='engagementPanelSectionListRenderer')

class EngagementPanelPresentationConfigs3(BaseModel):
    model_config = ConfigDict(extra='ignore')
    engagement_panel_popup_presentation_config: EngagementPanelPopupPresentationConfig | None = Field(None, alias='engagementPanelPopupPresentationConfig')

class ShowEngagementPanelEndpoint3(BaseModel):
    model_config = ConfigDict(extra='ignore')
    engagement_panel: EngagementPanel3 | None = Field(None, alias='engagementPanel')
    identifier: Identifier | None = None
    engagement_panel_presentation_configs: EngagementPanelPresentationConfigs3 | None = Field(None, alias='engagementPanelPresentationConfigs')

class InnertubeCommand4(BaseModel):
    model_config = ConfigDict(extra='ignore')
    click_tracking_params: str | None = Field(None, alias='clickTrackingParams')
    show_engagement_panel_endpoint: ShowEngagementPanelEndpoint3 | None = Field(None, alias='showEngagementPanelEndpoint')

class OnTap2(BaseModel):
    model_config = ConfigDict(extra='ignore')
    innertube_command: InnertubeCommand4 | None = Field(None, alias='innertubeCommand')

class CommandContext1(BaseModel):
    model_config = ConfigDict(extra='ignore')
    on_tap: OnTap2 | None = Field(None, alias='onTap')

class RendererContext3(BaseModel):
    model_config = ConfigDict(extra='ignore')
    logging_context: LoggingContext6 | None = Field(None, alias='loggingContext')
    accessibility_context: AccessibilityContext | None = Field(None, alias='accessibilityContext')
    command_context: CommandContext1 | None = Field(None, alias='commandContext')

class DescriptionPreviewViewModel(BaseModel):
    model_config = ConfigDict(extra='ignore')
    description: Description1 | None = None
    max_lines: int | None = Field(None, alias='maxLines')
    truncation_text: TruncationText | None = Field(None, alias='truncationText')
    always_show_truncation_text: bool | None = Field(None, alias='alwaysShowTruncationText')
    renderer_context: RendererContext3 | None = Field(None, alias='rendererContext')

class Description(BaseModel):
    model_config = ConfigDict(extra='ignore')
    description_preview_view_model: DescriptionPreviewViewModel | None = Field(None, alias='descriptionPreviewViewModel')

class WebCommandMetadata9(BaseModel):
    model_config = ConfigDict(extra='ignore')
    url: str | None = None
    web_page_type: str | None = Field(None, alias='webPageType')
    root_ve: int | None = Field(None, alias='rootVe')

class CommandMetadata9(BaseModel):
    model_config = ConfigDict(extra='ignore')
    web_command_metadata: WebCommandMetadata9 | None = Field(None, alias='webCommandMetadata')

class UrlEndpoint(BaseModel):
    model_config = ConfigDict(extra='ignore')
    url: str | None = None
    target: str | None = None

class InnertubeCommand5(BaseModel):
    model_config = ConfigDict(extra='ignore')
    click_tracking_params: str | None = Field(None, alias='clickTrackingParams')
    command_metadata: CommandMetadata9 | None = Field(None, alias='commandMetadata')
    url_endpoint: UrlEndpoint | None = Field(None, alias='urlEndpoint')

class OnTap3(BaseModel):
    model_config = ConfigDict(extra='ignore')
    innertube_command: InnertubeCommand5 | None = Field(None, alias='innertubeCommand')

class LoggingDirectives5(BaseModel):
    model_config = ConfigDict(extra='ignore')
    tracking_params: str | None = Field(None, alias='trackingParams')
    visibility: Visibility | None = None

class CommandRun1(BaseModel):
    model_config = ConfigDict(extra='ignore')
    start_index: int | None = Field(None, alias='startIndex')
    length: int | None = None
    on_tap: OnTap3 | None = Field(None, alias='onTap')
    logging_directives: LoggingDirectives5 | None = Field(None, alias='loggingDirectives')

class ColorMapItem(BaseModel):
    model_config = ConfigDict(extra='ignore')
    key: str | None = None
    value: int | None = None

class StyleRunColorMapExtension(BaseModel):
    model_config = ConfigDict(extra='ignore')
    color_map: list[ColorMapItem] | None = Field(None, alias='colorMap')

class StyleRunExtensions(BaseModel):
    model_config = ConfigDict(extra='ignore')
    style_run_color_map_extension: StyleRunColorMapExtension | None = Field(None, alias='styleRunColorMapExtension')

class StyleRun4(BaseModel):
    model_config = ConfigDict(extra='ignore')
    weight_label: str | None = Field(None, alias='weightLabel')
    style_run_extensions: StyleRunExtensions | None = Field(None, alias='styleRunExtensions')

class ClientResource2(BaseModel):
    model_config = ConfigDict(extra='ignore')
    icon: str | None = None

class YoutubeIconSource(BaseModel):
    model_config = ConfigDict(extra='ignore')
    client_resource: ClientResource2 | None = Field(None, alias='clientResource')

class CustomImageSource(BaseModel):
    model_config = ConfigDict(extra='ignore')
    youtube_icon_source: YoutubeIconSource | None = Field(None, alias='youtubeIconSource')

class Source4(BaseModel):
    model_config = ConfigDict(extra='ignore')
    custom_image_source: CustomImageSource | None = Field(None, alias='customImageSource')

class Image3(BaseModel):
    model_config = ConfigDict(extra='ignore')
    sources: list[Source4] | None = None

class ImageType(BaseModel):
    model_config = ConfigDict(extra='ignore')
    image: Image3 | None = None

class Type(BaseModel):
    model_config = ConfigDict(extra='ignore')
    image_type: ImageType | None = Field(None, alias='imageType')

class Height(BaseModel):
    model_config = ConfigDict(extra='ignore')
    value: int | None = None
    unit: str | None = None

class Width(BaseModel):
    model_config = ConfigDict(extra='ignore')
    value: int | None = None
    unit: str | None = None

class LayoutProperties(BaseModel):
    model_config = ConfigDict(extra='ignore')
    height: Height | None = None
    width: Width | None = None

class Properties(BaseModel):
    model_config = ConfigDict(extra='ignore')
    layout_properties: LayoutProperties | None = Field(None, alias='layoutProperties')

class Element(BaseModel):
    model_config = ConfigDict(extra='ignore')
    type: Type | None = None
    properties: Properties | None = None

class AttachmentRun(BaseModel):
    model_config = ConfigDict(extra='ignore')
    start_index: int | None = Field(None, alias='startIndex')
    length: int | None = None
    element: Element | None = None
    alignment: str | None = None

class Text5(BaseModel):
    model_config = ConfigDict(extra='ignore')
    content: str | None = None
    command_runs: list[CommandRun1] | None = Field(None, alias='commandRuns')
    style_runs: list[StyleRun4] | None = Field(None, alias='styleRuns')
    attachment_runs: list[AttachmentRun] | None = Field(None, alias='attachmentRuns')

class LoggingDirectives6(BaseModel):
    model_config = ConfigDict(extra='ignore')
    tracking_params: str | None = Field(None, alias='trackingParams')
    visibility: Visibility | None = None

class LoggingContext7(BaseModel):
    model_config = ConfigDict(extra='ignore')
    logging_directives: LoggingDirectives6 | None = Field(None, alias='loggingDirectives')

class RendererContext4(BaseModel):
    model_config = ConfigDict(extra='ignore')
    logging_context: LoggingContext7 | None = Field(None, alias='loggingContext')

class AttributionViewModel(BaseModel):
    model_config = ConfigDict(extra='ignore')
    text: Text5 | None = None
    renderer_context: RendererContext4 | None = Field(None, alias='rendererContext')

class Attribution(BaseModel):
    model_config = ConfigDict(extra='ignore')
    attribution_view_model: AttributionViewModel | None = Field(None, alias='attributionViewModel')

class Source5(BaseModel):
    model_config = ConfigDict(extra='ignore')
    url: str | None = None
    width: int | None = None
    height: int | None = None

class Image4(BaseModel):
    model_config = ConfigDict(extra='ignore')
    sources: list[Source5] | None = None

class LoggingDirectives7(BaseModel):
    model_config = ConfigDict(extra='ignore')
    tracking_params: str | None = Field(None, alias='trackingParams')
    visibility: Visibility | None = None

class LoggingContext8(BaseModel):
    model_config = ConfigDict(extra='ignore')
    logging_directives: LoggingDirectives7 | None = Field(None, alias='loggingDirectives')

class RendererContext5(BaseModel):
    model_config = ConfigDict(extra='ignore')
    logging_context: LoggingContext8 | None = Field(None, alias='loggingContext')

class ImageBannerViewModel(BaseModel):
    model_config = ConfigDict(extra='ignore')
    image: Image4 | None = None
    style: str | None = None
    renderer_context: RendererContext5 | None = Field(None, alias='rendererContext')

class Banner(BaseModel):
    model_config = ConfigDict(extra='ignore')
    image_banner_view_model: ImageBannerViewModel | None = Field(None, alias='imageBannerViewModel')

class LoggingDirectives8(BaseModel):
    model_config = ConfigDict(extra='ignore')
    tracking_params: str | None = Field(None, alias='trackingParams')
    visibility: Visibility | None = None

class LoggingContext9(BaseModel):
    model_config = ConfigDict(extra='ignore')
    logging_directives: LoggingDirectives8 | None = Field(None, alias='loggingDirectives')

class RendererContext6(BaseModel):
    model_config = ConfigDict(extra='ignore')
    logging_context: LoggingContext9 | None = Field(None, alias='loggingContext')

class PageHeaderViewModel(BaseModel):
    model_config = ConfigDict(extra='ignore')
    title: Title5 | None = None
    image: Image1 | None = None
    metadata: Metadata2 | None = None
    description: Description | None = None
    attribution: Attribution | None = None
    banner: Banner | None = None
    renderer_context: RendererContext6 | None = Field(None, alias='rendererContext')

class Content13(BaseModel):
    model_config = ConfigDict(extra='ignore')
    page_header_view_model: PageHeaderViewModel | None = Field(None, alias='pageHeaderViewModel')

class PageHeaderRenderer(BaseModel):
    model_config = ConfigDict(extra='ignore')
    page_title: str | None = Field(None, alias='pageTitle')
    content: Content13 | None = None

class Header3(BaseModel):
    model_config = ConfigDict(extra='ignore')
    page_header_renderer: PageHeaderRenderer | None = Field(None, alias='pageHeaderRenderer')

class Thumbnail(BaseModel):
    model_config = ConfigDict(extra='ignore')
    url: str | None = None
    width: int | None = None
    height: int | None = None

class Avatar1(BaseModel):
    model_config = ConfigDict(extra='ignore')
    thumbnails: list[Thumbnail] | None = None

class ChannelMetadataRenderer(BaseModel):
    model_config = ConfigDict(extra='ignore')
    title: str | None = None
    description: str | None = None
    rss_url: str | None = Field(None, alias='rssUrl')
    external_id: str | None = Field(None, alias='externalId')
    keywords: str | None = None
    owner_urls: list[str] | None = Field(None, alias='ownerUrls')
    avatar: Avatar1 | None = None
    channel_url: str | None = Field(None, alias='channelUrl')
    is_family_safe: bool | None = Field(None, alias='isFamilySafe')
    available_country_codes: list[str] | None = Field(None, alias='availableCountryCodes')
    music_artist_name: str | None = Field(None, alias='musicArtistName')
    android_deep_link: str | None = Field(None, alias='androidDeepLink')
    android_appindexing_link: str | None = Field(None, alias='androidAppindexingLink')
    ios_appindexing_link: str | None = Field(None, alias='iosAppindexingLink')
    vanity_channel_url: str | None = Field(None, alias='vanityChannelUrl')

class Metadata3(BaseModel):
    model_config = ConfigDict(extra='ignore')
    channel_metadata_renderer: ChannelMetadataRenderer | None = Field(None, alias='channelMetadataRenderer')

class IconImage(BaseModel):
    model_config = ConfigDict(extra='ignore')
    icon_type: str | None = Field(None, alias='iconType')

class Run1(BaseModel):
    model_config = ConfigDict(extra='ignore')
    text: str | None = None

class TooltipText(BaseModel):
    model_config = ConfigDict(extra='ignore')
    runs: list[Run1] | None = None

class WebCommandMetadata10(BaseModel):
    model_config = ConfigDict(extra='ignore')
    url: str | None = None
    web_page_type: str | None = Field(None, alias='webPageType')
    root_ve: int | None = Field(None, alias='rootVe')
    api_url: str | None = Field(None, alias='apiUrl')

class CommandMetadata10(BaseModel):
    model_config = ConfigDict(extra='ignore')
    web_command_metadata: WebCommandMetadata10 | None = Field(None, alias='webCommandMetadata')

class BrowseEndpoint2(BaseModel):
    model_config = ConfigDict(extra='ignore')
    browse_id: str | None = Field(None, alias='browseId')

class Endpoint2(BaseModel):
    model_config = ConfigDict(extra='ignore')
    click_tracking_params: str | None = Field(None, alias='clickTrackingParams')
    command_metadata: CommandMetadata10 | None = Field(None, alias='commandMetadata')
    browse_endpoint: BrowseEndpoint2 | None = Field(None, alias='browseEndpoint')

class TopbarLogoRenderer(BaseModel):
    model_config = ConfigDict(extra='ignore')
    icon_image: IconImage | None = Field(None, alias='iconImage')
    tooltip_text: TooltipText | None = Field(None, alias='tooltipText')
    endpoint: Endpoint2 | None = None
    tracking_params: str | None = Field(None, alias='trackingParams')
    override_entity_key: str | None = Field(None, alias='overrideEntityKey')

class Logo(BaseModel):
    model_config = ConfigDict(extra='ignore')
    topbar_logo_renderer: TopbarLogoRenderer | None = Field(None, alias='topbarLogoRenderer')

class PlaceholderText(BaseModel):
    model_config = ConfigDict(extra='ignore')
    runs: list[Run1] | None = None

class WebSearchboxConfig(BaseModel):
    model_config = ConfigDict(extra='ignore')
    request_language: str | None = Field(None, alias='requestLanguage')
    request_domain: str | None = Field(None, alias='requestDomain')
    has_onscreen_keyboard: bool | None = Field(None, alias='hasOnscreenKeyboard')
    focus_searchbox: bool | None = Field(None, alias='focusSearchbox')

class Config(BaseModel):
    model_config = ConfigDict(extra='ignore')
    web_searchbox_config: WebSearchboxConfig | None = Field(None, alias='webSearchboxConfig')

class WebCommandMetadata11(BaseModel):
    model_config = ConfigDict(extra='ignore')
    url: str | None = None
    web_page_type: str | None = Field(None, alias='webPageType')
    root_ve: int | None = Field(None, alias='rootVe')

class CommandMetadata11(BaseModel):
    model_config = ConfigDict(extra='ignore')
    web_command_metadata: WebCommandMetadata11 | None = Field(None, alias='webCommandMetadata')

class SearchEndpoint1(BaseModel):
    model_config = ConfigDict(extra='ignore')
    query: str | None = None

class SearchEndpoint(BaseModel):
    model_config = ConfigDict(extra='ignore')
    click_tracking_params: str | None = Field(None, alias='clickTrackingParams')
    command_metadata: CommandMetadata11 | None = Field(None, alias='commandMetadata')
    search_endpoint: SearchEndpoint1 | None = Field(None, alias='searchEndpoint')

class AccessibilityData11(BaseModel):
    model_config = ConfigDict(extra='ignore')
    label: str | None = None

class AccessibilityData10(BaseModel):
    model_config = ConfigDict(extra='ignore')
    accessibility_data: AccessibilityData11 | None = Field(None, alias='accessibilityData')

class ButtonRenderer7(BaseModel):
    model_config = ConfigDict(extra='ignore')
    style: str | None = None
    size: str | None = None
    is_disabled: bool | None = Field(None, alias='isDisabled')
    icon: Icon4 | None = None
    tracking_params: str | None = Field(None, alias='trackingParams')
    accessibility_data: AccessibilityData10 | None = Field(None, alias='accessibilityData')

class ClearButton(BaseModel):
    model_config = ConfigDict(extra='ignore')
    button_renderer: ButtonRenderer7 | None = Field(None, alias='buttonRenderer')

class Headline(BaseModel):
    model_config = ConfigDict(extra='ignore')
    content: str | None = None

class DialogHeaderViewModel(BaseModel):
    model_config = ConfigDict(extra='ignore')
    headline: Headline | None = None

class Header5(BaseModel):
    model_config = ConfigDict(extra='ignore')
    dialog_header_view_model: DialogHeaderViewModel | None = Field(None, alias='dialogHeaderViewModel')

class ButtonViewModel(BaseModel):
    model_config = ConfigDict(extra='ignore')
    title: str | None = None
    style: str | None = None
    tracking_params: str | None = Field(None, alias='trackingParams')
    is_full_width: bool | None = Field(None, alias='isFullWidth')
    type: str | None = None

class PrimaryButton(BaseModel):
    model_config = ConfigDict(extra='ignore')
    button_view_model: ButtonViewModel | None = Field(None, alias='buttonViewModel')

class SecondaryButton(BaseModel):
    model_config = ConfigDict(extra='ignore')
    button_view_model: ButtonViewModel | None = Field(None, alias='buttonViewModel')

class PanelFooterViewModel(BaseModel):
    model_config = ConfigDict(extra='ignore')
    primary_button: PrimaryButton | None = Field(None, alias='primaryButton')
    secondary_button: SecondaryButton | None = Field(None, alias='secondaryButton')
    should_hide_divider: bool | None = Field(None, alias='shouldHideDivider')

class Footer(BaseModel):
    model_config = ConfigDict(extra='ignore')
    panel_footer_view_model: PanelFooterViewModel | None = Field(None, alias='panelFooterViewModel')

class Text6(BaseModel):
    model_config = ConfigDict(extra='ignore')
    content: str | None = None

class Paragraph(BaseModel):
    model_config = ConfigDict(extra='ignore')
    text: Text6 | None = None

class BasicContentViewModel(BaseModel):
    model_config = ConfigDict(extra='ignore')
    paragraphs: list[Paragraph] | None = None

class Content17(BaseModel):
    model_config = ConfigDict(extra='ignore')
    basic_content_view_model: BasicContentViewModel | None = Field(None, alias='basicContentViewModel')

class DialogViewModel(BaseModel):
    model_config = ConfigDict(extra='ignore')
    header: Header5 | None = None
    footer: Footer | None = None
    content: Content17 | None = None

class InlineContent(BaseModel):
    model_config = ConfigDict(extra='ignore')
    dialog_view_model: DialogViewModel | None = Field(None, alias='dialogViewModel')

class PanelLoadingStrategy(BaseModel):
    model_config = ConfigDict(extra='ignore')
    inline_content: InlineContent | None = Field(None, alias='inlineContent')

class ShowDialogCommand(BaseModel):
    model_config = ConfigDict(extra='ignore')
    panel_loading_strategy: PanelLoadingStrategy | None = Field(None, alias='panelLoadingStrategy')

class ShowImageSourceDialog(BaseModel):
    model_config = ConfigDict(extra='ignore')
    click_tracking_params: str | None = Field(None, alias='clickTrackingParams')
    show_dialog_command: ShowDialogCommand | None = Field(None, alias='showDialogCommand')

class FusionSearchboxRenderer(BaseModel):
    model_config = ConfigDict(extra='ignore')
    icon: Icon4 | None = None
    placeholder_text: PlaceholderText | None = Field(None, alias='placeholderText')
    config: Config | None = None
    tracking_params: str | None = Field(None, alias='trackingParams')
    search_endpoint: SearchEndpoint | None = Field(None, alias='searchEndpoint')
    clear_button: ClearButton | None = Field(None, alias='clearButton')
    show_image_source_dialog: ShowImageSourceDialog | None = Field(None, alias='showImageSourceDialog')
    disable_ai_appearance: bool | None = Field(None, alias='disableAiAppearance')

class Searchbox(BaseModel):
    model_config = ConfigDict(extra='ignore')
    fusion_searchbox_renderer: FusionSearchboxRenderer | None = Field(None, alias='fusionSearchboxRenderer')

class WebCommandMetadata12(BaseModel):
    model_config = ConfigDict(extra='ignore')
    send_post: bool | None = Field(None, alias='sendPost')
    api_url: str | None = Field(None, alias='apiUrl')

class CommandMetadata12(BaseModel):
    model_config = ConfigDict(extra='ignore')
    web_command_metadata: WebCommandMetadata12 | None = Field(None, alias='webCommandMetadata')

class MultiPageMenuRenderer(BaseModel):
    model_config = ConfigDict(extra='ignore')
    tracking_params: str | None = Field(None, alias='trackingParams')
    style: str | None = None
    show_loading_spinner: bool | None = Field(None, alias='showLoadingSpinner')

class Popup(BaseModel):
    model_config = ConfigDict(extra='ignore')
    multi_page_menu_renderer: MultiPageMenuRenderer | None = Field(None, alias='multiPageMenuRenderer')

class OpenPopupAction(BaseModel):
    model_config = ConfigDict(extra='ignore')
    popup: Popup | None = None
    popup_type: str | None = Field(None, alias='popupType')
    be_reused: bool | None = Field(None, alias='beReused')

class Action(BaseModel):
    model_config = ConfigDict(extra='ignore')
    click_tracking_params: str | None = Field(None, alias='clickTrackingParams')
    open_popup_action: OpenPopupAction | None = Field(None, alias='openPopupAction')

class SignalServiceEndpoint(BaseModel):
    model_config = ConfigDict(extra='ignore')
    signal: str | None = None
    actions: list[Action] | None = None

class MenuRequest(BaseModel):
    model_config = ConfigDict(extra='ignore')
    click_tracking_params: str | None = Field(None, alias='clickTrackingParams')
    command_metadata: CommandMetadata12 | None = Field(None, alias='commandMetadata')
    signal_service_endpoint: SignalServiceEndpoint | None = Field(None, alias='signalServiceEndpoint')

class AccessibilityData12(BaseModel):
    model_config = ConfigDict(extra='ignore')
    label: str | None = None

class Accessibility6(BaseModel):
    model_config = ConfigDict(extra='ignore')
    accessibility_data: AccessibilityData12 | None = Field(None, alias='accessibilityData')

class TopbarMenuButtonRenderer(BaseModel):
    model_config = ConfigDict(extra='ignore')
    icon: Icon4 | None = None
    menu_request: MenuRequest | None = Field(None, alias='menuRequest')
    tracking_params: str | None = Field(None, alias='trackingParams')
    accessibility: Accessibility6 | None = None
    tooltip: str | None = None
    style: str | None = None

class Text7(BaseModel):
    model_config = ConfigDict(extra='ignore')
    runs: list[Run1] | None = None

class WebCommandMetadata13(BaseModel):
    model_config = ConfigDict(extra='ignore')
    url: str | None = None
    web_page_type: str | None = Field(None, alias='webPageType')
    root_ve: int | None = Field(None, alias='rootVe')

class CommandMetadata13(BaseModel):
    model_config = ConfigDict(extra='ignore')
    web_command_metadata: WebCommandMetadata13 | None = Field(None, alias='webCommandMetadata')

class SignInEndpoint(BaseModel):
    model_config = ConfigDict(extra='ignore')
    idam_tag: str | None = Field(None, alias='idamTag')

class NavigationEndpoint2(BaseModel):
    model_config = ConfigDict(extra='ignore')
    click_tracking_params: str | None = Field(None, alias='clickTrackingParams')
    command_metadata: CommandMetadata13 | None = Field(None, alias='commandMetadata')
    sign_in_endpoint: SignInEndpoint | None = Field(None, alias='signInEndpoint')

class ButtonRenderer8(BaseModel):
    model_config = ConfigDict(extra='ignore')
    style: str | None = None
    size: str | None = None
    text: Text7 | None = None
    icon: Icon4 | None = None
    navigation_endpoint: NavigationEndpoint2 | None = Field(None, alias='navigationEndpoint')
    tracking_params: str | None = Field(None, alias='trackingParams')
    target_id: str | None = Field(None, alias='targetId')

class TopbarButton(BaseModel):
    model_config = ConfigDict(extra='ignore')
    topbar_menu_button_renderer: TopbarMenuButtonRenderer | None = Field(None, alias='topbarMenuButtonRenderer')
    button_renderer: ButtonRenderer8 | None = Field(None, alias='buttonRenderer')

class Title7(BaseModel):
    model_config = ConfigDict(extra='ignore')
    runs: list[Run1] | None = None

class Title8(BaseModel):
    model_config = ConfigDict(extra='ignore')
    runs: list[Run1] | None = None

class Label(BaseModel):
    model_config = ConfigDict(extra='ignore')
    runs: list[Run1] | None = None

class HotkeyAccessibilityLabel(BaseModel):
    model_config = ConfigDict(extra='ignore')
    accessibility_data: AccessibilityData12 | None = Field(None, alias='accessibilityData')

class HotkeyDialogSectionOptionRenderer(BaseModel):
    model_config = ConfigDict(extra='ignore')
    label: Label | None = None
    hotkey: str | None = None
    hotkey_accessibility_label: HotkeyAccessibilityLabel | None = Field(None, alias='hotkeyAccessibilityLabel')

class Option(BaseModel):
    model_config = ConfigDict(extra='ignore')
    hotkey_dialog_section_option_renderer: HotkeyDialogSectionOptionRenderer | None = Field(None, alias='hotkeyDialogSectionOptionRenderer')

class HotkeyDialogSectionRenderer(BaseModel):
    model_config = ConfigDict(extra='ignore')
    title: Title8 | None = None
    options: list[Option] | None = None

class Section(BaseModel):
    model_config = ConfigDict(extra='ignore')
    hotkey_dialog_section_renderer: HotkeyDialogSectionRenderer | None = Field(None, alias='hotkeyDialogSectionRenderer')

class Text8(BaseModel):
    model_config = ConfigDict(extra='ignore')
    runs: list[Run1] | None = None

class ButtonRenderer9(BaseModel):
    model_config = ConfigDict(extra='ignore')
    style: str | None = None
    size: str | None = None
    is_disabled: bool | None = Field(None, alias='isDisabled')
    text: Text8 | None = None
    tracking_params: str | None = Field(None, alias='trackingParams')

class DismissButton(BaseModel):
    model_config = ConfigDict(extra='ignore')
    button_renderer: ButtonRenderer9 | None = Field(None, alias='buttonRenderer')

class HotkeyDialogRenderer(BaseModel):
    model_config = ConfigDict(extra='ignore')
    title: Title7 | None = None
    sections: list[Section] | None = None
    dismiss_button: DismissButton | None = Field(None, alias='dismissButton')
    tracking_params: str | None = Field(None, alias='trackingParams')

class HotkeyDialog(BaseModel):
    model_config = ConfigDict(extra='ignore')
    hotkey_dialog_renderer: HotkeyDialogRenderer | None = Field(None, alias='hotkeyDialogRenderer')

class WebCommandMetadata14(BaseModel):
    model_config = ConfigDict(extra='ignore')
    send_post: bool | None = Field(None, alias='sendPost')

class CommandMetadata14(BaseModel):
    model_config = ConfigDict(extra='ignore')
    web_command_metadata: WebCommandMetadata14 | None = Field(None, alias='webCommandMetadata')

class SignalAction(BaseModel):
    model_config = ConfigDict(extra='ignore')
    signal: str | None = None

class Action1(BaseModel):
    model_config = ConfigDict(extra='ignore')
    click_tracking_params: str | None = Field(None, alias='clickTrackingParams')
    signal_action: SignalAction | None = Field(None, alias='signalAction')

class SignalServiceEndpoint1(BaseModel):
    model_config = ConfigDict(extra='ignore')
    signal: str | None = None
    actions: list[Action1] | None = None

class Command4(BaseModel):
    model_config = ConfigDict(extra='ignore')
    click_tracking_params: str | None = Field(None, alias='clickTrackingParams')
    command_metadata: CommandMetadata14 | None = Field(None, alias='commandMetadata')
    signal_service_endpoint: SignalServiceEndpoint1 | None = Field(None, alias='signalServiceEndpoint')

class ButtonRenderer10(BaseModel):
    model_config = ConfigDict(extra='ignore')
    tracking_params: str | None = Field(None, alias='trackingParams')
    command: Command4 | None = None

class BackButton(BaseModel):
    model_config = ConfigDict(extra='ignore')
    button_renderer: ButtonRenderer10 | None = Field(None, alias='buttonRenderer')

class CommandMetadata15(BaseModel):
    model_config = ConfigDict(extra='ignore')
    web_command_metadata: WebCommandMetadata14 | None = Field(None, alias='webCommandMetadata')

class Action2(BaseModel):
    model_config = ConfigDict(extra='ignore')
    click_tracking_params: str | None = Field(None, alias='clickTrackingParams')
    signal_action: SignalAction | None = Field(None, alias='signalAction')

class SignalServiceEndpoint2(BaseModel):
    model_config = ConfigDict(extra='ignore')
    signal: str | None = None
    actions: list[Action2] | None = None

class Command5(BaseModel):
    model_config = ConfigDict(extra='ignore')
    click_tracking_params: str | None = Field(None, alias='clickTrackingParams')
    command_metadata: CommandMetadata15 | None = Field(None, alias='commandMetadata')
    signal_service_endpoint: SignalServiceEndpoint2 | None = Field(None, alias='signalServiceEndpoint')

class ButtonRenderer11(BaseModel):
    model_config = ConfigDict(extra='ignore')
    tracking_params: str | None = Field(None, alias='trackingParams')
    command: Command5 | None = None

class ForwardButton(BaseModel):
    model_config = ConfigDict(extra='ignore')
    button_renderer: ButtonRenderer11 | None = Field(None, alias='buttonRenderer')

class Text9(BaseModel):
    model_config = ConfigDict(extra='ignore')
    runs: list[Run1] | None = None

class CommandMetadata16(BaseModel):
    model_config = ConfigDict(extra='ignore')
    web_command_metadata: WebCommandMetadata14 | None = Field(None, alias='webCommandMetadata')

class Action3(BaseModel):
    model_config = ConfigDict(extra='ignore')
    click_tracking_params: str | None = Field(None, alias='clickTrackingParams')
    signal_action: SignalAction | None = Field(None, alias='signalAction')

class SignalServiceEndpoint3(BaseModel):
    model_config = ConfigDict(extra='ignore')
    signal: str | None = None
    actions: list[Action3] | None = None

class Command6(BaseModel):
    model_config = ConfigDict(extra='ignore')
    click_tracking_params: str | None = Field(None, alias='clickTrackingParams')
    command_metadata: CommandMetadata16 | None = Field(None, alias='commandMetadata')
    signal_service_endpoint: SignalServiceEndpoint3 | None = Field(None, alias='signalServiceEndpoint')

class ButtonRenderer12(BaseModel):
    model_config = ConfigDict(extra='ignore')
    style: str | None = None
    size: str | None = None
    is_disabled: bool | None = Field(None, alias='isDisabled')
    text: Text9 | None = None
    tracking_params: str | None = Field(None, alias='trackingParams')
    command: Command6 | None = None

class A11ySkipNavigationButton(BaseModel):
    model_config = ConfigDict(extra='ignore')
    button_renderer: ButtonRenderer12 | None = Field(None, alias='buttonRenderer')

class CommandMetadata17(BaseModel):
    model_config = ConfigDict(extra='ignore')
    web_command_metadata: WebCommandMetadata14 | None = Field(None, alias='webCommandMetadata')

class PlaceholderHeader(BaseModel):
    model_config = ConfigDict(extra='ignore')
    runs: list[Run1] | None = None

class PromptHeader(BaseModel):
    model_config = ConfigDict(extra='ignore')
    runs: list[Run1] | None = None

class ExampleQuery1(BaseModel):
    model_config = ConfigDict(extra='ignore')
    runs: list[Run1] | None = None

class ExampleQuery2(BaseModel):
    model_config = ConfigDict(extra='ignore')
    runs: list[Run1] | None = None

class PromptMicrophoneLabel(BaseModel):
    model_config = ConfigDict(extra='ignore')
    runs: list[Run1] | None = None

class LoadingHeader(BaseModel):
    model_config = ConfigDict(extra='ignore')
    runs: list[Run1] | None = None

class ConnectionErrorHeader(BaseModel):
    model_config = ConfigDict(extra='ignore')
    runs: list[Run1] | None = None

class ConnectionErrorMicrophoneLabel(BaseModel):
    model_config = ConfigDict(extra='ignore')
    runs: list[Run1] | None = None

class PermissionsHeader(BaseModel):
    model_config = ConfigDict(extra='ignore')
    runs: list[Run1] | None = None

class PermissionsSubtext(BaseModel):
    model_config = ConfigDict(extra='ignore')
    runs: list[Run1] | None = None

class DisabledHeader(BaseModel):
    model_config = ConfigDict(extra='ignore')
    runs: list[Run1] | None = None

class DisabledSubtext(BaseModel):
    model_config = ConfigDict(extra='ignore')
    runs: list[Run1] | None = None

class MicrophoneButtonAriaLabel(BaseModel):
    model_config = ConfigDict(extra='ignore')
    runs: list[Run1] | None = None

class AccessibilityData14(BaseModel):
    model_config = ConfigDict(extra='ignore')
    accessibility_data: AccessibilityData12 | None = Field(None, alias='accessibilityData')

class ButtonRenderer14(BaseModel):
    model_config = ConfigDict(extra='ignore')
    style: str | None = None
    size: str | None = None
    is_disabled: bool | None = Field(None, alias='isDisabled')
    icon: Icon4 | None = None
    tracking_params: str | None = Field(None, alias='trackingParams')
    accessibility_data: AccessibilityData14 | None = Field(None, alias='accessibilityData')

class ExitButton(BaseModel):
    model_config = ConfigDict(extra='ignore')
    button_renderer: ButtonRenderer14 | None = Field(None, alias='buttonRenderer')

class MicrophoneOffPromptHeader(BaseModel):
    model_config = ConfigDict(extra='ignore')
    runs: list[Run1] | None = None

class VoiceSearchDialogRenderer(BaseModel):
    model_config = ConfigDict(extra='ignore')
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

class Popup1(BaseModel):
    model_config = ConfigDict(extra='ignore')
    voice_search_dialog_renderer: VoiceSearchDialogRenderer | None = Field(None, alias='voiceSearchDialogRenderer')

class OpenPopupAction1(BaseModel):
    model_config = ConfigDict(extra='ignore')
    popup: Popup1 | None = None
    popup_type: str | None = Field(None, alias='popupType')

class Action4(BaseModel):
    model_config = ConfigDict(extra='ignore')
    click_tracking_params: str | None = Field(None, alias='clickTrackingParams')
    open_popup_action: OpenPopupAction1 | None = Field(None, alias='openPopupAction')

class SignalServiceEndpoint4(BaseModel):
    model_config = ConfigDict(extra='ignore')
    signal: str | None = None
    actions: list[Action4] | None = None

class ServiceEndpoint(BaseModel):
    model_config = ConfigDict(extra='ignore')
    click_tracking_params: str | None = Field(None, alias='clickTrackingParams')
    command_metadata: CommandMetadata17 | None = Field(None, alias='commandMetadata')
    signal_service_endpoint: SignalServiceEndpoint4 | None = Field(None, alias='signalServiceEndpoint')

class AccessibilityData17(BaseModel):
    model_config = ConfigDict(extra='ignore')
    label: str | None = None

class AccessibilityData16(BaseModel):
    model_config = ConfigDict(extra='ignore')
    accessibility_data: AccessibilityData17 | None = Field(None, alias='accessibilityData')

class ButtonRenderer13(BaseModel):
    model_config = ConfigDict(extra='ignore')
    style: str | None = None
    size: str | None = None
    is_disabled: bool | None = Field(None, alias='isDisabled')
    service_endpoint: ServiceEndpoint | None = Field(None, alias='serviceEndpoint')
    icon: Icon4 | None = None
    tooltip: str | None = None
    tracking_params: str | None = Field(None, alias='trackingParams')
    accessibility_data: AccessibilityData16 | None = Field(None, alias='accessibilityData')

class VoiceSearchButton(BaseModel):
    model_config = ConfigDict(extra='ignore')
    button_renderer: ButtonRenderer13 | None = Field(None, alias='buttonRenderer')

class DesktopTopbarRenderer(BaseModel):
    model_config = ConfigDict(extra='ignore')
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
    model_config = ConfigDict(extra='ignore')
    desktop_topbar_renderer: DesktopTopbarRenderer | None = Field(None, alias='desktopTopbarRenderer')

class Thumbnail1(BaseModel):
    model_config = ConfigDict(extra='ignore')
    thumbnails: list[Thumbnail] | None = None

class LinkAlternate(BaseModel):
    model_config = ConfigDict(extra='ignore')
    href_url: str | None = Field(None, alias='hrefUrl')

class MicroformatDataRenderer(BaseModel):
    model_config = ConfigDict(extra='ignore')
    url_canonical: str | None = Field(None, alias='urlCanonical')
    title: str | None = None
    description: str | None = None
    thumbnail: Thumbnail1 | None = None
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
    family_safe: bool | None = Field(None, alias='familySafe')
    available_countries: list[str] | None = Field(None, alias='availableCountries')
    link_alternates: list[LinkAlternate] | None = Field(None, alias='linkAlternates')

class Microformat(BaseModel):
    model_config = ConfigDict(extra='ignore')
    microformat_data_renderer: MicroformatDataRenderer | None = Field(None, alias='microformatDataRenderer')

class Thumbnail4(BaseModel):
    model_config = ConfigDict(extra='ignore')
    url: str | None = None
    width: int | None = None
    height: int | None = None

class SampledThumbnailColor(BaseModel):
    model_config = ConfigDict(extra='ignore')
    red: int | None = None
    green: int | None = None
    blue: int | None = None

class DarkColorPalette(BaseModel):
    model_config = ConfigDict(extra='ignore')
    section2_color: int | None = Field(None, alias='section2Color')
    icon_inactive_color: int | None = Field(None, alias='iconInactiveColor')
    icon_disabled_color: int | None = Field(None, alias='iconDisabledColor')

class VibrantColorPalette(BaseModel):
    model_config = ConfigDict(extra='ignore')
    icon_inactive_color: int | None = Field(None, alias='iconInactiveColor')

class Thumbnail3(BaseModel):
    model_config = ConfigDict(extra='ignore')
    thumbnails: list[Thumbnail4] | None = None
    sampled_thumbnail_color: SampledThumbnailColor | None = Field(None, alias='sampledThumbnailColor')
    dark_color_palette: DarkColorPalette | None = Field(None, alias='darkColorPalette')
    vibrant_color_palette: VibrantColorPalette | None = Field(None, alias='vibrantColorPalette')

class WebCommandMetadata18(BaseModel):
    model_config = ConfigDict(extra='ignore')
    url: str | None = None
    web_page_type: str | None = Field(None, alias='webPageType')
    root_ve: int | None = Field(None, alias='rootVe')

class CommandMetadata18(BaseModel):
    model_config = ConfigDict(extra='ignore')
    web_command_metadata: WebCommandMetadata18 | None = Field(None, alias='webCommandMetadata')

class LoggingContext10(BaseModel):
    model_config = ConfigDict(extra='ignore')
    vss_logging_context: VssLoggingContext | None = Field(None, alias='vssLoggingContext')

class Html5PlaybackOnesieConfig3(BaseModel):
    model_config = ConfigDict(extra='ignore')
    common_config: CommonConfig | None = Field(None, alias='commonConfig')

class WatchEndpointSupportedOnesieConfig3(BaseModel):
    model_config = ConfigDict(extra='ignore')
    html5_playback_onesie_config: Html5PlaybackOnesieConfig3 | None = Field(None, alias='html5PlaybackOnesieConfig')

class WatchEndpoint3(BaseModel):
    model_config = ConfigDict(extra='ignore')
    video_id: str | None = Field(None, alias='videoId')
    playlist_id: str | None = Field(None, alias='playlistId')
    params: str | None = None
    logging_context: LoggingContext10 | None = Field(None, alias='loggingContext')
    watch_endpoint_supported_onesie_config: WatchEndpointSupportedOnesieConfig3 | None = Field(None, alias='watchEndpointSupportedOnesieConfig')
    player_params: str | None = Field(None, alias='playerParams')

class NavigationEndpoint3(BaseModel):
    model_config = ConfigDict(extra='ignore')
    click_tracking_params: str | None = Field(None, alias='clickTrackingParams')
    command_metadata: CommandMetadata18 | None = Field(None, alias='commandMetadata')
    watch_endpoint: WatchEndpoint3 | None = Field(None, alias='watchEndpoint')

class Run23(BaseModel):
    model_config = ConfigDict(extra='ignore')
    text: str | None = None
    navigation_endpoint: NavigationEndpoint3 | None = Field(None, alias='navigationEndpoint')

class Title9(BaseModel):
    model_config = ConfigDict(extra='ignore')
    runs: list[Run23] | None = None

class WebCommandMetadata19(BaseModel):
    model_config = ConfigDict(extra='ignore')
    url: str | None = None
    web_page_type: str | None = Field(None, alias='webPageType')
    root_ve: int | None = Field(None, alias='rootVe')
    api_url: str | None = Field(None, alias='apiUrl')

class CommandMetadata19(BaseModel):
    model_config = ConfigDict(extra='ignore')
    web_command_metadata: WebCommandMetadata19 | None = Field(None, alias='webCommandMetadata')

class BrowseEndpoint3(BaseModel):
    model_config = ConfigDict(extra='ignore')
    browse_id: str | None = Field(None, alias='browseId')
    canonical_base_url: str | None = Field(None, alias='canonicalBaseUrl')

class NavigationEndpoint4(BaseModel):
    model_config = ConfigDict(extra='ignore')
    click_tracking_params: str | None = Field(None, alias='clickTrackingParams')
    command_metadata: CommandMetadata19 | None = Field(None, alias='commandMetadata')
    browse_endpoint: BrowseEndpoint3 | None = Field(None, alias='browseEndpoint')

class Run24(BaseModel):
    model_config = ConfigDict(extra='ignore')
    text: str | None = None
    navigation_endpoint: NavigationEndpoint4 | None = Field(None, alias='navigationEndpoint')

class ShortBylineText(BaseModel):
    model_config = ConfigDict(extra='ignore')
    runs: list[Run24] | None = None

class Run25(BaseModel):
    model_config = ConfigDict(extra='ignore')
    text: str | None = None

class VideoCountText(BaseModel):
    model_config = ConfigDict(extra='ignore')
    runs: list[Run25] | None = None

class WebCommandMetadata20(BaseModel):
    model_config = ConfigDict(extra='ignore')
    url: str | None = None
    web_page_type: str | None = Field(None, alias='webPageType')
    root_ve: int | None = Field(None, alias='rootVe')

class CommandMetadata20(BaseModel):
    model_config = ConfigDict(extra='ignore')
    web_command_metadata: WebCommandMetadata20 | None = Field(None, alias='webCommandMetadata')

class LoggingContext11(BaseModel):
    model_config = ConfigDict(extra='ignore')
    vss_logging_context: VssLoggingContext | None = Field(None, alias='vssLoggingContext')

class Html5PlaybackOnesieConfig4(BaseModel):
    model_config = ConfigDict(extra='ignore')
    common_config: CommonConfig | None = Field(None, alias='commonConfig')

class WatchEndpointSupportedOnesieConfig4(BaseModel):
    model_config = ConfigDict(extra='ignore')
    html5_playback_onesie_config: Html5PlaybackOnesieConfig4 | None = Field(None, alias='html5PlaybackOnesieConfig')

class WatchEndpoint4(BaseModel):
    model_config = ConfigDict(extra='ignore')
    video_id: str | None = Field(None, alias='videoId')
    playlist_id: str | None = Field(None, alias='playlistId')
    params: str | None = None
    logging_context: LoggingContext11 | None = Field(None, alias='loggingContext')
    watch_endpoint_supported_onesie_config: WatchEndpointSupportedOnesieConfig4 | None = Field(None, alias='watchEndpointSupportedOnesieConfig')
    player_params: str | None = Field(None, alias='playerParams')

class NavigationEndpoint5(BaseModel):
    model_config = ConfigDict(extra='ignore')
    click_tracking_params: str | None = Field(None, alias='clickTrackingParams')
    command_metadata: CommandMetadata20 | None = Field(None, alias='commandMetadata')
    watch_endpoint: WatchEndpoint4 | None = Field(None, alias='watchEndpoint')

class VideoCountShortText(BaseModel):
    model_config = ConfigDict(extra='ignore')
    simple_text: str | None = Field(None, alias='simpleText')

class Thumbnail5(BaseModel):
    model_config = ConfigDict(extra='ignore')
    url: str | None = None
    width: int | None = None
    height: int | None = None

class SidebarThumbnail(BaseModel):
    model_config = ConfigDict(extra='ignore')
    thumbnails: list[Thumbnail5] | None = None

class Run26(BaseModel):
    model_config = ConfigDict(extra='ignore')
    text: str | None = None
    bold: bool | None = None

class ThumbnailText(BaseModel):
    model_config = ConfigDict(extra='ignore')
    runs: list[Run26] | None = None

class Thumbnail6(BaseModel):
    model_config = ConfigDict(extra='ignore')
    thumbnails: list[Thumbnail5] | None = None
    sampled_thumbnail_color: SampledThumbnailColor | None = Field(None, alias='sampledThumbnailColor')
    dark_color_palette: DarkColorPalette | None = Field(None, alias='darkColorPalette')
    vibrant_color_palette: VibrantColorPalette | None = Field(None, alias='vibrantColorPalette')

class PlaylistCustomThumbnailRenderer(BaseModel):
    model_config = ConfigDict(extra='ignore')
    thumbnail: Thumbnail6 | None = None

class ThumbnailRenderer(BaseModel):
    model_config = ConfigDict(extra='ignore')
    playlist_custom_thumbnail_renderer: PlaylistCustomThumbnailRenderer | None = Field(None, alias='playlistCustomThumbnailRenderer')

class WebCommandMetadata21(BaseModel):
    model_config = ConfigDict(extra='ignore')
    url: str | None = None
    web_page_type: str | None = Field(None, alias='webPageType')
    root_ve: int | None = Field(None, alias='rootVe')
    api_url: str | None = Field(None, alias='apiUrl')

class CommandMetadata21(BaseModel):
    model_config = ConfigDict(extra='ignore')
    web_command_metadata: WebCommandMetadata21 | None = Field(None, alias='webCommandMetadata')

class NavigationEndpoint6(BaseModel):
    model_config = ConfigDict(extra='ignore')
    click_tracking_params: str | None = Field(None, alias='clickTrackingParams')
    command_metadata: CommandMetadata21 | None = Field(None, alias='commandMetadata')
    browse_endpoint: BrowseEndpoint3 | None = Field(None, alias='browseEndpoint')

class Run27(BaseModel):
    model_config = ConfigDict(extra='ignore')
    text: str | None = None
    navigation_endpoint: NavigationEndpoint6 | None = Field(None, alias='navigationEndpoint')

class LongBylineText(BaseModel):
    model_config = ConfigDict(extra='ignore')
    runs: list[Run27] | None = None

class Text10(BaseModel):
    model_config = ConfigDict(extra='ignore')
    simple_text: str | None = Field(None, alias='simpleText')

class ThumbnailOverlayBottomPanelRenderer(BaseModel):
    model_config = ConfigDict(extra='ignore')
    text: Text10 | None = None
    icon: Icon4 | None = None

class Run28(BaseModel):
    model_config = ConfigDict(extra='ignore')
    text: str | None = None

class Text11(BaseModel):
    model_config = ConfigDict(extra='ignore')
    runs: list[Run28] | None = None

class ThumbnailOverlayHoverTextRenderer(BaseModel):
    model_config = ConfigDict(extra='ignore')
    text: Text11 | None = None
    icon: Icon4 | None = None

class Text12(BaseModel):
    model_config = ConfigDict(extra='ignore')
    runs: list[Run28] | None = None

class ThumbnailOverlayNowPlayingRenderer(BaseModel):
    model_config = ConfigDict(extra='ignore')
    text: Text12 | None = None

class ThumbnailOverlay(BaseModel):
    model_config = ConfigDict(extra='ignore')
    thumbnail_overlay_bottom_panel_renderer: ThumbnailOverlayBottomPanelRenderer | None = Field(None, alias='thumbnailOverlayBottomPanelRenderer')
    thumbnail_overlay_hover_text_renderer: ThumbnailOverlayHoverTextRenderer | None = Field(None, alias='thumbnailOverlayHoverTextRenderer')
    thumbnail_overlay_now_playing_renderer: ThumbnailOverlayNowPlayingRenderer | None = Field(None, alias='thumbnailOverlayNowPlayingRenderer')

class CommandMetadata22(BaseModel):
    model_config = ConfigDict(extra='ignore')
    web_command_metadata: WebCommandMetadata21 | None = Field(None, alias='webCommandMetadata')

class BrowseEndpoint5(BaseModel):
    model_config = ConfigDict(extra='ignore')
    browse_id: str | None = Field(None, alias='browseId')

class NavigationEndpoint7(BaseModel):
    model_config = ConfigDict(extra='ignore')
    click_tracking_params: str | None = Field(None, alias='clickTrackingParams')
    command_metadata: CommandMetadata22 | None = Field(None, alias='commandMetadata')
    browse_endpoint: BrowseEndpoint5 | None = Field(None, alias='browseEndpoint')

class Run30(BaseModel):
    model_config = ConfigDict(extra='ignore')
    text: str | None = None
    navigation_endpoint: NavigationEndpoint7 | None = Field(None, alias='navigationEndpoint')

class ViewPlaylistText(BaseModel):
    model_config = ConfigDict(extra='ignore')
    runs: list[Run30] | None = None

class PublishedTimeText(BaseModel):
    model_config = ConfigDict(extra='ignore')
    simple_text: str | None = Field(None, alias='simpleText')

class GridPlaylistRenderer(BaseModel):
    model_config = ConfigDict(extra='ignore')
    playlist_id: str | None = Field(None, alias='playlistId')
    thumbnail: Thumbnail3 | None = None
    title: Title9 | None = None
    short_byline_text: ShortBylineText | None = Field(None, alias='shortBylineText')
    video_count_text: VideoCountText | None = Field(None, alias='videoCountText')
    navigation_endpoint: NavigationEndpoint5 | None = Field(None, alias='navigationEndpoint')
    video_count_short_text: VideoCountShortText | None = Field(None, alias='videoCountShortText')
    tracking_params: str | None = Field(None, alias='trackingParams')
    sidebar_thumbnails: list[SidebarThumbnail] | None = Field(None, alias='sidebarThumbnails')
    thumbnail_text: ThumbnailText | None = Field(None, alias='thumbnailText')
    thumbnail_renderer: ThumbnailRenderer | None = Field(None, alias='thumbnailRenderer')
    long_byline_text: LongBylineText | None = Field(None, alias='longBylineText')
    thumbnail_overlays: list[ThumbnailOverlay] | None = Field(None, alias='thumbnailOverlays')
    view_playlist_text: ViewPlaylistText | None = Field(None, alias='viewPlaylistText')
    published_time_text: PublishedTimeText | None = Field(None, alias='publishedTimeText')

class WebCommandMetadata23(BaseModel):
    model_config = ConfigDict(extra='ignore')
    send_post: bool | None = Field(None, alias='sendPost')
    api_url: str | None = Field(None, alias='apiUrl')

class CommandMetadata23(BaseModel):
    model_config = ConfigDict(extra='ignore')
    web_command_metadata: WebCommandMetadata23 | None = Field(None, alias='webCommandMetadata')

class ContinuationEndpoint4(BaseModel):
    model_config = ConfigDict(extra='ignore')
    click_tracking_params: str | None = Field(None, alias='clickTrackingParams')
    command_metadata: CommandMetadata23 | None = Field(None, alias='commandMetadata')
    continuation_command: ContinuationCommand | None = Field(None, alias='continuationCommand')

class ContinuationItemRenderer4(BaseModel):
    model_config = ConfigDict(extra='ignore')
    trigger: str | None = None
    continuation_endpoint: ContinuationEndpoint4 | None = Field(None, alias='continuationEndpoint')

class Item1(BaseModel):
    model_config = ConfigDict(extra='ignore')
    grid_playlist_renderer: GridPlaylistRenderer | None = Field(None, alias='gridPlaylistRenderer')
    continuation_item_renderer: ContinuationItemRenderer4 | None = Field(None, alias='continuationItemRenderer')

class GridRenderer(BaseModel):
    model_config = ConfigDict(extra='ignore')
    items: list[Item1] | None = None
    is_collapsible: bool | None = Field(None, alias='isCollapsible')
    tracking_params: str | None = Field(None, alias='trackingParams')
    target_id: UUID | None = Field(None, alias='targetId')

class Thumbnail9(BaseModel):
    model_config = ConfigDict(extra='ignore')
    url: str | None = None
    width: int | None = None
    height: int | None = None

class Thumbnail8(BaseModel):
    model_config = ConfigDict(extra='ignore')
    thumbnails: list[Thumbnail9] | None = None
    sampled_thumbnail_color: SampledThumbnailColor | None = Field(None, alias='sampledThumbnailColor')
    dark_color_palette: DarkColorPalette | None = Field(None, alias='darkColorPalette')
    vibrant_color_palette: VibrantColorPalette | None = Field(None, alias='vibrantColorPalette')

class WebCommandMetadata24(BaseModel):
    model_config = ConfigDict(extra='ignore')
    url: str | None = None
    web_page_type: str | None = Field(None, alias='webPageType')
    root_ve: int | None = Field(None, alias='rootVe')

class CommandMetadata24(BaseModel):
    model_config = ConfigDict(extra='ignore')
    web_command_metadata: WebCommandMetadata24 | None = Field(None, alias='webCommandMetadata')

class LoggingContext12(BaseModel):
    model_config = ConfigDict(extra='ignore')
    vss_logging_context: VssLoggingContext | None = Field(None, alias='vssLoggingContext')

class Html5PlaybackOnesieConfig5(BaseModel):
    model_config = ConfigDict(extra='ignore')
    common_config: CommonConfig | None = Field(None, alias='commonConfig')

class WatchEndpointSupportedOnesieConfig5(BaseModel):
    model_config = ConfigDict(extra='ignore')
    html5_playback_onesie_config: Html5PlaybackOnesieConfig5 | None = Field(None, alias='html5PlaybackOnesieConfig')

class WatchEndpoint5(BaseModel):
    model_config = ConfigDict(extra='ignore')
    video_id: str | None = Field(None, alias='videoId')
    playlist_id: str | None = Field(None, alias='playlistId')
    params: str | None = None
    player_params: str | None = Field(None, alias='playerParams')
    logging_context: LoggingContext12 | None = Field(None, alias='loggingContext')
    watch_endpoint_supported_onesie_config: WatchEndpointSupportedOnesieConfig5 | None = Field(None, alias='watchEndpointSupportedOnesieConfig')

class NavigationEndpoint8(BaseModel):
    model_config = ConfigDict(extra='ignore')
    click_tracking_params: str | None = Field(None, alias='clickTrackingParams')
    command_metadata: CommandMetadata24 | None = Field(None, alias='commandMetadata')
    watch_endpoint: WatchEndpoint5 | None = Field(None, alias='watchEndpoint')

class Run31(BaseModel):
    model_config = ConfigDict(extra='ignore')
    text: str | None = None
    navigation_endpoint: NavigationEndpoint8 | None = Field(None, alias='navigationEndpoint')

class Title10(BaseModel):
    model_config = ConfigDict(extra='ignore')
    runs: list[Run31] | None = None

class WebCommandMetadata25(BaseModel):
    model_config = ConfigDict(extra='ignore')
    url: str | None = None
    web_page_type: str | None = Field(None, alias='webPageType')
    root_ve: int | None = Field(None, alias='rootVe')
    api_url: str | None = Field(None, alias='apiUrl')

class CommandMetadata25(BaseModel):
    model_config = ConfigDict(extra='ignore')
    web_command_metadata: WebCommandMetadata25 | None = Field(None, alias='webCommandMetadata')

class BrowseEndpoint6(BaseModel):
    model_config = ConfigDict(extra='ignore')
    browse_id: str | None = Field(None, alias='browseId')
    canonical_base_url: str | None = Field(None, alias='canonicalBaseUrl')

class NavigationEndpoint9(BaseModel):
    model_config = ConfigDict(extra='ignore')
    click_tracking_params: str | None = Field(None, alias='clickTrackingParams')
    command_metadata: CommandMetadata25 | None = Field(None, alias='commandMetadata')
    browse_endpoint: BrowseEndpoint6 | None = Field(None, alias='browseEndpoint')

class Run32(BaseModel):
    model_config = ConfigDict(extra='ignore')
    text: str | None = None
    navigation_endpoint: NavigationEndpoint9 | None = Field(None, alias='navigationEndpoint')

class ShortBylineText1(BaseModel):
    model_config = ConfigDict(extra='ignore')
    runs: list[Run32] | None = None

class Run33(BaseModel):
    model_config = ConfigDict(extra='ignore')
    text: str | None = None

class VideoCountText1(BaseModel):
    model_config = ConfigDict(extra='ignore')
    runs: list[Run33] | None = None

class WebCommandMetadata26(BaseModel):
    model_config = ConfigDict(extra='ignore')
    url: str | None = None
    web_page_type: str | None = Field(None, alias='webPageType')
    root_ve: int | None = Field(None, alias='rootVe')

class CommandMetadata26(BaseModel):
    model_config = ConfigDict(extra='ignore')
    web_command_metadata: WebCommandMetadata26 | None = Field(None, alias='webCommandMetadata')

class LoggingContext13(BaseModel):
    model_config = ConfigDict(extra='ignore')
    vss_logging_context: VssLoggingContext | None = Field(None, alias='vssLoggingContext')

class Html5PlaybackOnesieConfig6(BaseModel):
    model_config = ConfigDict(extra='ignore')
    common_config: CommonConfig | None = Field(None, alias='commonConfig')

class WatchEndpointSupportedOnesieConfig6(BaseModel):
    model_config = ConfigDict(extra='ignore')
    html5_playback_onesie_config: Html5PlaybackOnesieConfig6 | None = Field(None, alias='html5PlaybackOnesieConfig')

class WatchEndpoint6(BaseModel):
    model_config = ConfigDict(extra='ignore')
    video_id: str | None = Field(None, alias='videoId')
    playlist_id: str | None = Field(None, alias='playlistId')
    params: str | None = None
    player_params: str | None = Field(None, alias='playerParams')
    logging_context: LoggingContext13 | None = Field(None, alias='loggingContext')
    watch_endpoint_supported_onesie_config: WatchEndpointSupportedOnesieConfig6 | None = Field(None, alias='watchEndpointSupportedOnesieConfig')

class NavigationEndpoint10(BaseModel):
    model_config = ConfigDict(extra='ignore')
    click_tracking_params: str | None = Field(None, alias='clickTrackingParams')
    command_metadata: CommandMetadata26 | None = Field(None, alias='commandMetadata')
    watch_endpoint: WatchEndpoint6 | None = Field(None, alias='watchEndpoint')

class Thumbnail10(BaseModel):
    model_config = ConfigDict(extra='ignore')
    url: str | None = None
    width: int | None = None
    height: int | None = None

class SidebarThumbnail1(BaseModel):
    model_config = ConfigDict(extra='ignore')
    thumbnails: list[Thumbnail10] | None = None

class Run34(BaseModel):
    model_config = ConfigDict(extra='ignore')
    text: str | None = None
    bold: bool | None = None

class ThumbnailText1(BaseModel):
    model_config = ConfigDict(extra='ignore')
    runs: list[Run34] | None = None

class Thumbnail11(BaseModel):
    model_config = ConfigDict(extra='ignore')
    thumbnails: list[Thumbnail10] | None = None
    sampled_thumbnail_color: SampledThumbnailColor | None = Field(None, alias='sampledThumbnailColor')
    dark_color_palette: DarkColorPalette | None = Field(None, alias='darkColorPalette')
    vibrant_color_palette: VibrantColorPalette | None = Field(None, alias='vibrantColorPalette')

class PlaylistCustomThumbnailRenderer1(BaseModel):
    model_config = ConfigDict(extra='ignore')
    thumbnail: Thumbnail11 | None = None

class ThumbnailRenderer1(BaseModel):
    model_config = ConfigDict(extra='ignore')
    playlist_custom_thumbnail_renderer: PlaylistCustomThumbnailRenderer1 | None = Field(None, alias='playlistCustomThumbnailRenderer')

class WebCommandMetadata27(BaseModel):
    model_config = ConfigDict(extra='ignore')
    url: str | None = None
    web_page_type: str | None = Field(None, alias='webPageType')
    root_ve: int | None = Field(None, alias='rootVe')
    api_url: str | None = Field(None, alias='apiUrl')

class CommandMetadata27(BaseModel):
    model_config = ConfigDict(extra='ignore')
    web_command_metadata: WebCommandMetadata27 | None = Field(None, alias='webCommandMetadata')

class NavigationEndpoint11(BaseModel):
    model_config = ConfigDict(extra='ignore')
    click_tracking_params: str | None = Field(None, alias='clickTrackingParams')
    command_metadata: CommandMetadata27 | None = Field(None, alias='commandMetadata')
    browse_endpoint: BrowseEndpoint6 | None = Field(None, alias='browseEndpoint')

class Run35(BaseModel):
    model_config = ConfigDict(extra='ignore')
    text: str | None = None
    navigation_endpoint: NavigationEndpoint11 | None = Field(None, alias='navigationEndpoint')

class LongBylineText1(BaseModel):
    model_config = ConfigDict(extra='ignore')
    runs: list[Run35] | None = None

class Text13(BaseModel):
    model_config = ConfigDict(extra='ignore')
    simple_text: str | None = Field(None, alias='simpleText')

class ThumbnailOverlayBottomPanelRenderer1(BaseModel):
    model_config = ConfigDict(extra='ignore')
    text: Text13 | None = None
    icon: Icon4 | None = None

class Run36(BaseModel):
    model_config = ConfigDict(extra='ignore')
    text: str | None = None

class Text14(BaseModel):
    model_config = ConfigDict(extra='ignore')
    runs: list[Run36] | None = None

class ThumbnailOverlayHoverTextRenderer1(BaseModel):
    model_config = ConfigDict(extra='ignore')
    text: Text14 | None = None
    icon: Icon4 | None = None

class Text15(BaseModel):
    model_config = ConfigDict(extra='ignore')
    runs: list[Run36] | None = None

class ThumbnailOverlayNowPlayingRenderer1(BaseModel):
    model_config = ConfigDict(extra='ignore')
    text: Text15 | None = None

class ThumbnailOverlay1(BaseModel):
    model_config = ConfigDict(extra='ignore')
    thumbnail_overlay_bottom_panel_renderer: ThumbnailOverlayBottomPanelRenderer1 | None = Field(None, alias='thumbnailOverlayBottomPanelRenderer')
    thumbnail_overlay_hover_text_renderer: ThumbnailOverlayHoverTextRenderer1 | None = Field(None, alias='thumbnailOverlayHoverTextRenderer')
    thumbnail_overlay_now_playing_renderer: ThumbnailOverlayNowPlayingRenderer1 | None = Field(None, alias='thumbnailOverlayNowPlayingRenderer')

class CommandMetadata28(BaseModel):
    model_config = ConfigDict(extra='ignore')
    web_command_metadata: WebCommandMetadata27 | None = Field(None, alias='webCommandMetadata')

class BrowseEndpoint8(BaseModel):
    model_config = ConfigDict(extra='ignore')
    browse_id: str | None = Field(None, alias='browseId')

class NavigationEndpoint12(BaseModel):
    model_config = ConfigDict(extra='ignore')
    click_tracking_params: str | None = Field(None, alias='clickTrackingParams')
    command_metadata: CommandMetadata28 | None = Field(None, alias='commandMetadata')
    browse_endpoint: BrowseEndpoint8 | None = Field(None, alias='browseEndpoint')

class Run38(BaseModel):
    model_config = ConfigDict(extra='ignore')
    text: str | None = None
    navigation_endpoint: NavigationEndpoint12 | None = Field(None, alias='navigationEndpoint')

class ViewPlaylistText1(BaseModel):
    model_config = ConfigDict(extra='ignore')
    runs: list[Run38] | None = None

class GridPlaylistRenderer1(BaseModel):
    model_config = ConfigDict(extra='ignore')
    playlist_id: str | None = Field(None, alias='playlistId')
    thumbnail: Thumbnail8 | None = None
    title: Title10 | None = None
    short_byline_text: ShortBylineText1 | None = Field(None, alias='shortBylineText')
    video_count_text: VideoCountText1 | None = Field(None, alias='videoCountText')
    navigation_endpoint: NavigationEndpoint10 | None = Field(None, alias='navigationEndpoint')
    video_count_short_text: VideoCountShortText | None = Field(None, alias='videoCountShortText')
    tracking_params: str | None = Field(None, alias='trackingParams')
    sidebar_thumbnails: list[SidebarThumbnail1] | None = Field(None, alias='sidebarThumbnails')
    thumbnail_text: ThumbnailText1 | None = Field(None, alias='thumbnailText')
    thumbnail_renderer: ThumbnailRenderer1 | None = Field(None, alias='thumbnailRenderer')
    long_byline_text: LongBylineText1 | None = Field(None, alias='longBylineText')
    thumbnail_overlays: list[ThumbnailOverlay1] | None = Field(None, alias='thumbnailOverlays')
    view_playlist_text: ViewPlaylistText1 | None = Field(None, alias='viewPlaylistText')
    published_time_text: PublishedTimeText | None = Field(None, alias='publishedTimeText')

class ContinuationItem(BaseModel):
    model_config = ConfigDict(extra='ignore')
    grid_renderer: GridRenderer | None = Field(None, alias='gridRenderer')
    grid_playlist_renderer: GridPlaylistRenderer1 | None = Field(None, alias='gridPlaylistRenderer')

class AppendContinuationItemsAction(BaseModel):
    model_config = ConfigDict(extra='ignore')
    continuation_items: list[ContinuationItem] | None = Field(None, alias='continuationItems')
    target_id: UUID | None = Field(None, alias='targetId')

class OnResponseReceivedEndpoint(BaseModel):
    model_config = ConfigDict(extra='ignore')
    click_tracking_params: str | None = Field(None, alias='clickTrackingParams')
    append_continuation_items_action: AppendContinuationItemsAction | None = Field(None, alias='appendContinuationItemsAction')

class TopicModel(BaseModel):
    model_config = ConfigDict(extra='ignore')
    response_context: ResponseContext | None = Field(None, alias='responseContext')
    contents: Contents | None = None
    header: Header3 | None = None
    metadata: Metadata3 | None = None
    tracking_params: str | None = Field(None, alias='trackingParams')
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
