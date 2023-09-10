class VPtype:

    def __init__(self):
        self.target_name = ""
        self.target_framework_name = ""


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



