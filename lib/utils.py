import settings


def allowed_file(
    filename: str, allowed_extensions: list[str] = settings.ALLOWED_EXTENSIONS
) -> bool:
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in allowed_extensions


def check_bucket_password(
    given_password: str, bucket: str, buckets: dict[str, str] = settings.BUCKETS
) -> bool:
    return given_password == buckets[bucket]
