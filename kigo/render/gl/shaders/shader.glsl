// kigo/render/gl/shaders/shader.glsl
#version 330 core

// Fullscreen quad vertex output
in vec2 v_uv;

// Output color
out vec4 FragColor;

// Input texture
uniform sampler2D u_scene;

void main()
{
    FragColor = texture(u_scene, v_uv);
}
