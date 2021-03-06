###
# (C) Copyright [2019-2020] Hewlett Packard Enterprise Development LP
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
##

from simplivity.resources.resource import ResourceBase

URL = '/external_stores'
DATA_FIELD = 'external_stores'


class ExternalStores(ResourceBase):
    """Implements features available for SimpliVity External store resources."""

    def __init__(self, connection):
        super(ExternalStores, self).__init__(connection)

    def get_all(self, pagination=False, page_size=0, limit=500, offset=0,
                sort=None, order='descending', filters=None, fields=None,
                case_sensitive=True):
        """
        Get all external stores
        Args:
            pagination: True if need pagination
            page_size: Size of the page (Required when pagination is on)
            limit: A positive integer that represents the maximum number of results to return
            offset: A positive integer that directs the service to start returning
              the <offset value> instance, up to the limit.
            sort: The name of the field where the sort occurs
            order: The sort order preference. Valid values: ascending or descending.
            filters: Dictionary with filter values. Example: {'name': 'name'}
                name: The name of the external_stores to return.
                    Accepts: Single value, comma-separated list, pattern using one or more asterisk characters as a wildcard.
                omnistack_cluster_id: The name of the omnistack_cluster that is associated with the instances to return
                cluster_group_id:The unique identifiers (UIDs) of the cluster_groups associated with the external stores to return
                    Accepts: Single value, comma-separated list
                management_ip: The IP address of the external store
                    Accepts: Single value, comma-separated list, pattern using one or more asterisk characters as a wildcard
                type: The type of external store
                    Default: StoreOnceOnPrem

        Returns:
            list: list of resources
        """
        return self._client.get_all(URL,
                                    members_field=DATA_FIELD,
                                    pagination=pagination,
                                    page_size=page_size,
                                    limit=limit,
                                    offset=offset,
                                    sort=sort,
                                    order=order,
                                    filters=filters,
                                    fields=fields,
                                    case_sensitive=case_sensitive)

    def get_by_data(self, data):
        """Gets ExternalStore object from data.

        Args:
            data: ExternalStore data

        Returns:
            object: ExternalStore object.
        """

        return ExternalStore(self._connection, self._client, data)


class ExternalStore(object):
    """Implements features available for a single External store resources."""

    def __init__(self, connection, resource_client, data):
        self.data = data
        self._connection = connection
        self._client = resource_client
