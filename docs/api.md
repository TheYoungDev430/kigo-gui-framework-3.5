Kigo API Reference
Version: 1.0
Status: Stable
API Contract: All symbols documented here are guaranteed stable within the 1.x series.
Breaking changes require a major (2.0) release. [ecolab-my....epoint.com]

1. Overview
Kigo is a Qt‑based, cross‑platform application and rendering framework with a strict separation between:

UI (PyQt)
Rendering backend (auto‑selected per platform)
Debugging & inspection
Tooling

Kigo automatically selects the optimal rendering backend at runtime while keeping the public API identical across platforms.

2. Application Core
kigo.app.App
The base class for all Kigo applications.
Pythonfrom kigo.app import AppShow more lines
Constructor
PythonApp(*, dev: bool = False)Show more lines















ParameterTypeDescriptiondevboolEnables developer tools (inspectors, diagnostics).

Lifecycle Hooks
Pythondef on_start(self) -> NoneShow more lines
Called once after the Qt application is initialized.
Pythondef on_exit(self) -> NoneShow more lines
Called once before application shutdown.

Methods
Pythondef run(self) -> NoReturnShow more lines
Starts the Qt event loop and blocks until exit.

3. Platform Detection
Pythonfrom kigo.platform_info import platform_name, summaryShow more lines
platform_name() -> str
Returns the current platform identifier.
Possible values:

"windows"
"linux"
"macos"
"chromeos"
"android"
"freebsd"
"openbsd"
"sunos"


summary() -> dict
Returns an immutable snapshot of the runtime environment.

4. Rendering System
Rendering is accessed through a single public entry point.
The backend is selected automatically based on platform.
Backend Selection Rules




















PlatformBackendShader LanguageWindowsDirectXHLSLOther OSOpenGLGLSL
This selection is automatic and does not require user configuration.

kigo.render.Renderer
Pythonfrom kigo.render import RendererShow more lines
The main rendering interface.
Constructor
PythonRenderer(qt_window)Show more lines













ParameterDescriptionqt_windowA PyQt window or widget to render into

Methods
Pythondef initialize(self) -> NoneShow more lines
Initializes the rendering backend and prepares resources.
Pythondef draw(self) -> NoneShow more lines
Renders a single frame.
Pythondef enable_ssao(self) -> NoneShow more lines
Enables Screen‑Space Ambient Occlusion if supported by the backend.

5. Screen‑Space Ambient Occlusion (SSAO)
SSAO is exposed through a backend‑agnostic API.
Enabling SSAO
Pythonrenderer.enable_ssao()Show more lines
The internal implementation is selected automatically:

Windows → HLSL implementation
Other OS → GLSL implementation

The SSAO algorithm and quality are consistent across backends.

6. Shader System
Shaders are not part of the public API.
Internal Shader Layout

Windows: .hlsl
Other platforms: .glsl

Shader management, compilation, and binding are handled internally by Kigo.
Users never directly load, compile, or bind shaders.

7. Debugging & Developer Tools
Time Freeze
Pythonfrom kigo.debug import freezeShow more lines
Pythonfreeze("Execution paused", data={...})Show more lines
Pauses application logic while keeping the UI responsive.

Visual Inspector
Pythonfrom kigo.inspector import enable_inspectorShow more lines
Enables Kigo’s in‑process visual inspector (dev mode only).

DOM Inspector (WebEngine)
Pythonfrom kigo.inspector.web import enable_dom_inspectorShow more lines
Allows DOM inspection for Qt WebEngine views.

8. Logging
Logging is opt‑in and disabled by default.
To enable logging:
Pythonlog = "on"Show more lines
Logging output is structured JSON.

9. Public vs Internal API
Public API

Everything documented in this reference
Everything re‑exported in package __init__.py files

Internal API

Modules prefixed with _
Backend‑specific implementations
Shader code
Compilation logic

Importing internal APIs is unsupported and may break without notice.

10. Versioning & Stability
Kigo follows Semantic Versioning:

PATCH: Bug fixes only
MINOR: Backwards‑compatible additions
MAJOR: Breaking changes

Deprecated features produce warnings for at least one minor release before removal. [ecolab-my....epoint.com]

11. Guarantees
Kigo guarantees:

Stable public APIs
Automatic backend selection
No backend leakage into user code
Honest platform behavior
No hidden background execution


✅ End of Official API Reference