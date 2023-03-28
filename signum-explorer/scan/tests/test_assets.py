from django.test import TestCase


class AssetListViewTests(TestCase):
    databases = {"default", "java_wallet"}

    def test_slash_redirect(self):
        response = self.client.get("/assets")
        self.assertEqual(response.status_code, 301)

    def test_ok(self):
        response = self.client.get("/assets/")
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "tokens found")
        self.assertContains(response, "Blockchain Explorer - Assets</title>")
        self.assertQuerysetEqual(response.context["assets"], [])


class AssetkDetailViewTests(TestCase):
    databases = {"default", "java_wallet"}

    def test_404(self):
        response = self.client.get("/asset/abc")
        self.assertEqual(response.status_code, 404)
