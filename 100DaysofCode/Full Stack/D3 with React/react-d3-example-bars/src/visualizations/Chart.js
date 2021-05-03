import React, { Component } from "react";
import * as d3 from "d3";

const width = 650;
const height = 400;
const margin = { top: 20, right: 5, bottom: 20, left: 35 };

class Chart extends Component {
  state = {
    bars: []
  };

  static getDerivedStateFromProps(nextProps, prevState) {
    const { data } = nextProps;
    if (!data) return {};
    const xScale = d3.scaleTime().range([0, width]);
    const yScale = d3.scaleLinear().range([height, 0]);
    const colorScale = d3.scaleSequential(d3.interpolateSpectral);

    const timeDomain = d3.extent(data, (d) => d.date);
    const tempMax = d3.max(data, (d) => d.high);
    const [minAvg, maxAvg] = d3.extent(data, (d) => d.avg);
    xScale.domain(timeDomain);
    yScale.domain([0, tempMax]);
    colorScale.domain([maxAvg, minAvg]);

    // calculate x and y for each rectangle
    const bars = data.map((d) => {
      const y1 = yScale(d.high);
      const y2 = yScale(d.low);
      return {
        x: xScale(d.date),
        y: y1,
        height: y2 - y1,
        fill: colorScale(d.avg)
      };
    });

    return { bars };
  }

  render() {
    return (
      <svg width={width} height={height}>
        {this.state.bars.map((d) => (
          <rect x={d.x} y={d.y} width={2} height={d.height} fill={d.fill} />
        ))}
      </svg>
    );
  }
}

export default Chart;
