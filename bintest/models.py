# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Agentname(models.Model):
    name_id = models.TextField(blank=True,primary_key=True, null=False)  # This field type is a guess.
    firstname = models.TextField(blank=True, null=True)  # This field type is a guess.
    lastname = models.TextField(blank=True, null=True)  # This field type is a guess.
    email = models.TextField(blank=True, null=True)  # This field type is a guess.
    phone = models.TextField(blank=True, null=True)  # This field type is a guess.
    pollingunit_uniqueid = models.TextField(blank=True, null=True)  # This field type is a guess.

    def __str__(self) -> str:
        return self.email

    class Meta:
        managed = False
        db_table = 'agentname'


class AnnouncedLgaResults(models.Model):
    result_id = models.TextField(blank=True, primary_key=True, null=False)  # This field type is a guess.
    lga_name = models.TextField(blank=True, null=True)  # This field type is a guess.
    party_abbreviation = models.TextField(blank=True, null=True)  # This field type is a guess.
    party_score = models.TextField(blank=True, null=True)  # This field type is a guess.
    entered_by_user = models.TextField(blank=True, null=True)  # This field type is a guess.
    date_entered = models.TextField(blank=True, null=True)  # This field type is a guess.
    user_ip_address = models.TextField(blank=True, null=True)  # This field type is a guess.

    def __str__(self) -> str:
        return self.lga_name
    class Meta:
        managed = False
        db_table = 'announced_lga_results'


class AnnouncedPuResults(models.Model):
    result_id = models.TextField(blank=True,primary_key=True, null=False)  # This field type is a guess.
    polling_unit_uniqueid = models.TextField(blank=True, null=True)  # This field type is a guess.
    party_abbreviation = models.TextField(blank=True, null=True)  # This field type is a guess.
    party_score = models.TextField(blank=True, null=True)  # This field type is a guess.
    entered_by_user = models.TextField(blank=True, null=True)  # This field type is a guess.
    date_entered = models.TextField(blank=True, null=True)  # This field type is a guess.
    user_ip_address = models.TextField(blank=True, null=True)  # This field type is a guess.
    def __str__(self) -> str:
        return self.polling_unit_uniqueid
    class Meta:
        managed = False
        db_table = 'announced_pu_results'


class AnnouncedStateResults(models.Model):
    result_id = models.TextField(blank=True,primary_key=True, null=False)  # This field type is a guess.
    state_name = models.TextField(blank=True, null=True)  # This field type is a guess.
    party_abbreviation = models.TextField(blank=True, null=True)  # This field type is a guess.
    party_score = models.TextField(blank=True, null=True)  # This field type is a guess.
    entered_by_user = models.TextField(blank=True, null=True)  # This field type is a guess.
    date_entered = models.TextField(blank=True, null=True)  # This field type is a guess.
    user_ip_address = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'announced_state_results'


class AnnouncedWardResults(models.Model):
    result_id = models.TextField(blank=True,primary_key=True, null=False)  # This field type is a guess.
    ward_name = models.TextField(blank=True, null=True)  # This field type is a guess.
    party_abbreviation = models.TextField(blank=True, null=True)  # This field type is a guess.
    party_score = models.TextField(blank=True, null=True)  # This field type is a guess.
    entered_by_user = models.TextField(blank=True, null=True)  # This field type is a guess.
    date_entered = models.TextField(blank=True, null=True)  # This field type is a guess.
    user_ip_address = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'announced_ward_results'


class Lga(models.Model):
    uniqueid = models.TextField(blank=True,primary_key=True, null=False)  # This field type is a guess.
    lga_id = models.TextField(blank=True, null=True)  # This field type is a guess.
    lga_name = models.TextField(blank=True, null=True)  # This field type is a guess.
    state_id = models.TextField(blank=True, null=True)  # This field type is a guess.
    lga_description = models.TextField(blank=True, null=True)  # This field type is a guess.
    entered_by_user = models.TextField(blank=True, null=True)  # This field type is a guess.
    date_entered = models.TextField(blank=True, null=True)  # This field type is a guess.
    user_ip_address = models.TextField(blank=True, null=True)  # This field type is a guess.
    def __str__(self) -> str:
        return self.lga_name
    class Meta:
        managed = False
        db_table = 'lga'


class Party(models.Model):
    id = models.TextField(primary_key=True, blank=True, null=False)  # This field type is a guess.
    partyid = models.TextField(blank=True, null=True)  # This field type is a guess.
    partyname = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'party'


class PollingUnit(models.Model):
    uniqueid = models.TextField(blank=True,primary_key=True, null=False)  # This field type is a guess.
    polling_unit_id = models.TextField(blank=True, null=True)  # This field type is a guess.
    ward_id = models.TextField(blank=True, null=True)  # This field type is a guess.
    lga_id = models.TextField(blank=True, null=True)  # This field type is a guess.
    uniquewardid = models.TextField(blank=True, null=True)  # This field type is a guess.
    polling_unit_number = models.TextField(blank=True, null=True)  # This field type is a guess.
    polling_unit_name = models.TextField(blank=True, null=True)  # This field type is a guess.
    polling_unit_description = models.TextField(blank=True, null=True)  # This field type is a guess.
    lat = models.TextField(blank=True, null=True)  # This field type is a guess.
    long = models.TextField(blank=True, null=True)  # This field type is a guess.
    entered_by_user = models.TextField(blank=True, null=True)  # This field type is a guess.
    date_entered = models.TextField(blank=True, null=True)  # This field type is a guess.
    user_ip_address = models.TextField(blank=True, null=True)  # This field type is a guess.
    def __str__(self) -> str:
        return self.polling_unit_name
    class Meta:
        managed = False
        db_table = 'polling_unit'


class States(models.Model):
    state_id = models.TextField(blank=True,primary_key=True, null=False)  # This field type is a guess.
    state_name = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'states'


class Ward(models.Model):
    uniqueid = models.TextField(blank=True, primary_key=True,null=False)  # This field type is a guess.
    ward_id = models.TextField(blank=True, null=True)  # This field type is a guess.
    ward_name = models.TextField(blank=True, null=True)  # This field type is a guess.
    lga_id = models.TextField(blank=True, null=True)  # This field type is a guess.
    ward_description = models.TextField(blank=True, null=True)  # This field type is a guess.
    entered_by_user = models.TextField(blank=True, null=True)  # This field type is a guess.
    date_entered = models.TextField(blank=True, null=True)  # This field type is a guess.
    user_ip_address = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'ward'
