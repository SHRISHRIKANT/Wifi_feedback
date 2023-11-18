
class ComplaintImageRouter:
    def db_for_read(self, model, **hints):
        if model._meta.app_label == 'app' and model._meta.model_name == 'complaintimage':
            return 'mongodb'  # Use 'mongodb' for the ComplaintImage model
        return 'default'

    def db_for_write(self, model, **hints):
        if model._meta.app_label == 'app' and model._meta.model_name == 'complaintimage':
            return 'mongodb'  # Use 'mongodb' for the ComplaintImage model
        return 'default'

    def allow_relation(self, obj1, obj2, **hints):
        return True

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        if db == 'mongodb' and model_name == 'complaintimage':
            return True
        return False
