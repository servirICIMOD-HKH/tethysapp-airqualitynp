<template>
  <el-row class="airquality">
    <el-col :span="6" class="full-height">
      <el-row class="first-row">
        <el-col :span="24"
                class="full-height full-width padding-left-10 padding-bottom-5 padding-top-10 padding-right-5">
          <mapControlsEmission></mapControlsEmission>
        </el-col>
      </el-row>
      <el-row class="second-row">
        <el-col :span="24"
                class="full-height full-width padding-left-10 padding-bottom-10 padding-top-5 padding-right-5">
            <chartComponent  :IndexValue="1"></chartComponent>
        </el-col>
      </el-row>
    </el-col>
    <el-col :span="12" class="full-height">
      <el-row class="first-row">
        <el-col :span="24"
                class="full-height full-width padding-left-5 padding-bottom-5 padding-top-10 padding-right-5">
          <mapComponentEmission></mapComponentEmission>
        </el-col>
      </el-row>
      <el-row class="second-row">
        <el-col :span="12"
                class="full-height full-width padding-left-5 padding-bottom-10 padding-top-5 padding-right-5">
          <chartComponent  :IndexValue="2"></chartComponent>
        </el-col>
        <el-col :span="12"
                class="full-height full-width padding-left-5 padding-bottom-10 padding-top-5 padding-right-5">
          <chartComponent  :IndexValue="3"></chartComponent>
        </el-col>
      </el-row>
    </el-col>
    <el-col :span="6" class="full-height">
      <el-row class="first-row">
        <el-col :span="24"
                class="full-height full-width padding-left-5 padding-bottom-5 padding-top-10 padding-right-10">
                    <about></about>

        </el-col>
      </el-row>
      <el-row class="second-row">
        <el-col :span="24"
                class="full-height full-width padding-left-5 padding-bottom-10 padding-top-5 padding-right-10">
          <chartComponent  :IndexValue="4"></chartComponent>
        </el-col>
      </el-row>
    </el-col>
  </el-row>
</template>

<script>
import about from "./about";
import chartComponent from "./chartComponent";
import mapControlsEmission from "./mapControlsEmission";
import mapComponentEmission from "./mapComponentEmission";
// import {mapActions} from "vuex";

export default {
  name: "emissionTabBody",
  components: {
    about,
    chartComponent,
    mapControlsEmission,
    mapComponentEmission,
  },
  methods: {
    // ...mapActions(["getCascaderOptions"]),
  },
  async mounted() {
    // let data = await this.getCascaderOptions();
    // console.log(data);
  }
}
</script>

<style scoped>

.bg-purple-dark {
  background: #99a9bf;
}

.bg-purple {
  background: #d3dce6;
}

.bg-purple-light {
  background: #e5e9f2;
}

.grid-content {
  min-height: 36px;
}

.row-bg {
  padding: 10px 0;
  background-color: #f9fafc;
}

.full-height {
  height: 100%;
}
.second-row div{
  /*height: calc(100% - 12.5px);*/
}
</style>
