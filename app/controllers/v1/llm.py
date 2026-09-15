from fastapi import Depends, Request

from app.controllers import base
from app.controllers.v1.base import new_router
from app.models.schema import (
    VideoScriptRequest,
    VideoScriptResponse,
    VideoSocialMetadataRequest,
    VideoSocialMetadataResponse,
    VideoTermsRequest,
    VideoTermsResponse,
    StudioPlanRequest,
    StudioRevisionRequest,
)
from app.services import llm
from app.services import content_studio
from app.utils import utils

# LLM 接口与视频接口共用同一鉴权规则，避免新增端点时遗漏保护。
# api_key 为空时 verify_token 直接放行，不改变默认本地使用体验。
router = new_router(dependencies=[Depends(base.verify_token)])


@router.post(
    "/scripts",
    response_model=VideoScriptResponse,
    summary="Create a script for the video",
)
def generate_video_script(request: Request, body: VideoScriptRequest):
    video_script = llm.generate_script(
        video_subject=body.video_subject,
        language=body.video_language,
        paragraph_number=body.paragraph_number,
        video_script_prompt=body.video_script_prompt,
        custom_system_prompt=body.custom_system_prompt,
    )
    response = {"video_script": video_script}
    return utils.get_response(200, response)


@router.post(
    "/terms",
    response_model=VideoTermsResponse,
    summary="Generate video terms based on the video script",
)
def generate_video_terms(request: Request, body: VideoTermsRequest):
    video_terms = llm.generate_terms(
        video_subject=body.video_subject,
        video_script=body.video_script,
        amount=body.amount,
        match_script_order=body.match_materials_to_script,
    )
    response = {"video_terms": video_terms}
    return utils.get_response(200, response)


@router.post(
    "/social-metadata",
    response_model=VideoSocialMetadataResponse,
    summary="Generate social publishing metadata",
)
def generate_video_social_metadata(
    request: Request, body: VideoSocialMetadataRequest
):
    metadata = llm.generate_social_metadata(
        video_subject=body.video_subject,
        video_script=body.video_script,
        language=body.language,
        platform=body.platform,
    )
    return utils.get_response(200, metadata)


@router.post("/studio/plan", summary="Create an intelligent video storyboard")
def create_studio_plan(request: Request, body: StudioPlanRequest):
    plan = content_studio.create_video_plan(
        topic=body.topic,
        script=body.script,
        language=body.language,
        style=body.style,
        duration_minutes=body.duration_minutes,
        brand_id=body.brand_id,
    )
    return utils.get_response(200, {"plan": plan})


@router.post("/studio/revise", summary="Revise a storyboard using natural language")
def revise_studio_plan(request: Request, body: StudioRevisionRequest):
    plan = content_studio.revise_video_plan(body.plan, body.instruction)
    return utils.get_response(200, {"plan": plan})
