import json

from django.core.urlresolvers import reverse

from rest_framework.test import APITestCase
from rest_framework.test import APIRequestFactory
from rest_framework.test import APIClient, RequestsClient
from rest_framework.test import force_authenticate

from membership.models import User, Account, Member, AccountData, Plan
from galleries.models import Gallery, Group
from galleries.api.views import DashboardAPIView, GroupViewSet


class DashboardApiViewTestCase(APITestCase):

    url = reverse("galleries-api:dashboard-data")

    def setUp(self):

        self.user = User.objects.create_user(
            email="rishabh@admin.com",
            username="rishabh@admin.com",
            password="rish@bhrusi@1234",
        )

        self.account = Account(
            account='TG',
            subdomain='rishabh',
            owner=self.user,
            created_by=self.user,
            modified_by=self.user,
        )

        self.user.save()
        self.account.save()

        self.member = Member(
            user=self.user,
            account=self.account,
            account_id=self.account.id,
            role=1000,
            created_by=self.user,
            modified_by=self.user,
        )

        self.plan = Plan(
            plan_code='free',
            name='Free',
            tenure=30,
            max_gallaries=12,
            max_resource_per_gallery=12,
            max_users=12,
            restoration_period=30,
            published=True,
            sso=False,
            developer_api=True,
        )

        self.member.save()
        self.plan.save()

        self.account_data = AccountData(
            account=self.account,
            storage_size=30,
        )

        self.group = Group(
            name='Cartoon',
            slug='galleries-url',
            account=self.account,
            created_by=self.user,
            modified_by=self.user,
        )

        self.group1 = Group(
            name='Cartoon_newtork',
            slug='galleries-url',
            account=self.account,
            created_by=self.user,
            modified_by=self.user,
        )

        self.group.save()
        self.group1.save()

        self.gallery = Gallery(
            name="Dester",
            slug="Dexter-lab",
            group=self.group,
            group_id=self.group.id,
            account=self.account,
            color='blue',
            created_by=self.user,
            modified_by=self.user,
        )

        self.gallery1 = Gallery(
            name="Dexter",
            slug="Dexter-lab",
            group=self.group1,
            group_id=self.group1.id,
            account=self.account,
            color='blue',
            created_by=self.user,
            modified_by=self.user,
        )

        self.account_data.save()
        self.gallery.save()
        self.gallery1.save()

        self.subdomain = 'rishabh'
        self.factory = APIRequestFactory()
        self.client = APIClient()

    def test_fetch_dashboard(self):

        view = DashboardAPIView.as_view()

        request = self.factory.get(self.url)
        request.subdomain = self.subdomain
        force_authenticate(request, user=self.user)
        response = view(request)

        self.assertEqual(200, response.status_code)
        # self.assertEqual(8, len(response.data))
        self.assertTrue(2, len(response.data['galleries']))

    def test_fetch_data_using_client(self):

        self.client.force_authenticate(user=self.user)
        response = self.client.get(self.url, HTTP_HOST='rishabh.test.com')

        self.assertEqual(200, response.status_code)
        self.assertEqual(8, len(response.data))


# class DeletedGalleryListAPIViewTestCase(APITestCase):

#     url = reverse("galleries-api:gallery-deleted-list")

#     def setUp(self):

#         self.user = User.objects.create_user(
#                         email="rishabh@admin.com",
#                         username="rishabh@admin.com",
#                         password="rish@bhrusi@1234",
#         )

#         self.account = Account(
#             account='TG',
#             subdomain='rishabh',
#             owner=self.user,
#             created_by=self.user,
#             modified_by=self.user,
#         )

#         self.user.save()
#         self.account.save()

#         self.member = Member(
#             user=self.user,
#             account=self.account,
#             account_id=self.account.id,
#             role=1000,
#             created_by=self.user,
#             modified_by=self.user,
#         )

#         self.plan = Plan(
#             plan_code='free',
#             name='Free',
#             tenure=30,
#             max_gallaries=12,
#             max_resource_per_gallery=12,
#             max_users=12,
#             restoration_period=30,
#             published=True,
#             sso=False,
#             developer_api=True,
#         )

#         self.member.save()
#         self.plan.save()

#         self.account_data = AccountData(
#             account=self.account,
#             storage_size=30,
#         )

#         self.group = Group(
#             name='Cartoon',
#             slug='galleries-url',
#             account=self.account,
#             created_by=self.user,
#             modified_by=self.user,
#         )

#         self.group1 = Group(
#             name='Cartoon_newtork',
#             slug='galleries-url',
#             account=self.account,
#             created_by=self.user,
#             modified_by=self.user,
#         )

#         self.group.save()
#         self.group1.save()

#         self.gallery = Gallery(
#             name="Dester",
#             slug="Dexter-lab",
#             group=self.group,
#             group_id=self.group.id,
#             account=self.account,
#             color='blue',
#             created_by=self.user,
#             modified_by=self.user,
#         )

#         self.gallery1 = Gallery(
#             name="Dexter",
#             slug="Dexter-lab",
#             group=self.group1,
#             group_id=self.group1.id,
#             account=self.account,
#             color='blue',
#             created_by=self.user,
#             modified_by=self.user,
#         )

#         self.account_data.save()
#         self.gallery.save()
#         self.gallery1.save()

#         self.subdomain = 'rishabh'
#         self.client = APIClient()

#     def test_delete_gallery_view(self):

#         self.client.force_authenticate(user=self.user)

#         response = self.client.get(self.url, HTTP_HOST='rishabh.test.com')

        # import pdb; pdb.set_trace()

class GroupViewSetTestCase(APITestCase):

    def setUp(self):

        self.user = User.objects.create_user(
            email="rishabh@admin.com",
            username="rishabh@admin.com",
            password="rish@bhrusi@1234",
        )

        self.account = Account(
            account='TG',
            subdomain='rishabh',
            owner=self.user,
            created_by=self.user,
            modified_by=self.user,
        )

        self.user.save()
        self.account.save()

        self.member = Member(
            user=self.user,
            account=self.account,
            account_id=self.account.id,
            role=1000,
            created_by=self.user,
            modified_by=self.user,
        )

        self.plan = Plan(
            plan_code='free',
            name='Free',
            tenure=30,
            max_gallaries=12,
            max_resource_per_gallery=12,
            max_users=12,
            restoration_period=30,
            published=True,
            sso=False,
            developer_api=True,
        )

        self.member.save()
        self.plan.save()

        # self.account_data = AccountData(
        #     account=self.account,
        #     storage_size=30,
        # )

        # self.group = Group(
        #     name='Cartoon',
        #     slug='galleries-url',
        #     account=self.account,
        #     created_by=self.user,
        #     modified_by=self.user,
        # )

        # self.group1 = Group(
        #     name='Cartoon_newtork',
        #     slug='galleries-url',
        #     account=self.account,
        #     created_by=self.user,
        #     modified_by=self.user,
        # )

        # self.group.save()
        # self.group1.save()

        # self.gallery = Gallery(
        #     name="Dester",
        #     slug="Dexter-lab",
        #     group=self.group,
        #     group_id=self.group.id,
        #     account=self.account,
        #     color='blue',
        #     created_by=self.user,
        #     modified_by=self.user,
        # )

        # self.gallery1 = Gallery(
        #     name="Dexter",
        #     slug="Dexter-lab",
        #     group=self.group1,
        #     group_id=self.group1.id,
        #     account=self.account,
        #     color='blue',
        #     created_by=self.user,
        #     modified_by=self.user,
        # )

        # self.account_data.save()
        # self.gallery.save()
        # self.gallery1.save()

        self.subdomain = 'rishabh'
        self.client = APIClient()
        self.factory = APIRequestFactory()

    def test_create_group(self):

        self.client.force_authenticate(user=self.user)

        group_data = {
            'name': 'Cartoon',
            'slug': 'galleries-url',
            'account': self.account,
            'created_by': self.user,
            'modified_by': self.user,
        }

        response = self.client.post(
            'api/v1/groups/', group_data, HTTP_HOST='rishabh.test.com')

        self.assertEqual(201, response.status_code)

    def test_create_galleries(self):
        self.group_data = {
            'name': 'Cartoon',
            'slug': 'galleries-url',
            'account': self.account,
            'created_by': self.user,
            'modified_by': self.user,
        }

        view = GroupViewSet.as_view(actions={'post': 'create'})

        request = self.factory.post('/api/v1/groups/', self.group_data)
        request.subdomain = self.subdomain
        force_authenticate(request, user=self.user)
        response = view(request)

        self.assertEqual(201, response.status_code)
