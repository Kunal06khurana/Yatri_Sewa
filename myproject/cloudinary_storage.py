"""
Custom Cloudinary storage backend for Django 5.x.
Uses the cloudinary SDK directly — no dependency on django-cloudinary-storage.
"""
import os
import cloudinary
import cloudinary.uploader
import cloudinary.api
from django.core.files.storage import Storage
from django.utils.deconstruct import deconstructible


@deconstructible
class CloudinaryMediaStorage(Storage):
    """
    A Django storage backend that saves uploaded files to Cloudinary.
    Works with Django 4.2+ STORAGES configuration.
    """

    def _save(self, name, content):
        # Normalize path separators — Cloudinary requires forward slashes
        name = name.replace("\\", "/")
        # Strip the extension so Cloudinary uses it as the public_id base
        public_id = os.path.splitext(name)[0]
        # Upload to Cloudinary
        response = cloudinary.uploader.upload(
            content,
            public_id=public_id,
            resource_type="auto",
        )
        # Store the full path including extension so url() can reconstruct it
        ext = os.path.splitext(name)[1]
        return response["public_id"] + ext

    def _open(self, name, mode="rb"):
        # We don't support reading files back — Cloudinary is write-only from Django's side
        raise NotImplementedError("CloudinaryMediaStorage does not support opening files.")

    def url(self, name):
        if not name:
            return ""
        # Remove extension for Cloudinary public_id lookup
        public_id = os.path.splitext(name)[0]
        return cloudinary.CloudinaryImage(public_id).build_url()

    def exists(self, name):
        try:
            public_id = os.path.splitext(name)[0]
            cloudinary.api.resource(public_id)
            return True
        except cloudinary.api.NotFound:
            return False
        except Exception:
            return False

    def delete(self, name):
        try:
            public_id = os.path.splitext(name)[0]
            cloudinary.uploader.destroy(public_id)
        except Exception:
            pass

    def get_available_name(self, name, max_length=None):
        return name  # Cloudinary handles duplicate names via overwrite=True
