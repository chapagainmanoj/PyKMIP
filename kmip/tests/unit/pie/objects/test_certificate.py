# Copyright (c) 2015 The Johns Hopkins University/Applied Physics Laboratory
# All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.

import testtools

from kmip.core import enums
from kmip.pie import objects


class DummyCertificate(objects.Certificate):
    """
    A dummy Certificate subclass for testing purposes.
    """

    def __init__(self, certificate_type, value, masks=None, name="Certificate"):
        """
        Create a DummyCertificate.
        """
        super(DummyCertificate, self).__init__(certificate_type, value, masks, name)

    def validate(self):
        super(DummyCertificate, self).validate()

    def __repr__(self):
        return ""

    def __str__(self):
        return ""

    def __eq__(self, other):
        return True

    def __ne__(self, other):
        return False


class TestCertificate(testtools.TestCase):
    """
    Test suite for Certificate.

    Since Certificate is an ABC abstract class, all tests are run against a
    dummy subclass defined above, DummyCertificate.
    """

    def setUp(self):
        super(TestCertificate, self).setUp()

        # Certificate values taken from Sections 13.2 and 13.4 of the KMIP 1.1
        # testing documentation.
        self.bytes_a = (
            b"\x30\x82\x03\x12\x30\x82\x01\xFA\xA0\x03\x02\x01\x02\x02\x01\x01"
            b"\x30\x0D\x06\x09\x2A\x86\x48\x86\xF7\x0D\x01\x01\x05\x05\x00\x30"
            b"\x3B\x31\x0B\x30\x09\x06\x03\x55\x04\x06\x13\x02\x55\x53\x31\x0D"
            b"\x30\x0B\x06\x03\x55\x04\x0A\x13\x04\x54\x45\x53\x54\x31\x0E\x30"
            b"\x0C\x06\x03\x55\x04\x0B\x13\x05\x4F\x41\x53\x49\x53\x31\x0D\x30"
            b"\x0B\x06\x03\x55\x04\x03\x13\x04\x4B\x4D\x49\x50\x30\x1E\x17\x0D"
            b"\x31\x30\x31\x31\x30\x31\x32\x33\x35\x39\x35\x39\x5A\x17\x0D\x32"
            b"\x30\x31\x31\x30\x31\x32\x33\x35\x39\x35\x39\x5A\x30\x3B\x31\x0B"
            b"\x30\x09\x06\x03\x55\x04\x06\x13\x02\x55\x53\x31\x0D\x30\x0B\x06"
            b"\x03\x55\x04\x0A\x13\x04\x54\x45\x53\x54\x31\x0E\x30\x0C\x06\x03"
            b"\x55\x04\x0B\x13\x05\x4F\x41\x53\x49\x53\x31\x0D\x30\x0B\x06\x03"
            b"\x55\x04\x03\x13\x04\x4B\x4D\x49\x50\x30\x82\x01\x22\x30\x0D\x06"
            b"\x09\x2A\x86\x48\x86\xF7\x0D\x01\x01\x01\x05\x00\x03\x82\x01\x0F"
            b"\x00\x30\x82\x01\x0A\x02\x82\x01\x01\x00\xAB\x7F\x16\x1C\x00\x42"
            b"\x49\x6C\xCD\x6C\x6D\x4D\xAD\xB9\x19\x97\x34\x35\x35\x77\x76\x00"
            b"\x3A\xCF\x54\xB7\xAF\x1E\x44\x0A\xFB\x80\xB6\x4A\x87\x55\xF8\x00"
            b"\x2C\xFE\xBA\x6B\x18\x45\x40\xA2\xD6\x60\x86\xD7\x46\x48\x34\x6D"
            b"\x75\xB8\xD7\x18\x12\xB2\x05\x38\x7C\x0F\x65\x83\xBC\x4D\x7D\xC7"
            b"\xEC\x11\x4F\x3B\x17\x6B\x79\x57\xC4\x22\xE7\xD0\x3F\xC6\x26\x7F"
            b"\xA2\xA6\xF8\x9B\x9B\xEE\x9E\x60\xA1\xD7\xC2\xD8\x33\xE5\xA5\xF4"
            b"\xBB\x0B\x14\x34\xF4\xE7\x95\xA4\x11\x00\xF8\xAA\x21\x49\x00\xDF"
            b"\x8B\x65\x08\x9F\x98\x13\x5B\x1C\x67\xB7\x01\x67\x5A\xBD\xBC\x7D"
            b"\x57\x21\xAA\xC9\xD1\x4A\x7F\x08\x1F\xCE\xC8\x0B\x64\xE8\xA0\xEC"
            b"\xC8\x29\x53\x53\xC7\x95\x32\x8A\xBF\x70\xE1\xB4\x2E\x7B\xB8\xB7"
            b"\xF4\xE8\xAC\x8C\x81\x0C\xDB\x66\xE3\xD2\x11\x26\xEB\xA8\xDA\x7D"
            b"\x0C\xA3\x41\x42\xCB\x76\xF9\x1F\x01\x3D\xA8\x09\xE9\xC1\xB7\xAE"
            b"\x64\xC5\x41\x30\xFB\xC2\x1D\x80\xE9\xC2\xCB\x06\xC5\xC8\xD7\xCC"
            b"\xE8\x94\x6A\x9A\xC9\x9B\x1C\x28\x15\xC3\x61\x2A\x29\xA8\x2D\x73"
            b"\xA1\xF9\x93\x74\xFE\x30\xE5\x49\x51\x66\x2A\x6E\xDA\x29\xC6\xFC"
            b"\x41\x13\x35\xD5\xDC\x74\x26\xB0\xF6\x05\x02\x03\x01\x00\x01\xA3"
            b"\x21\x30\x1F\x30\x1D\x06\x03\x55\x1D\x0E\x04\x16\x04\x14\x04\xE5"
            b"\x7B\xD2\xC4\x31\xB2\xE8\x16\xE1\x80\xA1\x98\x23\xFA\xC8\x58\x27"
            b"\x3F\x6B\x30\x0D\x06\x09\x2A\x86\x48\x86\xF7\x0D\x01\x01\x05\x05"
            b"\x00\x03\x82\x01\x01\x00\xA8\x76\xAD\xBC\x6C\x8E\x0F\xF0\x17\x21"
            b"\x6E\x19\x5F\xEA\x76\xBF\xF6\x1A\x56\x7C\x9A\x13\xDC\x50\xD1\x3F"
            b"\xEC\x12\xA4\x27\x3C\x44\x15\x47\xCF\xAB\xCB\x5D\x61\xD9\x91\xE9"
            b"\x66\x31\x9D\xF7\x2C\x0D\x41\xBA\x82\x6A\x45\x11\x2F\xF2\x60\x89"
            b"\xA2\x34\x4F\x4D\x71\xCF\x7C\x92\x1B\x4B\xDF\xAE\xF1\x60\x0D\x1B"
            b"\xAA\xA1\x53\x36\x05\x7E\x01\x4B\x8B\x49\x6D\x4F\xAE\x9E\x8A\x6C"
            b"\x1D\xA9\xAE\xB6\xCB\xC9\x60\xCB\xF2\xFA\xE7\x7F\x58\x7E\xC4\xBB"
            b"\x28\x20\x45\x33\x88\x45\xB8\x8D\xD9\xAE\xEA\x53\xE4\x82\xA3\x6E"
            b"\x73\x4E\x4F\x5F\x03\xB9\xD0\xDF\xC4\xCA\xFC\x6B\xB3\x4E\xA9\x05"
            b"\x3E\x52\xBD\x60\x9E\xE0\x1E\x86\xD9\xB0\x9F\xB5\x11\x20\xC1\x98"
            b"\x34\xA9\x97\xB0\x9C\xE0\x8D\x79\xE8\x13\x11\x76\x2F\x97\x4B\xB1"
            b"\xC8\xC0\x91\x86\xC4\xD7\x89\x33\xE0\xDB\x38\xE9\x05\x08\x48\x77"
            b"\xE1\x47\xC7\x8A\xF5\x2F\xAE\x07\x19\x2F\xF1\x66\xD1\x9F\xA9\x4A"
            b"\x11\xCC\x11\xB2\x7E\xD0\x50\xF7\xA2\x7F\xAE\x13\xB2\x05\xA5\x74"
            b"\xC4\xEE\x00\xAA\x8B\xD6\x5D\x0D\x70\x57\xC9\x85\xC8\x39\xEF\x33"
            b"\x6A\x44\x1E\xD5\x3A\x53\xC6\xB6\xB6\x96\xF1\xBD\xEB\x5F\x7E\xA8"
            b"\x11\xEB\xB2\x5A\x7F\x86"
        )
        self.bytes_b = (
            b"\x30\x82\x03\x26\x30\x82\x02\x0E\xA0\x03\x02\x01\x02\x02\x14\x6D"
            b"\x0C\x0F\x4F\x2F\xEF\xEA\xF0\xD2\x3D\x3B\xA2\x5D\x2F\x70\xF5\xEA"
            b"\x4A\xEF\xCB\x30\x0D\x06\x09\x2A\x86\x48\x86\xF7\x0D\x01\x01\x05"
            b"\x05\x00\x30\x3B\x31\x0B\x30\x09\x06\x03\x55\x04\x06\x13\x02\x55"
            b"\x53\x31\x0D\x30\x0B\x06\x03\x55\x04\x0A\x13\x04\x54\x45\x53\x54"
            b"\x31\x0E\x30\x0C\x06\x03\x55\x04\x0B\x13\x05\x4F\x41\x53\x49\x53"
            b"\x31\x0D\x30\x0B\x06\x03\x55\x04\x03\x13\x04\x4B\x4D\x49\x50\x30"
            b"\x1E\x17\x0D\x31\x32\x30\x34\x32\x37\x31\x30\x31\x34\x34\x31\x5A"
            b"\x17\x0D\x31\x33\x30\x34\x32\x37\x31\x30\x31\x34\x34\x31\x5A\x30"
            b"\x3C\x31\x0B\x30\x09\x06\x03\x55\x04\x06\x13\x02\x55\x53\x31\x0D"
            b"\x30\x0B\x06\x03\x55\x04\x0A\x13\x04\x41\x43\x4D\x45\x31\x0D\x30"
            b"\x0B\x06\x03\x55\x04\x0B\x13\x04\x4B\x4D\x49\x50\x31\x0F\x30\x0D"
            b"\x06\x03\x55\x04\x03\x13\x06\x43\x6C\x69\x65\x6E\x74\x30\x82\x01"
            b"\x22\x30\x0D\x06\x09\x2A\x86\x48\x86\xF7\x0D\x01\x01\x01\x05\x00"
            b"\x03\x82\x01\x0F\x00\x30\x82\x01\x0A\x02\x82\x01\x01\x00\xAB\x7F"
            b"\x16\x1C\x00\x42\x49\x6C\xCD\x6C\x6D\x4D\xAD\xB9\x19\x97\x34\x35"
            b"\x35\x77\x76\x00\x3A\xCF\x54\xB7\xAF\x1E\x44\x0A\xFB\x80\xB6\x4A"
            b"\x87\x55\xF8\x00\x2C\xFE\xBA\x6B\x18\x45\x40\xA2\xD6\x60\x86\xD7"
            b"\x46\x48\x34\x6D\x75\xB8\xD7\x18\x12\xB2\x05\x38\x7C\x0F\x65\x83"
            b"\xBC\x4D\x7D\xC7\xEC\x11\x4F\x3B\x17\x6B\x79\x57\xC4\x22\xE7\xD0"
            b"\x3F\xC6\x26\x7F\xA2\xA6\xF8\x9B\x9B\xEE\x9E\x60\xA1\xD7\xC2\xD8"
            b"\x33\xE5\xA5\xF4\xBB\x0B\x14\x34\xF4\xE7\x95\xA4\x11\x00\xF8\xAA"
            b"\x21\x49\x00\xDF\x8B\x65\x08\x9F\x98\x13\x5B\x1C\x67\xB7\x01\x67"
            b"\x5A\xBD\xBC\x7D\x57\x21\xAA\xC9\xD1\x4A\x7F\x08\x1F\xCE\xC8\x0B"
            b"\x64\xE8\xA0\xEC\xC8\x29\x53\x53\xC7\x95\x32\x8A\xBF\x70\xE1\xB4"
            b"\x2E\x7B\xB8\xB7\xF4\xE8\xAC\x8C\x81\x0C\xDB\x66\xE3\xD2\x11\x26"
            b"\xEB\xA8\xDA\x7D\x0C\xA3\x41\x42\xCB\x76\xF9\x1F\x01\x3D\xA8\x09"
            b"\xE9\xC1\xB7\xAE\x64\xC5\x41\x30\xFB\xC2\x1D\x80\xE9\xC2\xCB\x06"
            b"\xC5\xC8\xD7\xCC\xE8\x94\x6A\x9A\xC9\x9B\x1C\x28\x15\xC3\x61\x2A"
            b"\x29\xA8\x2D\x73\xA1\xF9\x93\x74\xFE\x30\xE5\x49\x51\x66\x2A\x6E"
            b"\xDA\x29\xC6\xFC\x41\x13\x35\xD5\xDC\x74\x26\xB0\xF6\x05\x02\x03"
            b"\x01\x00\x01\xA3\x21\x30\x1F\x30\x1D\x06\x03\x55\x1D\x0E\x04\x16"
            b"\x04\x14\x04\xE5\x7B\xD2\xC4\x31\xB2\xE8\x16\xE1\x80\xA1\x98\x23"
            b"\xFA\xC8\x58\x27\x3F\x6B\x30\x0D\x06\x09\x2A\x86\x48\x86\xF7\x0D"
            b"\x01\x01\x05\x05\x00\x03\x82\x01\x01\x00\x51\xE9\xCC\x2F\x09\x00"
            b"\xCD\x9C\x71\xE7\xDD\x3E\x40\x79\x33\xCA\xCC\xA2\x99\xE6\xC4\x1F"
            b"\xA0\x25\x16\x38\x6E\x92\x8F\x50\x6B\x04\x06\x2C\xCE\x90\x44\x4E"
            b"\xDE\xC9\x33\xCA\xBA\x74\xB9\x90\xAB\x08\x47\xC7\xB7\x32\x78\xD3"
            b"\x88\xA3\x49\xF9\x9F\x29\x6B\xF4\x58\xEC\x2C\x2C\x16\x3E\x8D\x87"
            b"\xBB\xEE\x47\xD2\x33\xB9\x14\x96\x61\xDD\x9A\x4C\x0A\xE5\x59\x25"
            b"\x2A\x5D\xE1\xDF\xEB\x69\xCF\xB7\x71\x38\xCB\xE0\xBB\x45\xB9\x11"
            b"\xFC\x0E\xF6\x75\xC3\x7B\x74\x92\x75\x54\x58\x36\xE3\x3C\xF7\x38"
            b"\x78\x23\x97\xAF\x4B\xC3\x70\x7A\xC1\x4A\xBA\x57\x24\xE0\x83\xBD"
            b"\xB0\xD2\x8F\xD2\x74\x7C\xDD\x8B\xCA\x74\xCE\x92\x56\x92\xF4\xD0"
            b"\x6C\x0D\x2B\x74\xD8\xD2\xB5\x40\xB7\xA1\x08\x31\x89\xE5\xE0\xF4"
            b"\x9F\x0B\x74\x06\x54\xD7\xD9\xF3\xFA\xA9\xB4\xC0\xF9\x05\x6F\xE4"
            b"\xF5\x2E\x4B\xEE\x81\x2F\xE4\x86\x19\x4C\xCD\x47\x8D\x65\x95\x7B"
            b"\xA6\x3F\xBC\xB0\xC3\x1F\x87\x02\x83\xAB\x4E\x84\x9C\x20\x99\x3D"
            b"\x6B\xEC\xB0\xF2\x70\x55\xB1\x03\xAF\x3B\x66\x75\xD1\x23\xCD\x3B"
            b"\x71\x79\xA4\x6C\x77\xC7\x3A\xE0\x0F\xFD\xEF\xA9\xB1\x25\xDA\x07"
            b"\x1E\xAD\x10\xD8\x5E\xAD\x0D\x0D\x44\x1F"
        )

    def tearDown(self):
        super(TestCertificate, self).tearDown()

    def test_init_certificate(self):
        """
        Test that direct instantiation of a Certificate fails.
        """
        args = (enums.CertificateType.X_509, self.bytes_a)
        self.assertRaises(TypeError, objects.Certificate, *args)

    def test_init(self):
        """
        Test that a complete subclass of Certificate can be instantiated.
        """
        certificate = DummyCertificate(enums.CertificateType.X_509, self.bytes_a)

        self.assertEqual(certificate.certificate_type, enums.CertificateType.X_509)
        self.assertEqual(certificate.value, self.bytes_a)
        self.assertEqual(certificate.cryptographic_usage_masks, list())
        self.assertEqual(certificate.names, ["Certificate"])

    def test_init_with_args(self):
        """
        Test that a complete subclass of Certificate can be instantiated with
        all arguments.
        """
        cert = DummyCertificate(
            enums.CertificateType.X_509,
            self.bytes_a,
            masks=[
                enums.CryptographicUsageMask.ENCRYPT,
                enums.CryptographicUsageMask.VERIFY,
            ],
            name="Test Certificate",
        )

        self.assertEqual(cert.certificate_type, enums.CertificateType.X_509)
        self.assertEqual(cert.value, self.bytes_a)
        self.assertEqual(
            cert.cryptographic_usage_masks,
            [enums.CryptographicUsageMask.ENCRYPT, enums.CryptographicUsageMask.VERIFY],
        )
        self.assertEqual(cert.names, ["Test Certificate"])

    def test_get_object_type(self):
        """
        Test that the object type can be retrieved from a complete subclass
        of Certificate.
        """
        expected = enums.ObjectType.CERTIFICATE
        cert = DummyCertificate(enums.CertificateType.X_509, self.bytes_a)
        observed = cert.object_type
        self.assertEqual(expected, observed)

    def test_validate_on_invalid_certificate_type(self):
        """
        Test that a TypeError is raised when an invalid certificate type is
        used to construct a complete subclass of Certificate.
        """
        args = ("invalid", self.bytes_a)
        self.assertRaises(TypeError, DummyCertificate, *args)

    def test_validate_on_invalid_value(self):
        """
        Test that a TypeError is raised when an invalid length value is used
        to construct a complete subclass of Certificate.
        """
        args = (enums.CertificateType.X_509, 0)
        self.assertRaises(TypeError, DummyCertificate, *args)

    def test_validate_on_invalid_masks(self):
        """
        Test that a TypeError is raised when an invalid masks value is used to
        construct a complete subclass of Certificate.
        """
        args = (enums.CertificateType.X_509, self.bytes_a)
        kwargs = {"masks": "invalid"}
        self.assertRaises(TypeError, DummyCertificate, *args, **kwargs)

    def test_validate_on_invalid_mask(self):
        """
        Test that a TypeError is raised when an invalid mask value is used to
        construct a complete subclass of Certificate.
        """
        args = (enums.CertificateType.X_509, self.bytes_a)
        kwargs = {"masks": ["invalid"]}
        self.assertRaises(TypeError, DummyCertificate, *args, **kwargs)

    def test_validate_on_invalid_name(self):
        """
        Test that a TypeError is raised when an invalid name value is used to
        construct a complete subclass of Certificate.
        """
        args = (enums.CertificateType.X_509, self.bytes_a)
        kwargs = {"name": 0}
        self.assertRaises(TypeError, DummyCertificate, *args, **kwargs)

    def test_repr(self):
        """
        Test that repr can be applied to a complete subclass of Certificate.
        """
        dummy = DummyCertificate(enums.CertificateType.X_509, self.bytes_a)
        repr(dummy)

    def test_str(self):
        """
        Test that str can be applied to a complete subclass of Certificate.
        """
        dummy = DummyCertificate(enums.CertificateType.X_509, self.bytes_a)
        str(dummy)

    def test_eq(self):
        """
        Test that equality can be applied to a complete subclass of
        Certificate.
        """
        dummy = DummyCertificate(enums.CertificateType.X_509, self.bytes_a)
        self.assertTrue(dummy == dummy)

    def test_ne(self):
        """
        Test that inequality can be applied to a complete subclass of
        Certificate.
        """
        dummy = DummyCertificate(enums.CertificateType.X_509, self.bytes_a)
        self.assertFalse(dummy != dummy)
