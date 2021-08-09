from django.db import models


class Project(models.Model):

    title = models.CharField(max_length=200, verbose_name="Titulo")
    description = models.TextField(verbose_name="Descripcion")
    image = models.ImageField(verbose_name="Fecha Creacion", upload_to="projects")
    link = models.URLField(verbose_name="Direccion web", null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha creacion")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha actualizacion")
    order = models.IntegerField(default=0, blank=True, null=True)

    class Meta:
        verbose_name = 'Proyecto'
        verbose_name_plural = 'proyectos'
        ordering = ['-created']  # descendente

    def __str__(self):
        return self.title
