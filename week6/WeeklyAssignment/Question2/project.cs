var builder = WebApplication.CreateBuilder(args);
var app = builder.Build();
 
app.MapGet("/", () => "Hello from .NET Core Docker app!");
 
app.Run();