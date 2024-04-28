from pydantic import BaseModel

from .driving_license import DrivingLicenseProps
from .identity_card import IdentityCardProps

from typing import Type


class OwnerProps(BaseModel):
    """owner fields"""
    identity_card: IdentityCardProps
    driving_license: DrivingLicenseProps
