#!/usr/bin/env python3

#
# Copyright (C) 2023 Nethesis S.r.l.
# SPDX-License-Identifier: GPL-3.0-or-later
#

from pathlib import Path

CUSTOM_CERTIFICATES_DIR = 'custom_certificates'
CUSTOM_TRAEFIK_CONFIG_DIR = 'configs'
CRT_SUFFIX = '.crt'
KEY_SUFFIX = '.key'


def info_custom_certificate(fqdn):
    """Get info for custom certificate

    :param fqdn: The FQDN to find in the certificates
    :type fqdn: str
    :return: dictionary containing custom certificate info
    :rtype: dict
    :raises FileNotFoundError: if no certificate is found for the given FQDN
    """
    custom_cert_path = Path(CUSTOM_CERTIFICATES_DIR)
    for item in custom_cert_path.iterdir():
        if item.is_file() and item.name == fqdn + CRT_SUFFIX:
            return {
                'fqdn': fqdn,
                'type': 'custom',
                'obtained': True
            }

    raise FileNotFoundError(f'Can\'t find custom certificate for {fqdn}.')


def list_custom_certificates():
    """Returns a list of custom certificates uploaded

    :return: list containing data for each custom_certificate found, see info_custom_certificate for more info
    :rtype: list
    """
    custom_certificates = []
    custom_cert_path = Path(CUSTOM_CERTIFICATES_DIR)
    for item in custom_cert_path.iterdir():
        if item.is_file() and item.suffix == CRT_SUFFIX:
            custom_certificates.append(info_custom_certificate(item.name.removesuffix(CRT_SUFFIX)))

    return custom_certificates


def delete_custom_certificate(fqdn):
    """Delete custom certificate from system and Traefik configuration

    :param fqdn: FQDN to delete from filesystem
    :type fqdn: str
    :raises FileNotFoundError: if certificate or key is missing
    """
    cert_file_path = Path(CUSTOM_CERTIFICATES_DIR + f'/{fqdn}{CRT_SUFFIX}')
    key_file_path = Path(CUSTOM_CERTIFICATES_DIR + f'/{fqdn}{KEY_SUFFIX}')
    cert_config_path = Path(CUSTOM_TRAEFIK_CONFIG_DIR + f'/certificate_{fqdn}.yml')
    # check the presence of both file before removing, ensures that both are deleted, avoiding system inconsistencies
    if cert_file_path.is_file() and key_file_path.is_file() and cert_config_path.is_file():
        cert_file_path.unlink()
        key_file_path.unlink()
        cert_config_path.unlink()
    else:
        raise FileNotFoundError(f'Invalid custom certificate state for {fqdn}.')
