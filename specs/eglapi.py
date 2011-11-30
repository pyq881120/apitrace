##########################################################################
#
# Copyright 2011 LunarG, Inc.
# All Rights Reserved.
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.
#
##########################################################################/

"""EGL API description."""


from stdapi import *

EGLNativeDisplayType = Opaque("EGLNativeDisplayType")
EGLNativeWindowType = Opaque("EGLNativeWindowType")
EGLNativePixmapType = Opaque("EGLNativePixmapType")

EGLDisplay = Opaque("EGLDisplay")
EGLConfig = Opaque("EGLConfig")
EGLContext = Opaque("EGLContext")
EGLSurface = Opaque("EGLSurface")

EGLClientBuffer = Opaque("EGLClientBuffer")

_EGLBoolean = Alias("EGLBoolean", UInt)
EGLBoolean = FakeEnum(_EGLBoolean, [
    "EGL_FALSE",
    "EGL_TRUE",
])

EGLint = Alias("EGLint", Int32)
EGLenum = Alias("EGLenum", UInt)

EGLError = FakeEnum(EGLint, [
    "EGL_SUCCESS",                  # 0x3000
    "EGL_NOT_INITIALIZED",          # 0x3001
    "EGL_BAD_ACCESS",               # 0x3002
    "EGL_BAD_ALLOC",                # 0x3003
    "EGL_BAD_ATTRIBUTE",            # 0x3004
    "EGL_BAD_CONFIG",               # 0x3005
    "EGL_BAD_CONTEXT",              # 0x3006
    "EGL_BAD_CURRENT_SURFACE",      # 0x3007
    "EGL_BAD_DISPLAY",              # 0x3008
    "EGL_BAD_MATCH",                # 0x3009
    "EGL_BAD_NATIVE_PIXMAP",        # 0x300A
    "EGL_BAD_NATIVE_WINDOW",        # 0x300B
    "EGL_BAD_PARAMETER",            # 0x300C
    "EGL_BAD_SURFACE",              # 0x300D
    "EGL_CONTEXT_LOST",             # 0x300E  /* EGL 1.1 - IMG_power_management */
])

EGLConfigAttrib = FakeEnum(EGLint, [
    "EGL_BUFFER_SIZE",              # 0x3020
    "EGL_ALPHA_SIZE",               # 0x3021
    "EGL_BLUE_SIZE",                # 0x3022
    "EGL_GREEN_SIZE",               # 0x3023
    "EGL_RED_SIZE",                 # 0x3024
    "EGL_DEPTH_SIZE",               # 0x3025
    "EGL_STENCIL_SIZE",             # 0x3026
    "EGL_CONFIG_CAVEAT",            # 0x3027
    "EGL_CONFIG_ID",                # 0x3028
    "EGL_LEVEL",                    # 0x3029
    "EGL_MAX_PBUFFER_HEIGHT",       # 0x302A
    "EGL_MAX_PBUFFER_PIXELS",       # 0x302B
    "EGL_MAX_PBUFFER_WIDTH",        # 0x302C
    "EGL_NATIVE_RENDERABLE",        # 0x302D
    "EGL_NATIVE_VISUAL_ID",         # 0x302E
    "EGL_NATIVE_VISUAL_TYPE",       # 0x302F
    "EGL_SAMPLES",                  # 0x3031
    "EGL_SAMPLE_BUFFERS",           # 0x3032
    "EGL_SURFACE_TYPE",             # 0x3033
    "EGL_TRANSPARENT_TYPE",         # 0x3034
    "EGL_TRANSPARENT_BLUE_VALUE",   # 0x3035
    "EGL_TRANSPARENT_GREEN_VALUE",  # 0x3036
    "EGL_TRANSPARENT_RED_VALUE",    # 0x3037
    "EGL_NONE",                     # 0x3038  /* Attrib list terminator */
    "EGL_BIND_TO_TEXTURE_RGB",      # 0x3039
    "EGL_BIND_TO_TEXTURE_RGBA",     # 0x303A
    "EGL_MIN_SWAP_INTERVAL",        # 0x303B
    "EGL_MAX_SWAP_INTERVAL",        # 0x303C
    "EGL_LUMINANCE_SIZE",           # 0x303D
    "EGL_ALPHA_MASK_SIZE",          # 0x303E
    "EGL_COLOR_BUFFER_TYPE",        # 0x303F
    "EGL_RENDERABLE_TYPE",          # 0x3040
    "EGL_MATCH_NATIVE_PIXMAP",      # 0x3041  /* Pseudo-attribute (not queryable) */
    "EGL_CONFORMANT",               # 0x3042

    # EGL_KHR_lock_surface
    "EGL_MATCH_FORMAT_KHR",         # 0x3043
])

EGLName = FakeEnum(EGLint, [
    "EGL_VENDOR",                   # 0x3053
    "EGL_VERSION",                  # 0x3054
    "EGL_EXTENSIONS",               # 0x3055
    "EGL_CLIENT_APIS",              # 0x308D
])

EGLSurfaceAttrib = FakeEnum(EGLint, [
    "EGL_HEIGHT",                   # 0x3056
    "EGL_WIDTH",                    # 0x3057
    "EGL_LARGEST_PBUFFER",          # 0x3058
    "EGL_TEXTURE_FORMAT",           # 0x3080
    "EGL_TEXTURE_TARGET",           # 0x3081
    "EGL_MIPMAP_TEXTURE",           # 0x3082
    "EGL_MIPMAP_LEVEL",             # 0x3083
    "EGL_RENDER_BUFFER",            # 0x3086
    "EGL_VG_COLORSPACE",            # 0x3087
    "EGL_VG_ALPHA_FORMAT",          # 0x3088
    "EGL_HORIZONTAL_RESOLUTION",    # 0x3090
    "EGL_VERTICAL_RESOLUTION",      # 0x3091
    "EGL_PIXEL_ASPECT_RATIO",       # 0x3092
    "EGL_SWAP_BEHAVIOR",            # 0x3093
    "EGL_MULTISAMPLE_RESOLVE",      # 0x3099
    "EGL_NONE",

    # EGL_KHR_lock_surface
    "EGL_BITMAP_POINTER_KHR",                   # 0x30C6
    "EGL_BITMAP_PITCH_KHR",                     # 0x30C7
    "EGL_BITMAP_ORIGIN_KHR",                    # 0x30C8
    "EGL_BITMAP_PIXEL_RED_OFFSET_KHR",          # 0x30C9
    "EGL_BITMAP_PIXEL_GREEN_OFFSET_KHR",        # 0x30CA
    "EGL_BITMAP_PIXEL_BLUE_OFFSET_KHR",         # 0x30CB
    "EGL_BITMAP_PIXEL_ALPHA_OFFSET_KHR",        # 0x30CC
    "EGL_BITMAP_PIXEL_LUMINANCE_OFFSET_KHR",    # 0x30CD
    # EGL_KHR_lock_surface2
    "EGL_BITMAP_PIXEL_SIZE_KHR",                # 0x3110
])

EGLContextAttrib = FakeEnum(EGLint, [
    "EGL_CONTEXT_CLIENT_TYPE",      # 0x3097
    "EGL_CONTEXT_CLIENT_VERSION",   # 0x3098
    "EGL_NONE",
])

EGLAPI = FakeEnum(EGLenum, [
    "EGL_OPENGL_ES_API",            # 0x30A0
    "EGL_OPENVG_API",               # 0x30A1
    "EGL_OPENGL_API",               # 0x30A2
])

EGLClientBufferType = FakeEnum(EGLenum, [
    "EGL_OPENVG_IMAGE",             # 0x3096
])

EGLBufferType = FakeEnum(EGLint, [
    "EGL_BACK_BUFFER",              # 0x3084
    "EGL_SINGLE_BUFFER",            # 0x3085
])

EGLEngine = FakeEnum(EGLint, [
    "EGL_CORE_NATIVE_ENGINE",       # 0x305B
])

# EGL_KHR_lock_surface
EGLLockSurfaceAttrib = FakeEnum(EGLint, [
    "EGL_MAP_PRESERVE_PIXELS_KHR",  # 0x30C4
    "EGL_LOCK_USAGE_HINT_KHR",      # 0x30C5
])

# EGL_KHR_image_base
EGLImageKHR = Opaque("EGLImageKHR")

EGLImageKHRAttrib = FakeEnum(EGLint, [
    "EGL_IMAGE_PRESERVED_KHR",      # 0x30D2

    # EGL_KHR_gl_*_image
    "EGL_GL_TEXTURE_LEVEL_KHR",     # 0x30BC
    "EGL_GL_TEXTURE_ZOFFSET_KHR",   # 0x30BD

    "EGL_NONE",
])

EGLImageKHRTarget = FakeEnum(EGLenum, [
    # EGL_KHR_image_pixmap
    "EGL_NATIVE_PIXMAP_KHR",                    # 0x30B0

    # EGL_KHR_vg_parent_image
    "EGL_VG_PARENT_IMAGE_KHR",                  # 0x30BA

    # EGL_KHR_gl_*_image
    "EGL_GL_TEXTURE_2D_KHR",                    # 0x30B1
    "EGL_GL_TEXTURE_3D_KHR",                    # 0x30B2
    "EGL_GL_TEXTURE_CUBE_MAP_POSITIVE_X_KHR",   # 0x30B3
    "EGL_GL_TEXTURE_CUBE_MAP_NEGATIVE_X_KHR",   # 0x30B4
    "EGL_GL_TEXTURE_CUBE_MAP_POSITIVE_Y_KHR",   # 0x30B5
    "EGL_GL_TEXTURE_CUBE_MAP_NEGATIVE_Y_KHR",   # 0x30B6
    "EGL_GL_TEXTURE_CUBE_MAP_POSITIVE_Z_KHR",   # 0x30B7
    "EGL_GL_TEXTURE_CUBE_MAP_NEGATIVE_Z_KHR",   # 0x30B8
    "EGL_GL_RENDERBUFFER_KHR",                  # 0x30B9
])

# EGL_KHR_reusable_sync
EGLSyncKHR = Opaque("EGLSyncKHR")
EGLTimeKHR = Alias("EGLTimeKHR", UInt64)

EGLSyncKHRType = FakeEnum(EGLenum, [
    "EGL_SYNC_REUSABLE_KHR",        # 0x30FA

    # EGL_KHR_fence_sync
    "EGL_SYNC_FENCE_KHR",           # 0x30F9
])

EGLSyncKHRAttrib = FakeEnum(EGLint, [
    "EGL_SYNC_STATUS_KHR",          # 0x30F1
    "EGL_SYNC_TYPE_KHR",            # 0x30F7

    # EGL_KHR_fence_sync
    "EGL_SYNC_CONDITION_KHR",       # 0x30F8

    "EGL_NONE",
])

EGLSyncKHRMode = FakeEnum(EGLenum, [
    "EGL_SIGNALED_KHR",             # 0x30F2
    "EGL_UNSIGNALED_KHR",           # 0x30F3
])

eglapi = API("EGL")

PROC = Opaque("__eglMustCastToProperFunctionPointerType")

eglapi.add_functions([
    # EGL 1.4
    Function(EGLError, "eglGetError", [], sideeffects=False),

    Function(EGLDisplay, "eglGetDisplay", [(EGLNativeDisplayType, "display_id")]),
    Function(EGLBoolean, "eglInitialize", [(EGLDisplay, "dpy"), Out(Pointer(EGLint), "major"), Out(Pointer(EGLint), "minor")]),
    Function(EGLBoolean, "eglTerminate", [(EGLDisplay, "dpy")]),

    Function(Const(String("char *")), "eglQueryString", [(EGLDisplay, "dpy"), (EGLName, "name")], sideeffects=False),

    Function(EGLBoolean, "eglGetConfigs", [(EGLDisplay, "dpy"), (Array(EGLConfig, "config_size"), "configs"), (EGLint, "config_size"), Out(Pointer(EGLint), "num_config")]),
    Function(EGLBoolean, "eglChooseConfig", [(EGLDisplay, "dpy"), (Array(Const(EGLConfigAttrib), "__AttribList_size(attrib_list, EGL_NONE)"), "attrib_list"), (Array(EGLConfig, "config_size"), "configs"), (EGLint, "config_size"), Out(Pointer(EGLint), "num_config")]),
    Function(EGLBoolean, "eglGetConfigAttrib", [(EGLDisplay, "dpy"), (EGLConfig, "config"), (EGLConfigAttrib, "attribute"), Out(Pointer(EGLint), "value")], sideeffects=False),

    Function(EGLSurface, "eglCreateWindowSurface", [(EGLDisplay, "dpy"), (EGLConfig, "config"), (EGLNativeWindowType, "win"), (Array(Const(EGLSurfaceAttrib), "__AttribList_size(attrib_list, EGL_NONE)"), "attrib_list")]),
    Function(EGLSurface, "eglCreatePbufferSurface", [(EGLDisplay, "dpy"), (EGLConfig, "config"), (Array(Const(EGLSurfaceAttrib), "__AttribList_size(attrib_list, EGL_NONE)"), "attrib_list")]),
    Function(EGLSurface, "eglCreatePixmapSurface", [(EGLDisplay, "dpy"), (EGLConfig, "config"), (EGLNativePixmapType, "pixmap"), (Array(Const(EGLSurfaceAttrib), "__AttribList_size(attrib_list, EGL_NONE)"), "attrib_list")]),
    Function(EGLBoolean, "eglDestroySurface", [(EGLDisplay, "dpy"), (EGLSurface, "surface")]),
    Function(EGLBoolean, "eglQuerySurface", [(EGLDisplay, "dpy"), (EGLSurface, "surface"), (EGLSurfaceAttrib, "attribute"), Out(Pointer(EGLint), "value")], sideeffects=False),

    Function(EGLBoolean, "eglBindAPI", [(EGLAPI, "api")]),
    Function(EGLAPI, "eglQueryAPI", [], sideeffects=False),

    Function(EGLBoolean, "eglWaitClient", []),

    Function(EGLBoolean, "eglReleaseThread", []),

    Function(EGLSurface, "eglCreatePbufferFromClientBuffer", [(EGLDisplay, "dpy"), (EGLClientBufferType, "buftype"), (EGLClientBuffer, "buffer"), (EGLConfig, "config"), (Array(Const(EGLSurfaceAttrib), "__AttribList_size(attrib_list, EGL_NONE)"), "attrib_list")]),

    Function(EGLBoolean, "eglSurfaceAttrib", [(EGLDisplay, "dpy"), (EGLSurface, "surface"), (EGLSurfaceAttrib, "attribute"), (EGLint, "value")]),
    Function(EGLBoolean, "eglBindTexImage", [(EGLDisplay, "dpy"), (EGLSurface, "surface"), (EGLBufferType, "buffer")]),
    Function(EGLBoolean, "eglReleaseTexImage", [(EGLDisplay, "dpy"), (EGLSurface, "surface"), (EGLBufferType, "buffer")]),

    Function(EGLBoolean, "eglSwapInterval", [(EGLDisplay, "dpy"), (EGLint, "interval")]),

    Function(EGLContext, "eglCreateContext", [(EGLDisplay, "dpy"), (EGLConfig, "config"), (EGLContext, "share_context"), (Array(Const(EGLContextAttrib), "__AttribList_size(attrib_list, EGL_NONE)"), "attrib_list")]),
    Function(EGLBoolean, "eglDestroyContext", [(EGLDisplay, "dpy"), (EGLContext, "ctx")]),
    Function(EGLBoolean, "eglMakeCurrent", [(EGLDisplay, "dpy"), (EGLSurface, "draw"), (EGLSurface, "read"), (EGLContext, "ctx")]),

    Function(EGLContext, "eglGetCurrentContext", [], sideeffects=False),
    Function(EGLSurface, "eglGetCurrentSurface", [(EGLBufferType, "readdraw")], sideeffects=False),
    Function(EGLDisplay, "eglGetCurrentDisplay", [], sideeffects=False),

    Function(EGLBoolean, "eglQueryContext", [(EGLDisplay, "dpy"), (EGLContext, "ctx"), (EGLContextAttrib, "attribute"), Out(Pointer(EGLint), "value")], sideeffects=False),

    Function(EGLBoolean, "eglWaitGL", []),
    Function(EGLBoolean, "eglWaitNative", [(EGLEngine, "engine")]),
    Function(EGLBoolean, "eglSwapBuffers", [(EGLDisplay, "dpy"), (EGLSurface, "surface")]),
    Function(EGLBoolean, "eglCopyBuffers", [(EGLDisplay, "dpy"), (EGLSurface, "surface"), (EGLNativePixmapType, "target")]),

    Function(PROC, "eglGetProcAddress", [(Const(CString), "procname")]),

    # EGL_KHR_lock_surface
    Function(EGLBoolean, "eglLockSurfaceKHR", [(EGLDisplay, "display"), (EGLSurface, "surface"), (Array(Const(EGLLockSurfaceAttrib), "__AttribList_size(attrib_list, EGL_NONE)"), "attrib_list")]),
    Function(EGLBoolean, "eglUnlockSurfaceKHR", [(EGLDisplay, "display"), (EGLSurface, "surface")]),

    # EGL_KHR_image_base
    Function(EGLImageKHR, "eglCreateImageKHR", [(EGLDisplay, "dpy"), (EGLContext, "ctx"), (EGLImageKHRTarget, "target"), (EGLClientBuffer, "buffer"), (Array(Const(EGLImageKHRAttrib), "__AttribList_size(attrib_list, EGL_NONE)"), "attrib_list")]),
    Function(EGLBoolean, "eglDestroyImageKHR", [(EGLDisplay, "dpy"), (EGLImageKHR, "image")]),

    # EGL_KHR_reusable_sync
    Function(EGLSyncKHR, "eglCreateSyncKHR", [(EGLDisplay, "dpy"), (EGLSyncKHRType, "type"), (Array(Const(EGLSyncKHRAttrib), "__AttribList_size(attrib_list, EGL_NONE)"), "attrib_list")]),
    Function(EGLBoolean, "eglDestroySyncKHR", [(EGLDisplay, "dpy"), (EGLSyncKHR, "sync")]),
    Function(EGLint, "eglClientWaitSyncKHR", [(EGLDisplay, "dpy"), (EGLSyncKHR, "sync"), (EGLint, "flags"), (EGLTimeKHR, "timeout")]),
    Function(EGLBoolean, "eglSignalSyncKHR", [(EGLDisplay, "dpy"), (EGLSyncKHR, "sync"), (EGLSyncKHRMode, "mode")]),
    Function(EGLBoolean, "eglGetSyncAttribKHR", [(EGLDisplay, "dpy"), (EGLSyncKHR, "sync"), (EGLSyncKHRAttrib, "attribute"), Out(Pointer(EGLint), "value")], sideeffects=False),
])