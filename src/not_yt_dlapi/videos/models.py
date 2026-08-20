# TODO: Validate
"""Videos models.

Shaped after the video resource as the API documents it: one class per
documented object, one field per documented property, and the API's own wording
for what each property is.

Every part the API will hand out is always asked for, so a property is optional
here only when the video itself decides whether to carry it, never because the
request might not have asked. `fileDetails`, `processingDetails`, `suggestions`
and `brandPartner` are the exception: they are modelled because they are
documented, but they only arrive for the video's own owner and the parts that
carry the first three are never asked for.
"""

from __future__ import annotations

from typing import Any, Self, override

from pydantic import Field, SkipValidation

from not_yt_dlapi.base_response_model import BaseResponseModel
from not_yt_dlapi.common_models import (
    APIModel,
    Localization,
    Localizations,
    PageInfo,
    Thumbnails,
)


# TODO: Validate
class VideoSnippet(APIModel):
    """The `snippet` object contains basic details about the video, such as its title, description, and category.

    Attributes:
        published_at: The date and time that the video was published. Note that
            this time might be different than the time that the video was
            uploaded.
        channel_id: The ID that YouTube uses to uniquely identify the channel
            that the video was uploaded to.
        title: The video's title. The property value has a maximum length of 100
            characters and may contain all valid UTF-8 characters except `<` and
            `>`.
        description: The video's description. The property value has a maximum
            length of 5000 bytes and may contain all valid UTF-8 characters
            except `<` and `>`.
        thumbnails: The thumbnail images associated with the video.
        channel_title: Channel title for the channel that the video belongs to.
        tags: A list of keyword tags associated with the video. Tags may contain
            spaces. The property value has a maximum length of 500 characters.
        category_id: The YouTube video category associated with the video.
        live_broadcast_content: Indicates if the video is an upcoming/active
            live broadcast. Its value is `none` if the video is not an
            upcoming/active live broadcast.
        default_language: The language of the text in the `video` resource's
            `snippet.title` and `snippet.description` properties.
        localized: The `snippet.localized` object contains either a localized
            title and description for the video or the title in the default
            language for the video's metadata.
        default_audio_language: The `default_audio_language` property specifies
            the language spoken in the video's default audio track.
    """  # noqa: E501

    published_at: str
    channel_id: str
    title: str
    description: str
    thumbnails: Thumbnails
    channel_title: str
    # Only a video the uploader gave keywords to has any.
    tags: list[str] | None = None
    category_id: str
    live_broadcast_content: str
    # Only a video whose uploader said what language it is in has these.
    default_language: str | None = None
    localized: Localization
    default_audio_language: str | None = None


# TODO: Validate
class RegionRestriction(APIModel):
    """The `regionRestriction` object contains information about the countries where a video is (or is not) viewable.

    Attributes:
        allowed: A list of region codes that identify countries where the video
            is viewable. If this property is present and a country is not listed
            in its value, then the video is blocked from appearing in that
            country.
        blocked: A list of region codes that identify countries where the video
            is blocked. If this property is present and a country is not listed
            in its value, then the video is viewable in that country.
    """  # noqa: E501

    allowed: list[str] | None = None
    blocked: list[str] | None = None


# TODO: Validate
class ContentRating(APIModel):
    """Specifies the ratings that the video received under various rating schemes.

    One field per rating board the API knows, because a video is rated by
    whichever boards happen to have rated it rather than on a single scale, and
    a video carries only the ratings it was given.

    Attributes:
        acb_rating: The video's Australian Classification Board (ACB) or
            Australian Communications and Media Authority (ACMA) rating.
        agcom_rating: The video's rating from Italy's Autorità per le Garanzie
            nelle Comunicazioni (AGCOM).
        anatel_rating: The video's Anatel (Asociación Nacional de Televisión)
            rating for Chilean television.
        bbfc_rating: The video's British Board of Film Classification (BBFC)
            rating.
        bfvc_rating: The video's rating from Thailand's Board of Film and Video
            Censors.
        bmukk_rating: The video's rating from the Austrian Board of Media
            Classification (Bundesministerium für Unterricht, Kunst und Kultur).
        catv_rating: The video's rating from the Canadian Radio-Television and
            Telecommunications Commission (CRTC).
        catvfr_rating: The video's rating from the Canadian Radio-Television and
            Telecommunications Commission (CRTC) for Canadian French-language
            broadcasts.
        cbfc_rating: The video's Central Board of Film Certification (CBFC -
            India) rating.
        ccc_rating: The video's Consejo de Calificación Cinematográfica (Chile)
            rating.
        cce_rating: The video's rating from Portugal's Comissão de Classificação
            de Espectáculos.
        chfilm_rating: The video's rating in Switzerland.
        chvrs_rating: The video's Canadian Home Video Rating System (CHVRS)
            rating.
        cicf_rating: The video's rating from the Commission de Contrôle des
            Films (Belgium).
        cna_rating: The video's rating from Romania's CONSILIUL NATIONAL AL
            AUDIOVIZUALULUI (CNA).
        cnc_rating: The video's rating from France's Commission de
            classification cinematographique.
        csa_rating: The video's rating from France's Conseil supérieur de
            l'audiovisuel, which rates broadcast content.
        cscf_rating: The video's rating from Luxembourg's Commission de
            surveillance de la classification des films (CSCF).
        czfilm_rating: The video's rating in the Czech Republic.
        djctq_rating: The video's Departamento de Justiça, Classificação,
            Qualificação e Títulos (DJCQT - Brazil) rating.
        djctq_rating_reasons: Reasons that explain why the video received its
            DJCQT (Brazil) rating.
        ecbmct_rating: The video's rating from Turkey's Evaluation and
            Classification Board of the Ministry of Culture and Tourism.
        eefilm_rating: The video's rating in Estonia.
        egfilm_rating: The video's rating in Egypt.
        eirin_rating: The video's Eirin (映倫) rating. Eirin is the Japanese
            rating system.
        fcbm_rating: The video's rating from Malaysia's Film Censorship Board.
        fco_rating: The video's rating from Hong Kong's Office for Film,
            Newspaper and Article Administration.
        fmoc_rating: This property has been deprecated as of November 2, 2015.
            Use the `contentDetails.contentRating.cncRating` property instead.
            The video's Centre national du cinéma et de l'image animé (French
            Ministry of Culture) rating.
        fpb_rating: The video's rating from South Africa's Film and Publication
            Board.
        fpb_rating_reasons: Reasons that explain why the video received its FPB
            (South Africa) rating.
        fsk_rating: The video's Freiwillige Selbstkontrolle der Filmwirtschaft
            (FSK - Germany) rating.
        grfilm_rating: The video's rating in Greece.
        icaa_rating: The video's Instituto de la Cinematografía y de las Artes
            Audiovisuales (ICAA - Spain) rating.
        ifco_rating: The video's Irish Film Classification Office (IFCO -
            Ireland) rating.
        ilfilm_rating: The video's rating in Israel.
        incaa_rating: The video's INCAA (Instituto Nacional de Cine y Artes
            Audiovisuales - Argentina) rating.
        kfcb_rating: The video's rating from the Kenya Film Classification
            Board.
        kijkwijzer_rating: The video's rating from the Nederlands Instituut voor
            de Classificatie van Audiovisuele Media (Netherlands).
        kmrb_rating: The video's Korea Media Rating Board (영상물등급위원회)
            rating. The KMRB rates videos in South Korea.
        lsf_rating: The video's rating from Indonesia's Lembaga Sensor Film.
        mccaa_rating: The video's rating from Malta's Film Age-Classification
            Board.
        mccyp_rating: The video's rating from the Danish Film Institute's (Det
            Danske Filminstitut) Media Council for Children and Young People.
        mcst_rating: The video's rating system for Vietnam - MCST.
        mda_rating: The video's rating from Singapore's Media Development
            Authority (MDA) and, specifically, it's Board of Film Censors (BFC).
        medietilsynet_rating: The video's rating from Medietilsynet, the
            Norwegian Media Authority.
        meku_rating: The video's rating from Finland's Kansallinen
            Audiovisuaalinen Instituutti (National Audiovisual Institute).
        mibac_rating: The video's rating from the Ministero dei Beni e delle
            Attività Culturali e del Turismo (Italy).
        moc_rating: The video's Ministerio de Cultura (Colombia) rating.
        moctw_rating: The video's rating from Taiwan's Ministry of Culture
            (文化部).
        mpaa_rating: The video's Motion Picture Association of America (MPAA)
            rating.
        mpaat_rating: The Motion Picture Association of America's rating for
            movie trailers and preview.
        mtrcb_rating: The video's rating from the Movie and Television Review
            and Classification Board (Philippines).
        nbc_rating: The video's rating from the Maldives National Bureau of
            Classification.
        nbcpl_rating: The docs list this property without a description of its
            own.
        nfrc_rating: The video's rating from the Bulgarian National Film Center.
        nfvcb_rating: The video's rating from Nigeria's National Film and Video
            Censors Board.
        nkclv_rating: The video's rating from the Nacionãlais Kino centrs
            (National Film Centre of Latvia).
        oflc_rating: The video's Office of Film and Literature Classification
            (OFLC - New Zealand) rating.
        pefilm_rating: The video's rating in Peru.
        rcnof_rating: The docs list this property without a description of its
            own.
        resorteviolencia_rating: The video's rating in Venezuela.
        rtc_rating: The video's General Directorate of Radio, Television and
            Cinematography (Mexico) rating.
        rte_rating: The video's rating from Ireland's Raidió Teilifís Éireann.
        russia_rating: The video's National Film Registry of the Russian
            Federation (MKRF - Russia) rating.
        skfilm_rating: The video's rating in Slovakia.
        smais_rating: The video's rating in Iceland.
        smsa_rating: The video's rating from Statens medieråd (Sweden's National
            Media Council).
        tvpg_rating: The video's TV Parental Guidelines (TVPG) rating.
        yt_rating: A rating that YouTube uses to identify age-restricted
            content.
    """

    acb_rating: str | None = None
    agcom_rating: str | None = None
    anatel_rating: str | None = None
    bbfc_rating: str | None = None
    bfvc_rating: str | None = None
    bmukk_rating: str | None = None
    catv_rating: str | None = None
    catvfr_rating: str | None = None
    cbfc_rating: str | None = None
    ccc_rating: str | None = None
    cce_rating: str | None = None
    chfilm_rating: str | None = None
    chvrs_rating: str | None = None
    cicf_rating: str | None = None
    cna_rating: str | None = None
    cnc_rating: str | None = None
    csa_rating: str | None = None
    cscf_rating: str | None = None
    czfilm_rating: str | None = None
    djctq_rating: str | None = None
    djctq_rating_reasons: list[str] | None = None
    ecbmct_rating: str | None = None
    eefilm_rating: str | None = None
    egfilm_rating: str | None = None
    eirin_rating: str | None = None
    fcbm_rating: str | None = None
    fco_rating: str | None = None
    fmoc_rating: str | None = None
    fpb_rating: str | None = None
    fpb_rating_reasons: list[str] | None = None
    fsk_rating: str | None = None
    grfilm_rating: str | None = None
    icaa_rating: str | None = None
    ifco_rating: str | None = None
    ilfilm_rating: str | None = None
    incaa_rating: str | None = None
    kfcb_rating: str | None = None
    kijkwijzer_rating: str | None = None
    kmrb_rating: str | None = None
    lsf_rating: str | None = None
    mccaa_rating: str | None = None
    mccyp_rating: str | None = None
    mcst_rating: str | None = None
    mda_rating: str | None = None
    medietilsynet_rating: str | None = None
    meku_rating: str | None = None
    mibac_rating: str | None = None
    moc_rating: str | None = None
    moctw_rating: str | None = None
    mpaa_rating: str | None = None
    mpaat_rating: str | None = None
    mtrcb_rating: str | None = None
    nbc_rating: str | None = None
    nbcpl_rating: str | None = None
    nfrc_rating: str | None = None
    nfvcb_rating: str | None = None
    nkclv_rating: str | None = None
    oflc_rating: str | None = None
    pefilm_rating: str | None = None
    rcnof_rating: str | None = None
    resorteviolencia_rating: str | None = None
    rtc_rating: str | None = None
    rte_rating: str | None = None
    russia_rating: str | None = None
    skfilm_rating: str | None = None
    smais_rating: str | None = None
    smsa_rating: str | None = None
    tvpg_rating: str | None = None
    yt_rating: str | None = None


# TODO: Validate
class VideoContentDetails(APIModel):
    """The `contentDetails` object contains information about the video content, including the length of the video and an indication of whether captions are available for the video.

    Attributes:
        duration: The length of the video. The property value is an ISO 8601
            duration. For example, for a video that is at least one minute long
            and less than one hour long, the duration is in the format `PT#M#S`.
        dimension: Indicates whether the video is available in 3D or in 2D.
        definition: Indicates whether the video is available in high definition
            (`HD`) or only in standard definition.
        caption: Indicates whether captions are available for the video.
        licensed_content: Indicates whether the video represents licensed
            content, which means that the content was uploaded to a channel
            linked to a YouTube content partner and then claimed by that
            partner.
        region_restriction: The `regionRestriction` object contains information
            about the countries where a video is (or is not) viewable.
        content_rating: Specifies the ratings that the video received under
            various rating schemes.
        projection: Specifies the projection format of the video.
        has_custom_thumbnail: Indicates whether the video uploader has provided
            a custom thumbnail image for the video. This property is only
            visible to the video uploader.
    """  # noqa: E501

    duration: str
    dimension: str
    definition: str
    caption: str
    licensed_content: bool
    # Only a video that is kept out of somewhere says where.
    region_restriction: RegionRestriction | None = None
    content_rating: ContentRating
    projection: str
    # Only the video's own uploader is told this.
    has_custom_thumbnail: bool | None = None


# TODO: Validate
class VideoStatus(APIModel):
    """The `status` object contains information about the video's uploading, processing, and privacy statuses.

    Attributes:
        upload_status: The status of the uploaded video.
        failure_reason: This value explains why a video failed to upload. This
            property is only present if the `uploadStatus` property indicates
            that the upload failed.
        rejection_reason: This value explains why YouTube rejected an uploaded
            video. This property is only present if the `uploadStatus` property
            indicates that the upload was rejected.
        privacy_status: The video's privacy status.
        publish_at: The date and time when the video is scheduled to publish. It
            can be set only if the privacy status of the video is private.
        license: The video's license.
        embeddable: This value indicates whether the video can be embedded on
            another website.
        public_stats_viewable: This value indicates whether the extended video
            statistics on the video's watch page are publicly viewable.
        made_for_kids: This value indicates whether the video is designated as
            child-directed, and it contains the current "made for kids" status
            of the video.
        self_declared_made_for_kids: In a `videos.insert` or `videos.update`
            request, this property allows the channel owner to designate the
            video as being child-directed.
        contains_synthetic_media: In a `videos.insert` or `videos.update`
            request, this property allows the channel owner to disclose that a
            video contains realistic Altered or Synthetic (A/S) content.
    """  # noqa: E501

    upload_status: str
    failure_reason: str | None = None
    rejection_reason: str | None = None
    privacy_status: str
    publish_at: str | None = None
    license: str
    embeddable: bool
    public_stats_viewable: bool
    made_for_kids: bool
    # Only the video's own uploader is told these.
    self_declared_made_for_kids: bool | None = None
    contains_synthetic_media: bool | None = None


# TODO: Validate
class VideoStatistics(APIModel):
    """The `statistics` object contains statistics about the video.

    A video that hides a count leaves it out rather than sending a zero, and the
    counts it does send are written as strings.

    Attributes:
        view_count: The number of times the video has been viewed. Starting
            March 31, 2025, for Shorts, viewCount will return the number of
            times a Short starts to play or replay, with no minimum watch time
            requirement.
        like_count: The number of users who have indicated that they liked the
            video.
        dislike_count: The number of users who have indicated that they disliked
            the video.
        favorite_count: This property has been deprecated. The deprecation is
            effective as of August 28, 2015. The property's value is now always
            set to `0`.
        comment_count: The number of comments for the video.
    """

    # A video whose uploader has hidden its views or its likes, or turned off
    # its comments, leaves that count out, and dislikes are only shown to the
    # uploader.
    view_count: int | None = None
    like_count: int | None = None
    dislike_count: int | None = None
    favorite_count: int
    comment_count: int | None = None


# TODO: Validate
class PaidProductPlacementDetails(APIModel):
    """The `paidProductPlacementDetails` object contains information about paid product placement in the video.

    Attributes:
        has_paid_product_placement: Set to `true` if the content uses paid
            product placement. Defaults to `false`.
    """  # noqa: E501

    has_paid_product_placement: bool


# TODO: Validate
class VideoPlayer(APIModel):
    """The `player` object contains information that you would use to play the video in an embedded player.

    Attributes:
        embed_html: An `<iframe>` tag that embeds a player that plays the video.
        embed_height: The height of the embedded player returned in the
            `player.embedHtml` property. This property is only returned if the
            request specified a value for the `maxHeight` and/or `maxWidth`
            parameters and the video's aspect ratio is known.
        embed_width: The width of the embedded player returned in the
            `player.embedHtml` property. This property is only returned if the
            request specified a value for the `maxHeight` and/or `maxWidth`
            parameters and the video's aspect ratio is known.
    """  # noqa: E501

    embed_html: str
    # Neither size is ever asked for, so neither is ever answered with.
    embed_height: int | None = None
    embed_width: int | None = None


# TODO: Validate
class VideoTopicDetails(APIModel):
    """The `topicDetails` object encapsulates information about topics associated with the video.

    Attributes:
        topic_ids: This property has been deprecated as of November 10, 2016.
            The API no longer returns values for this property, and any topics
            associated with a video are now returned by the
            `topicDetails.relevantTopicIds[]` property value.
        relevant_topic_ids: A list of topic IDs that are relevant to the video.
            This property has been deprecated as of November 10, 2016. It will
            be supported until November 10, 2017.
        topic_categories: A list of Wikipedia URLs that provide a high-level
            description of the video's content.
    """  # noqa: E501

    topic_ids: list[str] | None = None
    relevant_topic_ids: list[str] | None = None
    topic_categories: list[str] | None = None


# TODO: Validate
class GeoPoint(APIModel):
    """The geolocation information associated with the video.

    Note that the child property values identify the location that the video
    owner wants to associate with the video. The value is editable, searchable
    on public videos, and might be displayed to users for public videos.

    Attributes:
        latitude: This property has been deprecated as of June 1, 2017. Latitude
            in degrees.
        longitude: This property has been deprecated as of June 1, 2017.
            Longitude in degrees.
        altitude: This property has been deprecated as of July 9, 2018. Altitude
            above the reference ellipsoid, in meters.
    """

    latitude: float | None = None
    longitude: float | None = None
    altitude: float | None = None


# TODO: Validate
class RecordingDetails(APIModel):
    """The `recordingDetails` object encapsulates information about the location, date and address where the video was recorded.

    Attributes:
        recording_date: The date and time when the video was recorded. The value
            is specified in ISO 8601 (`YYYY-MM-DDThh:mm:ss.sssZ`) format.
        location: The geolocation information associated with the video.
        location_description: This property has been deprecated as of June 1,
            2017. The text description of the location where the video was
            recorded.
    """  # noqa: E501

    # Only a video whose uploader filled these in carries them.
    recording_date: str | None = None
    location: GeoPoint | None = None
    location_description: str | None = None


# TODO: Validate
class VideoStream(APIModel):
    """One of the video streams contained in the uploaded video file.

    Attributes:
        width_pixels: The encoded video content's width in pixels. You can
            calculate the video's encoding aspect ratio as `width_pixels` /
            `height_pixels`.
        height_pixels: The encoded video content's height in pixels.
        frame_rate_fps: The video stream's frame rate, in frames per second.
        aspect_ratio: The video content's display aspect ratio, which specifies
            the aspect ratio in which the video should be displayed.
        codec: The video codec that the stream uses.
        bitrate_bps: The video stream's bitrate, in bits per second.
        rotation: The amount that YouTube needs to rotate the original source
            content to properly display the video.
        vendor: A value that uniquely identifies a video vendor. Typically, the
            value is a four-letter vendor code.
    """

    width_pixels: int | None = None
    height_pixels: int | None = None
    frame_rate_fps: float | None = None
    aspect_ratio: float | None = None
    codec: str | None = None
    bitrate_bps: int | None = None
    rotation: str | None = None
    vendor: str | None = None


# TODO: Validate
class AudioStream(APIModel):
    """One of the audio streams contained in the uploaded video file.

    Attributes:
        channel_count: The number of audio channels that the stream contains.
        codec: The audio codec that the stream uses.
        bitrate_bps: The audio stream's bitrate, in bits per second.
        vendor: A value that uniquely identifies a video vendor. Typically, the
            value is a four-letter vendor code.
    """

    channel_count: int | None = None
    codec: str | None = None
    bitrate_bps: int | None = None
    vendor: str | None = None


# TODO: Validate
class FileDetails(APIModel):
    """The `fileDetails` object encapsulates information about the video file that was uploaded to YouTube, including the file's resolution, duration, audio and video codecs, stream bitrates, and more.

    The part that carries it is refused to anyone but the video's own owner, so
    it is never asked for and never arrives.

    Attributes:
        file_name: The uploaded file's name. This field is present whether a
            video file or another type of file was uploaded.
        file_size: The uploaded file's size in bytes. This field is present
            whether a video file or another type of file was uploaded.
        file_type: The uploaded file's type as detected by YouTube's video
            processing engine. Currently, YouTube only processes video files,
            but this field is present whether a video file or another type of
            file was uploaded.
        container: The uploaded video file's container format.
        video_streams: A list of video streams contained in the uploaded video
            file. Each item in the list contains detailed metadata about a video
            stream.
        audio_streams: A list of audio streams contained in the uploaded video
            file. Each item in the list contains detailed metadata about an
            audio stream.
        duration_ms: The length of the uploaded video in milliseconds.
        bitrate_bps: The uploaded video file's combined (video and audio)
            bitrate in bits per second.
        creation_time: The date and time when the uploaded video file was
            created. The value is specified in ISO 8601 format.
    """  # noqa: E501

    file_name: str | None = None
    file_size: int | None = None
    file_type: str | None = None
    container: str | None = None
    video_streams: list[VideoStream] | None = None
    audio_streams: list[AudioStream] | None = None
    duration_ms: int | None = None
    bitrate_bps: int | None = None
    creation_time: str | None = None


# TODO: Validate
class ProcessingProgress(APIModel):
    """The `processingProgress` object contains information about the progress YouTube has made in processing the video.

    Attributes:
        parts_total: An estimate of the total number of parts that need to be
            processed for the video.
        parts_processed: The number of parts of the video that YouTube has
            already processed.
        time_left_ms: An estimate of the amount of time, in millseconds, that
            YouTube needs to finish processing the video.
    """  # noqa: E501

    parts_total: int | None = None
    parts_processed: int | None = None
    time_left_ms: int | None = None


# TODO: Validate
class ProcessingDetails(APIModel):
    """The `processingDetails` object encapsulates information about YouTube's progress in processing the uploaded video file.

    The part that carries it is refused to anyone but the video's own owner, so
    it is never asked for and never arrives.

    Attributes:
        processing_status: The video's processing status. This value indicates
            whether YouTube was able to process the video or if the video is
            still being processed.
        processing_progress: The `processingProgress` object contains
            information about the progress YouTube has made in processing the
            video.
        processing_failure_reason: The reason that YouTube failed to process the
            video. This property will only have a value if the
            `processingStatus` property's value is `failed`.
        file_details_availability: This value indicates whether file details are
            available for the uploaded video.
        processing_issues_availability: This value indicates whether the video
            processing engine has generated suggestions that might improve
            YouTube's ability to process the video, warnings that explain video
            processing problems, or errors that cause video processing problems.
        tag_suggestions_availability: This value indicates whether keyword (tag)
            suggestions are available for the video.
        editor_suggestions_availability: This value indicates whether video
            editing suggestions, which might improve video quality or the
            playback experience, are available for the video.
        thumbnails_availability: This value indicates whether thumbnail images
            have been generated for the video.
    """  # noqa: E501

    processing_status: str | None = None
    processing_progress: ProcessingProgress | None = None
    processing_failure_reason: str | None = None
    file_details_availability: str | None = None
    processing_issues_availability: str | None = None
    tag_suggestions_availability: str | None = None
    editor_suggestions_availability: str | None = None
    thumbnails_availability: str | None = None


# TODO: Validate
class TagSuggestion(APIModel):
    """One of the keyword tags that could be added to the video's metadata.

    Attributes:
        tag: The keyword tag suggested for the video.
        category_restricts: A set of video categories for which the tag is
            relevant.
    """

    tag: str | None = None
    category_restricts: list[str] | None = None


# TODO: Validate
class Suggestions(APIModel):
    """The `suggestions` object encapsulates suggestions that identify opportunities to improve the video quality or the metadata for the uploaded video.

    The part that carries it is refused to anyone but the video's own owner, so
    it is never asked for and never arrives.

    Attributes:
        processing_errors: A list of errors that will prevent YouTube from
            successfully processing the uploaded video.
        processing_warnings: A list of reasons why YouTube may have difficulty
            transcoding the uploaded video or that might result in an erroneous
            transcoding.
        processing_hints: A list of suggestions that may improve YouTube's
            ability to process the video.
        tag_suggestions: A list of keyword tags that could be added to the
            video's metadata to increase the likelihood that users will locate
            your video when searching or browsing on YouTube.
        editor_suggestions: A list of video editing operations that might
            improve the video quality or playback experience of the uploaded
            video.
    """  # noqa: E501

    processing_errors: list[str] | None = None
    processing_warnings: list[str] | None = None
    processing_hints: list[str] | None = None
    tag_suggestions: list[TagSuggestion] | None = None
    editor_suggestions: list[str] | None = None


# TODO: Validate
class LiveStreamingDetails(APIModel):
    """The `liveStreamingDetails` object contains metadata about a live video broadcast.

    The object will only be present in a `video` resource if the video is an
    upcoming, live, or completed live broadcast.

    Attributes:
        actual_start_time: The time that the broadcast actually started. The
            value is specified in ISO 8601 format. This value will not be
            available until the broadcast begins.
        actual_end_time: The time that the broadcast actually ended. The value
            is specified in ISO 8601 format. This value will not be available
            until the broadcast is over.
        scheduled_start_time: The time that the broadcast is scheduled to begin.
            The value is specified in ISO 8601 format.
        scheduled_end_time: The time that the broadcast is scheduled to end. The
            value is specified in ISO 8601 format. If the value is empty or the
            property is not present, then the broadcast is scheduled to continue
            indefinitely.
        concurrent_viewers: The number of viewers currently watching the
            broadcast. The property and its value will be present if the
            broadcast has current viewers and the broadcast owner has not hidden
            the viewcount for the video.
        active_live_chat_id: The ID of the currently active live chat attached
            to this video. This field is filled only if the video is a currently
            live broadcast that has live chat.
    """

    actual_start_time: str | None = None
    actual_end_time: str | None = None
    scheduled_start_time: str | None = None
    scheduled_end_time: str | None = None
    concurrent_viewers: int | None = None
    active_live_chat_id: str | None = None


# TODO: Validate
class BrandPartner(APIModel):
    """The `brandPartner` object contains details about the brand partner linked to the video for Creator Initiated Brand Partner Access (CI BPA).

    Attributes:
        channel_id: The external channel ID of the brand partner. This field
            must begin with "UC". Either `channelId` or `channelHandle` must be
            set when establishing access, but only `channelId` is returned in
            the response.
        channel_handle: The channel handle of the brand partner. This field must
            begin with "@". Either `channelId` or `channelHandle` must be set
            when establishing access, but only `channelId` is returned in the
            response.
    """  # noqa: E501

    channel_id: str | None = None
    channel_handle: str | None = None


# TODO: Validate
class Video(APIModel):
    """One video.

    Attributes:
        kind: Identifies the API resource's type. The value will be
            `youtube#video`.
        etag: The Etag of this resource.
        id: The ID that YouTube uses to uniquely identify the video.
        snippet: The `snippet` object contains basic details about the video,
            such as its title, description, and category.
        content_details: The `contentDetails` object contains information about
            the video content, including the length of the video and an
            indication of whether captions are available for the video.
        status: The `status` object contains information about the video's
            uploading, processing, and privacy statuses.
        statistics: The `statistics` object contains statistics about the video.
        paid_product_placement_details: The `paidProductPlacementDetails` object
            contains information about paid product placement in the video.
        player: The `player` object contains information that you would use to
            play the video in an embedded player.
        topic_details: The `topicDetails` object encapsulates information about
            topics associated with the video.
        recording_details: The `recordingDetails` object encapsulates
            information about the location, date and address where the video was
            recorded.
        file_details: The `fileDetails` object encapsulates information about
            the video file that was uploaded to YouTube.
        processing_details: The `processingDetails` object encapsulates
            information about YouTube's progress in processing the uploaded
            video file.
        suggestions: The `suggestions` object encapsulates suggestions that
            identify opportunities to improve the video quality or the metadata
            for the uploaded video.
        live_streaming_details: The `liveStreamingDetails` object contains
            metadata about a live video broadcast.
        brand_partner: The `brandPartner` object contains details about the
            brand partner linked to the video for Creator Initiated Brand
            Partner Access (CI BPA).
        localizations: The `localizations` object contains translations of the
            video's metadata.
    """

    kind: str
    etag: str
    id: str
    snippet: VideoSnippet
    content_details: VideoContentDetails
    status: VideoStatus
    # A video with nothing to count at all carries no statistics object.
    statistics: VideoStatistics | None = None
    paid_product_placement_details: PaidProductPlacementDetails
    player: VideoPlayer
    # A video YouTube has worked out no topics for carries none.
    topic_details: VideoTopicDetails | None = None
    recording_details: RecordingDetails
    # These four only arrive for the video's own owner, and the parts carrying
    # the first three are never asked for.
    file_details: FileDetails | None = None
    processing_details: ProcessingDetails | None = None
    suggestions: Suggestions | None = None
    brand_partner: BrandPartner | None = None
    # Only a broadcast carries the first, only a translated video the second.
    live_streaming_details: LiveStreamingDetails | None = None
    localizations: Localizations | None = None


# TODO: Validate
class VideoListResponse(BaseResponseModel, APIModel):
    """Every video one request asked about.

    Attributes:
        kind: Identifies the API resource's type. The value will be
            `youtube#videoListResponse`.
        etag: The Etag of this resource.
        next_page_token: The token that can be used as the value of the
            `pageToken` parameter to retrieve the next page in the result set.
        prev_page_token: The token that can be used as the value of the
            `pageToken` parameter to retrieve the previous page in the result
            set.
        page_info: The `pageInfo` object encapsulates paging information for the
            result set.
        items: A list of videos that match the request criteria.
        raw: The response as it was downloaded.
    """

    kind: str
    etag: str
    next_page_token: str | None = None
    prev_page_token: str | None = None
    page_info: PageInfo
    # A response that found nothing has no `items` at all.
    items: list[Video] = Field(default_factory=list)
    raw: SkipValidation[dict[str, Any]] = Field(repr=False)

    # TODO: Validate
    @classmethod
    @override
    def from_response(cls, data: dict[str, Any]) -> Self:
        return cls.model_validate({**data, "raw": data})
