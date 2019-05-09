from subhub.api.webhooks.routes.abstractRoute import AbstractRoute


class FirefoxRoute(AbstractRoute):

    def route(self):
        self.report_route(self.payload);