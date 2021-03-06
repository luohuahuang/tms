PLATFORM_GENERIC = 0
PLATFORM_ANDROID = 1
PLATFORM_IOS = 2
PLATFORM_WEB = 3
PLATFORM_OTHERS = 4
PLATFORM_CHOICES = (
    (PLATFORM_GENERIC, 'Generic'),
    (PLATFORM_ANDROID, 'Android'),
    (PLATFORM_IOS, 'iOS'),
    (PLATFORM_WEB, 'Web'),
    (PLATFORM_OTHERS, 'Others'),
)
TEST_RUN_STATUS_CREATED = 0
TEST_RUN_STATUS_ACTIVE = 1
TEST_RUN_STATUS_BLOCKED = 2
TEST_RUN_STATUS_COMPLETED = 3
TEST_RUN_STATUS_DISCARDED = 4
TEST_RUN_STATUS_CHOICES = (
    (TEST_RUN_STATUS_CREATED, 'Created'),
    (TEST_RUN_STATUS_ACTIVE, 'Active'),
    (TEST_RUN_STATUS_BLOCKED, 'Blocked'),
    (TEST_RUN_STATUS_COMPLETED, 'Completed'),
    (TEST_RUN_STATUS_DISCARDED, 'Discarded'),
)
TEST_CASE_TYPE_FUNCTIONAL = 0
TEST_CASE_TYPE_ACCEPTANCE = 1
TEST_CASE_TYPE_ACCESSIBILITY = 2
TEST_CASE_TYPE_AUTOMATED = 3
TEST_CASE_TYPE_COMPATIBILITY = 4
TEST_CASE_TYPE_PERFORMANCE = 5
TEST_CASE_TYPE_REGRESSION = 6
TEST_CASE_TYPE_SECURITY = 7
TEST_CASE_TYPE_SANITY = 8
TEST_CASE_TYPE_USABILITY = 9
TEST_CASE_TYPE_LOCALIZATION = 10
TEST_CASE_TYPE_CHOICES = (
    (TEST_CASE_TYPE_FUNCTIONAL, 'Functional'),
    (TEST_CASE_TYPE_ACCEPTANCE, 'Acceptance'),
    (TEST_CASE_TYPE_ACCESSIBILITY, 'Accessibility'),
    (TEST_CASE_TYPE_AUTOMATED, 'Automated'),
    (TEST_CASE_TYPE_COMPATIBILITY, 'Compatibility'),
    (TEST_CASE_TYPE_PERFORMANCE, 'Performance'),
    (TEST_CASE_TYPE_REGRESSION, 'Regression'),
    (TEST_CASE_TYPE_SECURITY, 'Security'),
    (TEST_CASE_TYPE_SANITY, 'Sanity'),
    (TEST_CASE_TYPE_USABILITY, 'Usability'),
    (TEST_CASE_TYPE_LOCALIZATION, 'Localization'),

)
TEST_CASE_TIER_0 = 0
TEST_CASE_TIER_1 = 1
TEST_CASE_TIER_2 = 2
TEST_CASE_TIER_3 = 3
TEST_CASE_TIER_4 = 4
TEST_CASE_TIER_CHOICES = (
    (TEST_CASE_TIER_0, 'tier 0'),
    (TEST_CASE_TIER_1, 'tier 1'),
    (TEST_CASE_TIER_2, 'tier 2'),
    (TEST_CASE_TIER_3, 'tier 3'),
    (TEST_CASE_TIER_4, 'tier 4'),
)
RELEASE_STATUS_CREATED = 0
RELEASE_STATUS_ACTIVE = 1
RELEASE_STATUS_RELEASED = 2
RELEASE_STATUS_DISCARDED = 3
RELEASE_STATUS_CHOICES = (
    (RELEASE_STATUS_CREATED, 'Created'),
    (RELEASE_STATUS_ACTIVE, 'Active'),
    (RELEASE_STATUS_RELEASED, 'Released'),
    (RELEASE_STATUS_DISCARDED, 'Discarded'),
)
TEST_PLAN_STATUS_CREATED = 0
TEST_PLAN_STATUS_ACTIVE = 1
TEST_PLAN_STATUS_COMPLETED = 2
TEST_PLAN_STATUS_DISCARDED = 3
TEST_PLAN_STATUS_CHOICES = (
    (TEST_PLAN_STATUS_CREATED, 'Created'),
    (TEST_PLAN_STATUS_ACTIVE, 'Active'),
    (TEST_PLAN_STATUS_COMPLETED, 'Completed'),
    (TEST_PLAN_STATUS_DISCARDED, 'Discarded'),
)
TEST_RUN_CASE_STATUS_SUCCEED = 0
TEST_RUN_CASE_STATUS_FAILED = 1
TEST_RUN_CASE_STATUS_ERROR = 2
TEST_RUN_CASE_STATUS_SKIPPED = 3
TEST_RUN_CASE_STATUS_NOT_STARTED = 4
TEST_RUN_CASE_STATUS_CHOICES = (
    (TEST_RUN_CASE_STATUS_SUCCEED, 'Succeed'),
    (TEST_RUN_CASE_STATUS_FAILED, 'Failed'),
    (TEST_RUN_CASE_STATUS_ERROR, 'Error'),
    (TEST_RUN_CASE_STATUS_SKIPPED, 'Skipped'),
    (TEST_RUN_CASE_STATUS_NOT_STARTED, '-'),
)
DEVICE_PLATFORM_ANDROID = 0
DEVICE_PLATFORM_IOS = 1
DEVICE_PLATFORM_OTHERS = 2
DEVICE_PLATFORM = (
    (DEVICE_PLATFORM_ANDROID, 'Android'),
    (DEVICE_PLATFORM_IOS, 'iOS'),
    (DEVICE_PLATFORM_OTHERS, 'Others'),
)
DEVICE_STATUS_AVAILABLE = 0
DEVICE_STATUS_OCCUPIED = 1
DEVICE_STATUS_BROKEN = 2
DEVICE_STATUS_RETURNED = 3
DEVICE_STATUS_CHOICES = (
    (DEVICE_STATUS_AVAILABLE, 'Available'),
    (DEVICE_STATUS_OCCUPIED, 'Occupied'),
    (DEVICE_STATUS_BROKEN, 'Broken'),
    (DEVICE_STATUS_RETURNED, 'Returned'),
)