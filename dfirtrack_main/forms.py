from django import forms
from django.utils.translation import gettext_lazy
from dfirtrack_main.models import Analysisstatus, Analystmemo, Case, Company, Contact, Division, Domain, Entry, Headline, Ip, Location, Os, Osimportname, Reason, Recommendation, Reportitem, Serviceprovider, System, Systemstatus, Systemtype, Systemuser, Tag, Task, Taskname, Taskpriority, Taskstatus

class AnalysisstatusForm(forms.ModelForm):
    class Meta:
        model = Analysisstatus
        # this HTML forms are shown
        fields = (
            'analysisstatus_name',
            'analysisstatus_note',
        )
        # non default form labeling
        labels = {
            'analysisstatus_name': gettext_lazy('Analysisstatus name (*)'),
        }
        # special form type or option
        widgets = {
            'analysisstatus_name': forms.TextInput(attrs={'autofocus': 'autofocus'}),
        }

class AnalystmemoForm(forms.ModelForm):
    class Meta:
        model = Analystmemo
        # this HTML forms are shown
        fields = (
            'system',
            'analystmemo_note',
        )
        # non default form labeling
        labels = {
            'system': gettext_lazy('System (*)'),
            'analystmemo_note': gettext_lazy('Analystmemo note (*)'),
        }

class CaseForm(forms.ModelForm):
    class Meta:
        model = Case
        # this HTML forms are shown
        fields = (
            'case_name',
            'case_is_incident',
        )
        # non default form labeling
        labels = {
            'case_name': gettext_lazy('Case name (*)'),
        }
        # special form type or option
        widgets = {
            'case_name': forms.TextInput(attrs={'autofocus': 'autofocus'}),
        }

class CompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        # this HTML forms are shown
        fields = (
            'company_name',
            'division',
            'company_note',
        )
        # non default form labeling
        labels = {
            'company_name': gettext_lazy('Company name (*)'),
        }
        # special form type or option
        widgets = {
            'company_name': forms.TextInput(attrs={'autofocus': 'autofocus'}),
        }

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        # this HTML forms are shown
        fields = (
            'contact_name',
            'contact_phone',
            'contact_email',
            'contact_note',
        )
        # non default form labeling
        labels = {
            'contact_name': gettext_lazy('Contact name (*)'),
            'contact_email': gettext_lazy('Contact email (*)'),
        }
        # special form type or option
        widgets = {
            'contact_name': forms.TextInput(attrs={'autofocus': 'autofocus'}),
        }

class DivisionForm(forms.ModelForm):
    class Meta:
        model = Division
        # this HTML forms are shown
        fields = (
            'division_name',
            'division_note',
        )
        # non default form labeling
        labels = {
            'division_name': gettext_lazy('Division name (*)'),
        }
        # special form type or option
        widgets = {
            'division_name': forms.TextInput(attrs={'autofocus': 'autofocus'}),
        }

class DomainForm(forms.ModelForm):
    class Meta:
        model = Domain
        # this HTML forms are shown
        fields = (
            'domain_name',
            'domain_note',
        )
        # non default form labeling
        labels = {
            'domain_name': gettext_lazy('Domain name (*)'),
        }
        # special form type or option
        widgets = {
            'domain_name': forms.TextInput(attrs={'autofocus': 'autofocus'}),
        }

class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        # this HTML forms are shown
        fields = (
            'entry_time',
            'system',
            'entry_sha1',
            'entry_date',
            'entry_utc',
            'entry_system',
            'entry_type',
            'entry_content',
            'entry_note',
            'case',
        )
        # non default form labeling
        labels = {
            'entry_time': gettext_lazy('Entry time (for sorting) (YYYY-MM-DD HH:MM:SS) (*)'),
            'system': gettext_lazy('System (*)'),
            'entry_date': gettext_lazy('Entry date (YYYY-MM-DD)'),
            'entry_utc': gettext_lazy('Entry time (for report) (HH:MM:SS)'),
            'entry_system': gettext_lazy('Entry system (for report)'),
        }
        # special form type or option
        widgets = {
            'entry_time': forms.DateTimeInput(attrs={'autofocus': 'autofocus'}),
            'entry_sha1': forms.TextInput(),
            'entry_date': forms.TextInput(),
            'entry_utc': forms.TextInput(),
            'entry_system': forms.TextInput(),
            'entry_type': forms.TextInput(),
            'entry_content': forms.Textarea(attrs={'rows': 3}),
            'entry_note': forms.Textarea(attrs={'rows': 10}),
        }

class EntryFileImport(forms.ModelForm):

    # file upload field (variable is used in request object)
    entryfile = forms.FileField()

    class Meta:
        model = Entry
        fields = (
            'system',
        )

class HeadlineForm(forms.ModelForm):
    class Meta:
        model = Headline
        # this HTML forms are shown
        fields = (
            'headline_name',
        )
        # non default form labeling
        labels = {
            'headline_name': gettext_lazy('Headline (*)'),
        }
        # special form type or option
        widgets = {
            'headline_name': forms.TextInput(attrs={'autofocus': 'autofocus'}),
        }

class IpForm(forms.ModelForm):
    class Meta:
        model = Ip
        # this HTML forms are shown
        fields = (
            'ip_ip',
        )
        # non default form labeling
        labels = {
            'ip_ip': gettext_lazy('IP (*)'),
        }
        # special form type or option
        widgets = {
            'ip_ip': forms.TextInput(attrs={'autofocus': 'autofocus'}),
        }

class LocationForm(forms.ModelForm):
    class Meta:
        model = Location
        # this HTML forms are shown
        fields = (
            'location_name',
            'location_note',
        )
        # non default form labeling
        labels = {
            'location_name': gettext_lazy('Location name (*)'),
        }
        # special form type or option
        widgets = {
            'location_name': forms.TextInput(attrs={'autofocus': 'autofocus'}),
        }

class OsForm(forms.ModelForm):
    class Meta:
        model = Os
        # this HTML forms are shown
        fields = (
            'os_name',
        )
        # non default form labeling
        labels = {
            'os_name': gettext_lazy('Os name (*)'),
        }
        # special form type or option
        widgets = {
            'os_name': forms.TextInput(attrs={'autofocus': 'autofocus'}),
        }

class OsimportnameForm(forms.ModelForm):
    class Meta:
        model = Osimportname
        # this HTML forms are shown
        fields = (
            'osimportname_name',
            'os',
            'osimportname_importer',
        )
        # non default form labeling
        labels = {
            'osimportname_name': gettext_lazy('Importname (*)'),
            'os': gettext_lazy('Operating system (*)'),
            'osimportname_importer': gettext_lazy('Importer (*)'),
        }
        # special form type or option
        widgets = {
            'osimportname_name': forms.TextInput(attrs={'autofocus': 'autofocus'}),
        }

class ReasonForm(forms.ModelForm):
    class Meta:
        model = Reason
        # this HTML forms are shown
        fields = (
            'reason_name',
            'reason_note',
        )
        # non default form labeling
        labels = {
            'reason_name': gettext_lazy('Reason name (*)'),
        }
        # special form type or option
        widgets = {
            'reason_name': forms.TextInput(attrs={'autofocus': 'autofocus'}),
        }

class RecommendationForm(forms.ModelForm):
    class Meta:
        model = Recommendation
        # this HTML forms are shown
        fields = (
            'recommendation_name',
            'recommendation_note',
        )
        # non default form labeling
        labels = {
            'recommendation_name': gettext_lazy('Recommendation name (*)'),
        }
        # special form type or option
        widgets = {
            'recommendation_name': forms.TextInput(attrs={'autofocus': 'autofocus'}),
        }

class ReportitemForm(forms.ModelForm):
    class Meta:
        model = Reportitem
        # this HTML forms are shown
        fields = (
            'system',
            'headline',
            'reportitem_subheadline',
            'reportitem_note',
        )
        # non default form labeling
        labels = {
            'system': gettext_lazy('System (*)'),
            'headline': gettext_lazy('Headline (*)'),
            'reportitem_subheadline': gettext_lazy('Subheadline'),
            'reportitem_note': gettext_lazy('Note (*)'),
        }

class ServiceproviderForm(forms.ModelForm):
    class Meta:
        model = Serviceprovider
        # this HTML forms are shown
        fields = (
            'serviceprovider_name',
            'serviceprovider_note',
        )
        # non default form labeling
        labels = {
            'serviceprovider_name': gettext_lazy('Serviceprovider name (*)'),
        }
        # special form type or option
        widgets = {
            'serviceprovider_name': forms.TextInput(attrs={'autofocus': 'autofocus'}),
        }

class SystemForm(forms.ModelForm):
    # large text area for line separated iplist
    iplist = forms.CharField(
        widget=forms.Textarea(
            attrs={
                'rows': 3,
                'placeholder': 'One ip address per line',
            },
        ),
        required = False,
    )

    class Meta:
        model = System
        # this HTML forms are shown
        fields = (
            'system_name',
            'systemstatus',
            'analysisstatus',
            'reason',
            'recommendation',
            'systemtype',
            'domain',
            'system_dnssuffix',
            'os',
            'osarch',
            'system_install_time',
            'system_lastbooted_time',
            'system_deprecated_time',
            'system_is_vm',
            'host_system',
            'company',
            'location',
            'serviceprovider',
            'contact',
            'tag',
            'case',
        )
        # special form type or option
        widgets = {
            'system_name': forms.TextInput(attrs={'autofocus': 'autofocus'}),
            'systemstatus': forms.RadioSelect(),
            'analysisstatus': forms.RadioSelect(),
            'reason': forms.RadioSelect(),
            'recommendation': forms.RadioSelect(),
            'systemtype': forms.RadioSelect(),
            'ip': forms.GenericIPAddressField(),
            'domain': forms.RadioSelect(),
            'system_dnssuffix': forms.TextInput(),
            'os': forms.RadioSelect(),
            'osarch': forms.RadioSelect(),
            'system_install_time': forms.DateTimeInput(),
            'system_lastbooted_time': forms.DateTimeInput(),
            'system_deprecated_time': forms.DateTimeInput(),
            'system_is_vm': forms.NullBooleanSelect(),
            'host_system': forms.Select(),
            'company': forms.CheckboxSelectMultiple(),
            'location': forms.RadioSelect(),
            'serviceprovider': forms.RadioSelect(),
            'contact': forms.RadioSelect(),
            'tag': forms.CheckboxSelectMultiple(),
            'case': forms.CheckboxSelectMultiple(),
        }

class SystemIpFileImport(forms.ModelForm):

    # file upload field (variable is used in request object)
    systemipcsv = forms.FileField()

    class Meta:
        model = System
        # this HTML forms are shown
        fields = (
            'systemstatus',
            'analysisstatus',
            'reason',
            'systemtype',
            'domain',
            'os',
            'company',
            'location',
            'serviceprovider',
            'contact',
            'tag',
            'case',
        )
        # special form type or option
        widgets = {
            'systemstatus': forms.RadioSelect(),
            'analysisstatus': forms.RadioSelect(),
            'reason': forms.RadioSelect(),
            'systemtype': forms.RadioSelect(),
            'domain': forms.RadioSelect(),
            'os': forms.RadioSelect(),
            'company': forms.CheckboxSelectMultiple(),
            'location': forms.RadioSelect(),
            'serviceprovider': forms.RadioSelect(),
            'contact': forms.RadioSelect(),
            'tag': forms.CheckboxSelectMultiple(),
            'case': forms.CheckboxSelectMultiple(),
        }

class SystemTagFileImport(forms.Form):

    # file upload field (variable is used in request object)
    systemtagcsv = forms.FileField()

class SystemCreatorForm(forms.ModelForm):

    # large text area for line separated systemlist
    systemlist = forms.CharField(widget=forms.Textarea(attrs={
        'rows': 20,
        'placeholder': 'One systemname per line',
        'autofocus': 'autofocus',
    }))

    class Meta:
        model = System
        # this HTML forms are shown
        fields = (
            'systemstatus',
            'analysisstatus',
            'reason',
            'systemtype',
            'domain',
            'os',
            'osarch',
            'company',
            'location',
            'serviceprovider',
            'contact',
            'tag',
            'case',
        )
        # special form type or option
        widgets = {
            'systemstatus': forms.RadioSelect(),
            'analysisstatus': forms.RadioSelect(),
            'reason': forms.RadioSelect(),
            'systemtype': forms.RadioSelect(),
            'domain': forms.RadioSelect(),
            'os': forms.RadioSelect(),
            'osarch': forms.RadioSelect(),
            'company': forms.CheckboxSelectMultiple(),
            'location': forms.RadioSelect(),
            'serviceprovider': forms.RadioSelect(),
            'contact': forms.RadioSelect(),
            'tag': forms.CheckboxSelectMultiple(),
            'case': forms.CheckboxSelectMultiple(),
        }

class SystemstatusForm(forms.ModelForm):
    class Meta:
        model = Systemstatus
        # this HTML forms are shown
        fields = (
            'systemstatus_name',
            'systemstatus_note',
        )
        # non default form labeling
        labels = {
            'systemstatus_name': gettext_lazy('Systemstatus name (*)'),
        }
        # special form type or option
        widgets = {
            'systemstatus_name': forms.TextInput(attrs={'autofocus': 'autofocus'}),
        }

class SystemtypeForm(forms.ModelForm):
    class Meta:
        model = Systemtype
        # this HTML forms are shown
        fields = (
            'systemtype_name',
        )
        # non default form labeling
        labels = {
            'systemtype_name': gettext_lazy('Systemtype name (*)'),
        }
        # special form type or option
        widgets = {
            'systemtype_name': forms.TextInput(attrs={'autofocus': 'autofocus'}),
        }

class SystemuserForm(forms.ModelForm):
    class Meta:
        model = Systemuser
        # this HTML forms are shown
        fields = (
            'systemuser_name',
            'systemuser_lastlogon_time',
            'system',
        )
        # non default form labeling
        labels = {
            'systemuser_name': gettext_lazy('Systemuser name (*)'),
            'systemuser_lastlogon_time': gettext_lazy('Last logon time (YYYY-MM-DD HH:MM:SS)'),
            'system': gettext_lazy('System (*)'),
        }
        # special form type or option
        widgets = {
            'systemuser_name': forms.TextInput(attrs={'autofocus': 'autofocus'}),
        }

class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        # this HTML forms are shown
        fields = (
            'tag_name',
            'tagcolor',
            'tag_note',
        )
        # non default form labeling
        labels = {
            'tag_name': gettext_lazy('Tag name (*)'),
            'tagcolor': gettext_lazy('Tag color (*)'),
            'tag_note': gettext_lazy('Tag note'),
        }
        # special form type or option
        widgets = {
            'tag_name': forms.TextInput(attrs={'autofocus': 'autofocus'}),
        }

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        # this HTML forms are shown
        fields = (
            'taskname',
            'parent_task',
            'taskpriority',
            'taskstatus',
            'system',
            'task_assigned_to_user_id',
            'task_note',
            'tag',
            'task_scheduled_time',
            'task_due_time',
        )
        # special form type or option
        widgets = {
            'taskname': forms.Select(),
            'parent_task': forms.Select(),
            'taskpriority': forms.RadioSelect(),
            'taskstatus': forms.RadioSelect(),
            'system': forms.Select(),
            'task_assigned_to_user_id': forms.RadioSelect(),
            'task_note': forms.Textarea(attrs={'rows': 10}),
            'tag': forms.CheckboxSelectMultiple(),
            'task_scheduled_time': forms.DateTimeInput(),
            'task_due_time': forms.DateTimeInput(),
        }

class TaskCreatorForm(forms.ModelForm):

    # show all existing taskname objects as multiple choice field
    taskname = forms.ModelMultipleChoiceField(queryset=Taskname.objects.all(), widget=forms.CheckboxSelectMultiple())

    # show all existing system objects as multiple choice field
    system = forms.ModelMultipleChoiceField(queryset=System.objects.all(), widget=forms.CheckboxSelectMultiple())

    class Meta:
        model = Task
        # this HTML forms are shown
        fields = (
            'taskpriority',
            'taskstatus',
            'task_assigned_to_user_id',
            'tag',
        )
        # special form type or option
        widgets = {
            'taskpriority': forms.RadioSelect(),
            'taskstatus': forms.RadioSelect(),
            'task_assigned_to_user_id': forms.RadioSelect(),
            'tag': forms.CheckboxSelectMultiple(),
        }

class TasknameForm(forms.ModelForm):
    class Meta:
        model = Taskname
        # this HTML forms are shown
        fields = (
            'taskname_name',
        )
        # non default form labeling
        labels = {
            'taskname_name': gettext_lazy('Taskname (*)'),
        }
        # special form type or option
        widgets = {
            'taskname_name': forms.TextInput(attrs={'autofocus': 'autofocus'}),
        }

class TaskpriorityForm(forms.ModelForm):
    class Meta:
        model = Taskpriority
        # this HTML forms are shown
        fields = (
            'taskpriority_name',
        )
        # non default form labeling
        labels = {
            'taskpriority_name': gettext_lazy('Taskpriority name (*)'),
        }
        # special form type or option
        widgets = {
            'taskpriority_name': forms.TextInput(attrs={'autofocus': 'autofocus'}),
        }

class TaskstatusForm(forms.ModelForm):
    class Meta:
        model = Taskstatus
        # this HTML forms are shown
        fields = (
            'taskstatus_name',
        )
        # non default form labeling
        labels = {
            'taskstatus_name': gettext_lazy('Taskstatus name (*)'),
        }
        # special form type or option
        widgets = {
            'taskstatus_name': forms.TextInput(attrs={'autofocus': 'autofocus'}),
        }

