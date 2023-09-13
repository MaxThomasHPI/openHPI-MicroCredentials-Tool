class VerifyablePresentation:

    def __init__(self):
        self.xmlns = ""
        self.cred = ""
        self.ds = ""
        self.vp = ""
        self.xsi = ""
        self.id = ""
        self.xsi_scheme_location = ""

        self.vp_type = ""  # expects VPtype object
        self.vp_issuer = ""  # expects VPissuer object
        self.europass_credentials = ""  # expects EuropassCredentials object
        self.vp_proof = ""  # expects Signature object


class VPtype:

    def __init__(self):
        self.target_framework_url = ""
        self.uri = ""
        self.target_name = {}  # style: key is language code according to BCP 47, value is name
        self.target_framework_name = {}  # style: key is language code according to BCP 47, value is name


class VPissuer:

    def __init__(self):
        self.issuer_id = ""
        self.registration = ""
        self.pref_label = ""
        self.alt_label = ""
        self.has_location = []  # for Location objects


class EuropassCredentials:

    def __init__(self):
        self.type_target_framework_url = ""
        self.type_uri = ""
        self.type_target_name = ""
        self.type_target_framework_name = ""

        self.primary_language = ""
        self.available_languages = []

        self.cred_valid_from = ""
        self.cred_issued = ""
        self.cred_issuer_idref = ""

        self.title = {}  # style: key is language code according to BCP 47, value is title

        self.credential_subject_id = ""
        self.contact_point_mail_box = ""
        self.contact_point_full_name = ""
        self.contact_point_family_name = ""
        self.contact_point_given_name = ""

        self.activities = []  # contains Activity objects

        self.display_parameters = ""  # expects DisplayParameters object


class Activity:

    def __init__(self):
        self.activity_id = ""
        self.activity_title = {}  # style: key = language tag according to BCP 47, value = title
        self.activity_description = {}  # style: key = language tag according to BCP 47, value = title

        self.activity_started_at = ""
        self.activity_ended_at = ""
        self.activity_directed_by_id = ""

        self.activity_location_id = ""
        self.activity_location_name = {}  # style: key = language tag according to BCP 47, value = title

        self.activity_location_spatial_code_framework = ""
        self.activity_location_spatial_code_notation = ""
        self.activity_location_spatial_code_uri = ""

        self.activity_location_spatial_code_target_name = {}  # style: key = language tag according to BCP 47, value =
        # title
        self.activity_location_spatial_code_target_framework = {}  # style: key = language tag according to BCP 47,
        # value = title

        self.activity_specified_by = ""


class LearningActivitySpecification:

    def __init__(self):
        self.id = ""
        self.homepage_uri = ""

        self.type_target_framework_url = ""
        self.type_uri = ""
        self.type_target_name = {}  # style: key = language tag according to BCP 47, value = name
        self.type_target_framework_name = {}  # style: key = language tag according to BCP 47, value = title

        self.mode_target_framework_url = ""
        self.mode_uri = ""
        self.mode_target_name = {}  # style: key = language tag according to BCP 47, value = title
        self.mode_target_framework_name = {}  # style: key = language tag according to BCP 47, value = title


class Organization:

    def __init__(self):
        self.organization_id = ""
        self.organization_registration = ""

        self.organization_pref_label = {}  # style: key = language tag according to BCP 47, value = title
        self.organization_alt_label = {}  # style: key = language tag according to BCP 47, value = title
        self.organization_homepage_uri = ""

        self.hasLocation = []  # list of Location objects


class Location:

    def __init__(self):
        self.location_id = ""
        self.location_country_target_framework_url = ""
        self.location_country_target_notation = ""
        self.location_country_uri = ""
        self.location_country_target_name = {}  # style: key = language tag according to BCP 47, value = title
        self.location_country_target_framework_name = {}  # style: key = language tag according to BCP 47, value = title


class DisplayParameters:

    def __init__(self):
        self.content_type_target_framework_url = ""
        self.content_type_target_notation = ""
        self.content_type_uri = ""
        self.content_type_target_name = {}  # style: key = language tag according to BCP 47, value = content
        self.content_type_target_framework_name = {}  # style: key = language tag according to BCP 47, value = content

        self.content_encoding_target_framework_url = ""
        self.content_encoding_uri = ""
        self.content_encoding_target_name = {}
        self.content_encoding_target_framework_name = {}  # style: key = language tag according to BCP 47, value =
        # content

        self.content = ""

        self.html = ""  # link to html source code


class Signature:

    def __init__(self):
        self.signature_id = ""
        self.signed_info = ""

        self.signature_value_id = ""
        self.signature_value = ""

        self.key_info_x509_certificate = ""


class SignedInfo:

    def __init__(self):
        self.canonical_method_algorithm = ""
        self.signature_method_algorithm = ""

        self.reference = []  # expects Reference objects


class Reference:

    def __init__(self):
        self.reference_id = ""
        self.reference_uri = ""
        self.reference_type = ""

        self.transform_algorithm_1 = ""
        self.transform_dsig_filter2 = ""
        self.transform_dsig_filter = ""
        self.transform_content = ""
        self.transform_algorithm_2 = ""

        self.digest_method_algorithm = ""
        self.digest_value = ""


class SignatureObject:

    def __init__(self):
        self.xmlns_xades = ""
        self.qualifying_properties_target = ""

        self.signet_properties_id = ""
        self.signing_time = ""  # Date-Time datatype

        self.cert_digest_algorithm = ""
        self.cert_digest_value = ""
        self.cert_issuer_v2 = ""

        self.data_object_format_reference = ""
        self.xades_mime_type = ""

        self.all_data_object_time_stamp = ""  # expects SignatureTimeStamp object

        self.unsigned_properties = ""  # expects UnsignedProperties object


class UnsignedProperties:

    def __init__(self):
        self.unsigned_properties_time_stamp = ""  # expects SignatureTimeStamp object

        self.certification_values = []

        self.encapsulated_clr_values = []

        self.ocsp_values = []


class SignatureTimeStamp:

    def __init__(self):
        self.time_stamp_id = ""
        self.canonicalization_algorithm = ""
        self.encapsulated_time_stamp = ""
