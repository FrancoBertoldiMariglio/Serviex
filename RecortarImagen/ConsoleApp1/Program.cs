// Carga la imagen.
using Aspose.Imaging;

using (RasterImage rasterImage = (RasterImage)Image.Load("C:\\Users\\patit\\source\\repos\\RecortarImagen\\ImagenOriginal.tif"))
{
    // Antes de recortar, la imagen debe almacenarse en caché para un mejor rendimiento.
    if (!rasterImage.IsCached)
    {
        rasterImage.CacheData();
    }

    // Cree una instancia de la clase Rectangle con el tamaño deseado y recorte la imagen.
    Rectangle rectangle = new Rectangle(450, 1800, 750, 215);
    rasterImage.Crop(rectangle);

    // Guardar imagen recortada.
    rasterImage.Save("C:\\Users\\patit\\source\\repos\\RecortarImagen\\ImagenRecortada.tif");
}