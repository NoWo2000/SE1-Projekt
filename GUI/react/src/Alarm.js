import React from 'react';
import Accordion from 'react-bootstrap/Accordion';
import Card from 'react-bootstrap/Card';
import Button from 'react-bootstrap/Button';
import Row from 'react-bootstrap/Row';


class Alarm extends React.Component {

    constructor(props) {
        super(props);
        this.state = {
            card_head: { alarm_id: "Alarm #0014", alarm_cat: "SQL-Injection", alarm_time: "20" },
            card_body: props.card_body
        };


        this.calculateTag = this.calculateTag.bind(this);
    }

    calculateTag(probality) {
        var tag = {
            color: "yellow",
            cat: "MINOR"
        }
        if (probality >= 75) {
            tag.color = "orange"
            tag.cat = "MAJOR"
        };
        if (probality >= 95) {
            tag.color = "red"
            tag.cat = "CRITICAL"
        };
        return tag;
    }

    render() {
        return (
            <Card>

                <Card.Header>
                    <Accordion.Toggle as={Card.Header} variant="" eventKey="0">
                        <Row>
                            <h5 class="font-weight-lighter">{this.state.card_head.alarm_id}</h5>
                        </Row>
                        <Row>
                            <h3 class="font-weight-bolder">{this.state.card_head.alarm_cat}</h3>
                        </Row>
                        <Row>
                            <div class="tag" style={{ 'background-color': this.calculateTag(92).color }}>
                                &#8205; &#8205; {this.calculateTag(92).cat} &#8205; &#8205;
                            </div>
                            <div id="time_ago">
                                {this.state.card_head.alarm_time} minutes ago
                            </div>
                        </Row>
                    </Accordion.Toggle>
                </Card.Header>

                <Accordion.Collapse eventKey="0">
                    <Card.Body>
                        {this.state.card_body}
                    </Card.Body>
                </Accordion.Collapse>
            </Card>);
    }
}

export default Alarm;
