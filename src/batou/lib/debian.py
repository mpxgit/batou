from batou.component import Component, platform
from batou.lib.cron import CronJob
import batou.lib.service
import batou.lib.supervisor


@platform('debian', batou.lib.service.Service)
class RebootCronjob(Component):

    def configure(self):
        self += CronJob(
            self.expand(
                '{{component.root.workdir}}/{{component.parent.executable}}'),
            timing='@reboot', logger=self.root.name)


# XXX can't use @platform since that's too late (see #12418)
class Supervisor(batou.lib.supervisor.Supervisor):

    pidfile = 'var/supervisord.pid'
