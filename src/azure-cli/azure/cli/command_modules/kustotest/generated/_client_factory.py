# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------


def cf_kustotest_cl(cli_ctx, *_):
    from azure.cli.core.commands.client_factory import get_mgmt_service_client
    from azure.mgmt.kusto import KustoManagementClient
    return get_mgmt_service_client(cli_ctx,
                                   KustoManagementClient)


def cf_cluster(cli_ctx, *_):
    return cf_kustotest_cl(cli_ctx).clusters


def cf_cluster_principal_assignment(cli_ctx, *_):
    return cf_kustotest_cl(cli_ctx).cluster_principal_assignments


def cf_database(cli_ctx, *_):
    return cf_kustotest_cl(cli_ctx).databases


def cf_database_principal_assignment(cli_ctx, *_):
    return cf_kustotest_cl(cli_ctx).database_principal_assignments


def cf_attached_database_configuration(cli_ctx, *_):
    return cf_kustotest_cl(cli_ctx).attached_database_configurations


def cf_data_connection(cli_ctx, *_):
    return cf_kustotest_cl(cli_ctx).data_connections
