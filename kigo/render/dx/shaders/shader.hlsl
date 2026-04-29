// kigo/render/dx/shaders/shader.hlsl

struct PSInput
{
    float4 pos : SV_POSITION;
    float2 uv  : TEXCOORD0;
};

Texture2D sceneTex : register(t0);
SamplerState samp  : register(s0);

float4 PSMain(PSInput input) : SV_TARGET
{
    return sceneTex.Sample(samp, input.uv);
}